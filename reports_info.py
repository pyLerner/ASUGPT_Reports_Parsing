# organizations = {
# 'ГУП': '7|0|4|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|selectParksAllForClerk|1|2|3|4|0|',
# '5P': '7|0|4|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|selectParksAllForClerk|1|2|3|4|0|'
# }
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# В payload есть два параметра paramValue, первое из них числовое обозначение парка(организации при выборе отчета), второе это числовое обозначение даты отчета(дата при выборе отчета)
# Для формирования тех отчетов, которые мы хотим нужно передавать в payload переменные, являющиеся параметрами, про которые написано выше

# Пример payloads при формировании отчета С1 
# GUP = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522362%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait20149'
# P5 =  'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522222%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait201954'
# PAT = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%25221747%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait201848'
# P6 = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522168%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait201124'
# ZP = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522985%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait201295'
# P3 = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%25221205%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait20153'
# PKOL = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522382%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait201643'
# P2 = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522166%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait201387'
# P1 = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522165%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait201434'
# P7 = 'repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522181%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%25221677628800000%2522%257D%255D&format=xls&reportId=201&waitAttr=wait201928'

# Обозначение парков (разница в payloads)
# ГУП = '362'
# П5 = '222'
# ПАТ = '1747'
# П6 = '168'
# ЗП = '985'
# П3 = '1205'
# ПКОЛ = '382'
# П2 = '166'
# П1 = '165'
# П7 = '181'

# organizations_param_values =  {
#     'GUP': '362',
#     'P1': '165',
#     'P2': '166',
#     'P3': '1205',
#     'P5': '222',
#     'P6': '168',
#     'P7': '181',
#     'PKOL': '382',
#     'PAT': '1747',
#     'ZP': '985'
# }

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

# Пример paramValue для даты отчета(1 марта в милисекундах от 1970 года)
# first_of_march = '1677628800000'
# каждый последующий день + 86400000 мили сек

# Payloads при запросе всех отчетов до выбора организации(запрос при клике на выбранный отчет)
# reports = {
#     'C1': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|DJ|',
#     'C2': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|DK|',
#     'C4': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|DM|',
#     'C6': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|DO|',
#     'C8': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|Iw|',
#     'F2': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|BR|',
#     'F3': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|BT|',
#     'F4': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|BU|',
#     'F4P1': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|CO|',
#     'F4P2': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|CP|',
#     'F5': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|BV|',
#     'F7': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|9|',
#     'F7EXTRA': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|K_|',
#     'F9': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|B5|',
#     'F9P': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|CN|',
#     'DISP': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|GR|',
#     'PLANREYSOV': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|JY|',
#     'REESTRVIPUSKA': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|KB|'
# }


# в С4 диапазон дат, в С6 не конкретная дата , а месяц; Ф4 как С4, как Ф4П1, Ф4П2, как Ф5, PLANREYSOV, REESTRVIPUSKA
# разобраться какие данные нужны в Ф2, Ф9П, DISP,
# разобраться какие данные нужны в 
# Reports id
# C1 = '201'
# C2 = '202'
# C4 = '204'
# C6 = '206'
# C8 = '560'
# F2 = '81'
# F3 = '83'
# F4 = '84'
# F4P1 = '142'
# F4P2 = '143'
# F5 = '85'
# F7 = '61'
# F7EXTRA = '703'
# F9 = '121'
# F9P = '141'
# DISP = '401'
# PLANREYSOV = '600'
# REESTRVIPUSKA = '641'


# # РАЗДЕЛЕНИЕ ПО ДАННЫМ НУЖНЫМ ДЛЯ ПОЛУЧЕНИЯ ОТЧЕТА
# data_org = [C1, C2, C8, F7, F7EXTRA, F9]
# data_range_org = [C4, F4, F4P1, F4P2, F5, PLANREYSOV, REESTRVIPUSKA]
# data_mouth_org = [C6]
# data_range_route_number = [F2, F3]
# data_vehicle = [F9P]
# data_route = [DISP]
