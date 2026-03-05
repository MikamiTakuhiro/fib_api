from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Union
from fastapi.responses import JSONResponse

app = FastAPI()

class FibonacciResponse(BaseModel):
    result: int #フィボナッチ数の結果を格納

class ErrorResponse(BaseModel):
    status: int #エラーコードを格納
    message: str #エラーメッセージを格納

def calculate_fibonacci(n: int) -> int:
    """行列累乗法による高速計算 O(log n)"""
    def multiply(A, B):
        C = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def power(A, p):
        res = [[1, 0], [0, 1]]
        while p > 0:
            if p % 2 == 1:
                res = multiply(res, A)
            A = multiply(A, A)
            p //= 2
        return res

    if n <= 0: return 0
    if n == 1: return 1
    T = [[1, 1], [1, 0]]
    T_n = power(T, n - 1)
    return T_n[0][0]

@app.get("/fib")
async def get_fibonacci(n: str = Query(...)): # 文字列として受け取るのがコツ
    try:
        # 1. 整数に変換できるかチェック（1.2やabcはここでValueErrorへ）
        n_int = int(n)

        # 2. 整数だが、仕様外の数字（0以下）をチェック
        if n_int <= 0:
            return JSONResponse(
                status_code=400,
                content={"status": 400, "message": "Bad request."}
            )

        # 3. 計算実行
        result = calculate_fibonacci(n_int)
        return {"result": result}

    except ValueError:
        # 文字列や小数が入力された場合はここに来る
        return JSONResponse(
            status_code=400,
            content={"status": 400, "message": "Bad request."}
        )