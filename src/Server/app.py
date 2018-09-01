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
    form_count = Form_Builder_db['FormsNames'].count()

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
    form_count = Form_Builder_db['FormsNames'].count()
    
    all_Forms_Names = []
    for idx in range(1 , form_count + 1): #from 1 to form_count
        all_Forms_Names.append(Form_Builder_db['FormsNames'].find_one({"id": idx}, {"_id": False})) #returns a document
    return jsonify(all_Forms_Names)

if __name__ == '__main__':
    app.run(debug=True)