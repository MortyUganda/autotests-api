import httpx 

data = {
  "email": "user1@example.com",
  "password": "string"
}

login_response   = httpx.post('http://localhost:8000/api/v1/authentication/login', json=data)
login_response_data = login_response.json()

print(login_response.status_code)
print(login_response.json())


authorization_token = {
    "Authorization": f'Bearer {login_response_data["token"]["accessToken"]}'
}

# Выполняем запрос
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=authorization_token)
user_response_data = user_response.json()

# Выводим токены
print(user_response.status_code)
print(user_response_data)



