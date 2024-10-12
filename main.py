from time import *
import random as r
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def incorrectWords(para, userPara):
    error = 0

    for i in range(len(para)):
        try:
            if para[i] != userPara[i]:
                error = error + 1
        except:
            error = error + 1
    return error


sentences = [
    "The significance of reading in personal development is undeniable as it expands vocabulary ",
    "Technology has advanced greatly in recent decades profoundly altering how we live and work.",
    "Financial planning is a crucial skill for achieving economic stability and reaching personal and professional goals.",
]
para = r.choice(sentences)
t1 = time()
print(para)
userPara = input("Start Typing \n")
t2 = time()
print(t2 - t1)

para = para.split(" ")
userPara = userPara.split(" ")
error = incorrectWords(para, userPara)

speed = round((len(userPara)) * 60 / (round((t2 - t1), 2)), 0)
accuracy = round(((len(para) - error) / len(para)) * 100, 0)
print(f"your speed is {speed} wpm")
print(f"Your accuracy is {accuracy}")

with open("speed.csv", "a+") as sp:
    sp.write(str(speed) + "," + str(accuracy)+"\n" )
    sp.close()

flag=input("Do you want to see graphs (Y/N)?")
if(flag=='Y' or flag=='y'):
    df = pd.read_csv("speed.csv")
    s = df["Speed"]


    acc = df["Accuracy"]
    plt.plot(np.arange(len(s)), s)
    plt.ylabel("Speed")
    plt.show()

    plt.ylabel("Accuracy")
    plt.plot(np.arange(len(s)), acc)
    plt.show()
else:
    print("Thank for using Donkey-Typing")