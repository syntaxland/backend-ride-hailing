# Ride Hailing Dynamic Pricing API

## Setup Instructions
1. Clone the repository  
git clone https://github.com/syntaxland/backend-ride-hailing.git cd backend-ride-hailing

2. Create a virtual environment and install dependencies  
python -m venv venv 
source venv/bin/activate (Linux/Mac) 
venv\Scripts\activate (Windows) 
pip install -r requirements.txt

3. Run migrations  
python manage.py migrate

4. Start the server  
python manage.py runserver

5. Access API at  
http://127.0.0.1:8000/api/calculate-fare/?distance=10&traffic_level=high&demand_level=peak

6. Swagger Documentation  
http://127.0.0.1:8000/swagger/

7. Testing 

python manage.py test pricing 

<!-- 
To run this app:
In the root project directory run:

### `py -m venv venv` or `python -m venv venv`

To create the virtual env.

### `venv\Scripts\activate.bat` 

To activate the virtual env.

### `pip install -r requirements.txt` 

To install packages (including: Django, djangorestframework,djangorestframework-simplejwt, django-cors-headers, drf-yasg, etc.,) in the virtual env.

### `python manage.py migrate` 
 
To create the the db.

### `python manage.py runserver` 
 
To start the django server at default port 8000.


### Testing 

### `python manage.py test pricing` 

To test the test cases. -->
