# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from model import *
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:r00t@localhost/healthroom_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

url_prifix = '/dataplatform/api'

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
		realdata = data.get('data')
		for item in realdata:
			bloodpresuredata = tb_bloodpresure(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('SBP'), item.get('DBP'), item.get('MBP'), item.get('pulse'), item.get('conclusion'))
			db.session.add(bloodpresuredata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadBloodSugar', methods=['GET', 'POST'])
def uploadBloodSugar():
	if request.method == 'GET':
		return 'uploadHeighWeight'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data.get('data')
		for item in realdata:
			bloodsugardata = tb_bloodsugar(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('fastingBloodGlucose'),  item.get('conclusion'))
			db.session.add(bloodsugardata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadBodyComposion', methods=['GET', 'POST'])
def uploadBodyComposion():
	if request.method == 'GET':
		return 'uploadBodyComposion'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data.get('data')
		for item in realdata:
			bodycompositiondata = tb_bodycomposition(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), 
				item.get('abdominalBodyFatmass'), item.get('abdominalBodyFatmassAdjust'),item.get('trunkSoftleanmassFlag'),
				item.get('visceralFatArea'), item.get('visceralFatmass'), item.get('weight'), item.get('weightAdjust'), item.get('weightHighLimit'),
				item.get('weightlowlimit'), item.get('whr'),item.get('abdominalBodyFatmassHighLimit'), item.get('abdominalBodyFatmassLowLimit'),
				item.get('adbominalSoftleanmass'), item.get('basicMetabolicrate'),item.get('bmi'), item.get('bmiHighLimit'),
				item.get('bmiLowLimit'), item.get('bodyAge'),item.get('bodyFatRate'), item.get('bodyFatHeighLimit'),
				item.get('bodyFatLowLimit'), item.get('bodyType'),item.get('extracellularFluid'), item.get('impedance'),
				item.get('intracellularFluid'), item.get('leanBodymass'),item.get('leanBodymassHighLimit'), item.get('leanBodymassLowLimit'),
				item.get('leftArmBodyFatmass'), item.get('leftArmSoftleanmass'),item.get('leftArmsoftleanmassFlag'), item.get('leftLegBodyFatmass'),
				item.get('leftLegSoftleanmass'), item.get('leftLegSoftleanmassFlag'),item.get('massOfBodyFat'), item.get('mineral'),
				item.get('mineralHighLimit'), item.get('mineralLowLimit'),item.get('obesexaxis'), item.get('protein'),
				item.get('proteinHighLimit'), item.get('proteinLowLimit'),item.get('rightArmbodyFatmass'), item.get('rightArmSoftleanmassFlag'),
				item.get('rightLegBodyFatmass'), item.get('rightLegSoftleanmassFlag'),item.get('rigtArmSoftleanmass'), item.get('rigtLegSoftleanmass'),
				item.get('softleanmass'), item.get('softleanmassAdjust'),item.get('softleanmassHighLimit'), item.get('softleanmassLowLimit'),
				item.get('standardWeight'), item.get('subcutaneousFatmass'),item.get('totalBodyWater'), item.get('totalBodyWaterHighLimit'),				
				item.get('totalBodyWaterLowLimit'), item.get('totalEnergyConsumption'),item.get('conclusion'))
			db.session.add(bodycompositiondata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadBoneDensity', methods=['GET', 'POST'])
def uploadBoneDensity():
	if request.method == 'GET':
		return 'uploadBoneDensity'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data.get('data')
		for item in realdata:
			bonedensitydata = tb_bonedensity(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('acousticveLocity'), 
				item.get('tValue'), item.get('zValue'), item.get('thScale'), item.get('toScale'), item.get('zYear'), item.get('riskLeavel'), 
				item.get('oi'), item.get('youngAdult'), item.get('ageMatched'), item.get('bua'), item.get('opr'), item.get('conclusion'))
			db.session.add(bonedensitydata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadBWH', methods=['GET', 'POST'])
def uploadBWH():
	if request.method == 'GET':
		return 'uploadBWH'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data.get('data')
		for item in realdata:
			bwhdata = tb_bwh(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), 
				item.get('hip'), item.get('bust'),item.get('waist'), item.get('conclusion'))
			db.session.add(bwhdata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadEcg', methods=['GET', 'POST'])
def uploadEcg():
	if request.method == 'GET':
		return 'uploadEcg'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data.get('data')
		for item in realdata:
			ecgdata = tb_ecg(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('HR'), item.get('PR'),
				item.get('P_Duration'), item.get('T_Duration'), item.get('QT_Duration'), item.get('QTc_Duration'), item.get('P_Axis'), 
				item.get('R_V5'), item.get('S_V1'), item.get('conclusion'))
			db.session.add(ecgdata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadElectronicVision', methods=['GET', 'POST'])
def uploadElectronicVision():
	if request.method == 'GET':
		return 'uploadElectronicVision'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data.get('data')
		for item in realdata:
			electronicvisiondata = tb_electronicvision(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('checkType'),
				item.get('leftEye'), item.get('rightEye'), item.get('conclusion'))
			db.session.add(electronicvisiondata)
			db.session.commit()
		return 'upload data ok'

@app.route('/dataplatform/api/uploadHeighWeight', methods=['GET', 'POST'])
def uploadHeighWeight():
	if request.method == 'GET':
		return 'uploadHeighWeight'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data.get('data')
		for item in realdata:
			heighweightdata = tb_heighweight(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), 'as', 'asd', item.get('heigh'), item.get('weight'), item.get('bmi'), item.get('conclusion'))
		#heighweightdata = tb_heighweightdata()
			db.session.add(heighweightdata)
			db.session.commit()
		return 'upload data ok'#json.dumps(data)

@app.route(url_prifix+'/uploadLung', methods=['GET', 'POST'])
def uploadLung():
	if request.method == 'GET':
		return 'uploadlung'
	elif request.method == 'POST':
		data = request.get_json()
		realdata = data.get('data')
		for item in realdata:
			lungdata = tb_lung(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('residentEMPI'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), 
				item.get('FVC'), item.get('FEV1'),	item.get('FEV2'), 
				item.get('FEV1Percent'), item.get('FEV2Percent'), item.get('FEV3Percent'), 
				item.get('MMF'), item.get('MVV1'), item.get('BSA1'), 
				item.get('M_B1'), item.get('PEF'), item.get('V75'), 
				item.get('V50'), item.get('V25'), item.get('V50_V25'), item.get('V25_H'), 
				item.get('MVV'), item.get('MVV_BSA'), item.get('VC'), item.get('TV'), 
				item.get('IRV'), item.get('ERV'), item.get('IC'), item.get('MV'), item.get('RR'), 
				item.get('Result'),	item.get('conclusion'))
			db.session.add(lungdata)
			db.session.commit()
		return 'upload data ok'


@app.route('/dataplatform/api/uploadResident', methods=['GET', 'POST'])
def uploadResident():
	if request.method == 'GET':
		return 'uploadResident'

if __name__ == '__main__':
	app.run(debug=True)



