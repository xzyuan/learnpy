bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# print(bicycles[1].title())

# print(bicycles[-1])

#修改、删除、添加
# bicycles[1] = 'forever'
# print(bicycles)

# bicycles.append('giant')
# print(bicycles)

#插入
# bicycles.insert(0, 'forever')
# print(bicycles)

# del bicycles[0] #使用del方法删除
# print(bicycles)

# poped_bicycle = bicycles.pop()
# print(poped_bicycle)
# print(bicycles)     #取出末尾元素
# # specialized
# # ['trek', 'cannondale', 'redline']

# first_owned = bicycles.pop(0)   #取出指定位置元素
# print(bicycles)
# print(first_owned)

#根据值删除元素
# bicycles.remove('trek')#只删除第一个指定的值，删除多个需要循环
# print(bicycles)

#排序
# bicycles.sort()   #sort会改变列表
# bicycles.sort(reverse=True)
# print(bicycles)

# print(sorted(bicycles))     #sorted保留列表
# print(bicycles)

#倒着打印
# bicycles.reverse()
# print(bicycles)

#确定列表长度
# print(len(bicycles))

#列表为空时，访问-1会报错