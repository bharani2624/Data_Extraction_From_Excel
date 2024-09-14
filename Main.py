import dataExtraction as de
import preProcess as pp
import trainModel as tm
file="employee_data.xlsx"
data=de.data_extract(file)
data=data.drop(columns=['Unnamed: 6', 'Unnamed: 7'])
target_column="Exempt"
X,y,label_encoders=pp.preprocess_data(data,target_column)
print(label_encoders)
model=tm.train_model(X,y)
print(data)
