# -*- coding: utf-8 -*-
from model import *
import json
import logging
import pymysql

mydb = pymysql.connect('localhost', 'root', 'r00t', 'healthroom', charset='utf8')
mydb.autocommit(True)

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
			db.session.rollback()
			return return_msg
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

@app.route('/data_zh2/<idcard>')
def getOneResidentData_zh2(idcard):
	#tb_lung.query.filter_by(IDCARD=idcard).order_by(tb_ecg.dataID.desc()).first()
	idcard = idcard[0:idcard.find('?')]
	data_bloodpresure = tb_bloodpresure.query.filter_by(residentEMPI=idcard).order_by(tb_bloodpresure.dataID.desc()).first()
	data_bloodsugar = tb_bloodsugar.query.filter_by(residentEMPI=idcard).order_by(tb_bloodsugar.dataID.desc()).first()
	data_bodycomposition = tb_bodycomposition.query.filter_by(residentEMPI=idcard).order_by(tb_bodycomposition.dataID.desc()).first()
	data_bonedensity = tb_bonedensity.query.filter_by(residentEMPI=idcard).order_by(tb_bonedensity.dataID.desc()).first()
	data_bwh = tb_bwh.query.filter_by(residentEMPI=idcard).order_by(tb_bwh.dataID.desc()).first()
	data_ecg = tb_ecg.query.filter_by(residentEMPI=idcard).order_by(tb_ecg.dataID.desc()).first()
	data_heighweight = tb_heighweight.query.filter_by(residentEMPI=idcard).order_by(tb_heighweight.dataID.desc()).first()
	data_electronicvision = tb_electronicvision.query.filter_by(residentEMPI=idcard).order_by(tb_electronicvision.dataID.desc()).first()
	data_lung = tb_lung.query.filter_by(residentEMPI=idcard).order_by(tb_lung.dataID.desc()).first()

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


@app.route('/data_zh3/<idcard>')
def getOneResidentData_zh3(idcard):
	#tb_lung.query.filter_by(IDCARD=idcard).order_by(tb_ecg.dataID.desc()).first()
	idcard = idcard[0:idcard.find('?')]
	data_bloodpresure = tb_bloodpresure.query.filter_by(residentEMPI=idcard).first()
	data_bloodsugar = tb_bloodsugar.query.filter_by(residentEMPI=idcard).first()
	data_bodycomposition = tb_bodycomposition.query.filter_by(residentEMPI=idcard).first()
	data_bonedensity = tb_bonedensity.query.filter_by(residentEMPI=idcard).first()
	data_bwh = tb_bwh.query.filter_by(residentEMPI=idcard).first()
	data_ecg = tb_ecg.query.filter_by(residentEMPI=idcard).first()
	data_heighweight = tb_heighweight.query.filter_by(residentEMPI=idcard).first()
	data_electronicvision = tb_electronicvision.query.filter_by(residentEMPI=idcard).first()
	data_lung = tb_lung.query.filter_by(residentEMPI=idcard).first()

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


def get_bloodpresure(data):
	data_bloodpresure_zh = {}
	if data == None:
		return data_bloodpresure_zh
	data_bloodpresure_zh['收缩压'] = data.get('SBP')
	data_bloodpresure_zh['舒张压'] = data.get('DBP')
	data_bloodpresure_zh['平均压'] = data.get('MBP')
	data_bloodpresure_zh['脉搏'] = data.get('pulse')
	return data_bloodpresure_zh

def get_bloodsugar(data):
	data_bloodsugar_zh = {}
	if data == None:
		return data_bloodsugar_zh
	data_bloodsugar_zh['空腹血糖'] = data.get('fastingBloodGlucose')
	return data_bloodsugar_zh

