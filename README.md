## Installation
Make sure you have Python >= 3.8 installed before following these steps.

1 - Clone the project:
`git clone https://github.com/shywn-mrk/client-panel-api.git`

2 - Create a virtual environment:
`python -m venv env`

3 - Activate the virtual environment:
- Windows:
`env/Scripts/activate`
- Mac/Linux:
`source env/bin/activate`

4 - Install the required packages:
`pip install -r requirements.txt`

5 - Creating migrations and migrate:
```
python manage.py makemigrations
python manage.py migrate
```
6 - Create a super user:
`python manage.py createsuperuser`

7 - Run the server:
`python manage.py runserver`
