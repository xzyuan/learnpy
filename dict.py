# alien = {'color': 'green', 'points': '3'}
# print(alien)
# print(alien['color'])

# alien['name'] = 'Andi'
# print(alien)    #dict不关心顺序，之关心对应关系

# alien['color'] = 'Yellow'
# print(alien)

# del alien['color']  #删除键值对
# print(alien)

#较长的字典
# age = {
#     'Lihua': 18,
#     'Wanger': 20,
#     'Zhangsan': 30,
#     }
# print(age)

#遍历
# for key,value in alien.items():
#     print(key + ":" + value)

# for color in alien.keys():
    # print(color)

# for name in sorted(alien.keys()):
    # print(name)

#遍历值
# for value in alien.values():
    # print(value)   #不考虑值重复
# for value in set(alien.values()):
    # print(value)    #用set去除重复的值

#嵌套
#字典列表
# alien_0 = {'color': 'green', 'points': '3'}
# alien_1 = {'color': 'green', 'points': '3'}
# alien_2 = {'color': 'green', 'points': '3'}
# aliens = [alien_0, alien_1,alien_2]
# for alien in aliens:
#     print(alien)
#在字典中存储列表
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms','extra cheese'],
# }
# print(pizza)
#在字典中存储字典
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        }
}
for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'].title()+ "  " +user_info['last'].title()
    location = user_info['location'].title()
    print("\tFullname: " + full_name)
    print("\tLocation: " + location)


