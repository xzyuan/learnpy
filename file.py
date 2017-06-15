# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)       #末尾会多出一个空行，read()到达文件末尾会返回一个空字符串，形成空行，可用rstrip()消除

#可用相对路径和绝对路径，绝对路径可以存储在一个变量中再引用，因为太长不方便
#linux下用 / ,windows下用 \

file_name = 'pi_digits.txt'

#逐行读取
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line)
        #此时空白行更多,因为每行的末尾有一个换行符，print语句也会加一个换行符
        # print(line.rstrip())

#readlines方法
# #创建包含各行内容的列表
# with open(file_name) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line)

# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()

#对于想处理的数据量，python没有要求，只要系统的内存足够多，想处理多少都可以


#写入文件
#写入空文件
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("i love programming")

#python只能将字符串写入文本文件，要写入数值的话，要先用str()转化成字符串格式

#写入多行
# file_object.write("i asdasd asdasd\n")

#添加内容，而不是覆盖
# with open(filename,'a') as file_object:
