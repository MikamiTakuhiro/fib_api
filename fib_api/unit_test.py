from fastapi.testclient import TestClient
from main_api import app

client = TestClient(app)

def test_fibonacci_valid():
    response = client.get("/fib?n=9")
    assert response.status_code == 200
    assert response.json() == {"result": 34}

def test_fibonacci_99():
    response = client.get("/fib?n=99")
    assert response.status_code == 200
    assert response.json()["result"] == 218922995834555169026

def test_fibonacci_invalid_string():
    response = client.get("/fib?n=hello")
    assert response.status_code == 400

def test_fibonacci_negative():
    response = client.get("/fib?n=-1")
    assert response.status_code == 400