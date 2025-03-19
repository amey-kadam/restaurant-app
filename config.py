# config.py
import os

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key_for_development')

# For SQLite (simpler to start with)
SQLALCHEMY_DATABASE_URI = 'sqlite:///restaurant.db'

# If you want to use PostgreSQL later, you would use:
# SQLALCHEMY_DATABASE_URI = 'postgresql://real_username:real_password@localhost/restaurant.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False 

RAZORPAY_KEY_ID = 'rzp_test_MmHUhQCfHVSudO'  
RAZORPAY_KEY_SECRET = 'RKGFj6VX47Skmca6vAuOAhse'    