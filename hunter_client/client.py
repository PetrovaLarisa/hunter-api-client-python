"""
Working with Hunter API.

Implementing client for domain searcher, email finder, email verifier and CRUD operations
"""

import requests
from services.email_validator import validate_email


class HunterClient(object):
    """Client for interacting with the Hunter API."""

    def __init__(self, api_k: str):
        """Initialize the client with API key."""
        self.api_k: str = api_k
        self.base_url: str = 'https://api.hunter.io/v2'
        self.res: list[dict] = []

    def get_email_finder(self, domain: str, first_name: str, last_name: str) -> str:
        """Find an email address by domain and person's name using Hunter API."""
        url = ''.join([self.base_url, '/email-finder'])
        context = {'domain': domain, 'api_key': self.api_k, 'first_name': first_name, 'last_name': last_name}
        response = requests.get(url, params=context, timeout=10)
        return response.json()['data']['email']

    def get_email_verifier(self, email: str) -> dict:
        """Verify an email address using Hunter API."""
        if not validate_email(email):
            raise ValueError('Invalid email')
        url = ''.join([self.base_url, '/email-verifier'])
        context = {'email': email, 'api_key': self.api_k}
        response = requests.get(url, json=context, timeout=10)
        res_data = response.json()['data']
        res = {'email': res_data['email'], 'status': res_data['status']}
        self.add_result(res)
        return response.json()['data']

    def add_result(self, email: dict) -> bool:
        """Add a result to local storage."""
        self.res.append(email)
        return True

    def get_results(self) -> list[dict]:
        """Retrieve all results."""
        return self.res

    def update_result(self, index: int, new_result: dict) -> None:
        """Update result by its index."""
        self.res[index] = new_result

    def delete_result(self, index: int) -> None:
        """Delete result by its index."""
        self.res.pop(index)

# Usage:


api_key = 'YOUR_API_KEY'
client = HunterClient(api_key)

# Email finder
emails = client.get_email_finder('paypal.com', 'elon', 'mask')

# Email verification
email_verif_result = client.get_email_verifier('hamkhan@tesla.com')

client.add_result({'email': 'test@example.com', 'status': 'valid'})

client.update_result(0, {'email': 'hamkhan@tesla.com', 'status': 'invalid'})

client.delete_result(0)
