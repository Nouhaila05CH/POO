import streamlit as S
import pandas as P
def load_data():
    try:
        data = P.read_csv("patients.csv")
        S.write("Data loaded successfully")
    except FileNotFoundError:
        data = P.DataFrame(columns=['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke'])
        S.write("No data file found")
    return data
def save_data(data):
    data.to_csv("patients.csv", index=False)
def add_patient(id, gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status, stroke):
    global data
    new_patient = P.DataFrame({'id': [id],
                                'gender': [gender],
                                'age': [age],
                                'hypertension': [hypertension],
                                'heart_disease': [heart_disease],
                                'ever_married': [ever_married],
                                'work_type': [work_type],
                                'Residence_type': [residence_type],
                                'avg_glucose_level': [avg_glucose_level],
                                'bmi': [bmi],
                                'smoking_status': [smoking_status],
                                'stroke': [stroke]})
    data = P.concat([new_patient, data], ignore_index=True)  
    save_data(data)
def display_patients():
    global data
    S.write(data)
def update_patient(id, column, value):
    global data
    id = id.strip()
    if id in data['id'].astype(str).str.strip().values:
        data.loc[data['id'].astype(str).str.strip() == id, column] = value
        save_data(data)
        S.success('Patient data updated successfully')
    else:
        S.error('Patient ID not found')
def delete_patient(id):
    global data
    id = id.strip()
    if id in data['id'].astype(str).str.strip().values:
        data = data[data['id'].astype(str).str.strip() != id]
        save_data(data)
        S.success('Patient data deleted successfully')
    else:
        S.error('Patient ID not found')
def search_patient(id):
    global data
    id = id.strip()
    if id in data['id'].astype(str).str.strip().values:
        patient = data[data['id'].astype(str).str.strip() == id]
        S.write(patient)
    else:
        S.error('Patient ID not found')
S.title('Hospital Patients ')
data = load_data()
menu = S.sidebar.selectbox('Menu', ['Add Patient', 'View Patients', 'Update Patient', 'Delete Patient', 'Search Patient'])
