import json

import httpx
from jsonschema import validate
from Core.Contracts import USER_DATA_SCHEMA_CREATE_PERSON
import datetime
from Core.Contracts import USER_DATA_SCHEMA_UPDATE_PERSON
from Core.Contracts import REGISTRATION_DATA_SCHEMA
from Core.Contracts import LOGIN_DATA_SCHEMA
import pytest
def test_create_user():
    new_user = {
        "name": "morpheus",
        "job": "leader"
    }

    headers = {'Content-Type': 'application/json'}

    response = httpx.post("https://reqres.in/api/users", json = new_user, headers = headers)

    assert response.status_code == 201
    user = response.json()
    validate(user,USER_DATA_SCHEMA_CREATE_PERSON)
    assert new_user["name"] == user["name"]
    assert new_user["job"] == user ["job"]
    assert len(user["id"]) != 0
    response_date = user["createdAt"].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    assert response_date[0:16] == current_date[0:16]

def test_update_put_user():
    update_user = {
        "name": "morpheus",
        "job": "zion resident"
    }

    headers = {'Content-Type': 'application/json'}

    response = httpx.put("https://reqres.in/api/users/2", json = update_user, headers = headers)
    assert response.status_code == 200
    user = response.json()
    validate(user,USER_DATA_SCHEMA_UPDATE_PERSON)
    assert update_user["name"] == user["name"]
    assert update_user["job"] == user["job"]
    response_date = user["updatedAt"].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    assert response_date[0:16] == current_date[0:16]

def test_update_patch_user():
    update_user = {
        "name": "morpheus",
        "job": "zion resident"
    }

    headers = {'Content-Type': 'application/json'}

    response = httpx.patch("https://reqres.in/api/users/2", json = update_user, headers = headers)
    assert response.status_code == 200
    user = response.json()
    validate(user,USER_DATA_SCHEMA_UPDATE_PERSON)
    assert update_user["name"] == user["name"]
    assert update_user["job"] == user["job"]
    response_date = user["updatedAt"].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    assert response_date[0:16] == current_date[0:16]

def test_delete_user():
    headers = {'Content-Type': 'application/json'}
    response = httpx.delete("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 204
    
users_credentials = [{"name": "Roman", "job": "tester"}, {"name": "Anton", "job": "developer"}, {"name": "Ivan", "job": "project"}]

@pytest.mark.parametrize("users_credentials", users_credentials)
def test_create_user_parametrize(users_credentials):

    headers = {'Content-Type': 'application/json'}

    response = httpx.post("https://reqres.in/api/users", json = users_credentials, headers = headers)

    assert response.status_code == 201
    user = response.json()
    validate(user,USER_DATA_SCHEMA_CREATE_PERSON)
    assert users_credentials["name"] == user["name"]
    assert users_credentials["job"] == user ["job"]
    assert len(user["id"]) != 0
    response_date = user["createdAt"].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    assert response_date[0:16] == current_date[0:16]


# json_file_reader = open("Users_credentails.json")
# users_credentials = json.load(json_file_reader)
# @pytest.mark.parametrize("users_credentials", users_credentials)
# def test_create_user_parametrize_from_file(users_credentials):
#
#     headers = {'Content-Type': 'application/json'}
#
#     response = httpx.post("https://reqres.in/api/users", json = users_credentials, headers = headers)
#
#     assert response.status_code == 201
#     user = response.json()
#     validate(user,USER_DATA_SCHEMA_CREATE_PERSON)
#     assert users_credentials["name"] == user["name"]
#     assert users_credentials["job"] == user ["job"]
#     assert len(user["id"]) != 0
#     response_date = user["createdAt"].replace('T', ' ')
#     current_date = str(datetime.datetime.utcnow())
#     assert response_date[0:16] == current_date[0:16]


def test_register_successful():
    register_body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    response = httpx.post("https://reqres.in/api/register", json = register_body, headers = headers)
    assert response.status_code == 200
    register = response.json()
    validate(register, REGISTRATION_DATA_SCHEMA)
    id = 4
    token = "QpwL5tke4Pnpja7X4"
    assert id == register["id"]
    assert token == register["token"]

def test_register_unsuccessful():
    register_body = {
        "email": "sydney@fife"
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post("https://reqres.in/api/register", json = register_body, headers = headers)
    assert response.status_code == 400
    print(response.json())
    assert "Missing password" == response.json()["error"]

def test_login_successful():
    login_body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post("https://reqres.in/api/login", json=login_body, headers=headers)
    assert response.status_code == 200
    login = response.json()
    validate(login, LOGIN_DATA_SCHEMA)
    print(response.json())
    token = "QpwL5tke4Pnpja7X4"
    assert token == response.json()["token"]

def test_login_unsuccessful():
    login_body = {
        "email": "peter@klaven"
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post("https://reqres.in/api/login", json = login_body, headers = headers)
    assert response.status_code == 400
    assert "Missing password" == response.json()["error"]

















