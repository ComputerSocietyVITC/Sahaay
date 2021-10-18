import os

"""
Add SMTP files here and other related config files here

"""
# The SMTP configuration for mailtrap, during development
dev_smtp_config = {
    "port": 2525,
    "smtp_server": "smtp.mailtrap.io",
    "user": os.environ.get("MAILTRAP_USER"),
    "password": os.environ.get("MAILTRAP_PASSWORD"),
    "email_address": "sahaay@sahaay.sahaay",
}

prod_smtp_config = {
    
}