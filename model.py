# -*- coding: utf-8 -*-
from healthroom import db
from datetime import datetime
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class tb_resident(db.Model):
	dataID = db.Column(db.Integer, primary_key=True, autoincrement=True)
	familyCode = db.Column(db.String(255))
	familyName = db.Column(db.String(255))
	orgCode = db.Column(db.String(255))
	orgName = db.Column(db.String(255))
	dataSource = db.Column(db.Integer)
	mechineID = db.Column(db.Integer)
	IDCARD = db.Column(db.String(255), unique=True)
	gender = db.Column(db.Integer)
	birthday = db.Column(db.Date)
	phone = db.Column(db.String(255))
	nation = db.Column(db.String(255))
	address = db.Column(db.String(255))
	residentEMPI = db.Column(db.String(255))
	residentName = db.Column(db.String(255))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, IDCARD, gender, birthday, 
				phone, nation, address, residentEMPI, residentName):
		self.familyCode = familyCode
		self.familyName = familyName
		self.orgCode = orgCode
		self.orgName = orgName
		self.dataSource = dataSource
		self.mechineID = mechineID
		self.IDCARD = IDCARD
		self.gender = gender
		self.birthday = birthday
		self.phone = phone
		self.nation = nation
		self.address = address
		self.residentEMPI = residentEMPI
		self.residentName = residentName
		self.uploadTime = datetime.now()

	def getdata_en(self):
		data_resident_en = {}
		data_resident_en['IDCARD'] = self.IDCARD
		data_resident_en['gender'] = self.gender
		data_resident_en['birthday'] = self.birthday.strftime('%Y-%m-%d')
		data_resident_en['phone'] = self.phone
		data_resident_en['nation'] = self.nation
		data_resident_en['address'] = self.address
		return data_resident_en

	def getdata_zh(self):
		data_resident_zh = {}
		data_resident_zh['卡号'] = self.IDCARD
		data_resident_zh['性别'] = self.gender
		data_resident_zh['出生日期'] = self.birthday.strftime('%Y-%m-%d')
		data_resident_zh['电话'] = self.phone
		data_resident_zh['民族'] = self.nation
		data_resident_zh['家庭住址'] = self.address
		return data_resident_zh

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
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

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
		self.uploadTime = datetime.now()

	def getdata_en(self):
		data_bloodpresure_en = {}
		data_bloodpresure_en['SBP'] = self.SBP
		data_bloodpresure_en['DBP'] = self.DBP
		data_bloodpresure_en['MBP'] = self.MBP
		data_bloodpresure_en['pulse'] = self.pulse
		return data_bloodpresure_en

	def getdata_zh(self):
		data_bloodpresure_zh = {}
		data_bloodpresure_zh['收缩压'] = self.SBP
		data_bloodpresure_zh['舒张压'] = self.DBP
		data_bloodpresure_zh['平均压'] = self.MBP
		data_bloodpresure_zh['脉搏'] = self.pulse
		return data_bloodpresure_zh

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
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

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
		self.uploadTime = datetime.now()
	def getdata_en(self):
		data_bloodsugar_en = {}
		data_bloodsugar_en['fastingBloodGlucose'] = self.fastingBloodGlucose
		return data_bloodsugar_en

	def getdata_zh(self):
		data_bloodsugar_zh = {}
		data_bloodsugar_zh['空腹血糖'] = self.fastingBloodGlucose
		return data_bloodsugar_zh

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
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, abdominalBodyFatmass,
				abdominalBodyFatmassAdjust, trunkSoftleanmassFlag, visceralFatArea, visceralFatmass, weight, weightAdjust, weightHighLimit,
				weightlowlimit, whr, abdominalBodyFatmassHighLimit, abdominalBodyFatmassLowLimit, adbominalSoftleanmass, basicMetabolicrate,
				bmi, bmiHighLimit, bmiLowLimit, bodyAge, bodyFatRate, bodyFatHeighLimit, bodyFatLowLimit, bodyType, extracellularFluid, 
				impedance, intracellularFluid, leanBodymass,leanBodymassHighLimit, leanBodymassLowLimit, leftArmBodyFatmass,
				leftArmSoftleanmass, leftArmsoftleanmassFlag, leftLegBodyFatmass, leftLegSoftleanmass, leftLegSoftleanmassFlag,
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
		self.examDoctorEMPI = 'examDoctorEMPI'
		self.examDoctorName = 'examDoctorName'
		self.auditDoctorEMPI = auditDoctorEMPI
		self.auditDoctorName = auditDoctorName

		self.abdominalBodyFatmass = abdominalBodyFatmass
		self.abdominalBodyFatmassAdjust = abdominalBodyFatmassAdjust
		self.trunkSoftleanmassFlag = trunkSoftleanmassFlag
		self.visceralFatArea = visceralFatArea
		self.visceralFatmass = visceralFatmass
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
		self.uploadTime = datetime.now()

	def getdata_en(self):
		data_bodycomposition_en = {}
		data_bodycomposition_en['abdominalBodyFatmass'] = self.abdominalBodyFatmass
		data_bodycomposition_en['abdominalBodyFatmassAdjust'] = self.abdominalBodyFatmassAdjust
		data_bodycomposition_en['trunkSoftleanmassFlag'] = self.trunkSoftleanmassFlag
		data_bodycomposition_en['visceralFatArea'] = self.visceralFatArea
		data_bodycomposition_en['visceralFatmass'] = self.visceralFatmass
		data_bodycomposition_en['weight'] = self.weight
		data_bodycomposition_en['weightAdjust'] = self.weightAdjust
		data_bodycomposition_en['weightHighLimit'] = self.weightHighLimit
		data_bodycomposition_en['weightlowlimit'] = self.weightlowlimit
		data_bodycomposition_en['whr'] = self.whr
		data_bodycomposition_en['abdominalBodyFatmassHighLimit'] = self.abdominalBodyFatmassHighLimit
		data_bodycomposition_en['abdominalBodyFatmassLowLimit'] = self.abdominalBodyFatmassLowLimit
		data_bodycomposition_en['adbominalSoftleanmass'] = self.adbominalSoftleanmass
		data_bodycomposition_en['basicMetabolicrate'] = self.basicMetabolicrate
		data_bodycomposition_en['bmi'] = self.bmi
		data_bodycomposition_en['bmiHighLimit'] = self.bmiHighLimit
		data_bodycomposition_en['bmiLowLimit'] = self.bmiLowLimit
		data_bodycomposition_en['bodyAge'] = self.bodyAge
		data_bodycomposition_en['bodyFatRate'] = self.bodyFatRate
		data_bodycomposition_en['bodyFatHeighLimit'] = self.bodyFatHeighLimit
		data_bodycomposition_en['bodyFatLowLimit'] = self.bodyFatLowLimit
		data_bodycomposition_en['bodyType'] = self.bodyType
		data_bodycomposition_en['extracellularFluid'] = self.extracellularFluid
		data_bodycomposition_en['impedance'] = self.impedance
		data_bodycomposition_en['intracellularFluid'] = self.intracellularFluid
		data_bodycomposition_en['leanBodymass'] = self.leanBodymass
		data_bodycomposition_en['leanBodymassHighLimit'] = self.leanBodymassHighLimit
		data_bodycomposition_en['leanBodymassLowLimit'] = self.leanBodymassLowLimit
		data_bodycomposition_en['leftArmBodyFatmass'] = self.leftArmBodyFatmass
		data_bodycomposition_en['leftArmSoftleanmass'] = self.leftArmSoftleanmass
		data_bodycomposition_en['leftArmsoftleanmassFlag'] = self.leftArmsoftleanmassFlag
		data_bodycomposition_en['leftLegBodyFatmass'] = self.leftLegBodyFatmass
		data_bodycomposition_en['leftLegSoftleanmass'] = self.leftLegSoftleanmass
		data_bodycomposition_en['leftLegSoftleanmassFlag'] = self.leftLegSoftleanmassFlag
		data_bodycomposition_en['massOfBodyFat'] = self.massOfBodyFat
		data_bodycomposition_en['mineral'] = self.mineral
		data_bodycomposition_en['mineralHighLimit'] = self.mineralHighLimit
		data_bodycomposition_en['mineralLowLimit'] = self.mineralLowLimit
		data_bodycomposition_en['obesexaxis'] = self.obesexaxis
		data_bodycomposition_en['protein'] = self.protein
		data_bodycomposition_en['proteinHighLimit'] = self.proteinHighLimit
		data_bodycomposition_en['proteinLowLimit'] = self.proteinLowLimit
		data_bodycomposition_en['rightArmbodyFatmass'] = self.rightArmbodyFatmass
		data_bodycomposition_en['rightArmSoftleanmassFlag'] = self.rightArmSoftleanmassFlag
		data_bodycomposition_en['rightLegBodyFatmass'] = self.rightLegBodyFatmass
		data_bodycomposition_en['rigtArmSoftleanmass'] = self.rigtArmSoftleanmass
		data_bodycomposition_en['rigtLegSoftleanmass'] = self.rigtLegSoftleanmass
		data_bodycomposition_en['softleanmass'] = self.softleanmass
		data_bodycomposition_en['softleanmassAdjust'] = self.softleanmassAdjust
		data_bodycomposition_en['softleanmassHighLimit'] = self.softleanmassHighLimit
		data_bodycomposition_en['softleanmassLowLimit'] = self.softleanmassLowLimit
		data_bodycomposition_en['standardWeight'] = self.standardWeight
		data_bodycomposition_en['subcutaneousFatmass'] = self.subcutaneousFatmass
		data_bodycomposition_en['totalBodyWater'] = self.totalBodyWater
		data_bodycomposition_en['totalBodyWaterHighLimit'] = self.totalBodyWaterHighLimit
		data_bodycomposition_en['totalBodyWaterLowLimit'] = self.totalBodyWaterLowLimit
		data_bodycomposition_en['totalEnergyConsumption'] = self.totalEnergyConsumption
		return data_bodycomposition_en

	def getdata_zh(self):
		data_bodycomposition_en = {}
		data_bodycomposition_en['躯干脂肪量'] = self.abdominalBodyFatmass
		data_bodycomposition_en['体脂肪量调节值'] = self.abdominalBodyFatmassAdjust
		data_bodycomposition_en['躯干肌肉水平'] = self.trunkSoftleanmassFlag
		data_bodycomposition_en['内脏脂肪面积'] = self.visceralFatArea
		data_bodycomposition_en['内脏脂肪质量'] = self.visceralFatmass
		data_bodycomposition_en['体重'] = self.weight
		data_bodycomposition_en['体重调节值'] = self.weightAdjust
		data_bodycomposition_en['体重高值'] = self.weightHighLimit
		data_bodycomposition_en['体重低值'] = self.weightlowlimit
		data_bodycomposition_en['腰臀比'] = self.whr
		data_bodycomposition_en['体脂肪量高值'] = self.abdominalBodyFatmassHighLimit
		data_bodycomposition_en['体脂肪量低值'] = self.abdominalBodyFatmassLowLimit
		data_bodycomposition_en['躯干肌肉量'] = self.adbominalSoftleanmass
		data_bodycomposition_en['基础代谢量'] = self.basicMetabolicrate
		data_bodycomposition_en['身体质量指数'] = self.bmi
		data_bodycomposition_en['身体质量指数高值'] = self.bmiHighLimit
		data_bodycomposition_en['身体质量指数低值'] = self.bmiLowLimit
		data_bodycomposition_en['身体年龄'] = self.bodyAge
		data_bodycomposition_en['体脂肪率'] = self.bodyFatRate
		data_bodycomposition_en['体脂肪率高值'] = self.bodyFatHeighLimit
		data_bodycomposition_en['体脂肪率低值'] = self.bodyFatLowLimit
		data_bodycomposition_en['bodyType'] = self.bodyType
		data_bodycomposition_en['细胞外液'] = self.extracellularFluid
		data_bodycomposition_en['阻抗'] = self.impedance
		data_bodycomposition_en['细胞内液'] = self.intracellularFluid
		data_bodycomposition_en['去脂体重'] = self.leanBodymass
		data_bodycomposition_en['去脂体重高值'] = self.leanBodymassHighLimit
		data_bodycomposition_en['去脂体重低值'] = self.leanBodymassLowLimit
		data_bodycomposition_en['左上肢体脂肪量'] = self.leftArmBodyFatmass
		data_bodycomposition_en['左上肢肌肉量'] = self.leftArmSoftleanmass
		data_bodycomposition_en['左臂肌肉水平'] = self.leftArmsoftleanmassFlag
		data_bodycomposition_en['左下肢体脂肪量'] = self.leftLegBodyFatmass
		data_bodycomposition_en['左下肢肌肉量'] = self.leftLegSoftleanmass
		data_bodycomposition_en['左腿肌肉水平'] = self.leftLegSoftleanmassFlag
		data_bodycomposition_en['体脂肪量'] = self.massOfBodyFat
		data_bodycomposition_en['无机盐'] = self.mineral
		data_bodycomposition_en['无机盐高值'] = self.mineralHighLimit
		data_bodycomposition_en['无机盐低值'] = self.mineralLowLimit
		data_bodycomposition_en['obesexaxis'] = self.obesexaxis
		data_bodycomposition_en['蛋白质'] = self.protein
		data_bodycomposition_en['蛋白质高值'] = self.proteinHighLimit
		data_bodycomposition_en['蛋白质低值'] = self.proteinLowLimit
		data_bodycomposition_en['右上肢体脂肪量'] = self.rightArmbodyFatmass
		data_bodycomposition_en['右臂肌肉水平'] = self.rightArmSoftleanmassFlag
		data_bodycomposition_en['右下肢体脂肪量'] = self.rightLegBodyFatmass
		data_bodycomposition_en['右上肢肌肉量'] = self.rigtArmSoftleanmass
		data_bodycomposition_en['右下肢肌肉量'] = self.rigtLegSoftleanmass
		data_bodycomposition_en['肌肉量'] = self.softleanmass
		data_bodycomposition_en['肌肉量调节值'] = self.softleanmassAdjust
		data_bodycomposition_en['肌肉量高值'] = self.softleanmassHighLimit
		data_bodycomposition_en['肌肉量低值'] = self.softleanmassLowLimit
		data_bodycomposition_en['标准体重'] = self.standardWeight
		data_bodycomposition_en['皮下脂肪量'] = self.subcutaneousFatmass
		data_bodycomposition_en['身体水分'] = self.totalBodyWater
		data_bodycomposition_en['身体水分高值'] = self.totalBodyWaterHighLimit
		data_bodycomposition_en['身体水分低值'] = self.totalBodyWaterLowLimit
		data_bodycomposition_en['总能量消耗'] = self.totalEnergyConsumption
		return data_bodycomposition_en


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
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

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
		self.uploadTime = datetime.now()

	def getdata_en(self):
		data_bonedensity_en = {}
		data_bonedensity_en['acousticveLocity'] = self.acousticveLocity
		data_bonedensity_en['tValue'] = self.tValue
		data_bonedensity_en['zValue'] = self.zValue
		data_bonedensity_en['thScale'] = self.thScale
		data_bonedensity_en['toScale'] = self.toScale
		data_bonedensity_en['zYear'] = self.zYear
		data_bonedensity_en['riskLeavel'] = self.riskLeavel
		data_bonedensity_en['oi'] = self.oi
		data_bonedensity_en['youngAdult'] = self.youngAdult
		data_bonedensity_en['ageMatched'] = self.ageMatched
		data_bonedensity_en['bua'] = self.bua
		data_bonedensity_en['opr'] = self.opr
		return data_bonedensity_en

	def getdata_zh(self):
		data_bonedensity_zh = {}
		data_bonedensity_zh['声速'] = self.acousticveLocity
		data_bonedensity_zh['T值'] = self.tValue
		data_bonedensity_zh['Z值'] = self.zValue
		data_bonedensity_zh['测值/峰值比'] = self.thScale
		data_bonedensity_zh['测值/均值比'] = self.toScale
		data_bonedensity_zh['Z值相对年龄'] = self.zYear
		data_bonedensity_zh['相对骨折风险'] = self.riskLeavel
		data_bonedensity_zh['骨质疏松指数'] = self.oi
		data_bonedensity_zh['成人对比【%】'] = self.youngAdult
		data_bonedensity_zh['同龄对比【%】'] = self.ageMatched
		data_bonedensity_zh['宽波段超声衰减值'] = self.bua
		data_bonedensity_zh['多次测量误差'] = self.opr
		return data_bonedensity_zh

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
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

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
		self.uploadTime = datetime.now()
	def getdata_en(self):
		data_bwh_en = {}
		data_bwh_en['hip'] = self.hip
		data_bwh_en['bust'] = self.bust
		data_bwh_en['waist'] = self.waist
		return data_bwh_en

	def getdata_zh(self):
		data_bwh_zh = {}
		data_bwh_zh['胸围'] = self.hip
		data_bwh_zh['臀围'] = self.bust
		data_bwh_zh['胸围'] = self.waist
		return data_bwh_zh

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
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

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
		self.uploadTime = datetime.now()
	def getdata_en(self):
		data_ecg_en = {}
		data_ecg_en['HR'] = self.HR
		data_ecg_en['PR'] = self.PR
		data_ecg_en['P_Duration'] = self.P_Duration
		data_ecg_en['T_Duration'] = self.T_Duration
		data_ecg_en['QT_Duration'] = self.QT_Duration
		data_ecg_en['QTc_Duration'] = self.QTc_Duration
		data_ecg_en['P_Axis'] = self.P_Axis
		data_ecg_en['R_V5'] = self.R_V5
		data_ecg_en['S_V1'] = self.S_V1
		return data_ecg_en

	def getdata_zh(self):
		data_ecg_zh = {}
		data_ecg_zh['心率'] = self.HR
		data_ecg_zh['PR间期'] = self.PR
		data_ecg_zh['P时限'] = self.P_Duration
		data_ecg_zh['T时限'] = self.T_Duration
		data_ecg_zh['QT时限'] = self.QT_Duration
		data_ecg_zh['QTc时限'] = self.QTc_Duration
		data_ecg_zh['P电轴'] = self.P_Axis
		data_ecg_zh['R_V5'] = self.R_V5
		data_ecg_zh['S_V1'] = self.S_V1
		return data_ecg_zh

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
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

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
		self.uploadTime = datetime.now()
	def getdata_en(self):
		data_heighweight_en = {}
		data_heighweight_en['heigh'] = self.heigh
		data_heighweight_en['weight'] = self.weight
		data_heighweight_en['bmi'] = self.bmi
		return data_heighweight_en

	def getdata_zh(self):
		data_heighweight_zh = {}
		data_heighweight_zh['身高'] = self.heigh
		data_heighweight_zh['体重'] = self.weight
		data_heighweight_zh['BMI(体重/身高^2)'] = self.bmi
		return data_heighweight_zh

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
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

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
		self.uploadTime = datetime.now()
	def getdata_en(self):
		data_electronicvision_en = {}
		data_electronicvision_en['checkType'] = self.checkType
		data_electronicvision_en['leftEye'] = self.leftEye
		data_electronicvision_en['rightEye'] = self.rightEye
		return data_electronicvision_en

	def getdata_zh(self):
		data_electronicvision_zh = {}
		data_electronicvision_zh['检查类型'] = self.checkType
		data_electronicvision_zh['左眼'] = self.leftEye
		data_electronicvision_zh['右眼'] = self.rightEye
		return data_electronicvision_zh

