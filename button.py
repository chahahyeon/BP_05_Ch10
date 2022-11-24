#2번

def plus():
    global total
    total += int(e.get()) #e에 적은 숫자를 얻어서 int형으로 바꿔주고 total에 더해줌
    display()#바뀐 결과를 화면에 표시해줌

def minus():
    global total
    total -= int(e.get())#e에 적은 숫자를 얻어서 int형으로 바꿔주고 total에 빼줌
    display()#바뀐 결과를 화면에 표시해줌

def reset():
    global total
    total = 100
    display()

def display():
    global l2
    l2.destroy() #l2를 삭제함
    l2 = Label(window,text=total)#l2를 새로 만듦
    l2.grid(row=0,column=1) #새로 만든 l2를 원래 있던 l2의 위치인 0행 1열에 배치함


from tkinter import *

total = 100

window = Tk()
l1 = Label(window, text="현재 합계: ")
l2 = Label(window, text=total)
l1.grid(row=0,column=0) #0행 0열에 배치해줌
l2.grid(row=0, column=1)

e = Entry(window) #입력창을 만들어줌
e.grid(row=1,column=0, columnspan=3) #1행 0열에 위치하고 열위치를 조정함

b1 = Button(window, text="더하기(+)", command=plus) #버튼을 누르면 plus함수를 실행
b2 = Button(window, text="빼기(-)", command=minus) #버튼을 누르면 minus함수를 실행
b3 = Button(window, text="초기화", command=reset) #버튼을 누르면 total을 100으로 만들어줌
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)

window.mainloop()
