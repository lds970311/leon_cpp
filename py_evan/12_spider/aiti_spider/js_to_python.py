# coding:utf-8
# time: 2023/6/7
# author: evan

import js2py

jsExec = js2py.EvalJs()

with open('./index.js', 'r') as f:
    jsExec.execute(f.read())
    print(jsExec.add(1, 2))
