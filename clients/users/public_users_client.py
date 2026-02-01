from typing import TypedDict
import httpx
from clients.api_client import APIClient


class CreateRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateRequestDict) -> httpx.Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email, password, lastName, firstName и middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)