def get_bodycomposition(data):
	data_bodycomposition_en = {}
	if data == None:
		return data_bodycomposition_en
	data_bodycomposition_en['躯干脂肪量'] = data.get('abdominalBodyFatmass')
	data_bodycomposition_en['体脂肪量调节值'] = data.get('abdominalBodyFatmassAdjust')
	data_bodycomposition_en['躯干肌肉水平'] = data.get('trunkSoftleanmassFlag')
	data_bodycomposition_en['内脏脂肪面积'] = data.get('visceralFatArea')
	data_bodycomposition_en['内脏脂肪质量'] = data.get('visceralFatmass')
	data_bodycomposition_en['体重'] = data.get('weight')
	data_bodycomposition_en['体重调节值'] = data.get('weightAdjust')
	data_bodycomposition_en['体重高值'] = data.get('weightHighLimit')
	data_bodycomposition_en['体重低值'] = data.get('weightlowlimit')
	data_bodycomposition_en['腰臀比'] = data.get('whr')
	data_bodycomposition_en['体脂肪量高值'] = data.get('abdominalBodyFatmassHighLimit')
	data_bodycomposition_en['体脂肪量低值'] = data.get('abdominalBodyFatmassLowLimit')
	data_bodycomposition_en['躯干肌肉量'] = data.get('adbominalSoftleanmass')
	data_bodycomposition_en['基础代谢量'] = data.get('basicMetabolicrate')
	data_bodycomposition_en['身体质量指数'] = data.get('bmi')
	data_bodycomposition_en['身体质量指数高值'] = data.get('bmiHighLimit')
	data_bodycomposition_en['身体质量指数低值'] = data.get('bmiLowLimit')
	data_bodycomposition_en['身体年龄'] = data.get('bodyAge')
	data_bodycomposition_en['体脂肪率'] = data.get('bodyFatRate')
	data_bodycomposition_en['体脂肪率高值'] = data.get('bodyFatHeighLimit')
	data_bodycomposition_en['体脂肪率低值'] = data.get('bodyFatLowLimit')
	data_bodycomposition_en['bodyType'] = data.get('bodyType')
	data_bodycomposition_en['细胞外液'] = data.get('extracellularFluid')
	data_bodycomposition_en['阻抗'] = data.get('impedance')
	data_bodycomposition_en['细胞内液'] = data.get('intracellularFluid')
	data_bodycomposition_en['去脂体重'] = data.get('leanBodymass')
	data_bodycomposition_en['去脂体重高值'] = data.get('leanBodymassHighLimit')
	data_bodycomposition_en['去脂体重低值'] = data.get('leanBodymassLowLimit')
	data_bodycomposition_en['左上肢体脂肪量'] = data.get('leftArmBodyFatmass')
	data_bodycomposition_en['左上肢肌肉量'] = data.get('leftArmSoftleanmass')
	data_bodycomposition_en['左臂肌肉水平'] = data.get('leftArmsoftleanmassFlag')
	data_bodycomposition_en['左下肢体脂肪量'] = data.get('leftLegBodyFatmass')
	data_bodycomposition_en['左下肢肌肉量'] = data.get('leftLegSoftleanmass')
	data_bodycomposition_en['左腿肌肉水平'] = data.get('leftLegSoftleanmassFlag')
	data_bodycomposition_en['体脂肪量'] = data.get('massOfBodyFat')
	data_bodycomposition_en['无机盐'] = data.get('mineral')
	data_bodycomposition_en['无机盐高值'] = data.get('mineralHighLimit')
	data_bodycomposition_en['无机盐低值'] = data.get('mineralLowLimit')
	data_bodycomposition_en['obesexaxis'] = data.get('obesexaxis')
	data_bodycomposition_en['蛋白质'] = data.get('protein')
	data_bodycomposition_en['蛋白质高值'] = data.get('proteinHighLimit')
	data_bodycomposition_en['蛋白质低值'] = data.get('proteinLowLimit')
	data_bodycomposition_en['右上肢体脂肪量'] = data.get('rightArmbodyFatmass')
	data_bodycomposition_en['右臂肌肉水平'] = data.get('rightArmSoftleanmassFlag')
	data_bodycomposition_en['右下肢体脂肪量'] = data.get('rightLegBodyFatmass')
	data_bodycomposition_en['右上肢肌肉量'] = data.get('rigtArmSoftleanmass')
	data_bodycomposition_en['右下肢肌肉量'] = data.get('rigtLegSoftleanmass')
	data_bodycomposition_en['肌肉量'] = data.get('softleanmass')
	data_bodycomposition_en['肌肉量调节值'] = data.get('softleanmassAdjust')
	data_bodycomposition_en['肌肉量高值'] = data.get('softleanmassHighLimit')
	data_bodycomposition_en['肌肉量低值'] = data.get('softleanmassLowLimit')
	data_bodycomposition_en['标准体重'] = data.get('standardWeight')
	data_bodycomposition_en['皮下脂肪量'] = data.get('subcutaneousFatmass')
	data_bodycomposition_en['身体水分'] = data.get('totalBodyWater')
	data_bodycomposition_en['身体水分高值'] = data.get('totalBodyWaterHighLimit')
	data_bodycomposition_en['身体水分低值'] = data.get('totalBodyWaterLowLimit')
	data_bodycomposition_en['总能量消耗'] = data.get('totalEnergyConsumption')
	return data_bodycomposition_en


