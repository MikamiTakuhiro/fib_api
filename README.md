# fib_api

フィボナッチ数を返すAPI

システム概要
技術スタック：Python

main.api.py

・指定したn番目のフィボナッチ数を返すREST API

・calculate_fibonacci関数

└行列累乗法：計算量を減らし、応答速度を速くする

・get_fibonacci関数

└変なリクエストを追い返す

unit_test.py

正しく実装されているのかを検証するユニットテスト

エラー事象

・文字だった場合

・整数でない場合（小数点含む）

・０以下の数字だった場合
