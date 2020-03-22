import time

def test():
    while True:
        answer = input("eaz?:")
        if answer == "nem":
            return answer
        else:
            print("nemjó")

def test2():
    if test() == "nem":
        print("találat")
    else:
        print("nemtatálat")

test2()
