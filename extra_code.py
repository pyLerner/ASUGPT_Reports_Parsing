from get_report_file import get_report, session_id


# get_session_id()
# session_id = auth(session_id, content_type, cookie, headers)
get_report(session_id, 'C4', 'P3', '2023-03-03', '2023-03-01')


# MONITORING_URL = "https://prod.gpt.adc.spb.ru/Transport/main/service/Monitoring"
# REPORT_URL = "https://prod.gpt.adc.spb.ru/Transport/main/service/Reports"


# Получение страницы отчетов
# def get_report(session_id):
#     payload = "7|0|8|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getCustomReports|ru.csbi.transport.gwtapp.client.service.FetchCriteria/393594735|Z|ru.csbi.transport.gwtapp.client.service.SortDirection/2229634495|name|1|2|3|4|2|5|6|5|0|0|0|0|25|7|0|8|0|0|0|"
#     content_type = 'text/x-gwt-rpc; charset=utf-8'
#     cookie = f'JSESSIONID={session_id}; https%3A%2F%2Fprod.gpt.adc.spb.ru%2FTransport%2Fmain%2Ftheme=%7B%22state%22%3A%7B%22id%22%3A%22s%3Aslate%22%2C%20%22file%22%3A%22s%3Agxt%2Fthemes%2Fslate%2Fcss%2Fxtheme-slate.css%22%7D%7D'
#     headers = {
#         'Content-Type': content_type,
#         'Cookie': cookie,
#     }

#     report = requests.post(REPORT_URL, headers=headers, data=payload)
    


# Получение страницу БО С-1
# def get_report_c1_page(session_id):
#     payload = "7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|DJ|"
#     content_type = 'text/x-gwt-rpc; charset=utf-8'
#     cookie = f'JSESSIONID={session_id}; https%3A%2F%2Fprod.gpt.adc.spb.ru%2FTransport%2Fmain%2Ftheme=%7B%22state%22%3A%7B%22id%22%3A%22s%3Aslate%22%2C%20%22file%22%3A%22s%3Agxt%2Fthemes%2Fslate%2Fcss%2Fxtheme-slate.css%22%7D%7D'
#     headers = {
#         'Content-Type': content_type,
#         'Cookie': cookie,
#     }

#     report_c1_page = requests.post(REPORT_URL, headers=headers, data=payload)


# Получаем отчет БО С-1
# def get_report_c1(session_id):
#     payload = "7|0|6|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|checkReportParameters|ru.csbi.transport.gwtapp.client.service.FetchCriteria/393594735|java.util.HashMap/1797211028|1|2|3|4|1|5|5|0|0|6|0|0|0|0|0|0|0|"
#     content_type = 'text/x-gwt-rpc; charset=utf-8'
#     cookie = f'JSESSIONID={session_id}; https%3A%2F%2Fprod.gpt.adc.spb.ru%2FTransport%2Fmain%2Ftheme=%7B%22state%22%3A%7B%22id%22%3A%22s%3Aslate%22%2C%20%22file%22%3A%22s%3Agxt%2Fthemes%2Fslate%2Fcss%2Fxtheme-slate.css%22%7D%7D'
#     headers = {
#         'Content-Type': content_type,
#         'Cookie': cookie,
#     }

#     report_c1 = requests.post(REPORT_URL, headers=headers, data=payload)
#     print(report_c1.status_code)
    

# Получение страницы мониторинга
# def get_monitoring(session_id):
#     payload = "7|0|4|https://prod.gpt.adc.spb.ru/Transport/main/|1AD9DFB9187AFB2E66AC7CA1ADD23780|ru.csbi.transport.gwtapp.monitoring.client.service.MonitoringService|getAlarmedVehicles|1|2|3|4|0|"
#     content_type = 'text/x-gwt-rpc; charset=utf-8'
#     cookie = f'JSESSIONID={session_id}; https%3A%2F%2Fprod.gpt.adc.spb.ru%2FTransport%2Fmain%2Ftheme=%7B%22state%22%3A%7B%22id%22%3A%22s%3Aslate%22%2C%20%22file%22%3A%22s%3Agxt%2Fthemes%2Fslate%2Fcss%2Fxtheme-slate.css%22%7D%7D; JSESSIONID=64B0B876EC844BF4B0BDE04F638E82B6'
#     headers = {
#         'Content-Type': content_type,
#         'Cookie': cookie,
#     }

#     monitoring = requests.post(MONITORING_URL, headers=headers, data=payload)
#     print(monitoring.status_code)
#     print(monitoring.text)

# Обозначение отчетов? (разница в payloads)C1': '7|0|5|https://prod.gpt.adc.spb.ru/Transport/main/|CC98E44BD484DEF1703383C6EBFE80D8|ru.csbi.transport.gwtapp.reports.client.service.ReportsService|getReportParams|J|1|2|3|4|1|5|DJ|',
# C2 = 'DK|'
# C4 = 'DM|'
# C6 = 'DO|'
# C8 = 'Iw|'
# F2 = 'BR|'
# F3 = 'BT|'
# F4 = 'BU|'
# F4P1 = 'CO|'
# F4P2 = 'CP|'
# F5 = 'BV|'
# F7 = '9|'
# F7EXTRA = 'K_|'
# F9 = 'B5|'
# F9P = 'CN|'
# DISP = 'GR|'
# PLANREYSOV = 'JY|'
# REESTRVIPUSKA = 'KB|'