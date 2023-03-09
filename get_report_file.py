import pandas as pd
from authorization import *
import urllib.parse
from datetime import datetime


# URL's const's
REPORT_FILE_URL = "https://prod.gpt.adc.spb.ru/Transport/main/reports/userReportView"


# Значения организаций, вставляемое вместо paramValue(зачастую первое)
org_values = {
    'GUP': '362',
    'AP1': '165',
    'AP2': '166',
    'AP3': '1205',
    'AP5': '222',
    'AP6': '168',
    'AP7': '181',
    'AP8': '382',
    'SERVICE': '1747',
    'ORDER': '985'
}


# Значения отчетов, вставляемое вместо  reportId
reports_id = {
    'C1': '201',
    'C2': '202',
    'C4': '204',
    'C6': '206',
    'C8': '560',
    'F2': '81',
    'F3': '83',
    'F4': '84',
    'F4P1': '142',
    'F4P2': '143',
    'F5': '85',
    'F7': '61',
    'F7EXTRA': '703',
    'F9': '121',
    'F9P': '141',
    'DISP': '401',
    'PLAN_REYSOV': '600',
    'REESTR_VIPUSKA': '641'
}


# Значения маршрутов, вставляемые вместо route_id
routes_id = ['1260', '344', '1284', '1160', '305', '446', '234', '221', '235', '236', '3750', '1306', '304', '1245', '1318', '1342', '388', '385', '237', '1803', '331', '8409', '1600', '1292', '1274']


# Значения маршрутов, вставляемые вместо route_number
routes_number = ['6306', '4757', '5701', '6263', '6264', '4759', '4977', '4997', '4979', '4981', '8469', '4636', '4637', '4638', '8186', '8187', '8188', '8189', '8190', '8551', '3301', '3319', '3320', '4482', '4483']


# Получаем report_id, в зависимости от названия отчета в *args
def get_report_id(reports_id, *args):
    for arg in args: 
        for key, value in reports_id.items():
            if arg == key:
                report_id = value
                print(report_id)
                return report_id
    else:
        print('ВЫ ОШИБЛИСЬ ПРИ ВВОДЕ НАИМЕНОВАНИЯ ОТЧЕТА!!!!!')



# Получаем org_value, в зависимости от названия отчета в *args            
def get_org_value(org_values, *args):            
    for arg in args:
        for key, value in org_values.items():
            if arg == key:
                org_value = value
                print(org_value)
                return org_value
    else:
        print('ВЫ ОШИБЛИСЬ ПРИ ВВОДЕ НАИМЕНОВАНИЯ ОРГАНИЗАЦИИ!!!!!')            


# Получаем route_id, в зависимости от route_id в *args
def get_route_id(routes_id, *args):
    for arg in args: 
        for route_id in routes_id:
            if arg == route_id:
                return route_id
    else:
        print('ВЫ ОШИБЛИСЬ ПРИ ВВОДЕ ID МАРШРУТА!!!!!')          
            

# Получаем route_number, в зависимости от route_number в *args
def get_route_number(routes_number, *args):
    for arg in args: 
        for route_number in routes_number:
            if arg == route_number:
                return route_number
    else:
        print('ВЫ ОШИБЛИСЬ ПРИ ВВОДЕ НОМЕРА МАРШРУТА!!!!!')        


# Проверка на то что какой-то arg из *args является датой(строка содержит в себе числа)
def count_digits(s):
    return sum(c.isdigit() for c in s)


# Получаем report_date, в зависимости от даты в *args                
def get_report_date(*args):
    for arg in args:
        if count_digits(arg) == 8:
            date = datetime.fromisoformat(arg)
            def timestamp(date):
                return date.timestamp() * 1000
            report_date = (int(timestamp(date)))
            return report_date
    else:
        print('ВЫ ОШИБЛИСЬ ПРИ ВВОДЕ ДАТЫ!!!!!')    


# Получаем start_date и end_date, в зависимости от start_date и end_date в *args, объединяем их в 1 строку
def get_start_end_date(*args):
    s_date = ''
    for arg in args:
        if count_digits(arg) == 8: 
           s_date = s_date + arg + ' '
    return s_date


# Получаем start_date, в зависимости от start_date в *args
def get_start_date(*args):
    start_date = ''
    s_date = get_start_end_date(*args) 
    if len(args) > 3 :
        date_list = s_date.split()
        if date_list[0] > date_list[1]:
            start_date += date_list[1]
        elif date_list[0] < date_list[1]:
            start_date += date_list[0]        
        date = datetime.fromisoformat(start_date)
        def timestamp(date):
            return date.timestamp() * 1000
        start_date = (int(timestamp(date)))
        return start_date 


# Получаем end_date, в зависимости от end_date в *args
def get_end_date(*args):
    end_date = ''
    s_date = get_start_end_date(*args)
    if len(args) > 3 :
        date_list = s_date.split() 
        if date_list[0] > date_list[1]:
            end_date += date_list[0]
        elif date_list[0] < date_list[1]:
            end_date += date_list[1]  
        date = datetime.fromisoformat(end_date)
        def timestamp(date):
            return date.timestamp() * 1000
        end_date = (int(timestamp(date)))
        return end_date
    

