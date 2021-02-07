'''
计算一个数或者列表中的数的平方
'''


def square(x):
    return x**2

print(square(3))  # 方法一：直接调用函数，传参数

s = list(map(square,[1,2,3,4])) # 方法二：使用map函数，返回迭代器并转化成列表输出
print(s)

# 方法三：使用lambda匿名函数
L = list(map(lambda x: x ** 2,[2,3,4,5]))
print(L)

print('************分割线****************')

'''
用lambda函数求和

关键字lambda表示匿名函数，冒号前面的x表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，

也可以把匿名函数赋值给一个变量，再利用变量来调用该函数

'''
sum = lambda x,y,z : x+y+z
print(sum(10,2,3))
print(sum(12,2,8))

print('************分割线****************')

'''
也可以把匿名函数作为返回值返回
'''
def minus(x,y):
    return lambda: x - y
z = minus(10,2)
print(type(z))
print(z()) #z 是一个函数
