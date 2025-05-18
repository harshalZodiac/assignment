import requests

def get_user_data():
    url = "https://reqres.in/api/users"
    # payload = {}
    headers = {
      'x-api-key': 'reqres-free-v1'
    }
    response = requests.request("GET", url, headers=headers)
    return response

def create_new_user(payload):
    url = "https://reqres.in/api/users"
    headers = {
      'x-api-key': 'reqres-free-v1'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def update_user_data(payload, user_id):
    url = f"https://reqres.in/api/users/{user_id}"
    headers = {
      'x-api-key': 'reqres-free-v1'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response