# Получаем файл отчета, сохраняем локально и выводим его в консоль  добавить сюда параметр date
def get_report(session_id, *args):

    # Получаем report_id
    report_id = get_report_id(reports_id, *args)
    # org_value = get_org_value(org_values, *args)
    # report_date = get_report_date(*args)
    # start_date = get_start_date(*args)
    # end_date = get_end_date(*args)
    # route_number = get_route_number(routes_number, *args)
    # route_id = get_route_id(routes_id, *args)


    # Payload принимает в себя report_date вида YYYY-MM-DD, org_value и report_id. Только для отчетов C1, C2, C8, F7, F7EXTRA, F9.
    if report_id in ('201', '202', '560', '61', '703', '121'):
        org_value = get_org_value(org_values, *args)
        report_date = get_report_date(*args)
        payload = f"repName=equipmentWork_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522{org_value}%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%2522{report_date}%2522%257D%255D&format=xls&reportId={report_id}&waitAttr=wait201353"  
    

    # Payload принимает в себя диапазон дат start_date и end_date вида YYYY-MM-DD, org_value и report_id. Только для отчетов C4, F4, F4P1, F4P2, F5, PLANREYSOV, REESTRVIPUSKA.
    elif report_id in('204', '84', '142', '143', '85', '600', '641'):
        org_value = get_org_value(org_values, *args)
        start_date = get_start_date(*args)
        end_date = get_end_date(*args)
        payload = f"repName=equipmentWorkF4_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522{org_value}%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%2522{start_date}%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dend%2522%2C%2520%2522paramValue%2522%3A%2522{end_date}%2522%257D%255D&format=xls&reportId={report_id}&waitAttr=wait204780"  
        
    
    # Payload принимает в себя диапазон дат start_date и end_date вида YYYY-MM-DD, route_number и report_id. Только для отчетов F2, F3.
    elif report_id in ('81', '83'):
        start_date = get_start_date(*args)
        end_date = get_end_date(*args)
        route_number = get_route_number(routes_number, *args)
        payload = f"repName=transportWorkResultF2_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%2522{start_date}%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dend%2522%2C%2520%2522paramValue%2522%3A%2522{end_date}%2522%257D%2C%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522route%2522%2C%2520%2522paramValue%2522%3A%2522{route_number}%2522%257D%255D&format=xls&reportId={report_id}&waitAttr=wait81255&subreportsJson=%257B%2522entryArray%2522%3A%255B%257B%2522key%2522%3A%2522sub_report%2522%2C%2520%2522value%2522%3A%2522transportWorkResultF2_race_by_org.jasper%2522%257D%255D%257D"


    # Payload принимает в себя report_date вида YYYY-MM-DD, org_value и report_id. Только для отчета C6.
    elif report_id == '206':
        org_value = get_org_value(org_values, *args)
        report_date = get_report_date(*args)
        payload = f"repName=equipmentWorkF6_by_org.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522contragent%2522%2C%2520%2522paramValue%2522%3A%2522{org_value}%2522%257D%2C%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522month%2522%2C%2520%2522paramValue%2522%3A%2522{report_date}%2522%257D%255D&format=xls&reportId={report_id}&waitAttr=wait206960"


    # Payload принимает в себя report_date вида YYYY-MM-DD, route_id и report_id. Только для отчета DISP.
    elif report_id == '401':
        report_date = get_report_date(*args)
        route_id = get_route_id(routes_id, *args)
        payload = f"repName=dsp_traffic_log_oper.jasper&reportJson=%255B%257B%2522entityName%2522%3A%2522java.util.Date%2522%2C%2520%2522paramName%2522%3A%2522dbegin%2522%2C%2520%2522paramValue%2522%3A%2522{report_date}%2522%257D%2C%257B%2522entityName%2522%3A%2522java.lang.Long%2522%2C%2520%2522paramName%2522%3A%2522route%2522%2C%2520%2522paramValue%2522%3A%2522{route_id}%2522%257D%255D&format=xls&reportId={report_id}&waitAttr=wait40161"


    content_type = 'application/x-www-form-urlencoded'
    cookie = f'JSESSIONID={session_id}; https%3A%2F%2Fprod.gpt.adc.spb.ru%2FTransport%2Fmain%2Ftheme=%7B%22state%22%3A%7B%22id%22%3A%22s%3Aslate%22%2C%20%22file%22%3A%22s%3Agxt%2Fthemes%2Fslate%2Fcss%2Fxtheme-slate.css%22%7D%7D'
    headers = {
        'Content-Type': content_type,
        'Cookie': cookie,
    }
    report_file = requests.post(REPORT_FILE_URL, headers=headers, data=payload)
    file_name = get_file_name(report_file)
    df = get_excel_file(report_file, file_name)
    return df


# Получаем имя файла  (по сути такая реадизация не нужна, будем получать имя файла из данных в запросе(организация, отчет, дата))
def get_file_name(report_file):
    content_disposition = report_file.headers["Content-Disposition"] 
    encoded_file_name = content_disposition.split('filename=')[1].split(';')[0]
    file_name = urllib.parse.unquote(encoded_file_name, encoding='utf-8').replace('"', '')
    print(file_name)
    return file_name


# Получаем файл в формате excel
def get_excel_file(report_file,file_name):
    with open (file_name, 'wb') as file:
        file.write(report_file.content)
    df = pd.read_excel(file_name)
    return df
    # print(df)  


# Вызываем авторизацию и получаем session_id
get_session_id()
session_id = auth(session_id, content_type, cookie, headers)