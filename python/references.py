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
                "修改时间": "2021-09-30T03:54:32.473Z",
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
    }

]
