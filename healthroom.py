# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from model import *
import json
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:r00t@localhost/healthroom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#该配置为True,则每次请求结束都会自动commit数据库的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

url_prifix = '/dataplatform/api'
error_msg = 'the data you post is not json'
return_msg = 'upload data ok'

#logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
logFormatStr = '[%(asctime)s] %(lineno)d} %(levelname)s - %(message)s'
logging.basicConfig(format = logFormatStr, filename='error.log', level=logging.DEBUG)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/out', methods=['GET', 'POST'])
def out():
	if request.method == 'GET':
		return 'out page'
	elif request.method == 'POST':
		#data = request.get_json(force = True, silent = True)
		#if data == None:
		#	return 'please post json data'
		#return json.dumps(data)
		body = request.get_data()
		header = request.headers.__str__()
		print 'headeradfadfadfasdfasdf'
		return header+body

@app.route(url_prifix+'/uploadBloodPresure', methods=['GET', 'POST'])
def uploadBloodPresure():
	if request.method == 'GET':
		return 'uploadBloodPresure'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadBloodPresure')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			bloodpresuredata = tb_bloodpresure(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('SBP'), item.get('DBP'), item.get('MBP'), item.get('pulse'), item.get('conclusion'))
			db.session.add(bloodpresuredata)

		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

@app.route(url_prifix+'/uploadBloodSugar', methods=['GET', 'POST'])
def uploadBloodSugar():
	if request.method == 'GET':
		return 'uploadBloodSugar'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadBloodSugar')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			bloodsugardata = tb_bloodsugar(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('fastingBloodGlucose'),  item.get('conclusion'))
			db.session.add(bloodsugardata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

@app.route(url_prifix+'/uploadBodyComposion', methods=['GET', 'POST'])
def uploadBodyComposion():
	if request.method == 'GET':
		return 'uploadBodyComposion'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadBodyComposion')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			bodycompositiondata = tb_bodycomposition(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
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
				item.get('totalBodyWaterLowLimit'), item.get('totalEnergyConsumption'), item.get('conclusion'))
			db.session.add(bodycompositiondata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

@app.route(url_prifix+'/uploadBoneDensity', methods=['GET', 'POST'])
def uploadBoneDensity():
	if request.method == 'GET':
		return 'uploadBoneDensity'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadBoneDensity')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			bonedensitydata = tb_bonedensity(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('acousticveLocity'), 
				item.get('tValue'), item.get('zValue'), item.get('thScale'), item.get('toScale'), item.get('zYear'), item.get('riskLeavel'), 
				item.get('oi'), item.get('youngAdult'), item.get('ageMatched'), item.get('bua'), item.get('opr'), item.get('conclusion'))
			db.session.add(bonedensitydata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

@app.route(url_prifix+'/uploadBWH', methods=['GET', 'POST'])
def uploadBWH():
	if request.method == 'GET':
		return 'uploadBWH'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadBWH')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			bwhdata = tb_bwh(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), 
				item.get('hip'), item.get('bust'),item.get('waist'), item.get('conclusion'))
			db.session.add(bwhdata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

@app.route(url_prifix+'/uploadEcg', methods=['GET', 'POST'])
def uploadEcg():
	if request.method == 'GET':
		return 'uploadEcg'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadEcg')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			ecgdata = tb_ecg(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('HR'), item.get('PR'),
				item.get('P_Duration'), item.get('T_Duration'), item.get('QT_Duration'), item.get('QTc_Duration'), item.get('P_Axis'), 
				item.get('R_V5'), item.get('S_V1'), item.get('conclusion'))
			db.session.add(ecgdata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

@app.route(url_prifix+'/uploadElectronicVision', methods=['GET', 'POST'])
def uploadElectronicVision():
	if request.method == 'GET':
		return 'uploadElectronicVision'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadElectronicVision')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			electronicvisiondata = tb_electronicvision(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), item.get('checkType'),
				item.get('leftEye'), item.get('rightEye'), item.get('conclusion'))
			db.session.add(electronicvisiondata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

@app.route(url_prifix+'/uploadHeighWeight', methods=['GET', 'POST'])
def uploadHeighWeight():
	if request.method == 'GET':
		return 'uploadHeighWeight'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadHeighWeight')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			heighweightdata = tb_heighweight(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
				item.get('residentName'), 'as', 'asd', item.get('heigh'), item.get('weight'), item.get('bmi'), item.get('conclusion'))
			db.session.add(heighweightdata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

@app.route(url_prifix+'/uploadLung', methods=['GET', 'POST'])
def uploadLung():
	if request.method == 'GET':
		return 'uploadlung'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadLung')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			lungdata = tb_lung(data.get('familyCode'), data.get('familyName'), data.get('orgCode'), data.get('orgName'), 
				data.get('dataSource'), data.get('machineID'), item.get('examDate'), item.get('IDCARD'), item.get('residentEMPI'), 
				item.get('residentName'), item.get('auditDoctorEMPI'), item.get('auditDoctorName'), 
				item.get('FVC'), item.get('FEV1'),	item.get('FEV2'), 
				item.get('FEV1Percent'), item.get('FEV2Percent'), item.get('FEV3Percent'), 
				item.get('MMF'), item.get('MVV1'), item.get('BSA1'), 
				item.get('M_B1'), item.get('PEF'), item.get('V75'), 
				item.get('V50'), item.get('V25'), item.get('V50_V25'), item.get('V25_H'), 
				item.get('MVV'), item.get('BSA'), item.get('MVV_BSA'), item.get('VC'), 
				item.get('TV'), item.get('IRV'), item.get('ERV'), item.get('IC'), 
				item.get('MV'), item.get('RR'), item.get('Result'),	item.get('conclusion'))
			db.session.add(lungdata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg


@app.route(url_prifix+'/uploadResident', methods=['GET', 'POST'])
def uploadResident():
	if request.method == 'GET':
		return 'uploadResident'
	elif request.method == 'POST':
		#data = request.get_json()
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadResident')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			residentdata = tb_resident(item.get('familyCode'), item.get('familyName'), item.get('orgCode'), item.get('orgName'), 
				item.get('dataSource'), item.get('machineID'), item.get('cardNo'), item.get('gender'),
				item.get('birthday'),item.get('phone'),item.get('nation'),item.get('address'),
				item.get('cardNo'), item.get('name'))
			db.session.add(residentdata)
		try:
			db.session.commit()
		except Exception as ex:
			return ex.__class__
		else:
			return return_msg

