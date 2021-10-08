REFERENCES = [
    {
        "type": 'Map',
        "sql": "Select * from Table1 limit 1",
        "expected_result": [
            {
                "文本": "AA",
                "数字": 10,
                # 小数
                "数字1": 4.55,
                # 货币
                "数字2": 597.20,
                "日期": "2021-09-26",
                "单选": "男",
                "图片": [
                    "https://dev.seatable.cn/workspace/8/asset/469575a8-3422-42ed-b333-542ef9aa9e8e/images/2021-09/06.png"],
                "日期带分钟": "2021-09-29 09:30:00",
                "文件": [{
                    'name': '设计任务.dtable',
                    'size': 22,
                    'type': 'file',
                    'url': 'https://dev.seatable.cn/workspace/8/asset/469575a8-3422-42ed-b333-542ef9aa9e8e/files/2021-09/%E8%AE%BE%E8%AE%A1%E4%BB%BB%E5%8A%A1.dtable'
                }],
                "_participants": [],
                "_id": "G9c0P_fmQ8WG-lL5RG8bng",
                "邮箱": "350178982@qq.com",
                "勾选": True,
                "长文本": """### Introduction\n\n##### Abstract\n\nLong  long time ago....\n\n```python\nprint(111)\n\n```\n\n`Select * from Table1`\n\n> haahaha\n\n* Hello\n* Salute\n\n1. Hello1\n2. Salute1\n\n\n""",
                "协作人": ["jiwei.ran@seafile.com"],
                "时长": 3 * 3600 + 43 * 60,
                "多选": ['击剑', '足球'],
                "URL": "https://www.baidu.com",
                "评分": 4,
                "公式": 20,
                "链接其他记录": [{'row_id': 'VVvX3I8ISSSBN8-nqRlshQ', 'display_value': 'aa'},
                           {'row_id': 'VuCer3xMTs-9g3NoUKkR2g', 'display_value': 'cc'}],
                "链接公式": 2,
                "地理位置": {
                    'city': '北京市',
                    'detail': '回龙观新村东区2-3-1001',
                    'district': '昌平区',
                    'province': '北京市'
                },
                # 经纬度
                "地理位置2": {'lat': 42.5158032188098, 'lng': 113.20517001118883},
                # 国家/地区
                "地理位置3": {'country_region': '中国'},
                "创建者": "jiwei.ran@seafile.com",
                "修改者": "jiwei.ran@seafile.com",
                "创建时间": "2021-09-26T02:39:57.067Z",
                "修改时间": "2021-09-30T03:58:55.052Z",
                "自动序号": "Test-0001"
            }
        ]
    },
    {
        'type': 'GroupBy',
        'sql': "Select 文本,sum(数字) from Table1 group by 文本",
        'expected_result': [
            {'文本': 'AA', 'SUM(数字)': 30},
            {'文本': 'BB', 'SUM(数字)': 80}
        ]
    },
    {
        'type': 'GroupBy',
        'sql': "Select 单选, avg(数字) from Table1 group by 单选",
        'expected_result': [
            {'单选': '男', 'AVG(数字)': 30},
            {'单选': '女', 'AVG(数字)': 25}
        ]
    },
    {
        'type': 'GroupBy',
        'sql': "select  协作人, max(数字) from Table1 group by 协作人",
        'expected_result': [
            {'协作人': ['jiwei.ran@seafile.com'], 'MAX(数字)': 20},
            {'协作人': ['7406dc1aac61494cab5bca6c3fe958c1@auth.local'], 'MAX(数字)': 50}
        ]
    },
    {
        'type': 'GroupBy',
        'sql': "select  多选, min(数字) from Table1 group by 多选",
        'expected_result': [
            {'多选': ['击剑', '足球'], 'MIN(数字)': 10},
            {'多选': ['篮球', '击剑'], 'MIN(数字)': 20}
        ]
    },

    {
        'type': 'OrderBy',
        'sql': "select  文本, 数字, 评分 from Table1 order by 数字",
        'expected_result': [
            {"文本": 'AA', "数字": 10, "_id": 'G9c0P_fmQ8WG-lL5RG8bng', '评分': 4},
            {"文本": 'AA', "数字": 20, "_id": 'COASY7zyRaOUZAWKyFEyzQ', '评分': 5},
            {"文本": 'BB', "数字": 30, "_id": 'RKMQdKjQTamnaP23JrOZ1w', '评分': 3},
            {"文本": 'BB', "数字": 50, "_id": 'LWTLEcPRRj2eBtEDD7xbOQ', '评分': 1},
        ]
    },
    {
        'type': 'OrderBy',
        'sql': "select  文本, 数字, 评分 from Table1 order by 评分 DESC",
        'expected_result': [
            {"文本": 'AA', "数字": 20, "_id": 'COASY7zyRaOUZAWKyFEyzQ', '评分': 5},
            {"文本": 'AA', "数字": 10, "_id": 'G9c0P_fmQ8WG-lL5RG8bng', '评分': 4},
            {"文本": 'BB', "数字": 30, "_id": 'RKMQdKjQTamnaP23JrOZ1w', '评分': 3},
            {"文本": 'BB', "数字": 50, "_id": 'LWTLEcPRRj2eBtEDD7xbOQ', '评分': 1},
        ]
    },
    {
        'type': 'Common',
        'sql': "select 文本, 数字, 评分, URL, 邮箱, 单选 from Table1 where 单选='女' ",
        'expected_result': [
            {"文本": 'AA', '单选': '女', '数字': 20, "_id": 'COASY7zyRaOUZAWKyFEyzQ', '评分': 5, 'URL': 'https://google.com',
             '邮箱': 'r350178982@qq.com'},
            {"文本": 'BB', '单选': '女', '数字': 30, "_id": 'RKMQdKjQTamnaP23JrOZ1w', '评分': 3,
             'URL': 'https://cloud.seatable.io', '邮箱': 'ran.jiwei@seafile.com'},
        ]

    },
    {
        'type': 'Common',
        'sql': "select distinct 单选, 多选 from Table1",
        'expected_result': [
            {"单选": "男", "多选": ["击剑", "足球"], '_id': 'G9c0P_fmQ8WG-lL5RG8bng'},
            {"单选": "女", "多选": ['篮球', '击剑'], '_id': 'COASY7zyRaOUZAWKyFEyzQ'},
        ]

    },
    {
        'type': 'Common',
        'sql':  "select URL from Table1 where URL like '%com'",
        'expected_result':[
            {'_id':'COASY7zyRaOUZAWKyFEyzQ','URL':'https://google.com'},
            {'_id':'G9c0P_fmQ8WG-lL5RG8bng','URL':'https://www.baidu.com'},
        ]
    },
    {
        'type': 'Common',
        'sql':  "select 文本, 数字, 邮箱 from Table1 where 文本='AA' and 数字 < 30",
        'expected_result':[
            {'_id':'COASY7zyRaOUZAWKyFEyzQ','文本':'AA', '邮箱':'r350178982@qq.com', '数字':20},
            {'_id':'G9c0P_fmQ8WG-lL5RG8bng','文本':'AA', '邮箱':'350178982@qq.com', '数字':10},
        ]
    },
    {
        'type': 'Common',
        'sql':  "select 文本, 数字, 邮箱, URL, 日期 from Table1 where 日期 BETWEEN '2021-09-01' AND '2021-09-20'",
        'expected_result':[
            {'_id':'RKMQdKjQTamnaP23JrOZ1w','文本':'BB', '邮箱':'ran.jiwei@seafile.com', '数字':30,'URL':'https://cloud.seatable.io','日期':'2021-09-16'},
        ]
    },
    {
        'type': 'Common',
        'sql': "select 日期, Quarter(`日期`), ISODate(`日期`), ISOMonth(`日期`) from Table1",
        'expected_result':[
            {'日期': '2021-09-26', 'ISODATE(`日期`)': '2021-09-26', 'ISOMONTH(`日期`)': '2021-09', 'QUARTER(`日期`)': 3, '_id': 'G9c0P_fmQ8WG-lL5RG8bng'},
            {'日期': '2021-09-27', 'ISODATE(`日期`)': '2021-09-27', 'ISOMONTH(`日期`)': '2021-09', 'QUARTER(`日期`)': 3, '_id': 'COASY7zyRaOUZAWKyFEyzQ'},
            {'日期': '2021-03-02', 'ISODATE(`日期`)': '2021-03-02', 'ISOMONTH(`日期`)': '2021-03', 'QUARTER(`日期`)': 1, '_id': 'LWTLEcPRRj2eBtEDD7xbOQ'},
            {'日期': '2021-09-16', 'ISODATE(`日期`)': '2021-09-16', 'ISOMONTH(`日期`)': '2021-09', 'QUARTER(`日期`)': 3, '_id': 'RKMQdKjQTamnaP23JrOZ1w'}
        ]
    },
    {
        'type': 'Common',
        'sql': "select 数字, add(`数字`, 25), subtract(`数字`, 5), multiply(`数字`, `数字`), divide(`数字`,2), mod(`数字`,3), power(`数字`,2) from Table1",
        'expected_result':[
            {'ADD(`数字`, 25)': 35, 'DIVIDE(`数字`,2)': 5, 'MOD(`数字`,3)': 1, 'MULTIPLY(`数字`, `数字`)': 100, 'POWER(`数字`,2)': 100, 'SUBTRACT(`数字`, 5)': 5, '_id': 'G9c0P_fmQ8WG-lL5RG8bng', '数字': 10},
            {'ADD(`数字`, 25)': 45, 'DIVIDE(`数字`,2)': 10, 'MOD(`数字`,3)': 2, 'MULTIPLY(`数字`, `数字`)': 400, 'POWER(`数字`,2)': 400, 'SUBTRACT(`数字`, 5)': 15, '_id': 'COASY7zyRaOUZAWKyFEyzQ', '数字': 20},
            {'ADD(`数字`, 25)': 75, 'DIVIDE(`数字`,2)': 25, 'MOD(`数字`,3)': 2, 'MULTIPLY(`数字`, `数字`)': 2500, 'POWER(`数字`,2)': 2500, 'SUBTRACT(`数字`, 5)': 45, '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', '数字': 50},
            {'ADD(`数字`, 25)': 55, 'DIVIDE(`数字`,2)': 15, 'MOD(`数字`,3)': 0, 'MULTIPLY(`数字`, `数字`)': 900, 'POWER(`数字`,2)': 900, 'SUBTRACT(`数字`, 5)': 25, '_id': 'RKMQdKjQTamnaP23JrOZ1w', '数字': 30}
       ]
    },
    {
        'type': 'Common',
        'sql': "select 数字, greater(`数字`, 20), lessthan(`数字`, 30), greatereq(`数字`, 50), lessthaneq(`数字`,10), equal(`数字`,20), unequal(`数字`,30) from Table1",
        'expected_result':[
            {'EQUAL(`数字`,20)': False, 'GREATER(`数字`, 20)': False, 'GREATEREQ(`数字`, 50)': False, 'LESSTHAN(`数字`, 30)': True, 'LESSTHANEQ(`数字`,10)': True, 'UNEQUAL(`数字`,30)': -20, '_id': 'G9c0P_fmQ8WG-lL5RG8bng', '数字': 10},
            {'EQUAL(`数字`,20)': True, 'GREATER(`数字`, 20)': False, 'GREATEREQ(`数字`, 50)': False, 'LESSTHAN(`数字`, 30)': True, 'LESSTHANEQ(`数字`,10)': False, 'UNEQUAL(`数字`,30)': -10, '_id': 'COASY7zyRaOUZAWKyFEyzQ', '数字': 20},
            {'EQUAL(`数字`,20)': False, 'GREATER(`数字`, 20)': True, 'GREATEREQ(`数字`, 50)': True, 'LESSTHAN(`数字`, 30)': False, 'LESSTHANEQ(`数字`,10)': False, 'UNEQUAL(`数字`,30)': 20, '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', '数字': 50},
            {'EQUAL(`数字`,20)': False, 'GREATER(`数字`, 20)': True, 'GREATEREQ(`数字`, 50)': False, 'LESSTHAN(`数字`, 30)': False, 'LESSTHANEQ(`数字`,10)': False, 'UNEQUAL(`数字`,30)': 0, '_id': 'RKMQdKjQTamnaP23JrOZ1w', '数字': 30}
        ]
    },
    {
        'type': 'Common',
        'sql': "select 文本, URL, exact(`文本`,'AA'), find('goo',`URL`, 1), left(`URL`,5), len(`URL`), lower(`文本`), mid(`邮箱`, 1, 8), replace(`邮箱`, 1, 8, '12345678'), rept(`文本`, 2), right(`URL`, 5), search('www',`URL`,1), substitute(`邮箱`, '@', '^^',1) from Table1",
        'expected_result':[
            {'文本': 'AA', "EXACT(`文本`,'AA')": True, "FIND('goo',`URL`, 1)": 0, 'LEFT(`URL`,5)': 'https', 'LEN(`URL`)': 21, 'LOWER(`文本`)': 'aa', 'MID(`邮箱`, 1, 8)': '35017898', "REPLACE(`邮箱`, 1, 8, '12345678')": '123456782@qq.com', 'REPT(`文本`, 2)': 'AAAA', 'RIGHT(`URL`, 5)': 'u.com', "SEARCH('www',`URL`,1)": 9, "SUBSTITUTE(`邮箱`, '@', '^^',1)": '350178982^^qq.com', '_id': 'G9c0P_fmQ8WG-lL5RG8bng', 'URL': 'https://www.baidu.com'},
            {'文本': 'AA', "EXACT(`文本`,'AA')": True, "FIND('goo',`URL`, 1)": 9, 'LEFT(`URL`,5)': 'https', 'LEN(`URL`)': 18, 'LOWER(`文本`)': 'aa', 'MID(`邮箱`, 1, 8)': 'r3501789', "REPLACE(`邮箱`, 1, 8, '12345678')": '1234567882@qq.com', 'REPT(`文本`, 2)': 'AAAA', 'RIGHT(`URL`, 5)': 'e.com', "SEARCH('www',`URL`,1)": 0, "SUBSTITUTE(`邮箱`, '@', '^^',1)": 'r350178982^^qq.com', '_id': 'COASY7zyRaOUZAWKyFEyzQ', 'URL': 'https://google.com'},
            {'文本': 'BB', "EXACT(`文本`,'AA')": False, "FIND('goo',`URL`, 1)": 0, 'LEFT(`URL`,5)': 'https', 'LEN(`URL`)': 23, 'LOWER(`文本`)': 'bb', 'MID(`邮箱`, 1, 8)': 'rjw@gmai', "REPLACE(`邮箱`, 1, 8, '12345678')": '12345678l.com', 'REPT(`文本`, 2)': 'BBBB', 'RIGHT(`URL`, 5)': 'le.cn', "SEARCH('www',`URL`,1)": 0, "SUBSTITUTE(`邮箱`, '@', '^^',1)": 'rjw^^gmail.com', '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', 'URL': 'https://dev.seatable.cn'},
            {'文本': 'BB', "EXACT(`文本`,'AA')": False, "FIND('goo',`URL`, 1)": 0, 'LEFT(`URL`,5)': 'https', 'LEN(`URL`)': 25, 'LOWER(`文本`)': 'bb', 'MID(`邮箱`, 1, 8)': 'ran.jiwe', "REPLACE(`邮箱`, 1, 8, '12345678')": '12345678i@seafile.com', 'REPT(`文本`, 2)': 'BBBB', 'RIGHT(`URL`, 5)': 'le.io', "SEARCH('www',`URL`,1)": 0, "SUBSTITUTE(`邮箱`, '@', '^^',1)": 'ran.jiwei^^seafile.com', '_id': 'RKMQdKjQTamnaP23JrOZ1w', 'URL': 'https://cloud.seatable.io'}]
    },



]
