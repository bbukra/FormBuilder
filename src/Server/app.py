from flask import Flask
import pymongo
from pymongo import MongoClient
from flask import request, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.debug = True

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

client = MongoClient()
Form_Builder_db = client.FormBuilder
 #the number of forms currently in the forms list db


@app.route("/")
def hello():
    return ""

@app.route('/add_New_Form', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def add_New_Form():
    
    global Form_Builder_db
    form_count = Form_Builder_db['FormsNames'].count_documents({})

    jsoned_form_Name = request.get_json(force=True)
    form_Name = jsoned_form_Name['formName']
    form_id = form_count + 1
    form = {"id": form_id, "FormName": form_Name}
    Form_Builder_db['FormsNames'].insert_one(form)
    
    form_Id_Str = "\"" + str(form_id) + "\""
    resp = Response(form_Id_Str)
    return resp

@app.route('/add_New_Field', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def add_New_Field():
    global Form_Builder_db
    
    field = request.get_json(force=True)    
    
    Form_Builder_db['FormFields'].insert_one(field)
    resp = Response("")
    return resp

@app.route('/get_Forms_List', methods=['GET'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def get_Forms_List():
    global Form_Builder_db
    form_count = Form_Builder_db['FormsNames'].count_documents({})
    
    all_Forms_Names = []
    for idx in range(1 , form_count + 1): #from 1 to form_count
        form = Form_Builder_db['FormsNames'].find_one({"id": idx}, {"_id": False})
        all_Forms_Names.append(form) #returns a document
    return jsonify(all_Forms_Names)

@app.route('/get_Form_Fields', methods=['GET'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def get_Form_Fields():
    global Form_Builder_db
    form_id = request.args.get('form_id')
    form_id_str = "\"" + str(form_id) + "\"" #the form id is saved as str in the db

    all_Fields = []
    number_Of_Fields = Form_Builder_db['FormFields'].count_documents({"form_Id": form_id_str})
    for idx in range(1, number_Of_Fields + 1):
        field = Form_Builder_db['FormFields'].find_one({"form_Id": form_id_str, "index": idx}, {"_id": False, "id": False})
        all_Fields.append(field)
    
    return jsonify(all_Fields)

@app.route('/submit_Form', methods=['POST'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def submit_Form():
    global Form_Builder_db
    all_Fields = request.get_json(force=True)
    form_id = all_Fields["form_Id"]
    form_id_str = "\"" + str(form_id) + "\"" #the form id is saved as str in the db

    number_of_sumbissions = Form_Builder_db['FormSubmissions'].count_documents({"form_Id": form_id})
    all_Fields["submission_Index"] = number_of_sumbissions + 1
    
    number_Of_Fields = Form_Builder_db['FormFields'].count_documents({"form_Id": form_id_str})
    for idx in range (1, number_Of_Fields + 1):
        input_Name = all_Fields[str(idx)]['inputName']
        all_Fields[str(idx)]['field_Label'] = get_Field_Label_By_Name(form_id_str, input_Name)

    Form_Builder_db['FormSubmissions'].insert_one(all_Fields)

    resp = Response("")
    return resp

def get_Field_Label_By_Name(form_id_str, input_Name):
    global Form_Builder_db

    document = Form_Builder_db['FormFields'].find_one({"form_Id": form_id_str, "inputName": input_Name})
    field_Label = document['fieldLabel']
    return field_Label

@app.route('/get_Form_Submissions', methods=['GET'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def get_Form_Submissions():
    global Form_Builder_db
    form_id = request.args.get('form_id')
    form_id_str = "\"" + str(form_id) + "\"" #the form id is saved as str in the db

    number_of_sumbissions = Form_Builder_db['FormSubmissions'].count_documents({"form_Id": form_id})
    all_Submissions = []
    for idx in range(1, number_of_sumbissions + 1):
        submission = Form_Builder_db['FormSubmissions'].find_one({"form_Id": form_id, "submission_Index": idx}, {"_id": False})
        all_Submissions.append(submission)
    
    number_Of_Fields = Form_Builder_db['FormFields'].count_documents({"form_Id": form_id_str})
    all_Submissions.append(number_Of_Fields) #for usage on client side
    
    return jsonify(all_Submissions)

if __name__ == '__main__':
    app.run(debug=True)