def geten(data):
	if data == None:
		return {}
	return data.getdata_en()

@app.route('/halthroom/getalldata_en')
def getAllData_en():
	#tb_lung.query.filter_by(IDCARD=idcard).order_by(tb_ecg.dataID.desc()).first()
	data_bloodpresure = tb_bloodpresure.query.first()
	data_bloodsugar = tb_bloodsugar.query.first()
	data_bodycomposition = tb_bodycomposition.query.first()
	data_bonedensity = tb_bonedensity.query.first()
	data_bwh = tb_bwh.query.first()
	data_ecg = tb_ecg.query.first()
	data_heighweight = tb_heighweight.query.first()
	data_electronicvision = tb_electronicvision.query.first()
	data_lung = tb_lung.query.first()

	AllData = {}
	AllData['bloodpresure'] = geten(data_bloodpresure)
	AllData['bloodsugar'] = geten(data_bloodsugar)
	AllData['bodycomposition'] = geten(data_bodycomposition)
	AllData['bonedensity'] = geten(data_bonedensity)
	AllData['bwh'] = geten(data_bwh)
	AllData['ecg'] = geten(data_ecg)
	AllData['heighweight'] = geten(data_heighweight)
	AllData['electronicvision'] = geten(data_electronicvision)
	AllData['lung'] = geten(data_lung)
	return json.dumps(AllData)

def getzh(data):
	if data == None:
		return {}
	return data.getdata_zh()

@app.route('/halthroom/getalldata_zh')
def getAllData_zh():
	data_resident = tb_resident.query.first()
	data_bloodpresure = tb_bloodpresure.query.first()
	data_bloodsugar = tb_bloodsugar.query.first()
	data_bodycomposition = tb_bodycomposition.query.first()
	data_bonedensity = tb_bonedensity.query.first()
	data_bwh = tb_bwh.query.first()
	data_ecg = tb_ecg.query.first()
	data_heighweight = tb_heighweight.query.first()
	data_electronicvision = tb_electronicvision.query.first()
	data_lung = tb_lung.query.first()

	AllData = {}
	AllData['resident'] = getzh(data_resident)
	AllData['bloodpresure'] = getzh(data_bloodpresure)
	AllData['bloodsugar'] = getzh(data_bloodsugar)
	AllData['bodycomposition'] = getzh(data_bodycomposition)
	AllData['bonedensity'] = getzh(data_bonedensity)
	AllData['bwh'] = getzh(data_bwh)
	AllData['ecg'] = getzh(data_ecg)
	AllData['heighweight'] = getzh(data_heighweight)
	AllData['electronicvision'] = getzh(data_electronicvision)
	AllData['lung'] = getzh(data_lung)
	return json.dumps(AllData, ensure_ascii=False)

