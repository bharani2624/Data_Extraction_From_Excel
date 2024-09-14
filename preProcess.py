import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # or any other model
from sklearn.preprocessing import LabelEncoder

def preprocess_data(data,target_column):
    print(f'PreProcessing Started...')
    label_encoders={}
    data['Hyear']=pd.to_datetime(data['Date Hired']).dt.year
    data['Hmonth']=pd.to_datetime(data['Date Hired']).dt.month
    data['Hday']=pd.to_datetime(data['Date Hired']).dt.day
    data=data.drop(columns=['Date Hired'])
    for column in data.select_dtypes(include=['object']).columns:
        label_encoders[column]=LabelEncoder()
        data[column]=label_encoders[column].fit_transform(data[column])
    x=data.drop(columns=[target_column])
    y=data[target_column]
    print(f'PreProcessing Completed.')
    return x,y,label_encoders
