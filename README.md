# Ride Hailing Dynamic Pricing API

## Setup Instructions

1. Clone the repository  

```bash 
git clone https://github.com/syntaxland/backend-ride-hailing.git` 
```
and cd backend-ride-hailing

2. Create a virtual environment and install dependencies     
```bash 
python -m venv venv
```
```bash 
source venv/bin/activate
``` 
(Linux/Mac)

```bash 
venv\Scripts\activate 
``` 
(Windows) 

```bash 
pip install -r requirements.txt
```

3. Run migrations  

```bash 
python manage.py migrate
```

4. Start the server  

```bash 
python manage.py runserver
```

5. Access API at  

```bash 
http://127.0.0.1:8000/api/calculate-fare/?distance=10&traffic_level=high&demand_level=peak
```

6. Swagger Documentation  
```bash 
http://127.0.0.1:8000/swagger/
```

7. Testing 

```bash 
python manage.py test pricing
```