def get_bonedensity(data):
	data_bonedensity_zh = {}
	if data == None:
		return data_bonedensity_zh
	data_bonedensity_zh['声速'] = data.get('acousticveLocity')
	data_bonedensity_zh['T值'] = data.get('tValue')
	data_bonedensity_zh['Z值'] = data.get('zValue')
	data_bonedensity_zh['测值/峰值比'] = data.get('thScale')
	data_bonedensity_zh['测值/均值比'] = data.get('toScale')
	data_bonedensity_zh['Z值相对年龄'] = data.get('zYear')
	data_bonedensity_zh['相对骨折风险'] = data.get('riskLeavel')
	data_bonedensity_zh['骨质疏松指数'] = data.get('oi')
	data_bonedensity_zh['成人对比【%】'] = data.get('youngAdult')
	data_bonedensity_zh['同龄对比【%】'] = data.get('ageMatched')
	data_bonedensity_zh['宽波段超声衰减值'] = data.get('bua')
	data_bonedensity_zh['多次测量误差'] = data.get('opr')
	return data_bonedensity_zh

def get_bwh(data):
	data_bwh_zh = {}
	if data == None:
		return data_bwh_zh
	data_bwh_zh['胸围'] = data.get('hip')
	data_bwh_zh['臀围'] = data.get('bust')
	data_bwh_zh['胸围'] = data.get('waist')
	return data_bwh_zh

def get_ecg(data):
	data_ecg_zh = {}
	if data == None:
		return data_ecg_zh
	data_ecg_zh['心率'] = data.get('HR')
	data_ecg_zh['PR间期'] = data.get('PR')
	data_ecg_zh['P时限'] = data.get('P_Duration')
	data_ecg_zh['T时限'] = data.get('T_Duration')
	data_ecg_zh['QT时限'] = data.get('QT_Duration')
	data_ecg_zh['QTc时限'] = data.get('QTc_Duration')
	data_ecg_zh['P电轴'] = data.get('P_Axis')
	data_ecg_zh['R_V5'] = data.get('R_V5')
	data_ecg_zh['S_V1'] = data.get('S_V1')
	return data_ecg_zh

def get_heighweight(data):
	data_heighweight_zh = {}
	if data == None:
		return data_heighweight_zh
	data_heighweight_zh['身高'] = data.get('heigh')
	data_heighweight_zh['体重'] = data.get('weight')
	data_heighweight_zh['BMI(体重/身高^2)'] = data.get('bmi')
	return data_heighweight_zh


def get_electronicvision(data):
	data_electronicvision_zh = {}
	if data == None:
		return data_electronicvision_zh
	data_electronicvision_zh['检查类型'] = data.get('checkType')
	data_electronicvision_zh['左眼'] = data.get('leftEye')
	data_electronicvision_zh['右眼'] = data.get('rightEye')
	return data_electronicvision_zh

