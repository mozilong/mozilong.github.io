from operator import truediv


def 判断(回文数):
    if 回文数 // 10000 == 回文数 % 10:
        if 回文数 % 10000 // 1000 == 回文数 // 10 % 10:
            return True
    else:
        return False
回文数 = int(input("请输入一个五位数"))
print(判断(回文数))