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
                "链接其他记录": [{'row_id': 'VuCer3xMTs-9g3NoUKkR2g', 'display_value': 'cc'}],
                "链接公式": 1,
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
                # "修改时间": "2021-09-30T03:58:55.052Z",
                "自动序号": "Test-0001",
                # "Year":[{'row_id': 'VuCer3xMTs-9g3NoUKkR2g', 'display_value': 2019}],
                "Year": [2019],
                "if": 1,
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
            {'单选': '男', 'avg(数字)': 30},
            {'单选': '女', 'avg(数字)': 25}
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
        'sql': "select  _id, 文本, 数字, 评分 from Table1 order by 数字",
        'expected_result': [
            {"文本": 'AA', "数字": 10, "_id": 'G9c0P_fmQ8WG-lL5RG8bng', '评分': 4},
            {"文本": 'AA', "数字": 20, "_id": 'COASY7zyRaOUZAWKyFEyzQ', '评分': 5},
            {"文本": 'BB', "数字": 30, "_id": 'RKMQdKjQTamnaP23JrOZ1w', '评分': 3},
            {"文本": 'BB', "数字": 50, "_id": 'LWTLEcPRRj2eBtEDD7xbOQ', '评分': 1},
        ]
    },
    {
        'type': 'OrderBy',
        'sql': "select  _id, 文本, 数字, 评分 from Table1 order by 评分 DESC",
        'expected_result': [
            {"文本": 'AA', "数字": 20, "_id": 'COASY7zyRaOUZAWKyFEyzQ', '评分': 5},
            {"文本": 'AA', "数字": 10, "_id": 'G9c0P_fmQ8WG-lL5RG8bng', '评分': 4},
            {"文本": 'BB', "数字": 30, "_id": 'RKMQdKjQTamnaP23JrOZ1w', '评分': 3},
            {"文本": 'BB', "数字": 50, "_id": 'LWTLEcPRRj2eBtEDD7xbOQ', '评分': 1},
        ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 文本, 数字, 评分, URL, 邮箱, 单选 from Table1 where 单选='女' ",
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
            {"单选": "男", "多选": ["击剑", "足球"], },
            {"单选": "女", "多选": ['篮球', '击剑'], },
        ]

    },
    {
        'type': 'Common',
        'sql':  "select _id, URL from Table1 where URL like '%com'",
        'expected_result':[
            {'_id':'COASY7zyRaOUZAWKyFEyzQ','URL':'https://google.com'},
            {'_id':'G9c0P_fmQ8WG-lL5RG8bng','URL':'https://www.baidu.com'},
        ]
    },
    {
        'type': 'Common',
        'sql':  "select _id, 文本, 数字, 邮箱 from Table1 where 文本='AA' and 数字 < 30",
        'expected_result':[
            {'_id':'COASY7zyRaOUZAWKyFEyzQ','文本':'AA', '邮箱':'r350178982@qq.com', '数字':20},
            {'_id':'G9c0P_fmQ8WG-lL5RG8bng','文本':'AA', '邮箱':'350178982@qq.com', '数字':10},
        ]
    },
    {
        'type': 'Common',
        'sql':  "select _id, 文本, 数字, 邮箱, URL, 日期 from Table1 where 日期 BETWEEN '2021-09-01' AND '2021-09-20'",
        'expected_result':[
            {'_id':'RKMQdKjQTamnaP23JrOZ1w','文本':'BB', '邮箱':'ran.jiwei@seafile.com', '数字':30,'URL':'https://cloud.seatable.io','日期':'2021-09-16'},
        ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 日期, Quarter(`日期`), ISODate(`日期`), ISOMonth(`日期`) from Table1",
        'expected_result':[
            {'日期': '2021-09-26', 'ISODATE(`日期`)': '2021-09-26', 'ISOMONTH(`日期`)': '2021-09', 'QUARTER(`日期`)': 3, '_id': 'G9c0P_fmQ8WG-lL5RG8bng'},
            {'日期': '2021-09-27', 'ISODATE(`日期`)': '2021-09-27', 'ISOMONTH(`日期`)': '2021-09', 'QUARTER(`日期`)': 3, '_id': 'COASY7zyRaOUZAWKyFEyzQ'},
            {'日期': '2021-03-02', 'ISODATE(`日期`)': '2021-03-02', 'ISOMONTH(`日期`)': '2021-03', 'QUARTER(`日期`)': 1, '_id': 'LWTLEcPRRj2eBtEDD7xbOQ'},
            {'日期': '2021-09-16', 'ISODATE(`日期`)': '2021-09-16', 'ISOMONTH(`日期`)': '2021-09', 'QUARTER(`日期`)': 3, '_id': 'RKMQdKjQTamnaP23JrOZ1w'}
        ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 数字, add(`数字`, 25), subtract(`数字`, 5), multiply(`数字`, `数字`), divide(`数字`,2), mod(`数字`,3), power(`数字`,2) from Table1",
        'expected_result':[
            {'ADD(`数字`, 25)': 35, 'DIVIDE(`数字`,2)': 5, 'MOD(`数字`,3)': 1, 'MULTIPLY(`数字`, `数字`)': 100, 'POWER(`数字`,2)': 100, 'SUBTRACT(`数字`, 5)': 5, '_id': 'G9c0P_fmQ8WG-lL5RG8bng', '数字': 10},
            {'ADD(`数字`, 25)': 45, 'DIVIDE(`数字`,2)': 10, 'MOD(`数字`,3)': 2, 'MULTIPLY(`数字`, `数字`)': 400, 'POWER(`数字`,2)': 400, 'SUBTRACT(`数字`, 5)': 15, '_id': 'COASY7zyRaOUZAWKyFEyzQ', '数字': 20},
            {'ADD(`数字`, 25)': 75, 'DIVIDE(`数字`,2)': 25, 'MOD(`数字`,3)': 2, 'MULTIPLY(`数字`, `数字`)': 2500, 'POWER(`数字`,2)': 2500, 'SUBTRACT(`数字`, 5)': 45, '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', '数字': 50},
            {'ADD(`数字`, 25)': 55, 'DIVIDE(`数字`,2)': 15, 'MOD(`数字`,3)': 0, 'MULTIPLY(`数字`, `数字`)': 900, 'POWER(`数字`,2)': 900, 'SUBTRACT(`数字`, 5)': 25, '_id': 'RKMQdKjQTamnaP23JrOZ1w', '数字': 30}
       ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 数字, greater(`数字`, 20), lessthan(`数字`, 30), greatereq(`数字`, 50), lessthaneq(`数字`,10), equal(`数字`,20), unequal(`数字`,30) from Table1",
        'expected_result':[
            {'EQUAL(`数字`,20)': False, 'GREATER(`数字`, 20)': False, 'GREATEREQ(`数字`, 50)': False, 'LESSTHAN(`数字`, 30)': True, 'LESSTHANEQ(`数字`,10)': True, 'UNEQUAL(`数字`,30)': True, '_id': 'G9c0P_fmQ8WG-lL5RG8bng', '数字': 10},
            {'EQUAL(`数字`,20)': True, 'GREATER(`数字`, 20)': False, 'GREATEREQ(`数字`, 50)': False, 'LESSTHAN(`数字`, 30)': True, 'LESSTHANEQ(`数字`,10)': False, 'UNEQUAL(`数字`,30)': True, '_id': 'COASY7zyRaOUZAWKyFEyzQ', '数字': 20},
            {'EQUAL(`数字`,20)': False, 'GREATER(`数字`, 20)': True, 'GREATEREQ(`数字`, 50)': True, 'LESSTHAN(`数字`, 30)': False, 'LESSTHANEQ(`数字`,10)': False, 'UNEQUAL(`数字`,30)': True, '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', '数字': 50},
            {'EQUAL(`数字`,20)': False, 'GREATER(`数字`, 20)': True, 'GREATEREQ(`数字`, 50)': False, 'LESSTHAN(`数字`, 30)': False, 'LESSTHANEQ(`数字`,10)': False, 'UNEQUAL(`数字`,30)': False, '_id': 'RKMQdKjQTamnaP23JrOZ1w', '数字': 30}
        ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 文本, URL, exact(`文本`,'AA'), find('goo',`URL`, 1), left(`URL`,5), len(`URL`), lower(`文本`), mid(`邮箱`, 1, 8), replace(`邮箱`, 1, 8, '12345678'), rept(`文本`, 2), right(`URL`, 5), search('www',`URL`,1), substitute(`邮箱`, '@', '^^',1) from Table1",
        'expected_result':[
            {'文本': 'AA', "EXACT(`文本`,'AA')": True, "FIND('goo',`URL`, 1)": 0, 'LEFT(`URL`,5)': 'https', 'LEN(`URL`)': 21, 'LOWER(`文本`)': 'aa', 'MID(`邮箱`, 1, 8)': '35017898', "REPLACE(`邮箱`, 1, 8, '12345678')": '123456782@qq.com', 'REPT(`文本`, 2)': 'AAAA', 'RIGHT(`URL`, 5)': 'u.com', "SEARCH('www',`URL`,1)": 9, "SUBSTITUTE(`邮箱`, '@', '^^',1)": '350178982^^qq.com', '_id': 'G9c0P_fmQ8WG-lL5RG8bng', 'URL': 'https://www.baidu.com'},
            {'文本': 'AA', "EXACT(`文本`,'AA')": True, "FIND('goo',`URL`, 1)": 9, 'LEFT(`URL`,5)': 'https', 'LEN(`URL`)': 18, 'LOWER(`文本`)': 'aa', 'MID(`邮箱`, 1, 8)': 'r3501789', "REPLACE(`邮箱`, 1, 8, '12345678')": '1234567882@qq.com', 'REPT(`文本`, 2)': 'AAAA', 'RIGHT(`URL`, 5)': 'e.com', "SEARCH('www',`URL`,1)": 0, "SUBSTITUTE(`邮箱`, '@', '^^',1)": 'r350178982^^qq.com', '_id': 'COASY7zyRaOUZAWKyFEyzQ', 'URL': 'https://google.com'},
            {'文本': 'BB', "EXACT(`文本`,'AA')": False, "FIND('goo',`URL`, 1)": 0, 'LEFT(`URL`,5)': 'https', 'LEN(`URL`)': 23, 'LOWER(`文本`)': 'bb', 'MID(`邮箱`, 1, 8)': 'rjw@gmai', "REPLACE(`邮箱`, 1, 8, '12345678')": '12345678l.com', 'REPT(`文本`, 2)': 'BBBB', 'RIGHT(`URL`, 5)': 'le.cn', "SEARCH('www',`URL`,1)": 0, "SUBSTITUTE(`邮箱`, '@', '^^',1)": 'rjw^^gmail.com', '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', 'URL': 'https://dev.seatable.cn'},
            {'文本': 'BB', "EXACT(`文本`,'AA')": False, "FIND('goo',`URL`, 1)": 0, 'LEFT(`URL`,5)': 'https', 'LEN(`URL`)': 25, 'LOWER(`文本`)': 'bb', 'MID(`邮箱`, 1, 8)': 'ran.jiwe', "REPLACE(`邮箱`, 1, 8, '12345678')": '12345678i@seafile.com', 'REPT(`文本`, 2)': 'BBBB', 'RIGHT(`URL`, 5)': 'le.io', "SEARCH('www',`URL`,1)": 0, "SUBSTITUTE(`邮箱`, '@', '^^',1)": 'ran.jiwei^^seafile.com', '_id': 'RKMQdKjQTamnaP23JrOZ1w', 'URL': 'https://cloud.seatable.io'}
        ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 文本, 数字, URL, T(`文本`), T(`数字`), text(`数字`,'dollar'), upper(`URL`) from Table1",
        'expected_result':[
            {'文本': 'AA', 'T(`数字`)': '', 'T(`文本`)': 'AA', "TEXT(`数字`,'dollar')": '$10.000000', 'UPPER(`URL`)': 'HTTPS://WWW.BAIDU.COM', '_id': 'G9c0P_fmQ8WG-lL5RG8bng', 'URL': 'https://www.baidu.com', '数字': 10},
            {'文本': 'AA', 'T(`数字`)': '', 'T(`文本`)': 'AA', "TEXT(`数字`,'dollar')": '$20.000000', 'UPPER(`URL`)': 'HTTPS://GOOGLE.COM', '_id': 'COASY7zyRaOUZAWKyFEyzQ', 'URL': 'https://google.com', '数字': 20},
            {'文本': 'BB', 'T(`数字`)': '', 'T(`文本`)': 'BB', "TEXT(`数字`,'dollar')": '$50.000000', 'UPPER(`URL`)': 'HTTPS://DEV.SEATABLE.CN', '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', 'URL': 'https://dev.seatable.cn', '数字': 50},
            {'文本': 'BB', 'T(`数字`)': '', 'T(`文本`)': 'BB', "TEXT(`数字`,'dollar')": '$30.000000', 'UPPER(`URL`)': 'HTTPS://CLOUD.SEATABLE.IO', '_id': 'RKMQdKjQTamnaP23JrOZ1w', 'URL': 'https://cloud.seatable.io', '数字': 30}
        ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 数字, 数字1, abs(`数字1`), ceiling(`数字1`), even(`数字1`), exp(2), floor(`数字1`), int(`数字1`), log(`数字`, 2), lg(`数字`), odd(`数字1`), round(`数字1`), rounddown(`数字1`),roundup(`数字1`), sign(`数字1`), sqrt(`数字1`) from Table1",
        'expected_result':[
            {'ABS(`数字1`)': 4.55, 'CEILING(`数字1`)': 5, 'EVEN(`数字1`)': 6, 'EXP(2)': 7.38905609893065, 'FLOOR(`数字1`)': 4, 'INT(`数字1`)': 4, 'LG(`数字`)': 1, 'LOG(`数字`, 2)': 3.321928094887362, '数字1': 4.55, 'ODD(`数字1`)': 5, 'ROUND(`数字1`)': 5, 'ROUNDDOWN(`数字1`)': 4, 'ROUNDUP(`数字1`)': 5, 'SIGN(`数字1`)': 1, 'SQRT(`数字1`)': 2.1330729007701543, '_id': 'G9c0P_fmQ8WG-lL5RG8bng', '数字': 10},
            {'ABS(`数字1`)': 100, 'CEILING(`数字1`)': -100, 'EVEN(`数字1`)': -100, 'EXP(2)': 7.38905609893065, 'FLOOR(`数字1`)': -100, 'INT(`数字1`)': -100, 'LG(`数字`)': 1.301029995663981, 'LOG(`数字`, 2)': 4.321928094887362, '数字1': -100, 'ODD(`数字1`)': -99, 'ROUND(`数字1`)': -100, 'ROUNDDOWN(`数字1`)': -100, 'ROUNDUP(`数字1`)': -100, 'SIGN(`数字1`)': -1, 'SQRT(`数字1`)': None, '_id': 'COASY7zyRaOUZAWKyFEyzQ', '数字': 20},
            {'ABS(`数字1`)': 3.33, 'CEILING(`数字1`)': -3, 'EVEN(`数字1`)': -2, 'EXP(2)': 7.38905609893065, 'FLOOR(`数字1`)': -4, 'INT(`数字1`)': -4, 'LG(`数字`)': 1.6989700043360187, 'LOG(`数字`, 2)': 5.643856189774724, '数字1': -3.33, 'ODD(`数字1`)': -3, 'ROUND(`数字1`)': -3, 'ROUNDDOWN(`数字1`)': -3, 'ROUNDUP(`数字1`)': -4, 'SIGN(`数字1`)': -1, 'SQRT(`数字1`)': None, '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', '数字': 50},
            {'ABS(`数字1`)': 10, 'CEILING(`数字1`)': 10, 'EVEN(`数字1`)': 10, 'EXP(2)': 7.38905609893065, 'FLOOR(`数字1`)': 10, 'INT(`数字1`)': 10, 'LG(`数字`)': 1.4771212547196624, 'LOG(`数字`, 2)': 4.906890595608519, '数字1': 10, 'ODD(`数字1`)': 11, 'ROUND(`数字1`)': 10, 'ROUNDDOWN(`数字1`)': 10, 'ROUNDUP(`数字1`)': 10, 'SIGN(`数字1`)': 1, 'SQRT(`数字1`)': 3.1622776601683795, '_id': 'RKMQdKjQTamnaP23JrOZ1w', '数字': 30}
        ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 日期, 日期带分钟, 创建时间, date(2021,10,8), dateAdd(`日期`, 2, 'days'), datedif('2021-01-01', `日期`, 'D'), day(`日期带分钟`), eomonth(`日期`, 3), hour(`日期带分钟`), minute(`日期带分钟`), month(`日期带分钟`), second(`创建时间`), year(`日期`) from Table1",
        'expected_result':[
            {'日期': '2021-09-26', 'DATE(2021,10,8)': '2021-10-08T00:00:00+08:00', "DATEADD(`日期`, 2, 'days')": '2021-09-28T00:00:00+08:00', "DATEDIF('2021-01-01', `日期`, 'D')": 268, 'DAY(`日期带分钟`)': 29, 'EOMONTH(`日期`, 3)': '2021-12-31T00:00:00+08:00', 'HOUR(`日期带分钟`)': 9, 'MINUTE(`日期带分钟`)': 30, 'MONTH(`日期带分钟`)': 9, 'SECOND(`创建时间`)': 57, 'YEAR(`日期`)': 2021, '创建时间': '2021-09-26T02:39:57.067Z', '_id': 'G9c0P_fmQ8WG-lL5RG8bng', '日期带分钟': '2021-09-29 09:30:00'},
            {'日期': '2021-09-27', 'DATE(2021,10,8)': '2021-10-08T00:00:00+08:00', "DATEADD(`日期`, 2, 'days')": '2021-09-29T00:00:00+08:00', "DATEDIF('2021-01-01', `日期`, 'D')": 269, 'DAY(`日期带分钟`)': 30, 'EOMONTH(`日期`, 3)': '2021-12-31T00:00:00+08:00', 'HOUR(`日期带分钟`)': 10, 'MINUTE(`日期带分钟`)': 0, 'MONTH(`日期带分钟`)': 9, 'SECOND(`创建时间`)': 57, 'YEAR(`日期`)': 2021, '创建时间': '2021-09-26T02:39:57.068Z', '_id': 'COASY7zyRaOUZAWKyFEyzQ', '日期带分钟': '2021-09-30 10:00:00'},
            {'日期': '2021-03-02', 'DATE(2021,10,8)': '2021-10-08T00:00:00+08:00', "DATEADD(`日期`, 2, 'days')": '2021-03-04T00:00:00+08:00', "DATEDIF('2021-01-01', `日期`, 'D')": 60, 'DAY(`日期带分钟`)': 1, 'EOMONTH(`日期`, 3)': '2021-06-30T00:00:00+08:00', 'HOUR(`日期带分钟`)': 15, 'MINUTE(`日期带分钟`)': 8, 'MONTH(`日期带分钟`)': 10, 'SECOND(`创建时间`)': 57, 'YEAR(`日期`)': 2021, '创建时间': '2021-09-26T02:39:57.068Z', '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', '日期带分钟': '2021-10-01 15:08:00'},
            {'日期': '2021-09-16', 'DATE(2021,10,8)': '2021-10-08T00:00:00+08:00', "DATEADD(`日期`, 2, 'days')": '2021-09-18T00:00:00+08:00', "DATEDIF('2021-01-01', `日期`, 'D')": 258, 'DAY(`日期带分钟`)': 3, 'EOMONTH(`日期`, 3)': '2021-12-31T00:00:00+08:00', 'HOUR(`日期带分钟`)': 8, 'MINUTE(`日期带分钟`)': 0, 'MONTH(`日期带分钟`)': 9, 'SECOND(`创建时间`)': 3, 'YEAR(`日期`)': 2021, '创建时间': '2021-09-30T06:08:03.422Z', '_id': 'RKMQdKjQTamnaP23JrOZ1w', '日期带分钟': '2021-09-03 08:00:00'}
        ]
    },
    {
        'type': 'Common',
        'sql': "select _id, 勾选, 数字, 数字1, and(`勾选`, 3), if(`数字` > 20, 100, -100), ifs(`数字`>30, 200, `数字1` < 0, -200), not(`勾选`), or(`勾选`, ''), xor(`勾选`, ''), switch(`数字`, 10,'Low', 20, 'Fare', 30, 'High', 'default') from Table1",
        'expected_result':[
            {'AND(`勾选`, 3)': True, 'IF(`数字` > 20, 100, -100)': -100, 'IFS(`数字`>30, 200, `数字1` < 0, -200)': None, '数字1': 4.55, 'NOT(`勾选`)': False, "OR(`勾选`, '')": True, '勾选': True, "XOR(`勾选`, '')": True, "SWITCH(`数字`, 10,'Low', 20, 'Fare', 30, 'High', 'default')": 'Low', '_id': 'G9c0P_fmQ8WG-lL5RG8bng', '数字': 10},
            {'AND(`勾选`, 3)': True, 'IF(`数字` > 20, 100, -100)': -100, 'IFS(`数字`>30, 200, `数字1` < 0, -200)': -200, '数字1': -100, 'NOT(`勾选`)': False, "OR(`勾选`, '')": True, '勾选': True, "XOR(`勾选`, '')": True, "SWITCH(`数字`, 10,'Low', 20, 'Fare', 30, 'High', 'default')": 'Fare', '_id': 'COASY7zyRaOUZAWKyFEyzQ', '数字': 20},
            {'AND(`勾选`, 3)': False, 'IF(`数字` > 20, 100, -100)': 100, 'IFS(`数字`>30, 200, `数字1` < 0, -200)': 200, '数字1': -3.33, 'NOT(`勾选`)': True, "OR(`勾选`, '')": False, '勾选': None, "XOR(`勾选`, '')": False, "SWITCH(`数字`, 10,'Low', 20, 'Fare', 30, 'High', 'default')": 'default', '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', '数字': 50},
            {'AND(`勾选`, 3)': False, 'IF(`数字` > 20, 100, -100)': 100, 'IFS(`数字`>30, 200, `数字1` < 0, -200)': None, '数字1': 10, 'NOT(`勾选`)': True, "OR(`勾选`, '')": False,   '勾选': None, "XOR(`勾选`, '')": False, "SWITCH(`数字`, 10,'Low', 20, 'Fare', 30, 'High', 'default')": 'High', '_id': 'RKMQdKjQTamnaP23JrOZ1w', '数字': 30}
        ]

    },
    {
        'type': 'Common',
        'sql': "select _id, 数字, 数字1, 文本, 地理位置2, average(`数字`, `数字1`), counta(`文本`, `地理位置2`), countall(`数字`, `数字1`, `文本`, `地理位置2`), countblank(`数字`, `数字1`, `文本`, `地理位置2`) from Table1",
        'expected_result':[

            {'文本': 'AA', 'AVERAGE(`数字`, `数字1`)': 7.275, 'COUNTA(`文本`, `地理位置2`)': 2, 'COUNTALL(`数字`, `数字1`, `文本`, `地理位置2`)': 4, 'COUNTBLANK(`数字`, `数字1`, `文本`, `地理位置2`)': 0, '数字1': 4.55, '地理位置2': {'lat': 42.5158032188098, 'lng': 113.20517001118883}, '_id': 'G9c0P_fmQ8WG-lL5RG8bng', '数字': 10},
            {'文本': 'AA', 'AVERAGE(`数字`, `数字1`)': -40, 'COUNTA(`文本`, `地理位置2`)': 1, 'COUNTALL(`数字`, `数字1`, `文本`, `地理位置2`)': 4, 'COUNTBLANK(`数字`, `数字1`, `文本`, `地理位置2`)': 1, '数字1': -100, '_id': 'COASY7zyRaOUZAWKyFEyzQ', '数字': 20, '地理位置2': None},
            {'文本': 'BB', 'AVERAGE(`数字`, `数字1`)': 23.335, 'COUNTA(`文本`, `地理位置2`)': 1, 'COUNTALL(`数字`, `数字1`, `文本`, `地理位置2`)': 4, 'COUNTBLANK(`数字`, `数字1`, `文本`, `地理位置2`)': 1, '数字1': -3.33, '_id': 'LWTLEcPRRj2eBtEDD7xbOQ', '数字': 50,'地理位置2': None },
            {'文本': 'BB', 'AVERAGE(`数字`, `数字1`)': 20, 'COUNTA(`文本`, `地理位置2`)': 1, 'COUNTALL(`数字`, `数字1`, `文本`, `地理位置2`)': 4, 'COUNTBLANK(`数字`, `数字1`, `文本`, `地理位置2`)': 1, '数字1': 10, '_id': 'RKMQdKjQTamnaP23JrOZ1w', '数字': 30,'地理位置2': None}
        ]

    },
]
