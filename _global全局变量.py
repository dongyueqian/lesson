num1  = 1000
num2  = 48

def add():
    global num1
    num1 = 400
    return num1

def mins():
    num2 = 99
    return num2


print(num1)
add()
print(num1) #add()函数中，num加了global ，才会被重新赋值

print('*****************这是分割线*******************')

print(num2)
mins()
print(num2) # mins()函数中没有给num2添加全局变量关键字，所有没有修改num2的值


