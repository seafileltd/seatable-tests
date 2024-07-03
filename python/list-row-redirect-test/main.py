EXPECTED_RESULT = {
    '文本': 'AA',
    '长文本': 'fsfvvcxvvxvzs\n',
    '数字': 10,
    '数字（百分数）': 1,
    '数字（人民币格式数字）': 100,
    '数字（美元格式数字）': 90,
    '数字（欧元格式数字）': 300,
    '数字（自定义货币格式）': 1000,
    '数字（逗号小数点空格千分位精度小数点后两位）': 19925,
    '数字（长小数点百分数）': 19.92353535,
    '数字（空格千分位）': 94534581,
    '协作人': ['jiwei.ran@seafile.com'],
    '日期 （ISO格式）': '2024-06-04',
    '日期 （ISO精确到分钟）': '2024-06-13 10:35',
    '日期（美国格式）': '2024-06-14',
    '日期（美国格式精确到分钟）': '2024-06-12 10:35',
    '日期（欧洲格式）': '2024-06-05',
    '日期（欧洲格式精确到分钟）': '2024-06-05 10:00',
    '日期（德国格式）': '2024-06-10',
    '日期（德国格式精确到分钟）': '2024-06-14 09:30',
    '时长（分钟）': 5400,
    '时长（秒）': 5456,
    '单选': 'A',
    '多选': ["B","A","C"],
    '图片': ['https://dev.seatable.cn/workspace/8/asset/6ae6da82-90fb-4d55-b140-4a78ce59a494/images/2024-07/02.png'],
    '邮件': 'support@seafile.com',
    'URL': 'https://dev.seatable.cn',
    '勾选': True,
    '评分': 8,
    '地理位置': {
                "province": "江苏省",
                "city": "常州市",
                "district": "新北区",
                "detail": "新南路江南小区19栋2单元22号"
                },
    '创建时间': '2024-07-01T03:29:20.623+00:00',
    '修改时间': '2024-07-01T09:34:14.348+00:00',
    '自动序号': '0001',
    '创建人': 'jiwei.ran@seafile.com',
    '修改人': 'jiwei.ran@seafile.com',
    '按钮': None,
    '部门': 9,
    '返回时间的公式（欧洲格式）': '05/06/2024',
    '返回时间的公式（欧洲格式精确到分钟）': '05/06/2024 10:00',
    '返回时间的公式（德国格式）': '10.06.2024',
    '返回时间的公式（德国格式精确到分钟）': '14.06.2024 09:30',
    '返回时间的公式（ISO格式）': '2024-06-04',
    '返回时间的公式（ISO精确到分钟）': '2024-06-13 10:35',
    '返回时间的公式（美国格式）': '6/14/2024',
    '返回时间的公式（美国格式精确到分钟）': '6/12/2024 10:35',
    '链接列': ['YVGwSfrSTAuJZTfK2i9G3w', 'GlV_FVsNTgS3N7R-6CxLLQ'],
    '返回数组的链接公式': ['AA', 'BB']
}


def write_msg(base, err_msg=None):
    data = {
        'Success': 'Yes',
    }
    if err_msg:
        data['Success'] = 'No'
        data['Errors'] = err_msg
        
    base.append_row('TestResults', data)



def run_test(base):
    row = base.list_rows(RAW_TABLE)[0]
    
    row.pop('_locked')
    row.pop('_locked_by')
    row.pop('_archived')
    row.pop('_id')
    row_keys = row.keys()
    err_msgs = []
    if len(row_keys) != len(EXPECTED_RESULT.keys()):
        err_msgs.append('error: %s' % 'returned data missed')
        
    if set(row_keys) != set(EXPECTED_RESULT.keys()):
        err_msgs.append('error: %s' % 'inconsistency of returned data')
        
    
    for col_name, expected_results in EXPECTED_RESULT.items():
        try:
            res = row[col_name]
            if res != expected_results:
                err_msgs.append('Unexpected results: col_name: %s, expected: %s, retured: %s' % (
                    col_name,
                    expected_results,
                    res
                ))
        except Exception as e:
            err_msgs.append(str(e))
            continue
    write_msg(base, '\n'.join(err_msgs))
        
        

if __name__ == '__main__':
    from seatable_api import Base
    
    api_token = "d33e8c40c16d6a3c78ee86ff623ed892b8f0a746"
    server_url = "https://dev.seatable.cn"
    
    base = Base(api_token, server_url)
    base.auth()
    
    base.use_api_gateway = False
    
    RAW_TABLE = 'Raw Table'
    
    run_test(base)