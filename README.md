# flexioncodechallenge

## Overview
This application was built for the Flexion Coding Challenge. It does the following:
- Converts temperatures between Kelvin, Celsius, Fahrenheit and Rankine
- Converts volumes between liters, tablespoons, cubic-inches, cups, cubic-feet, and gallons
- The system indicates that the response is correct, incorrect, or invalid. 
- The student’s response must match an authoritative answer after both the student’s response 
    and authoritative answer are rounded to the tenths place. 
    
   
## Technologies Used
- Python(Django) for the backend
- Javascript(Vue) for the frontend
- AWS Elastic Container Service for deployment
- AWS Codepipeline for the CI/CD

## How to install

### Requirements

- python3
- node
- yarn

### Before install
- Clone the project using `git clone https://github.com/comiyale/flexioncodechallenge`
### To run the backend
- On the root folder of the project cd into api folder.
- Run `pip install requirements.txt`
- Run `python manage.py runserver`
### To run the frontend
- On the root folder of the project cd into app folder.
- yarn install
- yarn serve

### Future Improvement

- Build a more robust system to handle other unit types apart from volume and temperature.
- Improve on the UI to make it more elegant and colorful.
