from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:r00t@localhost/healthroom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class tb_user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128))
	email = db.Column(db.String(128))
	def __init__(self, username, email):
		self.username = username
		self.email = email


class tb_bloodpresure(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.Date)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))
	SBP = db.Column(db.Float)
	DBP = db.Column(db.Float)
	MBP = db.Column(db.Float)
	pluse = db.Column(db.Integer)
	conclusion = db.Column(db.String(255))

	def ___init__(self, dataID, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, SBP, DBP, MBP, pluse, conclusion):
		self.dataID = dataID
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.examDate = examDate
		self.IDCARD = IDCARD
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.examDoctorEMPI = examDoctorEMPI
		self.examDoctorName = examDoctorName
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.SBP = SBP
		self.DBP = DBP
		self.MBP = MBP
		self.pluse = pluse
		self.conclusion = conclusion



class tb_bloodsugar(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.Date)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))
	fastingBloodGlucose = db.Column(db.Float)
	conclusion = db.Column(db.String(255))

	def ___init__(self, dataID, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, fastingBloodGlucose, conclusion):
		self.dataID = dataID
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.examDate = examDate
		self.IDCARD = IDCARD
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.examDoctorEMPI = examDoctorEMPI
		self.examDoctorName = examDoctorName
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.fastingBloodGlucose = fastingBloodGlucose
		self.conclusion = conclusion

