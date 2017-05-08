# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from model import *
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:r00t@localhost/healthroom_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/out', methods=['GET', 'POST'])
def out():
	if request.method == 'GET':
		return 'out page'
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
	if request.method == 'GET':
		return 'uploadHeighWeight'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			bloodpresuredata = tb_bloodpresure(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], item['auditDoctorEMPI'], item['auditDoctorName'], item['SBP'], item['DBP'], item['MBP'], item['pulse'], item['conclusion'])
			db.session.add(bloodpresuredata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadBloodSugar', methods=['GET', 'POST'])
def uploadBloodSugar():
	if request.method == 'GET':
		return 'uploadHeighWeight'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			bloodsugardata = tb_bloodsugar(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], item['auditDoctorEMPI'], item['auditDoctorName'], item['fastingBloodGlucose'],  item['conclusion'])
			db.session.add(bloodsugardata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadBodyComposion', methods=['GET', 'POST'])
def uploadBodyComposion():
	if request.method == 'GET':
		return 'uploadBodyComposion'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			bwhdata = tb_bwh(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], item['auditDoctorEMPI'], item['auditDoctorName'], 
				item['abdominalBodyFatmass'], item['abdominalBodyFatmassAdjust'],item['trunkSoftleanmassFlag'],
				item['visceralFatArea'], item['visceralFatmass'],item['weightAdjust'], item['weightHighLimit'],
				item['weightlowlimit'], item['whr'],item['abdominalBodyFatmassHighLimit'], item['abdominalBodyFatmassLowLimit'],
				item['adbominalSoftleanmass'], item['basicMetabolicrate'],item['bmi'], item['bmiHighLimit'],
				item['bmiLowLimit'], item['bodyAge'],item['bodyFatRate'], item['bodyFatHeighLimit'],
				item['bodyFatLowLimit'], item['bodyType'],item['extracellularFluid'], item['impedance'],
				item['intracellularFluid'], item['leanBodymass'],item['leanBodymassHighLimit'], item['leanBodymassLowLimit'],
				item['leftArmBodyFatmass'], item['leftArmSoftleanmass'],item['leftArmsoftleanmassFlag'], item['leftLegBodyFatmass'],
				item['leftLegSoftleanmass'], item['leftLegSoftleanmassFlag'],item['massOfBodyFat'], item['mineral'],
				item['mineralHighLimit'], item['mineralLowLimit'],item['obesexaxis'], item['protein'],
				item['proteinHighLimit'], item['proteinLowLimit'],item['rightArmbodyFatmass'], item['rightArmSoftleanmassFlag'],
				item['rightLegBodyFatmass'], item['rightLegSoftleanmassFlag'],item['rigtArmSoftleanmass'], item['rigtLegSoftleanmass'],
				item['softleanmass'], item['softleanmassAdjust'],item['softleanmassHighLimit'], item['softleanmassLowLimit'],
				item['standardWeight'], item['subcutaneousFatmass'],item['totalBodyWater'], item['totalBodyWaterHighLimit'],				
				item['totalBodyWaterLowLimit'], item['totalEnergyConsumption'],item['conclusion'])
			db.session.add(bwhdata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadBoneDensity', methods=['GET', 'POST'])
def uploadBoneDensity():
	if request.method == 'GET':
		return 'uploadBoneDensity'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			bonedensitydata = tb_bonedensity(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], item['auditDoctorEMPI'], item['auditDoctorName'], item['acousticveLocity'], 
				item['tValue'], item['zValue'], item['thScale'], item['toScale'], item['zYear'], item['riskLeavel'], 
				item['oi'], item['youngAdult'], item['ageMatched'], item['bua'], item['opr'], item['conclusion'])
			db.session.add(bonedensitydata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadBWH', methods=['GET', 'POST'])
def uploadBWH():
	if request.method == 'GET':
		return 'uploadBWH'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			bwhdata = tb_bwh(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], item['auditDoctorEMPI'], item['auditDoctorName'], 
				item['hip'], item['bust'],item['waist'], item['conclusion'])
			db.session.add(bwhdata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadEcg', methods=['GET', 'POST'])
def uploadEcg():
	if request.method == 'GET':
		return 'uploadEcg'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			ecgdata = tb_ecg(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], item['auditDoctorEMPI'], item['auditDoctorName'], item['HR'], item['PR'],
				item['P_Duration'], item['T_Duration'], item['QT_Duration'], item['QTc_Duration'], item['P_Axis'], 
				item['R_V5'], item['S_V1'], item['conclusion'])
			db.session.add(ecgdata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadElectronicVision', methods=['GET', 'POST'])
def uploadElectronicVision():
	if request.method == 'GET':
		return 'uploadElectronicVision'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			ecgdata = tb_ecg(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], item['auditDoctorEMPI'], item['auditDoctorName'], item['checkType'],
				item['leftEye'], item['rightEye'], item['conclusion'])
			db.session.add(ecgdata)
			db.session.commit()
		return 'upload data ok'

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

@app.route('/dataplatform/api/uploadLung', methods=['GET', 'POST'])
def uploadLung():
	if request.method == 'GET':
		return 'uploadlung'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data['data']
		for item in realdata:
			lungdata = tb_lung(data['familyCode'], data['familyName'], data['orgCode'], data['orgName'], 
				data['dataSource'], data['machineID'], item['examDate'], item['residentEMPI'], item['residentEMPI'], 
				item['residentName'], item['auditDoctorEMPI'], item['auditDoctorName'], item['HR'], item['PR'],
				item['P_Duration'], item['T_Duration'], item['QT_Duration'], item['QTc_Duration'], item['P_Axis'], 
				item['R_V5'], item['S_V1'], item['conclusion'])
			db.session.add(lungdata)
			db.session.commit()
		return 'upload data ok'


@app.route('/dataplatform/api/uploadResident', methods=['GET', 'POST'])
def uploadResident():
	if request.method == 'GET':
		return 'uploadResident'

if __name__ == '__main__':
	app.run(debug=True)



