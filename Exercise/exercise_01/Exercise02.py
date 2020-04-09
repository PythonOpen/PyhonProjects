"""
编写一个程序，接受用户输入的内容，并且保存为新的文件
如果用户单独输入:w
表示文件保存推出
open()
input()
"w"
"""
# file_name = input("请用户输入文件名:")
#
#
# def file_write(file):
#     # 打开我们用户的文件
#     f = open(file, "w")
#     print("请输入内容, (单独输入:w保存并退出)")
#     while True:
#         write_something = input()
#         # 判断用户输入的是不是:w
#         if write_something != ":w":
#             # 向文件中写入用户输入的内容
#             f.write("%s\n"%write_something)
#
#         else:
#             # 用户输入的是:w
#             break
#
#     f.close()
#
#
# file_write(file_name)


# 编写一个程序，比较用户输入的文件是否相同，如果不同，显示出所有不同处的行号
"""
f.readline()
open()
differ
"""
# file1 = input("请输入需要比较的第一个文件名:")
# file2 = input("请输入需要比较的第二个文件名:")
#
#
# def file_compare(file_1, file_2):
#     f1 = open(file_1)
#     f2 = open(file_2)
#
#     count = 0  # 统计行数
#     differ = []  # 统计不一样的数量
#     for line1 in f1:
#         line2 = f2.readline()
#         count += 1
#         if line1 != line2:  # 文件不同
#             differ.append(count)
#
#     f1.close()
#     f2.close()
#
#
#
#     return differ
#
#
# different = file_compare(file1, file2)
# if len(different) == 0:
#     print("两个文件完全相同")
# else:
#     print("两个文件有%d行不同" % len(different))
#     for each in different:
#         print("第%d行不一样" % each)


"""
编写一个程序,当用户输入文件名和行数的时候，将该文件的前N行内容打印到屏幕上
input去接收一个文件名
input去接收一个行数
"""
# r"字符串", r表示字符串不进行转义，例如\n则为\和n两个字符，并不代表换行
# fileName = input(r"请输入你要打开的文件名:")
# lineNum = input(r"请输入你要显示的前几行:")
#
#
# def file_view(file_name, line_num):
#     print("\n文件%s的前%s行的内容如下" %(file_name, line_num))
#     # 去打开file_name的文件
#     f = open(file_name)
#     for i in range(int(line_num)):
#         print(f.readline())
#
#     f.close()
#
#
# file_view(fileName, lineNum)


"""
在上一道题的基础上，增加一点功能，使用户可以随意的输入需要显示的行数
12:32
:
:9
用以上的形式来表示我们想要打印的起始和结束的行数
"""
# fileName = input(r"请输入你要打开的文件名:")
# lineNum = input(r"请输入你要显示的行数,格式为2:9/:/:9：")
#
#
# def print_line(file_name, line_num):
#     f = open(file_name)
#     # 对输入内容进行切片
#     begin, end = line_num.split(":")
#     if begin == "":
#         begin = "1"
#     if end == "":
#         end = "-1"
#     begin = int(begin)-1
#     end = int(end)
#
#     lines = end - begin
#     # 消耗掉begin之前的行数
#     for i in range(begin):
#         f.readline()
#     # lines < 0,即end = -1的情况
#     if lines < 0:
#         # 输出剩下的内容
#         print(f.read())
#
#     else:
#         for j in range(lines):
#             print(f.readline())
#     f.close()
#
#
# print_line(fileName, lineNum)

"""
编写一个程序，实现"全部替换"的功能
打开一个文件
把文件中xxx这样的字符串，替换成sss
open打开文件
readline读取文件的内容
replace替换
"""
# fileName = input(r"请输入你要打开的文件名:")
# repWord = input("请输入你要替换的字符:")
# newWord = input("请输入替换的新的字符串:")
#
#
# def file_replace(file_name, rep_word, new_word):
#     f = open(file_name)
#     content = []
#     for each_line in f:
#         if rep_word in each_line:
#             each_line = each_line.replace(rep_word, new_word)
#         content.append(each_line)
#
#     decide = input("你确定要和样子做吗？请输入YES/NO:")
#     if decide in ["YES", "Yes", "yes"]:
#         f_write = open(file_name, "w")
#         f_write.write("".join(content))
#         f_write.close()
#
#
# file_replace(fileName, repWord, newWord)

