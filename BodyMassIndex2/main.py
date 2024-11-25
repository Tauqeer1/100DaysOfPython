height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = round(weight / height**2)
bmi_report = ''

if bmi < 18.5:
    bmi_report = 'slightly underweight'
elif bmi < 25:
    bmi_report = 'normal weight'
elif bmi < 30:
    bmi_report = 'slightly overweight'
elif bmi < 35:
    bmi_report = 'obese'
else:
    bmi_report = 'clinically obese'
        

print(f'Your BMI is {bmi}, you are {bmi_report}')