class tb_bodycompositiondata(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.Date)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))

	abdominalBodyFatmass = db.Column(db.String(32))
	abdominalBodyFatmassAdjust = db.Column(db.String(32))
	trunkSoftleanmassFlag = db.Column(db.String(32))
	visceralFatArea = db.Column(db.String(32))
	visceralFatmass = db.Column(db.String(32))
	weight = db.Column(db.String(32))
	weightAdjust = db.Column(db.String(32))
	weightHighLimit = db.Column(db.String(32))
	weightlowlimit = db.Column(db.String(32))
	whr = db.Column(db.String(32))
	abdominalBodyFatmassHighLimit = db.Column(db.String(32))
	abdominalBodyFatmassLowLimit = db.Column(db.String(32))
	adbominalSoftleanmass = db.Column(db.String(32))
	basicMetabolicrate = db.Column(db.String(32))
	bmi = db.Column(db.String(32))
	bmiHighLimit = db.Column(db.String(32))
	bmiLowLimit = db.Column(db.String(32))
	bodyAge = db.Column(db.String(32))
	bodyFatRate = db.Column(db.String(32))
	bodyFatHeighLimit = db.Column(db.String(32))
	bodyFatLowLimit = db.Column(db.String(32))
	bodyType = db.Column(db.String(32))
	extracellularFluid = db.Column(db.String(32))
	impedance = db.Column(db.String(32))
	intracellularFluid = db.Column(db.String(32))
	leanBodymass = db.Column(db.String(32))
	leanBodymassHighLimit = db.Column(db.String(32))
	leanBodymassLowLimit = db.Column(db.String(32))
	leftArmBodyFatmass = db.Column(db.String(32))
	leftArmSoftleanmass = db.Column(db.String(32))
	leftArmsoftleanmassFlag = db.Column(db.String(32))
	leftLegBodyFatmass = db.Column(db.String(32))
	leftLegSoftleanmass = db.Column(db.String(32))
	leftLegSoftleanmassFlag = db.Column(db.String(32))
	massOfBodyFat = db.Column(db.String(32))
	mineral = db.Column(db.String(32))
	mineralHighLimit = db.Column(db.String(32))
	mineralLowLimit = db.Column(db.String(32))
	obesexaxis = db.Column(db.String(32))
	protein = db.Column(db.String(32))
	proteinHighLimit = db.Column(db.String(32))
	proteinLowLimit = db.Column(db.String(32))
	rightArmbodyFatmass = db.Column(db.String(32))
	rightArmSoftleanmassFlag = db.Column(db.String(32))
	rightLegBodyFatmass = db.Column(db.String(32))
	rightLegSoftleanmassFlag = db.Column(db.String(32))
	rigtArmSoftleanmass = db.Column(db.String(32))
	rigtLegSoftleanmass = db.Column(db.String(32))
	softleanmass = db.Column(db.String(32))
	softleanmassAdjust = db.Column(db.String(32))
	softleanmassHighLimit = db.Column(db.String(32))
	softleanmassLowLimit = db.Column(db.String(32))
	standardWeight = db.Column(db.String(32))
	subcutaneousFatmass = db.Column(db.String(32))
	totalBodyWater = db.Column(db.String(32))
	totalBodyWaterHighLimit = db.Column(db.String(32))
	totalBodyWaterLowLimit = db.Column(db.String(32))
	totalEnergyConsumption = db.Column(db.String(32))
	conclusion = db.Column(db.String(255))

	def ___init__(self, dataID, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, 
				abdominalBodyFatmassAdjust, trunkSoftleanmassFlag, visceralFatArea, visceralFatmass, weight, weightAdjust, weightHighLimit,
				weightlowlimit, whr, abdominalBodyFatmassHighLimit, abdominalBodyFatmassLowLimit, adbominalSoftleanmass, basicMetabolicrate,
				bmi, bmiHighLimit, bmiLowLimit, bodyAge, bodyFatRate, bodyFatHeighLimit, bodyFatLowLimit, bodyType, extracellularFluid, 
				leanBodymass,leanBodymassHighLimit, leanBodymassLowLimit, leftArmBodyFatmass,leftArmSoftleanmass,
				leftArmsoftleanmassFlag, leftLegBodyFatmass, leftLegSoftleanmass, leftLegSoftleanmassFlag,
				massOfBodyFat, mineral, mineralHighLimit, mineralLowLimit, obesexaxis, protein,
				proteinHighLimit, proteinLowLimit, rightArmbodyFatmass, rightArmSoftleanmassFlag, 
				rightLegBodyFatmass, rightLegSoftleanmassFlag, rigtArmSoftleanmass, rigtLegSoftleanmass,
				softleanmass, softleanmassAdjust, softleanmassHighLimit, softleanmassLowLimit,
				standardWeight, subcutaneousFatmass, totalBodyWater, totalBodyWaterHighLimit,
				totalBodyWaterLowLimit, totalEnergyConsumption, conclusion):
		self.dataID = dataID
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.examDate = examDate
		self.IDCARD = IDCARD
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.examDoctorEMPI = examDoctorEMPI
		self.examDoctorName = examDoctorName
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName

		self.abdominalBodyFatmassAdjust = abdominalBodyFatmassAdjust
		self.trunkSoftleanmassFlag = trunkSoftleanmassFlag
		self.visceralFatArea = visceralFatArea
		self.visceralFatmass = visceralFatArea
		self.weight = weight
		self.weightAdjust = weightAdjust
		self.weightHighLimit = weightHighLimit
		self.weightlowlimit = weightlowlimit
		self.whr = whr
		self.abdominalBodyFatmassHighLimit = abdominalBodyFatmassHighLimit
		self.abdominalBodyFatmassLowLimit = abdominalBodyFatmassLowLimit
		self.adbominalSoftleanmass = adbominalSoftleanmass
		self.basicMetabolicrate = basicMetabolicrate
		self.bmi = bmi
		self.bmiHighLimit = bmiHighLimit
		self.bmiLowLimit = bmiLowLimit
		self.bodyAge = bodyAge
		self.bodyFatRate = bodyFatRate
		self.bodyFatHeighLimit = bodyFatHeighLimit
		self.bodyFatLowLimit = bodyFatLowLimit
		self.bodyType = bodyType
		self.extracellularFluid = extracellularFluid
		self.impedance = impedance
		self.intracellularFluid = intracellularFluid
		self.leanBodymass = leanBodymass
		self.leanBodymassHighLimit = leanBodymassHighLimit
		self.leanBodymassLowLimit = leanBodymassLowLimit
		self.leftArmBodyFatmass = leftArmBodyFatmass
		self.leftArmSoftleanmass = leftArmSoftleanmass
		self.leftArmsoftleanmassFlag = leftArmsoftleanmassFlag
		self.leftLegBodyFatmass = leftLegBodyFatmass
		self.leftLegSoftleanmass = leftLegSoftleanmass
		self.leftLegSoftleanmassFlag = leftLegSoftleanmassFlag
		self.massOfBodyFat = massOfBodyFat
		self.mineral = mineral
		self.mineralHighLimit = mineralHighLimit
		self.mineralLowLimit = mineralLowLimit
		self.obesexaxis = obesexaxis
		self.protein = protein
		self.proteinHighLimit = proteinHighLimit
		self.proteinLowLimit = proteinLowLimit
		self.rightArmbodyFatmass = rightArmbodyFatmass
		self.rightArmSoftleanmassFlag = rightArmSoftleanmassFlag
		self.rightLegBodyFatmass = rightLegBodyFatmass
		self.rightLegSoftleanmassFlag = rightLegSoftleanmassFlag
		self.rigtArmSoftleanmass = rigtArmSoftleanmass
		self.rigtLegSoftleanmass = rigtLegSoftleanmass
		self.softleanmass = softleanmass
		self.softleanmassAdjust = softleanmassAdjust
		self.softleanmassHighLimit = softleanmassHighLimit
		self.softleanmassLowLimit = softleanmassLowLimit
		self.standardWeight = standardWeight
		self.subcutaneousFatmass = subcutaneousFatmass
		self.totalBodyWater = totalBodyWater
		self.totalBodyWaterHighLimit = totalBodyWaterHighLimit
		self.totalBodyWaterLowLimit = totalBodyWaterLowLimit
		self.totalEnergyConsumption = totalEnergyConsumption
		self.conclusion = conclusion