def ge_lung(data):
	data_lung_zh = {}
	if data == None:
		return data_lung_zh
	data_lung_zh['用力肺活量'] = data.get('FVC')
	data_lung_zh['1秒钟肺活量'] = data.get('FEV1')
	data_lung_zh['2秒钟肺活量'] = data.get('FEV2')
	data_lung_zh['1秒率(FEV1%)'] = data.get('FEV1Percent')
	data_lung_zh['2秒率(FEV2%)'] = data.get('FEV2Percent')
	data_lung_zh['3秒率(FEV3%)'] = data.get('FEV3Percent')
	data_lung_zh['最大呼气中段流速(MMF)'] = data.get('MMF')
	data_lung_zh['最大通气量/1秒量(MVV1)'] = data.get('MVV1')
	data_lung_zh['BSA1(BSA1)'] = data.get('BSA1')
	data_lung_zh['M_B1'] = data.get('M_B1')
	data_lung_zh['峰值流量(PEF)'] = data.get('PEF')
	data_lung_zh['呼气至75%肺活量时对应流速值(V75)'] = data.get('V75')
	data_lung_zh['呼气至50%肺活量时对应流速值(V50)'] = data.get('V50')
	data_lung_zh['呼气至25%肺活量时对应流速值(V25)'] = data.get('V25')
	data_lung_zh['呼气至50%25%肺活量时对应流速值(V50/V25)'] = data.get('V50_V25')
	data_lung_zh['V25与身高之比(V25/H)'] = data.get('V25_H')
	data_lung_zh['实测最大通气量(MVV)'] = data.get('MVV')
	data_lung_zh['体表面积(BSA)'] = data.get('BSA')
	data_lung_zh['实测最大通气量与体表面积之比(MVV/BSA)'] = data.get('MVV_BSA')
	data_lung_zh['实测肺活量(VC)'] = data.get('VC')
	data_lung_zh['潮气量(TV)'] = data.get('TV')
	data_lung_zh['补吸气量(IRV)'] = data.get('IRV')
	data_lung_zh['补呼气量(ERV)'] = data.get('ERV')
	data_lung_zh['深呼气量(IC)'] = data.get('IC')
	data_lung_zh['静息通气量(MV)'] = data.get('MV')
	data_lung_zh['呼吸频率(RR)'] = data.get('RR')
	data_lung_zh['结果(Result)'] = data.get('Result')
	return data_lung_zh

@app.route('/data_zh/<idcard>')
def ttt(idcard):
	#cursor = db.cursor()
	cursor = mydb.cursor(cursor=pymysql.cursors.DictCursor)
	sql = "SELECT * FROM tb_bloodpresure WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_bloodpresure = cursor.fetchone()

	sql = "SELECT * FROM tb_bloodsugar WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_bloodsugar = cursor.fetchone()

	sql = "SELECT * FROM tb_bodycomposition WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_bodycomposition = cursor.fetchone()

	sql = "SELECT * FROM tb_bonedensity WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_bonedensity = cursor.fetchone()

	sql = "SELECT * FROM tb_bwh WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_bwh = cursor.fetchone()

	sql = "SELECT * FROM tb_ecg WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_ecg = cursor.fetchone()

	sql = "SELECT * FROM tb_heighweight WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_heighweight= cursor.fetchone()

	sql = "SELECT * FROM tb_electronicvision WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_electronicvision = cursor.fetchone()

	sql = "SELECT * FROM tb_lung WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_lung = cursor.fetchone()

	AllData = {}
	AllData['bloodpresure'] = get_bloodpresure(data_bloodpresure)
	AllData['bloodsugar'] = get_bloodsugar(data_bloodsugar)
	AllData['bodycomposition'] = get_bodycomposition(data_bodycomposition)
	AllData['bonedensity'] = get_bonedensity(data_bonedensity)
	AllData['bwh'] = get_bwh(data_bwh)
	AllData['ecg'] = get_ecg(data_ecg)
	AllData['heighweight'] = get_heighweight(data_heighweight)
	AllData['electronicvision'] = get_electronicvision(data_electronicvision)
	AllData['lung'] = ge_lung(data_lung)
	# db.close()
	
	return json.dumps(AllData, ensure_ascii=False)

@app.route(url_prifix+'/getAllResident', methods=['GET', 'POST'])
def get_all_resient():
	data = tb_resident.query.all()
	if data == None:
		return 'there is no resident'
	AllData = []
	for item in data:
		it = {}
		it['name'] = item.residentName
		it['idcard'] = item.residentEMPI
		#AllData.append(item.getdata_zh())
		AllData.append(it)
	db.session.commit()
	return json.dumps(AllData, ensure_ascii=False)

@app.route('/getSpecialData/<idcard>')
def get_special_data(idcard):
	#cursor = db.cursor()
	cursor = mydb.cursor(cursor=pymysql.cursors.DictCursor)
	sql = "SELECT * FROM tb_bloodpresure WHERE residentEMPI='%s' ORDER BY dataID DESC" % idcard
	cursor.execute(sql)
	data_bloodpresure = cursor.fetchone()
	return 'getSpecialData'


def main():
	logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
	logging.basicConfig(format = logFormatStr, filename='error.log', level=logging.DEBUG)
	app.run(debug=True, host='0.0.0.0', port=10086)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=10089)