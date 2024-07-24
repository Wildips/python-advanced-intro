import json

import allure
import pytest
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


@step
def test_user_creation(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Создание пользователя")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users"
    test_schema = load_schema("users_endpoint/create.json")
    body = json.loads('{"name": "morpheus1", "job": "leader_new"}')

    # ACTIONS (WHEN)
    response = requests.post(test_url, data=body)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus1"
    assert response.json()["job"] == "leader_new"
    jsonschema.validate(instance=response.json(), schema=test_schema)


@step
def test_user_creation_with_name_only(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Создание пользователя с одни параметром")
    # ARRANGE (GIVEN)
    test_url = f"{get_base_api_url}users"
    test_schema = load_schema("users_endpoint/create_with_name_only.json")
    body = json.loads('{"name": "morpheus1"}')

    # ACTIONS (WHEN)
    response = requests.post(test_url, data=body)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus1"
    jsonschema.validate(instance=response.json(), schema=test_schema)


@step
def test_get_users_list_for_page(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Получение списка пользователей")
    # ARRANGE (GIVEN)
    page_number = 1
    test_url = f"{get_base_api_url}users/?page={page_number}"
    test_schema = load_schema("users_endpoint/list_users.json")

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    assert response.json()["page"] == page_number
    jsonschema.validate(instance=response.json(), schema=test_schema)


@step
def test_get_users_list_with_miss_print_url_return_first_page(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Возврат первой страницы при ошибке в параметре")
    # ARRANGE (GIVEN)
    page_id = 2
    test_url = f"{get_base_api_url}users/?pe={page_id}"
    test_schema = load_schema("users_endpoint/list_users.json")

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    assert response.json()["page"] == 1
    jsonschema.validate(instance=response.json(), schema=test_schema)


def test_get_users_list_with_non_existence_page(get_base_api_url):
    allure.dynamic.tag("api")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Тесты ручки users")

    allure.dynamic.story("Возврат пустой страницы при большом значении параметра")
    # ARRANGE (GIVEN)
    page_id = 9999999
    test_url = f"{get_base_api_url}users/?page={page_id}"
    test_schema = load_schema("users_endpoint/huge_list_users.json")

    # ACTIONS (WHEN)
    response = requests.get(test_url)
    response_logging(response)
    response_attaching(response)

    # ASSERT (THEN)
    assert response.status_code == 200
    assert response.json()["page"] == page_id
    jsonschema.validate(instance=response.json(), schema=test_schema)