@app.route('/get_en/<type>')
def get_en(type):
	data = {}
	itype = int(type)
	if itype == 0:
		data_resident = tb_resident.query.first()
		if data_resident != None:
			data = data_resident.getdata_en()
	elif itype == 1:
		data_bloodpresure = tb_bloodpresure.query.first()
		if data_bloodpresure != None:
			data = data_bloodpresure.getdata_en()
	elif itype == 2:
		data_bloodsugar = tb_bloodsugar.query.first()
		if data_bloodsugar != None:
			data = data_bloodsugar.getdata_en()
	elif itype == 3:
		data_bodycomposition = tb_bodycomposition.query.first()
		if data_bodycomposition != None:
			data = data_bodycomposition.getdata_en()
	elif itype == 4:
		data_bonedensity = tb_bonedensity.query.first()
		if data_bonedensity != None:
			data = data_bonedensity.getdata_en()
	elif itype == 5:
		data_bwh = tb_bwh.query.first()
		if data_bwh != None:
			data = data_bwh.getdata_en()
	elif itype == 6:
		data_ecg = tb_ecg.query.first()
		if data_ecg != None:
			data = data_ecg.getdata_en()
	elif itype == 7:
		data_heighweight = tb_heighweight.query.first()
		if data_heighweight != None:
			data = data_heighweight.getdata_en()
	elif itype == 8:
		data_electronicvision = tb_electronicvision.query.first()
		if data_electronicvision != None:
			data = data_electronicvision.getdata_en()
	elif itype == 9:
		data_lung = tb_lung.query.first()
		if data_lung != None:
			data = data_lung.getdata_en()
	else:
		data_lung = tb_lung.query.first()
		if data_lung != None:
			data = data_lung.getdata_en()

	return json.dumps(data, ensure_ascii=False)


@app.route('/get_zh/<type>')
def get_zh(type):
	data = {}
	itype = int(type)
	if itype == 0:
		data_resident = tb_resident.query.first()
		if data_resident != None:
			data = data_resident.getdata_zh()
	elif itype == 1:
		data_bloodpresure = tb_bloodpresure.query.first()
		if data_bloodpresure != None:
			data = data_bloodpresure.getdata_zh()
	elif itype == 2:
		data_bloodsugar = tb_bloodsugar.query.first()
		if data_bloodsugar != None:
			data = data_bloodsugar.getdata_zh()
	elif itype == 3:
		data_bodycomposition = tb_bodycomposition.query.first()
		if data_bodycomposition != None:
			data = data_bodycomposition.getdata_zh()
	elif itype == 4:
		data_bonedensity = tb_bonedensity.query.first()
		if data_bonedensity != None:
			data = data_bonedensity.getdata_zh()
	elif itype == 5:
		data_bwh = tb_bwh.query.first()
		if data_bwh != None:
			data = data_bwh.getdata_zh()
	elif itype == 6:
		data_ecg = tb_ecg.query.first()
		if data_ecg != None:
			data = data_ecg.getdata_zh()
	elif itype == 7:
		data_heighweight = tb_heighweight.query.first()
		if data_heighweight != None:
			data = data_heighweight.getdata_zh()
	elif itype == 8:
		data_electronicvision = tb_electronicvision.query.first()
		if data_electronicvision != None:
			data = data_electronicvision.getdata_zh()
	elif itype == 9:
		data_lung = tb_lung.query.first()
		if data_lung != None:
			data = data_lung.getdata_zh()
	else:
		data_lung = tb_lung.query.first()
		if data_lung != None:
			data = data_lung.getdata_zh()

	return json.dumps(data, ensure_ascii=False)

@app.route('/query', methods=['GET', 'POST'])
def query():
	if request.method == 'GET':
		return 'pls post sql'
	else:
		sql = request.get_data()
		if sql == None:
			return 'post data can not be none'
		import pymysql
		db = pymysql.connect('localhost', 'root', 'r00t', 'healthroom_flask')
		cursor = db.cursor()
		#cursor.execute('select * from tb_lung')
		cursor.execute(sql)
		data = cursor.fetchone()
		db.close()
		return data.__str__()

