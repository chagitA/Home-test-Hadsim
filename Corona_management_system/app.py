from flask import Flask, request, jsonify
from queries.patient import Patient_queries
from queries.vaccination import Vaccination_queries
from sqlalchemy import create_engine
from flask_cors import CORS

# creating the app:
app = Flask(__name__)
CORS(app)

# Initialize classes:
patient = Patient_queries()
vaccine = Vaccination_queries()


# Routing to create a new patient:
@app.route('/api/new-patient', methods=['POST'])
def new_patient():
    data = request.get_json()
    patient_id = data.get('patient_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    city = data.get('city')
    street = data.get('street')
    house_num = data.get('house_num')
    birthday = data.get('birthday')
    phone = data.get('phone')
    cellphone = data.get('cellphone')
    positive_result_date = data.get('positive_result_date')
    recovery_date = data.get('recovery_date')

    try:
        patient.new_patient(patient_id, first_name, last_name,
                            city, street, house_num,
                            birthday, phone, cellphone,
                            positive_result_date, recovery_date)
        response = {'success': True, 'message': 'Patient created successfully'}
    except Exception as e:
        response = {'success': False, 'message': str(e)}

    return jsonify(response), 200


# Routing to get the patient by ID:
@app.route('/api/get-patients', methods=['GET'])
def get_patient(patient_id):
    try:
        patient_data = patient.get_patient(patient_id)
        if patient_data:
            response = {'success': True, 'data': patient_data}
        else:
            response = {'success': False, 'message': 'Patient not found'}
    except Exception as e:
        response = {'success': False, 'message': str(e)}

    return jsonify(response), 200


# Routing to create a new vaccine:
@app.route('/api/new-vaccine', methods=['POST'])
def new_vaccine():
    data = request.get_json()
    vaccine_id = data.get('vaccine_id')
    patient_id = data.get('patient_id')
    date = data.get('date')
    manufacturer = data.get('manufacturer')

    try:
        vaccine.new_vaccine(patient_id, date, manufacturer)
        response = {'success': True, 'message': 'Vaccination created successfully'}
    except Exception as e:
        response = {'success': False, 'message': str(e)}

    return jsonify(response), 200


# Routing to get the vaccine by ID:
@app.route('/api/get-vaccine', methods=['GET'])
def get_vaccine():
    data = request.get_json()
    vaccine_id = data.get('vaccine_id')
    type_id = data.get('type_id')
    try:
        vaccine_data = vaccine.get_vaccine(vaccine_id, type_id)
        if vaccine_data:
            response = {'success': True, 'data': vaccine_data}
        else:
            response = {'success': False, 'message': 'Vaccine not found'}
    except Exception as e:
        response = {'success': False, 'message': str(e)}

    return jsonify(response), 200


# Routing to update the date of receiving a positive result for Corona:
@app.route('/api/update-positive-date', methods=['UPDATE'])
def update_positive_date():
    data = request.get_json()
    patient_id = data.get('patient_id')
    date = data.get('date')
    try:
        patient.update_positive_result_date(patient_id, date)
        response = {'success': True, 'message': 'The date of receiving a positive result has been successfully updated'}
    except Exception as e:
        response = {'success': False, 'message': str(e)}
    return jsonify(response), 200


# Routing to update the date of recovery from Corona:
@app.route('/api/update-recovery-date', methods=['UPDATE'])
def update_recovery_date():
    data = request.get_json()
    patient_id = data.get('patient_id')
    date = data.get('date')
    try:
        patient.update_recovery_date(patient_id, date)
        response = {'success': True, 'message': 'Recovery date has been successfully updated'}
    except Exception as e:
        response = {'success': False, 'message': str(e)}
    return jsonify(response), 200
