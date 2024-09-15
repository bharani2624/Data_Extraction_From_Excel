import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def load_excel(file_path):
    try:
        data = pd.read_excel(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

def process_query(query):
    doc = nlp(query)
    
    tokens = [token.text for token in doc]
    lemmas = [token.lemma_ for token in doc]
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    print(f"Tokens: {tokens}")
    print(f"Lemmas: {lemmas}")
    print(f"Entities: {entities}")
    
    return tokens, lemmas, entities

def answer_query_nlp(df, query):
    tokens, lemmas, entities = process_query(query.lower())
    
    if any(lemma in ['salary', 'location', 'sex', 'hired', 'exempt'] for lemma in lemmas):
        for ent_text, ent_label in entities:
            if ent_label == 'PERSON':
                employee_name = ent_text
                result = df[df['Employee'].str.lower() == employee_name.lower()]
                
                if not result.empty:
                    if 'salary' in lemmas:
                        return f"{employee_name} has a salary of {result.iloc[0]['Salary']}."
                    elif 'location' in lemmas:
                        return f"{employee_name} is located in {result.iloc[0]['Location']}."
                    elif 'sex' in lemmas:
                        return f"{employee_name} is {result.iloc[0]['Sex']}."
                    elif 'hired' in lemmas or 'date' in lemmas:
                        return f"{employee_name} was hired on {result.iloc[0]['Date Hired']}."
                    elif 'exempt' in lemmas:
                        exempt_status = "exempt" if result.iloc[0]['Exempt'] else "not exempt"
                        return f"{employee_name} is {exempt_status} from overtime."
                else:
                    return "Employee not found."

    if "average" in tokens and "salary" in tokens:
        if any(lemma in ['male', 'female'] for lemma in lemmas):
            gender = 'Male' if 'male' in lemmas else 'Female'
            if 'Salary' in df.columns and 'Sex' in df.columns:
                avg_salary = df[df['Sex'] == gender]['Salary'].mean()
                return f"Average salary for {gender} employees is {avg_salary:.2f}."
            else:
                return "Salary or Sex column not found in the data."

    if "average" in tokens and "salary" in tokens and "location" in lemmas:
        for ent_text, ent_label in entities:
            if ent_label == 'GPE':
                location = ent_text
                if 'Salary' in df.columns and 'Location' in df.columns:
                    avg_salary = df[df['Location'].str.lower() == location.lower()]['Salary'].mean()
                    return f"Average salary in {location} is {avg_salary:.2f}."
                else:
                    return "Salary or Location column not found in the data."

    return "Sorry, I don't understand the query."

if __name__ == "__main__":
    file_path = "employee_data.xlsx"
    df = load_excel(file_path)

    if df is not None:
        while True:
            query = input("Ask a question (type 'exit' to stop): ")
            if query.lower() == 'exit':
                break
            response = answer_query_nlp(df, query)
            print(response)
