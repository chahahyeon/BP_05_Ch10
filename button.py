#1번
from tkinter import *

window = Tk()         #tkinter를 실행
l = Label(window, text="간단한 GUI 프로그램!")       #텍스트를 만들어줌
l.pack()#최소 크기로 화면에 표시함

b1 = Button(window, text="환영합니다.")     #환영합니다가 적힌 버튼을 만듬
b2 = Button(window, text="종료")           #종료가 적힌 버튼을 만듬
b1.pack()           #최소 크기로 화면에 표시
b2.pack()           #최소 크기로 화면에 표시

window.mainloop()




#2번

def plus():
    global total
    total += int(e.get())     #e에 적은 숫자를 얻어서 int형으로 바꿔주고 total에 더함
    display()      #바뀐 결과를 화면에 표시함

def minus():
    global total
    total -= int(e.get())     #e에 적은 숫자를 얻어서 int형으로 바꿔주고 total에 뺌
    display()       #바뀐 결과를 화면에 표시함

def reset():
    global total
    total = 100
    display()

def display():
    global l2
    l2.destroy()         #l2를 삭제함
    l2 = Label(window,text=total)       #l2를 새로 만듦
    l2.grid(row=0,column=1)      #새로 만든 l2를 원래 있던 l2의 위치인 0행 1열에 배치


from tkinter import *

total = 100

window = Tk()
l1 = Label(window, text="현재 합계: ")
l2 = Label(window, text=total)
l1.grid(row=0,column=0)       #0행 0열에 배치
l2.grid(row=0, column=1)

e = Entry(window)             #입력창을 만듬
e.grid(row=1,column=0, columnspan=3)        #1행 0열에 위치하고 열위치를 조정

b1 = Button(window, text="더하기(+)", command=plus)      #버튼을 누르면 plus함수를 실행
b2 = Button(window, text="빼기(-)", command=minus)      #버튼을 누르면 minus함수를 실행
b3 = Button(window, text="초기화", command=reset)       #버튼을 누르면 total을 100으로 만듬
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)

window.mainloop()

#3번문제
rom tkinter import*
import random
window=Tk()
r=random.randint(0,100)
total=0
a=0
def c1():             #게임 룰 함수 정의
b=int(e1.get())
if b==r:
l1["text"]="정답입니다!"
elif b>r:
l1["text"]="너무 높아요!"
else:
l1["text"]="너무 낮아요!"


def c2():            #초기화 함수 정의
global r
r=random.randint(0,100)
return

#상단 라벨 생성
l1= Label(window,text="즐거운 숫자 게임")
l1.grid(row=0,column=0)


e1=Entry(window)
e1.grid(row=1)

#하단 버튼 생성
b1=Button(window,text="숫자를 입력",command=c1)
b2=Button(window,text="게임을 다시시작",command=c2)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)


window.mainloop()


#4번문제

def convert():
    inch_val = int(e.get())             #e에 입력한 문자를 int형으로 바꿔주고 inch_val에 저장함
    cm_val = inch_val * 2.54                       #inch를 cm로 바꿔 줌
    l4.configure(text = str(cm_val)+" 센티미터")           #l4의 텍스트를 교체함
    

from tkinter import *

window = Tk()

l1 = Label(window, text = "인치를 센티미터로 변환하는 프로그램: ")
l1.grid(row=0, column=0,columnspan=2)         #columnspan을 이용해 열을 2개 차지하게 만들어줌

l2 = Label(window, text = "인치를 입력하시오:")
e = Entry()                          #입력칸을 만들어서 인치를 입력하게 만들어 줌
l2.grid(row=1, column=0)
e.grid(row=1, column=1)

l3 = Label(window, text = "변환결과:")
l4 = Label(window, text = "0 센티미터")
l3.grid(row=2, column=0)
l4.grid(row=2, column=1)

b = Button(window, text="변환!", command=convert)             #이 버튼을 누르면 convert함수가 실행
b.grid(row=3, column=1)

window.mainloop()
