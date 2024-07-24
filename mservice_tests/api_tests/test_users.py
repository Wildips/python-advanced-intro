import allure
import requests
import jsonschema as jsonschema
from allure_commons.types import Severity

from mservice_tests.utils.allure_attach import response_logging, response_attaching
from mservice_tests.utils.log_extending import step
from mservice_tests.utils.resource import load_schema

USER_ID = 2


@step
def test_get_user_by_id(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Получение данных пользователя по id")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/{USER_ID}"
    test_schema = load_schema("users_endpoint/single_user.json")

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=test_schema)


@step
def test_get_user_by_id_with_not_exists_user_id_in_url(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Получение данных по id не существующего пользователя")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/99999"

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


@step
def test_get_user_by_id_with_incorrect_id_value_in_url(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Получение данных при не корректном id")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users/unknown_id"

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 422
    assert response.json()["detail"][0][
               "msg"] == "Input should be a valid integer, unable to parse string as an integer"
