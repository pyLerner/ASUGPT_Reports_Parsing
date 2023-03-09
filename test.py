from get_report_file import get_report, session_id
import pandas as pd


df = get_report(session_id, 'C2','P5', '2023-03-02')
print('DataFrame:', df)