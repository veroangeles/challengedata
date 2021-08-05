import requests 
import json

data={"Age":37, "BusinessTravel":"Travel_Frequently", "DailyRate":29, "Department":"Research & Development", "DistanceFromHome":12, "Education":3, "EducationField":"Life Sciences", "EmployeeNumber":23333999, "EnvironmentSatisfaction":13, "Gender":"Male", "HourlyRate":61, "JobInvolvement":2, "JobRole":"Research Scientist", "JobSatisfaction":2, "MaritalStatus":"Married", "MonthlyIncome":5130,  "MonthlyRate":24907, "NumCompaniesWorked":1, "OverTime":"No", "PercentSalaryHike":23, "PerformanceRating":4, "RelationshipSatisfaction":4, "StockOptionLevel":1, "TrainingTimesLastYear":3,  "WorkLifeBalance":3, "YearsAtCompany":10, "YearsInCurrentRole":1, "YearsSinceLastPromotion":1, "YearsWithCurrManager":1}
#data_json=json.dumps(data)
#import json
url = 'http://0.0.0.0:4000/'
payload = {"Age":37, "BusinessTravel":"Travel_Frequently", "DailyRate":29, "Department":"Research & Development", "DistanceFromHome":12, "Education":3, "EducationField":"Life Sciences", "EmployeeNumber":23333999, "EnvironmentSatisfaction":13, "Gender":"Male", "HourlyRate":61, "JobInvolvement":2, "JobRole":"Research Scientist", "JobSatisfaction":2, "MaritalStatus":"Married", "MonthlyIncome":5130,  "MonthlyRate":24907, "NumCompaniesWorked":1, "OverTime":"No", "PercentSalaryHike":23, "PerformanceRating":4, "RelationshipSatisfaction":4, "StockOptionLevel":1, "TrainingTimesLastYear":3,  "WorkLifeBalance":3, "YearsAtCompany":10, "YearsInCurrentRole":1, "YearsSinceLastPromotion":1, "YearsWithCurrManager":1}
#{'some': 'data'}
headers = {'content-type': 'application/json'}
respond=requests.get(url)
respond.text
respond2=requests.post('http://0.0.0.0:4000/evaluate', data=json.dumps(payload), headers=headers)
#print(respond2.text)