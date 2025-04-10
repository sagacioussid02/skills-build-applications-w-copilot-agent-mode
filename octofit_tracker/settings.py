# Database configuration for djongo
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',  # Replace with your MongoDB database name
        'ENFORCE_SCHEMA': True,  # Optional: Enforce schema validation
        'CLIENT': {
            'host': 'localhost',  # Replace with your MongoDB host
            'port': 27017,        # Replace with your MongoDB port
            'username': '',       # Optional: Add your MongoDB username
            'password': '',       # Optional: Add your MongoDB password
            'authSource': 'admin', # Optional: Authentication database
        }
    }
}