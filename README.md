# flexioncodechallenge

## Overview
This application was built for the Flexion Coding Challenge. It does the following:
- Converts temperatures between Kelvin, Celsius, Fahrenheit and Rankine
- Converts volumes between liters, tablespoons, cubic-inches, cups, cubic-feet, and gallons
- The system indicates that the response is correct, incorrect, or invalid. 
- The student’s response must match an authoritative answer after both the student’s response 
    and authoritative answer are rounded to the tenths place.

A Python package Pint was used for the conversion, more information here https://pint.readthedocs.io/en/stable/
    
## URL 
http://unit-converter-791446476.us-east-1.elb.amazonaws.com/
   
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
- Run `export DJANGO_SECRET_KEY="<Your Secret Value>"
- Run `python manage.py runserver`
### To run the frontend
- On the root folder of the project cd into app folder.
- yarn install
- yarn serve

### Future Improvement

- Include a test stage to the CI/CD process.
- Build a system that makes it easy to add, update and delete new units and unit types
- Scan the image for security vulnerabilities before pushing them to Elastic Container Registry
- Include auto scaling features for when there is high traffick, 
