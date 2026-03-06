# fib_api

# フィボナッチ数を返すAPI

## システム概要

### 技術スタック：Python

### main.api.py

・指定したn番目のフィボナッチ数を返すREST API

・calculate_fibonacci関数

└行列累乗法：計算量を減らし、応答速度を速くする

・get_fibonacci関数

└期待にそぐわないリクエストを追い返す

### unit_test.py

・正しく実装されているのかを検証するユニットテスト

### エラー事象

・文字だった場合

・整数でない場合（小数点含む）

・０以下の数字だった場合

## 実行方法

APIエンドポイント: https://fib-api-55tb.onrender.com/fib?n= {n}

└{n}の部分に文字を入力するとその結果が出力されます。

テスト実行: pytest unit_test.py

API仕様書: https://fib-api-55tb.onrender.com/docs (FastAPI標準機能)

1.GETボタン　を押下

2.Try it out　を押下

3.リクエストしたい n を入力（数字でも文字でも構いません）

4.Execute　を押下

5.ステータスコード、及びResponse body を確認
