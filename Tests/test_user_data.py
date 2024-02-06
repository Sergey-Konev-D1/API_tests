import httpx
from jsonschema import validate
from Core.Contracts import USER_DATA_SCHEMA
from Core.Contracts import LIST_RESOURSE_DATA_SCHEMA
from Core.Contracts import LIST_RESOURSE_DATA_SCHEMA_BLOCK_SUPPORT
def test_get_user_list():
    response = httpx.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    for user in response.json()["data"]:
        validate(user,USER_DATA_SCHEMA)
        email = user["email"]
        assert email.endswith("reqres.in")
        #id = str(user["id"])
        #avatar = user["avatar"]
        #assert id in avatar
        id = str(user["id"])
        avatar_template = f"https://reqres.in/img/faces/{id}-image.jpg"
        avatar = user["avatar"]
        assert avatar_template == avatar

def test_get_single_user():
    response = httpx.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    user = response.json()["data"]
    validate(user,USER_DATA_SCHEMA)
    email = user["email"]
    assert email.endswith("reqres.in")
    id = str(user["id"])
    avatar_template = f"https://reqres.in/img/faces/{id}-image.jpg"
    avatar = user["avatar"]
    assert avatar_template == avatar

def test_get_single_user_note_found():
    response = httpx.get("https://reqres.in/api/users/23")
    assert response.status_code == 404
    responce_size = response.json()
    assert len(responce_size) == 0

def test_get_list_resourse():
    response = httpx.get("https://reqres.in/api/unknown")
    assert response.status_code == 200
    for user in response.json()["data"]:
        validate(user,LIST_RESOURSE_DATA_SCHEMA)
        delta_id = 2000 + (user["id"]-1)
        year = user["year"]
        assert delta_id == year

def test_get_single_resourse():
    response = httpx.get("https://reqres.in/api/unknown/2")
    assert response.status_code == 200
    user = response.json()["data"]
    validate(user, LIST_RESOURSE_DATA_SCHEMA)
    print(user)
    user_2 = response.json()["support"]
    validate(user_2, LIST_RESOURSE_DATA_SCHEMA_BLOCK_SUPPORT)
    print(user_2)
    url = str(user_2["url"])
    text = "reqres.in"
    #assert url.endswith("reqres.in")
    assert text in url
    assert user["id"] == 2
    assert user_2["text"] == "To keep ReqRes free, contributions towards server costs are appreciated!"

def test_get_single_resourse_note_found():
    response = httpx.get("https://reqres.in/api/unknown/23")
    assert response.status_code == 404
    response_size = response.json()
    assert len(response_size) == 0

def test_get_delayed_response():
    response = httpx.get("https://reqres.in/api/users?delay=3", timeout=3)
    assert response.status_code == 200
    for user in response.json()["data"]:
        validate(user,USER_DATA_SCHEMA)
        email = user["email"]
        assert email.endswith("reqres.in")
        #id = str(user["id"])
        #avatar = user["avatar"]
        #assert id in avatar
        id = str(user["id"])
        avatar_template = f"https://reqres.in/img/faces/{id}-image.jpg"
        avatar = user["avatar"]
        assert avatar_template == avatar




















