# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import joblib

# def train_model(X,y):
#     print(f'Model Training Started...')
#     X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#     model=LogisticRegression()
#     model.fit(X_train,y_train)
#     print(f'Model Training Completed.')
#     joblib.dump(model,'model.pkl')
#     y_pred=model.predict(X_test)
#     accuracy=accuracy_score(y_test,y_pred)
#     print(f'{accuracy*100:.2f}')
#     return model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model(X, y):
    print(f'Model Training Started...')
    
    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create a Random Forest Classifier
    model = RandomForestClassifier()
    
    # Train the model
    model.fit(X_train, y_train)
    print(f'Model Training Completed.')
    
    # Save the model
    joblib.dump(model, 'model.pkl')
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%')
    
    return model