@app.route('/data_en/<idcard>')
def getOneResidentData_en(idcard):
	#tb_lung.query.filter_by(IDCARD=idcard).order_by(tb_ecg.dataID.desc()).first()
	data_bloodpresure = tb_bloodpresure.query.filter_by(IDCARD=idcard).order_by(tb_bloodpresure.dataID.desc()).first()
	data_bloodsugar = tb_bloodsugar.query.filter_by(IDCARD=idcard).order_by(tb_bloodsugar.dataID.desc()).first()
	data_bodycomposition = tb_bodycomposition.query.filter_by(IDCARD=idcard).order_by(tb_bodycomposition.dataID.desc()).first()
	data_bonedensity = tb_bonedensity.query.filter_by(IDCARD=idcard).order_by(tb_bonedensity.dataID.desc()).first()
	data_bwh = tb_bwh.query.filter_by(IDCARD=idcard).order_by(tb_bwh.dataID.desc()).first()
	data_ecg = tb_ecg.query.filter_by(IDCARD=idcard).order_by(tb_ecg.dataID.desc()).first()
	data_heighweight = tb_heighweight.query.filter_by(IDCARD=idcard).order_by(tb_heighweight.dataID.desc()).first()
	data_electronicvision = tb_electronicvision.query.filter_by(IDCARD=idcard).order_by(tb_electronicvision.dataID.desc()).first()
	data_lung = tb_lung.query.filter_by(IDCARD=idcard).order_by(tb_lung.dataID.desc()).first()

	AllData = {}
	AllData['bloodpresure'] = geten(data_bloodpresure)
	AllData['bloodsugar'] = geten(data_bloodsugar)
	AllData['bodycomposition'] = geten(data_bodycomposition)
	AllData['bonedensity'] = geten(data_bonedensity)
	AllData['bwh'] = geten(data_bwh)
	AllData['ecg'] = geten(data_ecg)
	AllData['heighweight'] = geten(data_heighweight)
	AllData['electronicvision'] = geten(data_electronicvision)
	AllData['lung'] = geten(data_lung)
	return json.dumps(AllData)		

@app.route('/data_zh/<idcard>')
def getOneResidentData_zh(idcard):
	#tb_lung.query.filter_by(IDCARD=idcard).order_by(tb_ecg.dataID.desc()).first()
	data_bloodpresure = tb_bloodpresure.query.filter_by(IDCARD=idcard).order_by(tb_bloodpresure.dataID.desc()).first()
	data_bloodsugar = tb_bloodsugar.query.filter_by(IDCARD=idcard).order_by(tb_bloodsugar.dataID.desc()).first()
	data_bodycomposition = tb_bodycomposition.query.filter_by(IDCARD=idcard).order_by(tb_bodycomposition.dataID.desc()).first()
	data_bonedensity = tb_bonedensity.query.filter_by(IDCARD=idcard).order_by(tb_bonedensity.dataID.desc()).first()
	data_bwh = tb_bwh.query.filter_by(IDCARD=idcard).order_by(tb_bwh.dataID.desc()).first()
	data_ecg = tb_ecg.query.filter_by(IDCARD=idcard).order_by(tb_ecg.dataID.desc()).first()
	data_heighweight = tb_heighweight.query.filter_by(IDCARD=idcard).order_by(tb_heighweight.dataID.desc()).first()
	data_electronicvision = tb_electronicvision.query.filter_by(IDCARD=idcard).order_by(tb_electronicvision.dataID.desc()).first()
	data_lung = tb_lung.query.filter_by(IDCARD=idcard).order_by(tb_lung.dataID.desc()).first()

	AllData = {}
	AllData['bloodpresure'] = getzh(data_bloodpresure)
	AllData['bloodsugar'] = getzh(data_bloodsugar)
	AllData['bodycomposition'] = getzh(data_bodycomposition)
	AllData['bonedensity'] = getzh(data_bonedensity)
	AllData['bwh'] = getzh(data_bwh)
	AllData['ecg'] = getzh(data_ecg)
	AllData['heighweight'] = getzh(data_heighweight)
	AllData['electronicvision'] = getzh(data_electronicvision)
	AllData['lung'] = getzh(data_lung)
	del data_ecg
	
	s = json.dumps(AllData, ensure_ascii=False)
	del AllData
	return s#json.dumps(AllData, ensure_ascii=False)


def main():
	logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
	logging.basicConfig(format = logFormatStr, filename='error.log', level=logging.DEBUG)
	app.run(debug=True, host='0.0.0.0', port=10086)

if __name__ == '__main__':
    #main()
	app.run(debug=True, host='0.0.0.0', port=10089)



