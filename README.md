# hunter-api-client-python

A simple Python client for the Hunter.io API

Installation

pip install hunter-client

Usage

Insert your API key in line:
api_key = 'YOUR_API_KEY'

# Initialize the client
client = HunterClient('YOUR_API_KEY')

# Verify an email
email_verif_result = client.get_email_verifier('test@example.com')

# Search for emails
emails = client.get_email_finder('example.com', 'John','Doe')

# Get results
results = client.get_results()

# API Reference HunterClient

get_email_verifier - Verify if an email address valid

get_email_finder - Find email addresses for a domain and person's name

# CRUD operations

add_result - Add an email address to a local storage

get_results - Retrieve list of email addresses from the local storage

update_result - Update some record in the list of email addresses

delete_result - Delete some record



# Contact
LarysaPetrova - @PetrovaLarisa - mamapanama1984@example.com
