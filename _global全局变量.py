num  = 1000

def add():
    global num
    num = 400
    return num

print(num)
add()
print(num) #add()函数中，num加了global ，才会被重新赋值
