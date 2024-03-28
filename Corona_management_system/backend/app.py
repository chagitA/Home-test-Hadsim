from flask import Flask, request, jsonify
from Corona_management_system.backend.queries.patient import Patient_queries
from Corona_management_system.backend.queries.vaccination import Vaccination_queries
from flask_cors import CORS
import validation
from werkzeug.utils import secure_filename
import uuid as uuid
import os


# creating the app:
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = '/images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize classes:
patient = Patient_queries()
vaccine = Vaccination_queries()


# Routing to create a new patient:
@app.route('/api/new-patient', methods=['POST'])
def new_patient():
    #data = request.get_json()
    patient_id = request.form['patient_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    city = request.form['city']
    street = request.form['street']
    house_num = request.form['house_num']
    birthday = request.form['birthday']
    phone = request.form['phone']
    cellphone = request.form['cellphone']

    image = request.files['image']
    image_original_name = image.filename
    image_type = request.form['imageType']
    #File name security:
    image_sec_name = secure_filename(image_original_name)
    #set uuid:
    image_name = str(uuid.uuid1()) + "_" + image_sec_name
    #save the image:
    image_location = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
    image.save(image_location)
    try:
        # Checking the correctness of the ID number:
        if not validation.israeli_id_validation(patient_id):
            response = {'success': False, 'message': 'ID number is wrong'}
        else:
            patient.new_patient(patient_id, first_name, last_name,
                                city, street, house_num,
                                birthday, phone, cellphone)

            # decoded_image_data = base64.b64decode(image)
            # patient.new_picture(patient_id, decoded_image_data, image_name, image_type)
            try:
                patient.new_picture(patient_id, image_location, image_name, image_type)
                response = {'success': True, 'message': 'Patient created successfully'}
            except Exception as e:
                response = {'success': False, 'message': 'Failed to save picture'}
    except Exception as e:
        response = {'success': False, 'message': str(e)}

    return jsonify(response), 200


# Routing to get the patient by ID:
@app.route('/api/get-patients', methods=['POST'])
def get_patient():
    data = request.get_json()
    patient_id = data.get('id')
    try:
        patient_data = patient.get_patient(patient_id)
        if patient_data:
            # Read image file
            #image_location = patient.get_image(patient_id)
            # Send patient data along with the image file
            #if os.path.exists(image_location):
                # Add image data to patient data
                #patient_data['image'] = send_file(image_location, as_attachment=True)
                #response = {'success': True, 'data': patient_data}
            #else:
            response = {'success': True, 'message': 'Image not found for patient', 'data': patient_data}
        else:
            response = {'success': False, 'message': 'Patient not found'}
    except Exception as e:
        response = {'success': False, 'message': str(e)}

    return jsonify(response), 200


# Routing to create a new vaccine:
@app.route('/api/new-vaccine', methods=['POST'])
def new_vaccine():
    data = request.get_json()
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


if __name__ == '__main__':
    app.run(port=5000)
