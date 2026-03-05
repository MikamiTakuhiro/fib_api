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
    assert response.json() == {"result": 218922995834555169026}

def test_fibonacci_invalid_string():
    response = client.get("/fib?n=hello")
    assert response.status_code == 400
    assert response.json() == {"status": 400, "message": "Bad request."}
def test_fibonacci_negative():
    response = client.get("/fib?n=-1")
    assert response.status_code == 400
    assert response.json() == {"status": 400, "message": "Bad request."}

def test_fibonacci_float():
    # 小数点が含まれるリクエストのテスト
    response = client.get("/fib?n=1.2")
    # 期待値: 整数ではないため 400 エラーが返ること
    assert response.status_code == 400
    assert response.json() == {"status": 400, "message": "Bad request."}

def test_fibonacci_float_string():
    # 文字列として小数が送られた場合のテスト
    response = client.get("/fib?n=3.14")
    assert response.status_code == 400
    assert response.json() == {"status": 400, "message": "Bad request."}