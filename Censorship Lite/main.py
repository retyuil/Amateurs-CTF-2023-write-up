#!/usr/local/bin/python
flag = "amateursCTF{123}"

for _ in [flag]:
    while True:
        try:
            code = ascii(input("Give code: "))
            print(_)
            if any([i in code for i in "\lite0123456789"]):
                raise ValueError("invalid input")
            exec(eval(code))
        except Exception as err:
            print(err)
