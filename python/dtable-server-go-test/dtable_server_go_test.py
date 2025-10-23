import requests
from seatable_api import Base

from local_settings import SERVER_URL_FOR_GO, BASE_API_TOKEN_FOR_GO, BASE_API_TOKEN_FOR_GO_READONLY, SERVER_URL, \
    BASE_API_TOKEN_FOR_GO_TEST_RESULT

table_name = 'Table1'
link_table_name = 'Table2'

class APIBase(object):
    
    def __init__(self, server_url, api_token, api_token_readonly):
        self.server_url = server_url
        self.api_token = api_token
        self.api_token_readonly = api_token_readonly
        self.base = None
        self.base_r = None
        
        self._init_base()
        
        self.error_count = 0
        self.error_msgs = []
        
    
    def _init_base(self):
        base = Base(self.api_token, self.server_url)
        base.auth()
        base.dtable_server_url = '%s/dtable-server' % self.server_url.rstrip('/')
        base.use_api_gateway = False
        base_r = Base(self.api_token_readonly, self.server_url)
        base_r.auth()
        base_r.dtable_server_url = '%s/dtable-server' % self.server_url.rstrip('/')
        base_r.use_api_gateway = False
        self.base = base
        self.base_r = base_r
        
        
    def record_error(self, msg):
        self.error_count += 1
        self.error_msgs.append(msg)
        print(msg)
        return msg
        

class MetaAPI(APIBase):
    
    def __init__(self, server_url, api_token, api_token_readonly):
        super(MetaAPI, self).__init__(server_url, api_token, api_token_readonly)
        
        self.errors_count = 0

    def get_metadata(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/metadata/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid
        })
        try:
            resp = requests.get(url, headers=self.base.headers)
            result = resp.json()
            if not result['metadata']:
                self.record_error('get_metadata error: %s' % result)
        except Exception as e:
            self.record_error('raise get_metadata error: %s' % e)
            
        
    def get_table_metadata(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/metadata/table/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid
        })
        params = {
            'table_name': table_name
        }
        try:
            resp = requests.get(url, params=params, headers=self.base.headers)
            result = resp.json()
            if not result['table']:
                self.record_error('get_table_metadata error: %s' % result)
        except Exception as e:
            self.record_error('raise get_table_metadata error: %s' % e)
            
    def get_plugin_meatadata(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/metadata/plugin/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid
        })

        try:
            resp = requests.get(url, headers=self.base.headers)
            result = resp.json()
            if not result['tables']:
                self.record_error('get_plugin_metadata error: %s' % result)
        except Exception as e:
            self.record_error('raise get_plugin_metadata error: %s' % e)
        

    def run_test(self):
        self.get_metadata()
        self.get_table_metadata()
        self.get_plugin_meatadata()
        
