from fastapi.testclient import TestClient
from index import app


client = TestClient(app)


data = {
    "question": "Which API framework are we using?",
    "option1": "Django",
    "option2": "Flask",
    "option3": "RestAPI",
    "option4": "FastAPI",
    "answer": "FastAPI"
}


def test_create_mcq():
    responce = client.post('/', json=data)
    assert responce.status_code == 200
    data["_id"] = responce.json()[0]["_id"]
    assert responce.json()[0] == data


def test_get_all_mcq():
    responce = client.get('/', json=data)
    assert responce.status_code == 200
    assert data in responce.json()


def test_get_one_mcq():
    responce = client.get('/'+data['_id'])
    assert responce.status_code == 200
    assert responce.json() == data


def test_update_mcq():
    data["question"] = "changed"
    responce = client.put("/"+data['_id'], json=data)
    assert responce.status_code == 200
    assert responce.json() == data


def test_delete_mcq():
    responce = client.delete("/"+data['_id'])
    assert responce.status_code == 200
    assert responce.json() == data
