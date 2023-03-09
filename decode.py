import urllib.parse
from datetime import datetime, timezone
import time

# timestamp = 1677757477914
# dt = datetime.datetime.fromtimestamp(timestamp)
# print(dt)


# millisec = int(time.time() * 1000)
# print(millisec)
# s = '2023-03'
# dt = datetime.fromisoformat(s)
# def timestamp(dt):
#     return dt.timestamp() * 1000
# new_num = (int(timestamp(dt)))
# print(new_num)

# ss = 'Hello, world! 123'

# def count_digits(s):
#     return sum(c.isdigit() for c in s)

# print(count_digits(s)) 

a = datetime.fromtimestamp(1679907600000/1000)
print(a)

# c = datetime(2020,4,4).strftime('%Y-%m')
# print(c)

# # Округление миллисекунд до 
# int(round(time.time()*1000))
# # 1613649588303

# b = datetime.utcnow().strftime('%Y-%m')
# print(b)

# first = '%5B%7B%22entityName%22:%22java.lang.Long%22,%20%22paramName%22:%22contragent%22,%20%22paramValue%22:%22362%22%7D,%7B%22entityName%22:%22java.util.Date%22,%20%22paramName%22:%22dbegin%22,%20%22paramValue%22:%221676246400000%22%7D%5D'
# second = '%5B%7B%22entityName%22:%22java.lang.Long%22,%20%22paramName%22:%22contragent%22,%20%22paramValue%22:%22362%22%7D,%7B%22entityName%22:%22java.util.Date%22,%20%22paramName%22:%22dbegin%22,%20%22paramValue%22:%221676332800000%22%7D%5D'
# third = '%5B%7B%22entityName%22:%22java.lang.Long%22,%20%22paramName%22:%22contragent%22,%20%22paramValue%22:%22362%22%7D,%7B%22entityName%22:%22java.util.Date%22,%20%22paramName%22:%22dbegin%22,%20%22paramValue%22:%221676419200000%22%7D%5D'

# payload = '%5B%7B%22entityName%22:%22java.lang.Long%22,%20%22paramName%22:%22contragent%22,%20%22paramValue%22:%22362%22%7D,%7B%22entityName%22:%22java.util.Date%22,%20%22paramName%22:%22dbegin%22,%20%22paramValue%22:%221677628800000%22%7D%5D'

# one = [{"entityName":"java.lang.Long", "paramName":"contragent", "paramValue":"362"},{"entityName":"java.util.Date", "paramName":"dbegin", "paramValue":"1676505600000"}]
# one = str(one)
# def decode_data(str):
#     decode_str = urllib.parse.unquote(str, encoding='utf-8')
#     print(decode_str)


# def encode_data(str):
#     encode_str = urllib.parse.quote(str, encoding='utf-8')
#     print(encode_str)

# decode_data(first)
# decode_data(second)
# decode_data(third)

# encode_data(one)

# def get_file_name(report_file):
#     content_disposition = report_file.headers["Content-Disposition"] 
#     encoded_file_name = content_disposition.split('filename=')[1].split(';')[0]
#     file_name = urllib.parse.unquote(encoded_file_name, encoding='utf-8')   
#     return file_name


# Получение имени файла и его декодирование
# content_disposition = report_file.headers["Content-Disposition"] 
# encoded_file_name = content_disposition.split('filename=')[1].split(';')[0]
# file_name = urllib.parse.unquote(encoded_file_name, encoding='utf-8')   

# decode_data(payload)


# Разница между запросами гупа и 5 парка C1 в payloads отчета в том что разные paramValue и waitAttr
# При запросах 

# reports_id = {
#     'C1': '201',
#     'C2': '202',
#     'C4': '204',
#     'C6': '206',
#     'C8': '560',
#     'F2': '81',
#     'F3': '83',
#     'F4': '84',
#     'F4P1': '142',
#     'F4P2': '143',
#     'F5': '85',
#     'F7': '61',
#     'F7EXTRA': '703',
#     'F9': '121',
#     'F9P': '141',
#     'DISP': '401',
#     'PLANREYSOV': '600',
#     'REESTRVIPUSKA': '641'
# }

# # print(reports_id.items)

# def get_key(reports_id, report_name):
#     for key, value in reports_id.items():
#         if report_name == key:
#             print(value) 

# get_key(reports_id, 'C1')

# 1677747600000
# 1679907600000