class tb_bonedensitydata(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.Date)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))
	acousticveLocity = db.Column(db.String(32))
	tValue = db.Column(db.String(32))
	zValue = db.Column(db.String(32))
	thScale = db.Column(db.String(32))
	toScale = db.Column(db.String(32))
	zYear = db.Column(db.String(32))
	riskLeavel = db.Column(db.String(32))
	oi = db.Column(db.String(32))
	youngAdult = db.Column(db.String(32))
	ageMatched = db.Column(db.String(32))
	bua = db.Column(db.String(32))
	opr = db.Column(db.String(32))
	conclusion = db.Column(db.String(255))

	def ___init__(self, dataID, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, acousticveLocity, tValue, zValue, thScale, 
				toScale, zYear, riskLeavel, oi, youngAdult, ageMatched, bua, opr, conclusion):
		self.dataID = dataID
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.examDate = examDate
		self.IDCARD = IDCARD
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.examDoctorEMPI = examDoctorEMPI
		self.examDoctorName = examDoctorName
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.acousticveLocity = acousticveLocity
		self.tValue = tValue
		self.zValue = zValue
		self.thScale = thScale
		self.toScale = toScale
		self.zYear = zYear
		self.riskLeavel = riskLeavel
		self.oi = oi
		self.youngAdult = youngAdult
		self.ageMatched = ageMatched
		self.bua = bua
		self.opr = opr
		self.conclusion = conclusion


class tb_bwhdata(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.Date)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))
	hip = db.Column(db.Float)
	bust = db.Column(db.Float)
	waist = db.Column(db.Float)
	conclusion = db.Column(db.String(255))

	def ___init__(self, dataID, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, hip, bust, waist, conclusion):
		self.dataID = dataID
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.examDate = examDate
		self.IDCARD = IDCARD
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.examDoctorEMPI = examDoctorEMPI
		self.examDoctorName = examDoctorName
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.hip = hip
		self.bust = bust
		self.waist = waist
		self.conclusion = conclusion


class tb_ecgdata(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.Date)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))
	HR = db.Column(db.Integer)
	PR = db.Column(db.Integer)
	P_Duration = db.Column(db.Integer)
	T_Duration = db.Column(db.Integer)
	QT_Duration = db.Column(db.Integer)
	QTc_Duration = db.Column(db.Integer)
	P_Axis = db.Column(db.Integer)
	R_V5 = db.Column(db.Integer)
	S_V1 = db.Column(db.Integer)
	conclusion = db.Column(db.String(255))

	def ___init__(self, dataID, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, HR, PR, P_Duration, T_Duration, QT_Duration, QTc_Duration, P_Axis, R_V5, S_V1, conclusion):
		self.dataID = dataID
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.examDate = examDate
		self.IDCARD = IDCARD
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.examDoctorEMPI = examDoctorEMPI
		self.examDoctorName = examDoctorName
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.HR = HR
		self.PR = PR
		self.P_Duration = P_Duration
		self.T_Duration = T_Duration
		self.QT_Duration = QT_Duration
		self.QTc_Duration = QTc_Duration
		self.P_Axis = P_Axis
		self.R_V5 = R_V5
		self.S_V1 = S_V1
		self.conclusion = conclusion


class tb_heighweightdata(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.Date)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))
	heigh = db.Column(db.Float)
	weight = db.Column(db.Float)
	bmi = db.Column(db.Float)
	conclusion = db.Column(db.String(255))

	def ___init__(self, dataID, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, heigh, weight, bmi, conclusion):
		self.dataID = dataID
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.examDate = examDate
		self.IDCARD = IDCARD
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.examDoctorEMPI = examDoctorEMPI
		self.examDoctorName = examDoctorName
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.heigh = heigh
		self.weight = weight
		self.bmi = bmi
		self.conclusion = conclusion

class tb_electronicvisiondata(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.Date)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))
	checkType = db.Column(db.String(128))
	leftEye = db.Column(db.String(128))
	rightEye = db.Column(db.String(128))
	conclusion = db.Column(db.String(255))

	def ___init__(self, dataID, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, checkType, leftEye, rightEye, conclusion):
		self.dataID = dataID
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.examDate = examDate
		self.IDCARD = IDCARD
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.examDoctorEMPI = examDoctorEMPI
		self.examDoctorName = examDoctorName
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.checkType = checkType
		self.leftEye = leftEye
		self.rightEye = rightEye
		self.conclusion = conclusion

@app.route('/')
def index():
	return 'index page'

@app.route('/data/<id>')
def get_data(id):
	return id



if __name__ == '__main__':
	app.run(debug=True)
