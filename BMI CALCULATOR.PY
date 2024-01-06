while True:

    height = float(input('Enter your height cm: \n'))
    height = height / 100
    weight = float(input('Enter your weight kg: \n'))

    BMI = round (weight /(height * height),2)
    print(f'Your body mass index (BMI) is {BMI}')
    if(BMI<=18.5):
        print('You are underweight')
    elif(BMI<=24.9):
        print('you are overweight')
    else:
        print('You are obese') 
    userWantsToContinue = input('Do you want to continue? (yes/no):\n')
    if(userWantsToContinue == 'no'):
        print('Over')
        break   