class tb_lung(db.Model, dict):
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
	BSA = db.Column(db.String(255))
	MVV_BSA = db.Column(db.String(255))
	VC = db.Column(db.String(255))
	TV = db.Column(db.String(255))
	IRV = db.Column(db.String(255))
	ERV = db.Column(db.String(255))
	IC = db.Column(db.String(255))
	MV = db.Column(db.String(255))
	RR = db.Column(db.String(255))
	Result = db.Column(db.String(255))
	conclusion = db.Column(db.String(512))
	uploadTime = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, familyCode, familyName, orgCode, orgName, dataSource, mechineID, examDate, IDCARD, residentEMPI, residentName,
				auditDoctorEMPI, auditDoctorName, FVC, FEV1, FEV2, FEV1Percent, FEV2Percent, FEV3Percent, MMF,
				MVV1, BSA1, M_B1, PEF, V75, V50, V25, V50_V25, V25_H, MVV, BSA, MVV_BSA, VC, TV, IRV, ERV, IC,
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
		self.BSA = BSA
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
		self.uploadTime = datetime.now()

	def getdata_en(self):
		data_lung_en = {}
		data_lung_en['FVC'] = self.FVC
		data_lung_en['FEV1'] = self.FEV1
		data_lung_en['FEV2'] = self.FEV2
		data_lung_en['FEV1Percent'] = self.FEV1Percent
		data_lung_en['FEV2Percent'] = self.FEV2Percent
		data_lung_en['FEV3Percent'] = self.FEV3Percent
		data_lung_en['MMF'] = self.MMF
		data_lung_en['MVV1'] = self.MVV1
		data_lung_en['BSA1'] = self.BSA1
		data_lung_en['M_B1'] = self.M_B1
		data_lung_en['PEF'] = self.PEF
		data_lung_en['V75'] = self.V75
		data_lung_en['V50'] = self.V50
		data_lung_en['V25'] = self.V25
		data_lung_en['V50_V25'] = self.V50_V25
		data_lung_en['V25_H'] = self.V25_H
		data_lung_en['MVV'] = self.MVV
		data_lung_en['BSA'] = self.BSA
		data_lung_en['MVV_BSA'] = self.MVV_BSA
		data_lung_en['VC'] = self.VC
		data_lung_en['TV'] = self.TV
		data_lung_en['IRV'] = self.IRV
		data_lung_en['ERV'] = self.ERV
		data_lung_en['IC'] = self.IC
		data_lung_en['MV'] = self.MV
		data_lung_en['RR'] = self.RR
		data_lung_en['Result'] = self.Result
		return data_lung_en

	def getdata_zh(self):
		data_lung_zh = {}
		data_lung_zh['用力肺活量'] = self.FVC
		data_lung_zh['1秒钟肺活量'] = self.FEV1
		data_lung_zh['2秒钟肺活量'] = self.FEV2
		data_lung_zh['1秒率(FEV1%)'] = self.FEV1Percent
		data_lung_zh['2秒率(FEV2%)'] = self.FEV2Percent
		data_lung_zh['3秒率(FEV3%)'] = self.FEV3Percent
		data_lung_zh['最大呼气中段流速(MMF)'] = self.MMF
		data_lung_zh['最大通气量/1秒量(MVV1)'] = self.MVV1
		data_lung_zh['BSA1(BSA1)'] = self.BSA1
		data_lung_zh['M_B1'] = self.M_B1
		data_lung_zh['峰值流量(PEF)'] = self.PEF
		data_lung_zh['呼气至75%肺活量时对应流速值(V75)'] = self.V75
		data_lung_zh['呼气至50%肺活量时对应流速值(V50)'] = self.V50
		data_lung_zh['呼气至25%肺活量时对应流速值(V25)'] = self.V25
		data_lung_zh['呼气至50%25%肺活量时对应流速值(V50/V25)'] = self.V50_V25
		data_lung_zh['V25与身高之比(V25/H)'] = self.V25_H
		data_lung_zh['实测最大通气量(MVV)'] = self.MVV
		data_lung_zh['体表面积(BSA)'] = self.BSA
		data_lung_zh['实测最大通气量与体表面积之比(MVV/BSA)'] = self.MVV_BSA
		data_lung_zh['实测肺活量(VC)'] = self.VC
		data_lung_zh['潮气量(TV)'] = self.TV
		data_lung_zh['补吸气量(IRV)'] = self.IRV
		data_lung_zh['补呼气量(ERV)'] = self.ERV
		data_lung_zh['深呼气量(IC)'] = self.IC
		data_lung_zh['静息通气量(MV)'] = self.MV
		data_lung_zh['呼吸频率(RR)'] = self.RR
		data_lung_zh['结果(Result)'] = self.Result
		return data_lung_zh

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
