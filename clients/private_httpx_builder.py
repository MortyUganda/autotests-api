from httpx import Client
from clients.authentication.authentication_client import LoginRequestDict, get_authentication_client


def get_private_http_client() -> Client:
    authentication_client = get_authentication_client()

    login_request = LoginRequestDict(email="", password="")
    login_response = authentication_client.login(request=login_request)


    return Client(timeout=100, base_url="http://localhost:8000", headers={"Authorization": f"Bearer: {login_response}['token']['accessToken]"})