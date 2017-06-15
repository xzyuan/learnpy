# def greet_user():
#     """显示"""
#     print("hello")
#
# greet_user()

def greet_user(name):
    for name_1 in name:
        print("Hello, " + name_1)

# greet_user("xzyuan")

#关键字实参
#顺序不重要
# def pets(type, name):
#     print(type + "  " + name)
#
# pets(type="hamster",name="Jam")

#默认值
# def pets(name, type='dog'):     #带默认值的要放在后面

#返回值
# return
#可以返回一个字典，这样有可选形参时return可变


#传递列表
usernames = ['asdasd', 'asd', 'asdsd']
# greet_user(usernames)

#在函数中对列表作的修改都是永久性的,但对切片操作不会影响列表
# def change(name):
#     name[0]='aaaaaaaa'
# change(usernames[0:1])
# print(usernames)

#传递任意数量的实参
def makepizza(size,*toppings):       #创建了一个名为toppings的空元组，
    print(size,toppings)
makepizza(77,'dff', 'asdasd')

#任意数量的关键字实参
#待看


