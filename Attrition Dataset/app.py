from flask import Flask, render_template, request
import pickle
import numpy as np

#load our RandomForestClassifier model
filename = 'emp-attrition-rf-classifier.pkl'
classifier = pickle.load(open(filename,'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    temp_array = list()

    if request.method == 'POST':

        Age = int(request.form['Age'])
        DistanceFromHome = int(request.form['DistanceFromHome'])
        Education = int(request.form['Education'])
        EnvironmentSatisfaction = int(request.form['EnvironmentSatisfaction'])
        JobInvolvement = int(request.form['JobInvolvement'])
        JobLevel = int(request.form['JobLevel'])
        JobSatisfaction = int(request.form['JobSatisfaction'])
        MonthlyIncome = int(request.form['MonthlyIncome'])
        NumCompaniesWorked = int(request.form['NumCompaniesWorked'])
        PercentSalaryHike = int(request.form['PercentSalaryHike'])
        PerformanceRating = int(request.form['PerformanceRating'])
        RelationshipSatisfaction = int(request.form['RelationshipSatisfaction'])
        TotalWorkingYears = int(request.form['TotalWorkingYears'])
        TrainingTimesLastYear = int(request.form['TrainingTimesLastYear'])
        WorkLifeBalance = int(request.form['WorkLifeBalance'])
        YearsAtCompany = int(request.form['YearsAtCompany'])
        YearsInCurrentRole = int(request.form['YearsInCurrentRole'])
        YearsSinceLastPromotion = int(request.form['YearsSinceLastPromotion'])
        YearsWithCurrManager = int(request.form['YearsWithCurrManager'])

        temp_array = [Age, DistanceFromHome, Education, EnvironmentSatisfaction, JobInvolvement, JobLevel,
                      JobSatisfaction, MonthlyIncome, NumCompaniesWorked, PercentSalaryHike, PerformanceRating,
                      RelationshipSatisfaction, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance,
                      YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager]

        BusinessTravel = request.form['BusinessTravel']
        if BusinessTravel == 'Non-Travel':
            temp_array = temp_array + [1, 0, 0]
        elif BusinessTravel == 'Travel_Frequently':
            temp_array = temp_array + [0, 1, 0]
        elif BusinessTravel == 'Travel_Rarely':
            temp_array = temp_array + [0, 0, 1]

        Department = request.form['Department']
        if Department == 'Human Resources':
            temp_array = temp_array + [1, 0, 0]
        elif Department == 'Research & Development':
            temp_array = temp_array + [0, 1, 0]
        elif Department == 'Sales':
            temp_array = temp_array + [0, 0, 1]

        EducationField = request.form['EducationField']
        if EducationField == 'Human Resources':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0]
        elif EducationField == 'Life Sciences':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0]
        elif EducationField == 'Marketing':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0]
        elif EducationField == 'Medical':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0]
        elif EducationField == 'Other':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0]
        elif EducationField == 'Technical Degree':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1]

        Gender = request.form['Gender']
        if Gender == 'Female':
            temp_array = temp_array + [1, 0]
        elif Gender == 'Male':
            temp_array = temp_array + [0, 1]

        JobRole = request.form['JobRole']
        if JobRole == 'Healthcare Representative':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif JobRole == 'Human Resources':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif JobRole == 'Laboratory Technician':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif JobRole == 'Manager':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif JobRole == 'Manufacturing Director':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif JobRole == 'Research Director':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif JobRole == 'Research Scientist':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif JobRole == 'Sales Executive':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif JobRole == 'Sales Representative':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 1]

        MaritalStatus = request.form['MaritalStatus']
        if MaritalStatus == 'Divorced':
            temp_array = temp_array + [1, 0, 0]
        elif MaritalStatus == 'Married':
            temp_array = temp_array + [0, 1, 0]
        elif MaritalStatus == 'Single':
            temp_array = temp_array + [0, 0, 1]

        OverTime = request.form['OverTime']
        if OverTime == 'No':
            temp_array = temp_array + [1, 0]
        elif OverTime == 'Yes':
            temp_array = temp_array + [0, 1]

        data = np.array([temp_array])
        my_classification = int(classifier.predict(data)[0])

        return render_template('result.html',classification=my_classification)

if __name__ == '__main__':
    app.run(debug=True)