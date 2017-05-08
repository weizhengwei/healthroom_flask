# -*- coding: utf-8 -*-
from healthroom import db
from datetime import datetime


class tb_resident(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	cardNo = db.Column(db.String(255))
	gender = db.Column(db.Integer)
	birthday = db.Column(db.Date)
	phone = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	updateTime = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechindID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctor, auditDoctorName, SBP, DBP, MBP, pluse, conclusion):
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		# self.dataSource = dataSource
		# self.mechineID = mechineID
		# self.examDate = examDate
		# self.IDCARD = IDCARD
		# self.residentEMPI = residentEMPI
		# self.residentName = residentName
		# self.examDoctorEMPI = examDoctorEMPI
		# self.examDoctorName = examDoctorName
		# self.auditDoctorEMPI = auditDoctorEMPI
		# self.auditDoctorName = auditDoctorName
		# self.SBP = SBP
		# self.DBP = DBP
		# self.MBP = MBP
		# self.pluse = pluse
		# self.conclusion = conclusion


class tb_bloodpresure(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
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
	pulse = db.Column(db.Integer)
	conclusion = db.Column(db.String(255))

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, SBP, DBP, MBP, pulse, conclusion):
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.SBP = SBP
		self.DBP = DBP
		self.MBP = MBP
		self.pulse = pulse
		self.conclusion = conclusion



class tb_bloodsugar(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))
	fastingBloodGlucose = db.Column(db.Float)
	conclusion = db.Column(db.String(255))

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, fastingBloodGlucose, conclusion):
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.fastingBloodGlucose = fastingBloodGlucose
		self.conclusion = conclusion

class tb_bodycomposition(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
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

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, abdominalBodyFatmass,
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'

		self.abdominalBodyFatmass = abdominalBodyFatmass
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

class tb_bonedensity(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
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

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, acousticveLocity, tValue, zValue, thScale, 
				toScale, zYear, riskLeavel, oi, youngAdult, ageMatched, bua, opr, conclusion):
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
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


class tb_bwh(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
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

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, hip, bust, waist, conclusion):
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.hip = hip
		self.bust = bust
		self.waist = waist
		self.conclusion = conclusion


class tb_ecg(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
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

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, HR, PR, P_Duration, T_Duration, QT_Duration, QTc_Duration, P_Axis, R_V5, S_V1, conclusion):
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
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


class tb_heighweight(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
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

	# def __init__(self, data):
	# 	self.familyCode = data['familyCode']
	# 	self.familyName = data['familyName']
	# 	self.orgCode = data['orgCode']
	# 	self.orgName = data['orgName']
	# 	self.dataSource = data['dataSource']
	# 	self.mechineID = data['mechineID']
	# 	self.examDate = data['examDate']
	# 	self.IDCARD = 'IDCARD'
	# 	self.residentEMPI = data['residentEMPI']
	# 	self.residentName = 'residentName'
	# 	self.examDoctorEMPI = 'examDoctorEMPI'
	# 	self.examDoctorName = 'examDoctorName'
	# 	self.auditDoctorEMPI = 'auditDoctorEMPI'
	# 	self.auditDoctorName = 'auditDoctorName'
	# 	self.heigh = 123
	# 	self.weight = 123
	# 	self.bmi = 123
	# 	self.conclusion = 'conclusion'

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, 
		IDCARD, residentEMPI, residentName, auditDoctorEMPI, auditDoctorName, heigh, weight, bmi, conclusion):
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
		self.auditDoctorEMPI = 'auditDoctorEMPI'
		self.auditDoctorName = 'auditDoctorName'
		self.heigh = heigh
		self.weight = weight
		self.bmi = bmi
		self.conclusion = conclusion

class tb_electronicvision(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
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

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, checkType, leftEye, rightEye, conclusion):
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.checkType = checkType
		self.leftEye = leftEye
		self.rightEye = rightEye
		self.conclusion = conclusion


class tb_lung(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.String(255))
	examDate = db.Column(db.DateTime)
	IDCARD = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	examDoctorEMPI = db.Column(db.String(255))
	examDoctorName = db.Column(db.String(255))
	auditDoctorEMPI = db.Column(db.String(255))
	auditDoctorName = db.Column(db.String(255))

	FVC = db.Column(db.String(255))
	FEV1 = db.Column(db.String(255))
	FEV2 = db.Column(db.String(255))
	FEV1Percent = db.Column(db.String(255))
	FEV2Percent = db.Column(db.String(255))
	FEV3Percent = db.Column(db.String(255))
	MMF = db.Column(db.String(255))
	MVV1 = db.Column(db.String(255))
	BSA1 = db.Column(db.String(255))
	M_B1 = db.Column(db.String(255))
	PEF = db.Column(db.String(255))
	V75 = db.Column(db.String(255))
	V50 = db.Column(db.String(255))
	V25 = db.Column(db.String(255))
	V50_V25 = db.Column(db.String(255))
	V25_H = db.Column(db.String(255))
	MVV = db.Column(db.String(255))
	MVV_BSA = db.Column(db.String(255))
	VC = db.Column(db.String(255))
	TV = db.Column(db.String(255))
	IRV = db.Column(db.String(255))
	ERV = db.Column(db.String(255))
	IC = db.Column(db.String(255))
	MV = db.Column(db.String(255))
	RR = db.Column(db.String(255))
	Result = db.Column(db.String(255))
	conclusion = db.Column(db.String(255))

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, FVC, FEV1, FEV2, FEV1Percent, FEV2Percent, FEV3Percent, MMF,
				MVV1, BSA1, M_B1, PEF, V75, V50, V25, V50_V25, V25_H, MVV, MVV_BSA, VC, TV, IRV, ERV, IC,
				MV, RR, Result, conclusion):
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName
		self.FVC = FVC
		self.FEV1 = FEV1
		self.FEV2 = FEV2
		self.FEV1Percent = FEV1Percent
		self.FEV2Percent = FEV2Percent
		self.FEV3Percent = FEV3Percent
		self.MMF = MMF
		self.MVV1 = MVV1
		self.BSA1 = BSA1
		self.M_B1 = M_B1
		self.PEF = PEF
		self.V75 = V75
		self.V50 = V50
		self.V25 = V25
		self.V50_V25 = V50_V25
		self.V25_H = V25_H
		self.MVV = MVV
		self.MVV_BSA = MVV_BSA
		self.VC = VC
		self.TV = TV
		self.IRV = IRV
		self.ERV = ERV
		self.IC = IC
		self.MV = MV
		self.RR = RR
		self.Result = Result
		self.conclusion = conclusion



'''
肺功能：Lung function
用力肺活量(FVC)
1秒钟肺活量(FEV1)
2秒钟肺活量(FEV2)
3秒钟肺活量(FEV3)
1秒率(FEV1%)
2秒率(FEV2%)
3秒率(FEV3%)
最大呼气中段流速(MMF)
最大通气量/1秒量(MVV1)
BSA1(BSA1)
M/B1(M/B1)
峰值流量(PEF)
呼气至75%肺活量时对应流速值(V75)
呼气至50%肺活量时对应流速值(V50)
呼气至25%肺活量时对应流速值(V25)
呼气至50%25%肺活量时对应流速值(V50/V25)
V25与身高之比(V25/H)
实测最大通气量(MVV)
体表面积(BSA)
实测最大通气量与体表面积之比(MVV/BSA)
实测肺活量(VC)
潮气量(TV)
补吸气量(IRV)
补呼气量(ERV)
深呼气量(IC)
静息通气量(MV)
呼吸频率(RR)
结果(Result)
'''
