# 個人的にあると便利な自作モジュール群

## const.py

Pythonでconstを使うためのmodule
以下のようなコードはエラーを吐く

```
import const

const.foo = 100

const.foo = 'hoge'
```