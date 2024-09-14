import pandas as pd
import openpyxl as ox
def data_extract(file):
    try:
        data=pd.read_excel(file)
        print(data.tail())
        return data
    except Exception as e:
        print(f'Error Has Arrived:{e}')
        return None

