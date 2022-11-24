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

import random
from tkinter import *

window = Tk()
secret_number = random.randint(1, 100)
guess = None
num_guesses = 0

def guess_number():
  global num_guesses
  guess = int(entry.get())
  num_guesses += 1
  if guess == secret_number:
    message = "축하합니다!!"
  elif guess < secret_number:
    message = "너무 낮아요!!"
  else:
    message = "너무 높아요!!"
  label['text']= message

def reset():
  global num_guesses
  entry.delete(0, END)
  secret_number = random.randint(1, 100)
  guess = 0
  num_guesses = 0
  message = "1부터 100사이의 숫자를 추측하시오"
  label['text']= message

message = "1부터 100사이의 숫자를 추측하시오"
label = Label(window, text=message)
entry = Entry(window)

guess_button = Button(window, text="숫자를 입력", command=guess_number)
reset_button = Button(window, text="게임을 다시 실행", command=reset)

label.grid(row=0, column=0, columnspan=2, sticky=W+E)
entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
guess_button.grid(row=2, column=0)
reset_button.grid(row=2, column=1)


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



#5번

from tkinter import*


window=Tk()
#상단 라벨 생성
l1= Label(window,text="이름")
l2= Label(window,text="직업")
l3= Label(window,text="국적")


# 격자배열을 통해 1행에 배치
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)


#입력부분 생성
e1=Entry(window)
e2=Entry(window)
e3=Entry(window)


# 격자배열을 통해 2행에 배치
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)


#하단 버튼 생성
b1=Button(window,text="Show")
b2=Button(window,text="Quit")


# 격자배열을 통해 3열에 배치
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)


window.mainloop()



#6번
from random import *
from tkinter import *
# 선택 하는 부분
def user_choice_rock():
 user_choice = "rock"
 turn(user_choice)
 user_image.configure(image=rock_image)
def user_choice_paper():
 user_choice = "paper"
 turn(user_choice)
 user_image.configure(image=paper_image)
def user_choice_scissors():
 user_choice = "scissors"
 turn(user_choice)
 user_image.configure(image=scissors_image)
# 게임부분
def turn(user_choice):
 oppo = ['rock', 'paper', 'scissors']
 oppo_choice=oppo[randint(0,2)]
 if(oppo_choice=='rock'):
 oppo_image.configure(image=rock_image)
 if(user_choice=='paper'):
 turn_result.configure(text="사용자 승!", fg="green")
 compare.configure(text=">>>>>")
 elif(user_choice=='scissors'):
 turn_result.configure(text="컴퓨터 승!", fg="red")
 compare.configure(text="<<<<<")
 else:
 turn_result.configure(text="무승부", fg="gray")
 compare.configure(text="=====")

 elif(oppo_choice=='paper'):
 oppo_image.configure(image=paper_image)
 if(user_choice=='scissors'):
 turn_result.configure(text="사용자 승!", fg="green")
 compare.configure(text=">>>>>")
 elif(user_choice=='rock'):
