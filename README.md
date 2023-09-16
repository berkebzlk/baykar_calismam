# baykar_calismam

1- create virtual environment
    for windows:
        py -m venv venv

2- activate virtual environment
    for windows:
        venv\Scripts\activate

3- download required packages
    pip install -r requirements.txt

4- run the project
    for windows:
        py manage.py runserver

######### SUPER USER #########
username: admin
password: admin

######### ENDPOINTS #########

http://127.0.0.1:8000/dashboard/
    IHA crud operations

http://127.0.0.1:8000/accounts/register/
    register user

http://127.0.0.1:8000/accounts/login/
    login user
