# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:r00t@localhost/healthroom_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return 'index page'
	elif request.method == 'POST':
		data = request.get_json(force = True, silent = True)
		if data == None:
			return 'please post json data'
		return json.dumps(data)

@app.route('/data/<id>')
def get_data(id):
	return id

@app.route('/dataplatform/api/uploadBloodPresure', methods=['GET', 'POST'])
def uploadBloodPresure():
	pass

@app.route('/dataplatform/api/uploadBloodSugar', methods=['GET', 'POST'])
def uploadBloodSugar():
	pass

@app.route('/dataplatform/api/uploadBodyComposion', methods=['GET', 'POST'])
def uploadBodyComposion():
	pass

@app.route('/dataplatform/api/uploadBoneDensity', methods=['GET', 'POST'])
def uploadBoneDensity():
	pass

@app.route('/dataplatform/api/uploadBWH', methods=['GET', 'POST'])
def uploadBWH():
	pass

@app.route('/dataplatform/api/uploadEcg', methods=['GET', 'POST'])
def uploadEcg():
	pass

@app.route('/dataplatform/api/uploadElectronicVision', methods=['GET', 'POST'])
def uploadElectronicVision():
	pass

@app.route('/dataplatform/api/uploadHeighWeight', methods=['GET', 'POST'])
def uploadHeighWeight():
	if request.method == 'GET':
		return 'uploadHeighWeight'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			heighweightdata = tb_heighweightdata(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], 'as', 'asd', item['heigh'], item['weight'], item['bmi'], item['conclusion'])
		#heighweightdata = tb_heighweightdata()
			db.session.add(heighweightdata)
			db.session.commit()
		return json.dumps(data)

@app.route('/dataplatform/api/uploadResident', methods=['GET', 'POST'])
def uploadResident():
	pass

if __name__ == '__main__':
	app.run(debug=True)