"""
编写一个程序，统计当前目录下每个文件类型的文件数
思路：
打开当前的文件夹
获取当前文件夹下面所有的文件
处理我们当前文件夹下面可能有文件夹的情况(也要应答出来)
做出统计
"""
# import os
# 获取当前文件夹下面所有的文件
# os.curdir表示当前目录curdir: currentdirectory
# typeDict = dict()
#
#
# def all_type_files(dir_path, type_dict):
#     all_files = os.listdir(dir_path)
#     for each_file in all_files:
#         # 拼接完整的的路径
#         full_path = os.path.join(dir_path, each_file)
#         # 如果说我们的each_file是文件夹
#         if os.path.isdir(full_path):
#             type_dict.setdefault("文件夹", 0)
#             type_dict['文件夹'] += 1
#             all_type_files(full_path, type_dict)
#         elif os.path.isfile(full_path):
#             # 如果不是文件夹，而是文件，统计我们的文件
#             # os.path.splitext("文件路径") 分离文件名与扩展名，默认返回元组
#             ext = os.path.splitext(each_file)[1]  # 获取到文件的后缀
#             # dict.setdefault(key, a),如果键不存在于字典中，将会添加键并将值设为默认值。
#             type_dict.setdefault(ext, 0)
#             type_dict[ext] += 1
#
#
# all_type_files(os.curdir, typeDict)
# for each_type in typeDict:
#     print("该文件夹下面有类型为'{}'的文件{}个".format(each_type, typeDict[each_type]))
#

"""
编写一个程序，计算当前文件夹下面所有文件的大小
打开当前文件夹
获取所有的文件，和文件大小
保存我们获到的数据，然后打印出来
"""
# import os
# count = 0
#
#
# def allfiles(dir_path):
#     global count
#     all_files = os.listdir(dir_path)
#     for each_file in all_files:
#         # 拼接完整的的路径
#         full_path = os.path.join(dir_path, each_file)
#         # 如果说我们的each_file是文件夹
#         if os.path.isdir(full_path):
#             allfiles(full_path)
#         elif os.path.isfile(full_path):
#             size = os.path.getsize(full_path)
#             print("{}文件的大小:{}".format(full_path, size))
#             count += size
#
#
# allfiles(os.curdir)
# print(count)


""" 
编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在，如果遇到文件夹，则进入该文件夹继续搜索
input 去接收用户输入的文件名和开始搜索的路径
os.path.isdir去判断是不是文件夹，如果是的话，就需要进入该文件夹继续搜索，循环调用一下我们的函数来实现
"""
# import os
#
# startDir = input("请输入目录:")
# target = input("请输入文件名:")
#
#
# def search_file(start_dir, target):
#     # 切换到用户输入的路径
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         if each_file == target:
#             # os.getcwd()为获取当前完整路径
#             print(os.getcwd() + "\\" + each_file)
#
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             # 回到上层目录，即父目录
#             os.chdir(os.pardir)
#
#
# search_file(startDir, target)


"""
对上述题目加一些需求，模糊匹配，判断我们的target是否包含在某一个文件名字中
in 去判断target这个字符串是否在文件的名字中
"""
# import os
#
# startDir = input("please input start directory:")
# target = input("enter your file name:")
#
#
# def search_file(start_dir, target):
#     # 切换到用户输入的路径
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         if target in each_file:
#             # print(os.getcwd() + "\\" + each_file)
#             # os.sep表示反斜杠的意思
#             print(os.getcwd() + os.sep + each_file)
#
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             # 回到上层目录，即父目录
#             os.chdir(os.pardir)
#
#
# search_file(startDir, target)


# 对上述题目增加一个需求，我们需要保存我们的文件存在的地方，到我们指定的路径
# file I/O写文件
import os

startDir = input("please input start directory:")
target = input("enter your file name:")
backup = []


def search_file(start_dir, targets):
    # 切换到用户输入的路径
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        if targets in each_file:
            # print(os.getcwd() + "\\" + each_file)
            # os.sep表示反斜杠的意思
            full_path = os.getcwd() + os.sep + each_file
            # print(full_path)
            backup.append(full_path)

        if os.path.isdir(each_file):
            search_file(each_file, targets)  # 递归调用
            # 回到上层目录，即父目录
            os.chdir(os.pardir)

    return backup


rd = search_file(startDir, target)
f = open(os.getcwd() + os.sep + "backup.txt", "wb")
f.write("\n".join(rd).encode("utf-8"))
f.close()
# print(rd)
