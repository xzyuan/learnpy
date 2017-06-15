#使用列表一部分
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#切片
# print(bicycles[0:2])
# print(bicycles[2:3])
# print(bicycles[:4]) #没指定，从头开始
# print(bicycles[0:])
# print(bicycles[-3:])    #最后三名成员
#
# for bicycle in bicycles[0:3]:
#     print(bicycle)

#复制列表
# motor = bicycles[:]
# print(motor)

#不能直接复制   motor = bicycles

# motor = []
# for bicycle in bicycles:
#     motor.append(bicycle)
# print(motor)

#元组
#不可变的列表

dimensions = (200,50)
# print(dimensions[0])
##dimensions[0] = 20 #不合法

# for dimension in dimensions:
#     print(dimension)

#修改元组变量
# dimensions = (400,100)
# print(dimensions)