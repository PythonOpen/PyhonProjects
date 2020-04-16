# 用tkinter写一个小游戏，来随机生成我们需要的名字
# import tkinter as tk
# import random
#
# window = tk.Tk()
#
#
# def random_1():
#     s1 = ['cats', 'hippos', 'cakes']
#     s = random.choice(s1)
#     return s
#
#
# def random_2():
#     s2 = ['eats', 'likes', 'hates', 'has']
#     s = random.choice(s2)
#     return s
#
#
# def button_click():
#     name = nameEntry.get()
#     verb = random_1()
#     noun = random_2()
#     sentence = name + '' + verb + '' + noun
#     result.delete(0, tk.END)
#     result.insert(0, sentence)
#
#
# # 用于在屏幕上显示文本或者图像
# nameLabel = tk.Label(window, text='Name:')
# # 显示文本框
# nameEntry = tk.Entry(window)
# button = tk.Button(window, text='生成随机名称', command=button_click)
# # 文本框
# result = tk.Entry(window)
#
# nameLabel.pack()
# nameEntry.pack()
# button.pack()
# result.pack()
#
# window.mainloop()

# 是一个输入密码的小程序，我们自己设定一个密码，如果用户输入正确则显示正确，否则显示不正确
# encoding:utf-8
# import tkinter as tk
# window = tk.Tk()
#
#
# def check_password():
#     password = '123456'
#     entered_password = passwordEntry.get()
#     if password == entered_password:
#         # 设置显示的文字
#         confirmLabel.config(text="正确")
#     else:
#         confirmLabel.config(text="不正确")
#
#
# passwordLabel = tk.Label(window, text="Password:")
# passwordEntry = tk.Entry(window, show="*")
# button = tk.Button(window, text="校验", command=check_password)
# confirmLabel = tk.Label(window)
#
# passwordLabel.pack()
# passwordEntry.pack()
# button.pack()
# confirmLabel.pack()
#
# window.mainloop()


# encoding:utf-8
"""
一个猜数字的小游戏，
让计算机随机生成一个整数，
用户输入去猜这个整数，
如果用户输入正确，
那么我们分数加1，
并且显示计算机生成的数字。
如果用户没有输入正确，
那么我们的分数不变，
还是要显示计算机生成的数字。
"""
import tkinter as tk
import random
window = tk.Tk()

maxNo = 10
score = 0
rounds = 0


def button_click():
    global score
    global rounds

    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxNo:
            result = random.randrange(1, maxNo+1)
            if guess == result:
                score += 1
            rounds += 1
        else:
            result = "输入不合法"
    except:
        result = "输入不合法"
    resultLabel.config(text=result)
    scoreLabel.config(text=str(score)+"/"+str(rounds))
    guessBox.delete(0, tk.END)


scoreLabel = tk.Label(window)
resultLabel = tk.Label(window)
guessBox = tk.Entry(window)
guessLabel = tk.Label(window, text="请输入1到"+str(maxNo))
button = tk.Button(window, text="guess", command=button_click)

scoreLabel.pack()
resultLabel.pack()
guessBox.pack()
guessLabel.pack()
button.pack()

window.mainloop()