class TableAPI(APIBase):
    
    def __init__(self, server_url, api_token, api_token_readonly):
        super(TableAPI, self).__init__(server_url, api_token, api_token_readonly)
    
    def add_table(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/tables/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid
        })
        json_data = {
            'table_name': "Table3"
        }
        try:
            resp = requests.post(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['_id']:
                self.record_error('add_table error: %s' % result)
        except Exception as e:
            self.record_error('raise add_table error: %s' % e)
    
    def rename_table(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/tables/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid
        })
        json_data = {
            'table_name': "Table3",
            'new_table_name': "Table3_New"
        }
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('rename_table error: %s' % result)
        except Exception as e:
            self.record_error('raise rename_table error: %s' % e)
        
    
    def delete_table(self, table_name=None):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/tables/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid
        })
        json_data = {
            'table_name': table_name or "Table3_New",
        }
        try:
            resp = requests.delete(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('delete_table error: %s' % result)
        except Exception as e:
            self.record_error('raise delete_table error: %s' % e)
            
    def duplicate_table(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/tables/duplicate-table/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid
        })
        json_data = {
            'table_name': "Table1",
            'is_duplicate_records': True
        }
        try:
            resp = requests.post(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['name']:
                self.record_error('duplicate_table error: %s' % result)
            self.delete_table(result['name'])
        except Exception as e:
            self.record_error('raise duplicate_table error: %s' % e)
    
    def run_test(self):
        self.add_table()
        self.rename_table()
        self.delete_table()
        self.duplicate_table()
        
class ViewAPI(APIBase):
    def __init__(self, server_url, api_token, api_token_readonly):
        super(ViewAPI, self).__init__(server_url, api_token, api_token_readonly)

    def create_view(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/views/?table_name=%(table_name)s' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'table_name': table_name
        })
        json_data = {
            'name': 'New view',
        }
        try:
            resp = requests.post(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['_id']:
                self.record_error('add_view error: %s' % result)
            self.view_name = result['name']
        except Exception as e:
            self.record_error('raise add_view error: %s' % e)
        
    
    def get_view_by_name(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/views/%(view_name)s' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'view_name': self.view_name
        })
        json_data = {
            'table_name': table_name
        }
        try:
            resp = requests.get(url, params=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['_id']:
                self.record_error('get_view_by_name error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise get_view_by_name error: %s' % e)

    def update_view(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/views/%(view_name)s/?table_name=%(table_name)s' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'view_name': self.view_name,
            'table_name': table_name,
        })
        
        json_data = {
              "filters": [
                {
                  "column_key": "0000",
                  "filter_predicate": "contains",
                  "filter_term": "A"
                }
              ],
              "filter_conjunction": "And",
              "sorts": [
                {
                  "column_key": "0000",
                  "sort_type": "down"
                }
              ],
              "groupbys": [
                {
                  "column_key": "0000",
                  "sort_type": "down"
                }
              ],
              "name": "NewView"
            }
        
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['_id']:
                self.record_error('update_view error: %s' % result)
                return
            self.view_name = result['name']
        except Exception as e:
            self.record_error('raise update_view error: %s' % e)


        
    def list_views(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/views/?table_name=%(table_name)s' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'table_name': table_name
        })
        try:
            resp = requests.get(url, headers=self.base.headers)
            result = resp.json()
            if not result['views']:
                self.record_error('list_views error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise list_views error: %s' % e)
    
    def delete_view(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/views/%(view_name)s' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'view_name': self.view_name
        })
        json_data = {
            'table_name': table_name
        }
        try:
            resp = requests.delete(url, params=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('delete_view error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise delete_view error: %s' % e)
    
    
    def run_test(self):
        self.create_view()
        self.get_view_by_name()
        self.update_view()
        self.list_views()
        self.delete_view()
    
class ColumnAPI(APIBase):
    def __init__(self, server_url, api_token, api_token_readonly):
        super(ColumnAPI, self).__init__(server_url, api_token, api_token_readonly)
        
        
    def list_columns(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/columns/?table_name=%(table_name)s' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'table_name': table_name
        })

        try:
            resp = requests.get(url, headers=self.base.headers)
            result = resp.json()
            if not result['columns']:
                self.record_error('list_columns error: %s' % result)
                return
            
            s_col = [c for c in result['columns'] if c.get('name') == 'Options']
            options = s_col[0].get('data', {}).get('options')
            option_ids = [o.get('name') for o in options if o.get('id') != '938349']
            self.option_names = option_ids
        except Exception as e:
            self.record_error('raise list_columns error: %s' % e)

    def add_column(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/columns/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
          "column_type": "text",
          "table_name": "Table1",
          "column_name": "NewCol"
        }
    
        try:
            resp = requests.post(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['name']:
                self.record_error('list_columns error: %s' % result)
                return
            self.column_name = result['name']
        except Exception as e:
            self.record_error('raise list_columns error: %s' % e)
    
    
    def update_column(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/columns/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
            "op_type": "rename_column",
            "table_name": "Table1",
            "column": "NewCol",
            "new_column_name": "RNewCol"
        }
    
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not resp.ok:
                self.record_error('update_columns error: %s' % result)
                return
            self.column_name = "RNewCol"
        except Exception as e:
            self.record_error('raise update_columns error: %s' % e)
    
    
    def delete_column(self, column_name=None):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/columns/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
            "column": column_name or self.column_name,
            "table_name": "Table1"
        }
    
        try:
            resp = requests.delete(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('delete_columns error: %s' % result)
                return
            self.column_name = "RNewCol"
        except Exception as e:
            self.record_error('raise delete_columns error: %s' % e)
    
    
    def batch_add_columns(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/batch-append-columns/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
            "table_name": "Table1",
              "columns": [
                {
                  "column_name": "C",
                  "column_type": "text"
                },
                  {
                      "column_name": "N",
                      "column_type": "number"
                  }
              ]
            }
        
    
        try:
            resp = requests.post(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['columns']:
                self.record_error('list_columns error: %s' % result)
                return
            
            self.delete_column('C')
            self.delete_column('N')
        except Exception as e:
            self.record_error('raise list_columns error: %s' % e)
        
    
    def add_column_options(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/column-options/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
              "options": [
                {
                  "name": "O1",
                  "color": "#FF8000",
                  "textColor": "#DDDDDD"
                },
                {
                  "name": "O2",
                  "color": "#123456",
                  "textColor": "#1111111"
                }
              ],
              "column": "Options",
              "table_name": "Table1"
        }
    
        try:
            resp = requests.post(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('add_column_options error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise add_column_options error: %s' % e)
    
    
    def update_column_options(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/column-options/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
              "return_options": True,
              "column": "Options",
              "table_name": "Table1",
              "options": [
                {
                  "id": "938349",
                  "color": "#4ECCCB",
                  "textColor": "#1DDD1D",
                  "name": "O100"
                }
              ]
            }
        
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['options']:
                self.record_error('update_column_options error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise update_column_options error: %s' % e)

    def delete_column_options(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/column-options/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
                  "option_names": self.option_names,
                  "column": "Options",
                  "table_name": "Table1"
                }
    
        try:
            resp = requests.delete(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('delete_column_options error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise delete_column_options error: %s' % e)
    
    def run_test(self):
        self.add_column()
        self.update_column()
        self.delete_column()
        self.batch_add_columns()
        self.add_column_options()
        self.update_column_options()
        self.list_columns()
        self.delete_column_options()
        
class RowAPI(APIBase):
    def __init__(self, server_url, api_token, api_token_readonly):
        super(RowAPI, self).__init__(server_url, api_token, api_token_readonly)
        
    def append_row(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/rows/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'table_name': table_name
        })
        json_data = {
            'table_name': table_name,
            'row': {'Name': "Test"},
        }
    
        try:
            resp = requests.post(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['_id']:
                self.record_error('append_row error: %s' % result)
                return
            self.row_id = result['_id']
        except Exception as e:
            self.record_error('raise append_row error: %s' % e)
    
    def update_row(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/rows/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'table_name': table_name
        })
        json_data = {
            'table_name': table_name,
            'row': {'Name': "TestUpdate"},
            'row_id': self.row_id
        }
    
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('update_row error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise update_row error: %s' % e)
    
    def lock_row(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/lock-rows/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'table_name': table_name
        })
        json_data = {
                  "row_ids": [
                    self.row_id
                  ],
                  "table_name": table_name
                }
    
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('lock_row error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise lock_row error: %s' % e)
    
    def unlock_row(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/unlock-rows/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'table_name': table_name
        })
        json_data = {
            "row_ids": [
                self.row_id
            ],
            "table_name": table_name
        }
    
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('unlock_row error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise unlock_row error: %s' % e)
    
    def delete_row(self, row_id=None):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/rows/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
            'table_name': table_name
        })
        json_data = {
            'table_name': table_name,
            'row': {'Name': "TestUpdate"},
            'row_id': row_id or self.row_id
        }
    
        try:
            resp = requests.delete(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['deleted_rows']:
                self.record_error('delete_row error: %s' % result)
                return
        except Exception as e:
            self.record_error('raise delete_row error: %s' % e)
    
    def batch_append_rows(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/batch-append-rows/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
            'table_name': table_name,
            'rows': [
                {'Name': '0'},
                {'Name': '1'}
            ],
            'return_rows': True,
        }
    
        try:
            resp = requests.post(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['rows']:
                self.record_error('batch_append_rows error: %s' % result)
                return
            
            self.row_ids = [r.get('_id') for r in result['rows']]
        except Exception as e:
            self.record_error('raise batch_append_row error: %s' % e)
    
    
    def batch_update_rows(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/batch-update-rows/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
            'table_name': table_name,
            'updates': [
                {
                    "row_id": self.row_ids[0],
                    "row": {'Name': 'BatchUpdatedRows0'}
                },
                {
                    "row_id": self.row_ids[1],
                    "row": {'Name': 'BatchUpdatedRows1'}
                }
            ]
        }
    
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('batch_update_rows error: %s' % result)
                return
        
        except Exception as e:
            self.record_error('raise batch_update_row error: %s' % e)
    
    
    def batch_delete_rows(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/batch-delete-rows/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
            'table_name': table_name,
            'row_ids': self.row_ids,
        }
    
        try:
            resp = requests.delete(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['deleted_rows']:
                self.record_error('batch_delete_rows error: %s' % result)
                return
        
        except Exception as e:
            self.record_error('raise batch_delete_row error: %s' % e)
    
    def run_test(self):
        self.append_row()
        self.update_row()
        self.lock_row()
        self.unlock_row()
        self.delete_row()
        self.batch_append_rows()
        self.batch_update_rows()
        self.batch_delete_rows()
    
    
class LinkAPI(APIBase):
    def __init__(self, server_url, api_token, api_token_readonly):
        super(LinkAPI, self).__init__(server_url, api_token, api_token_readonly)
        
        
    def update_links(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/links/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
            'table_name': table_name,
            'other_table_name': link_table_name,
            'link_id':'EDHV',
            'row_id': 'BMF8RsaQRcyelMAr0ew6tw',
            'other_rows_ids': ['RqZUdbXsTmqBVZzNQNvNFg', 'RMdv4bd7SumIz308PKf-7Q']
        }
    
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('update_links error: %s' % result)
                return
    
        except Exception as e:
            self.record_error('raise update_links error: %s' % e)
    
    
    def batch_update_links(self):
        url = '%(dtable_server_url)s/api/v1/dtables/%(dtable_uuid)s/batch-update-links/' % ({
            'dtable_server_url': self.base.dtable_server_url,
            'dtable_uuid': self.base.dtable_uuid,
        })
        json_data = {
            'table_name': table_name,
            'other_table_name': link_table_name,
            'link_id': 'EDHV',
            'row_id_list': ['BMF8RsaQRcyelMAr0ew6tw'],
            'other_rows_ids_map': {
                'BMF8RsaQRcyelMAr0ew6tw': ['RqZUdbXsTmqBVZzNQNvNFg', 'RMdv4bd7SumIz308PKf-7Q']
            }
            
        }
    
        try:
            resp = requests.put(url, json=json_data, headers=self.base.headers)
            result = resp.json()
            if not result['success']:
                self.record_error('batch_update_links error: %s' % result)
                return
    
        except Exception as e:
            self.record_error('raise batch_update_links error: %s' % e)
    
    
    def run_test(self):
        self.update_links()
        self.batch_update_links()
        
        
        
class APIGateWay(APIBase):
    def __init__(self, server_url, api_token, api_token_readonly):
        super(APIGateWay, self).__init__(server_url, api_token, api_token_readonly)
        self.base.use_api_gateway = True
        
    def list_rows(self):
        res = self.base.list_rows('Table1')
        print(res)
    
    def run_test(self):
        self.list_rows()
        
        
    
    
    
class MainTest(object):
    
    
    def __init__(self, server_url, api_token, api_token_readonly, test_classes=None):
        self.test_classes = test_classes
        self.total_errors = 0
        self.server_url = server_url
        self.api_token = api_token
        self.api_token_readonly = api_token_readonly
        self.total_error_msgs = []
        
    def run_test(self):
        for cls in self.test_classes:
            test_obj = cls(self.server_url, self.api_token, self.api_token_readonly)
            test_obj.run_test()
            self.total_errors += test_obj.error_count
            self.total_error_msgs.extend(test_obj.error_msgs)
            
        return self.total_errors, self.total_error_msgs
        
    
def main():
    server_url = SERVER_URL_FOR_GO
    api_token = BASE_API_TOKEN_FOR_GO
    api_token_readonly = BASE_API_TOKEN_FOR_GO_READONLY
    
    
    result_base_token = BASE_API_TOKEN_FOR_GO_TEST_RESULT
    result_server_url = SERVER_URL

    
    # test meta_api
    test_classes = [
        MetaAPI,
        TableAPI,
        ViewAPI,
        ColumnAPI,
        RowAPI,
        LinkAPI,
        # APIGateWay,
    ]
    test_obj = MainTest(server_url, api_token, api_token_readonly, test_classes)
    err_cnt, err_msgs = test_obj.run_test()
    
    
    result_base = Base(result_base_token, result_server_url)
    result_base.auth()
    result_base.append_row('Test', {
        'FailNo': err_cnt,
        'ErrorMsg': '\n'.join(err_msgs)
    })
    
    
    
    
    

if __name__ == '__main__':
    
    main()