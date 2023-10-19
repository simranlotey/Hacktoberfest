from tkinter import *

import pickle
import random as r
import sys
'''tk=Tk()
tk.title('Login ')
tk.geometry('500x500') #Dimensions of the space
tk.configure(bg='#ffecad')#background color'''
OPTIONS=["Battleship","Submarine","Patrol Boat"]

List = []
lis={}
reg = { }
LogDict= { }
addlis=[]
cpoint=0
def TakeUNPW():
     flag = 0 
     User_nameL=UNT.get("1.0","end-1c")
     PasswordL=PWT.get()#("1.0","end-1c")

     with ( open("Ship.log", "rb")) as log_file:
          while True:
               try:
                    List.append( pickle.load(log_file))
                    print(List)
                    break
               except EOFError:
                    break
     for j in range( len(List)):
          print('len',len(List))
          x = List[j]
          print('yh',x)
          for Key in x:
               print('key',Key)
               if Key == User_nameL and x[Key] == PasswordL:
                    print("Access Granted")
                    Play_Game()
                    flag = 1
                    break
     if flag == 0:
          print('Access Denied')
          screen3=Tk() 
          screen3=Canvas(screen3,width=380,height=200,bg='red') 
          screen3.pack() 
          screen3.create_text(190,110,text='''Incorrect password or username''',font=('courier',15),fill='black')

     
def StoreUNPW():
     User_name=UNT.get("1.0","end-1c")
     Password=PWT.get()#("1.0","end-1c")
     if len(Password)<=5:
          screen2=Tk() 
          screen2=Canvas(screen2,width=400,height=250,bg='red') 
          screen2.pack() 
          screen2.create_text(150,100,text='''
          Very weak password,no
          of password characters
          should be at least 6''',font=('courier',15),fill='black')
     else:
         reg[User_name] = Password
         reg_file = open("Ship.log", 'ab')
         pickle.dump(reg, reg_file)
         reg_file.close()
         Sign.destroy()
         print(reg)

def Register():
     global Sign
     Sign=Tk()
     Sign.title('Register ')
     Sign.geometry('500x500') #Dimensions of the space
     Sign.configure(bg='#ffecad')#background color
     
     #User Name
     UserNameL=Label(Sign,text='User Name-',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-150, y=100, anchor = W)
     global UNT
     UNT=Text(Sign, height=2, width=30)
     UNT.place(x=200, y=90)
     
     #PassWord
     PasswordL=Label(Sign,text='Password-',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-150, y=150, anchor = W)
     global PWT
     PWT = Entry(Sign, bd = 4, show="*")
     #PWT=Text(Sign, height=2, width=30, fg="white")
     PWT.place(x=200,y=150)
     Button(Sign, height=1, width=10, text="Submit", 
                    command=lambda: StoreUNPW()).place(x=200,y=200) 
    
     
def Login():
     global Login
     Login=Tk()
     Login.title('Login ')
     Login.geometry('500x500') #Dimensions of the space
     Login.configure(bg='#ffecad')#background color
     UserNameL=Label(Login,text='User Name-',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-150, y=100, anchor = W)
     global UNT
     UNT=Text(Login, height=2, width=30)
     UNT.place(x=200, y=90)
     
     #PassWord
     PasswordL=Label(Login,text='Password-',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-150, y=157, anchor = W)
     global PWT
     #PWT=Text(Login, height=2, width=30)
     PWT = Entry(Login, bd=4, show="*")
     PWT.place(x=200, y=150)
     Button(Login, height=1, width=10, text="Login", command=lambda: TakeUNPW()).place(x=200,y=200)
     
 

def Play_Game():
     global Play
     global rows, cols, buttons 
     global window
     global OPTIONS
     '''Play=Tk()
     Play.title('Play The Game ')
     Play.geometry('500x500') #Dimensions of the space
     Play.configure(bg='#ffecad')#background color
     Login.destroy()
     tk.destroy()'''
     import tkinter
     window = Tk() 
     window.configure(background='orange') 
     window.title("BATTLESHIP") 
     window.geometry('1500x1500')

     #prepare default values
     '''Textvalue=StringVar()
     Textvalue.set('')
     
     def ShowShip():
          Textvalue.set('Oopss!SHIP')'''
    

     global f
     global h
     global b
     global sky
     sky='sky blue'
     tkinter.Button(window, text="\t\t\t\tPlayer-1\t\t\t\t\t\t\t  INDIAN OCEAN\t\t\t\t\t\t     Player-2\t\t\t\t\t",bg='sky blue').grid(row=0, column=0, columnspan=19) 
     #buttons = {} 
     rows = 12
     #global x
     for x in range(0, rows-3):
          #buttons[x]=[]
          cols = 19
          #global y
          for y in range(0, cols):
               if y!=9 and x!=0 and y!=10 and y!=0:
                    b= tkinter.Button(window, text=" ", command=lambda: Cfire(),width=8,height=4,bg=sky)
                    #b.bind(lambda e, ShowShip:onRightClick())
                    b.grid(row=x+1, column=y)
                    #buttons[x].append([])
                    #buttons[x].append(y)
                    #(buttons.get(x)).append('y')
                    #print((buttons.get(x)).append(y)) 
                    b=IntVar()   
                    b.set(0) 
               if y==9:
                    if x==0:
                         b = tkinter.Button(window, text=" ", width=4,height=2,bg='black')
                         #b.bind("<Button-3>", lambda e, x=x, y=y:(x, y)) 
                         b.grid(row=x+1, column=y) 
                         #buttons[x].append(y)
                    else:
                         b = tkinter.Button(window, text=" ", width=4,height=4,bg='black')
                         #b.bind("<Button-3>", lambda e, x=x, y=y:(x, y)) 
                         b.grid(row=x+1, column=y) 
                         #buttons[x].append(y)
               if y==1 and x==0:
                    b = tkinter.Button(window, text="1", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==2 and x==0:
                    b = tkinter.Button(window, text="2", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==3 and x==0:
                    b = tkinter.Button(window, text="3", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==4 and x==0:
                    b = tkinter.Button(window, text="4", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==5 and x==0:
                    b = tkinter.Button(window, text="5", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==11 and x==0:
                    b = tkinter.Button(window, text="1", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==12 and x==0:
                    b = tkinter.Button(window, text="2", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==13 and x==0:
                    b = tkinter.Button(window, text="3", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==14 and x==0:
                    b = tkinter.Button(window, text="4", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==15 and x==0:
                    b = tkinter.Button(window, text="5", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==0 and x==1:
                    b = tkinter.Button(window, text="1", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==0 and x==2: 
                    b = tkinter.Button(window, text="2", width=4,height=4,bg='brown')
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==0 and x==3:
                    b = tkinter.Button(window, text="3", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==0 and x==4:
                    b = tkinter.Button(window, text="4", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==0 and x==5:
                    b = tkinter.Button(window, text="5", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==10 and x==1:
                    b = tkinter.Button(window, text="1", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==10 and x==2:
                    b = tkinter.Button(window, text="2", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==10 and x==3:
                    b = tkinter.Button(window, text="3", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==10 and x==4: 
                    b = tkinter.Button(window, text="4", width=4,height=4,bg='brown')
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y)) 
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y) 
               if y==10 and x==5: 
                    b = tkinter.Button(window, text="5", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
               if y==0 and x==0: 
                    b = tkinter.Button(window, text="", width=4,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
               if y==10 and x==0: 
                    b = tkinter.Button(window, text="", width=4,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
               if y==6 and x==0 or y==16 and x==0: 
                    b = tkinter.Button(window, text="6", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
               if y==7 and x==0 or y==17 and x==0: 
                    b = tkinter.Button(window, text="7", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
               if y==8 and x==0 or y==18 and x==0: 
                    b = tkinter.Button(window, text="8", width=8,height=2,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
               if y==0 and x==6 or y==10 and x==6: 
                    b = tkinter.Button(window, text="6", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
               if y==0 and x==7 or y==10 and x==7: 
                    b = tkinter.Button(window, text="7", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
               if y==0 and x==8 or y==10 and x==8: 
                    b = tkinter.Button(window, text="8", width=4,height=4,bg='brown') 
                    #b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
                    b.grid(row=x+1, column=y) 
                    #buttons[x].append(y)
            
               #a=Label(window,text="Please enter the number of ship which must be placed :-").grid(row=7, column=0, columnspan=13) 
               #j=Entry(window,textvariable= StringVar(),bg="silver").grid(row=7, column=7, columnspan=13)
               #c=Label(window,text="DO you want to place the ship horizontally or vertically(h/v):-").grid(row=8, column=0, columnspan=13)
               #d=Entry(window,textvariable= StringVar(),bg="silver").grid(row=8, column=7, columnspan=13)
               #print(buttons)    
               e=Label(window,text="Please enter the row number here :-").place(x=290, y=660, anchor = W)
               f=Text(window, height=1, width=10)
               f.place(x=550, y=635)
               g=Label(window,text="Please enter the column number here :-").place(x=280, y=640, anchor = W)
               h=Text(window, height=1, width=10)
               h.place(x=550, y=655)
               #Button(window, height=1, width=10, text="Fire", command=lambda: command()).place(x=540,y=500)
               Label(window,text='BATTLESHIP-3 BLOCKS\n\nSUBMARINE-2 BLOCKS\n\nPATROL BOAT-1 BLOCK', width=20,height=10, bg='burlywood1').place(x=1195, y=700, anchor = W)
               
               ship=Label(window,text="Please enter the ship to choose:-").place(x=650,y=635)
               ship1=Text(window, height=1, width=10)
               global variable
               variable = StringVar(window)
               variable.set("select") # default value
               
               w = OptionMenu(window,variable,*OPTIONS,command=command).place(x=885,y=635)
               
     window.mainloop()

def complace():
     global vvv
     global dot11
     global dot12
     global dot13
     global dot21
     global dot22
     global dot3
     global OPTIONS
     vvv=r.choice(OPTIONS)
     rem=OPTIONS.remove(vvv)
     print('this',OPTIONS,vvv)
     
     print(vvv)
     if vvv=="Battleship":
          pla=r.choice(["Vertical","Horizontal"])
          print(pla)
          if pla=='Vertical':
               row=r.randint(1,6)
               column=r.randint(11,18)
               print(row,column)
               
               dot11=Button(window, width=8,height=4,command=lambda: H31point(),bg='sky blue')
               dot11.grid(row=row+2, column=column, rowspan=1)
               
               dot12=Button(window, width=8,height=4,command=lambda: H32point(),bg='sky blue')
               dot12.grid(row=row+3, column=column, rowspan=1)
               
               dot13=Button(window, width=8,height=4,command=lambda: H33point(),bg='sky blue')
               dot13.grid(row=row+4, column=column, rowspan=1)
               '''dot=IntVar()
               dot.set(1)'''
          elif pla=='Horizontal':
               row=r.randint(1,8)
               column=r.randint(11,16)
               #print(row,column)
               
               dot11=Button(window,width=8,command=lambda: H31point(),height=4,bg='sky blue')
               dot11.grid(row=row+1, column=column+1, columnspan=1)
               
               dot12=Button(window,width=8,command=lambda: H32point(),height=4,bg='sky blue')
               dot12.grid(row=row+1, column=column+2, columnspan=1)
               
               dot13=Button(window,width=8,command=lambda: H33point(),height=4,bg='sky blue')
               dot13.grid(row=row+1, column=column+3, columnspan=1)
               '''dot=IntVar()
               dot.set(1)'''
     elif vvv=="Submarine":
          pla=r.choice(["Vertical","Horizontal"])
          print(pla)
          if pla=='Vertical':
               row=r.randint(1,7)
               column=r.randint(11,18)
               print(row,column)
               #row,column=7,18
               
               dot21=Button(window,  width=8,height=4,command=lambda: H21point(),bg='sky blue')
               dot21.grid(row=row+2,column=column, rowspan=1)
               
               dot22=Button(window,  width=8,height=4,command=lambda: H22point(),bg='sky blue')
               dot22.grid(row=row+2,column=column, rowspan=1)
               
               '''dot=IntVar()
               dot.set(1)'''
          elif pla=='Horizontal':
               row=r.randint(1,8)
               column=r.randint(11,16)
               print(row,column)
               
               dot21=Button(window, width=8,height=4,command=lambda: H21point(),bg='sky blue')
               dot21.grid(row=row+1, column=column+1, columnspan=1)
               
               dot22=Button(window, width=8,height=4,command=lambda: H22point(),bg='sky blue')
               dot22.grid(row=row+1,column=column+2, rowspan=1)
               '''dot=IntVar()
               dot.set(1)'''
     elif vvv=='Patrol Boat':
          row=r.randint(1,8)
          column=r.randint(11,18)
          for i in range(1):
               dot3=Button(window,  width=8,command=lambda: H1point(),height=4,bg='sky blue')
               dot3.grid(row=row+1+i, column=column, columnspan=1)
               '''dot=IntVar()
               dot.set(1)'''

point=0
des=0
def H31point():
     global point
     print(vvv)
     point+=1
     dot11.destroy()
     Hpoint()

def H32point():
     global point
     print(vvv)
     point+=1
     dot12.destroy()
     Hpoint()

def H33point():
     global point
     print(vvv)
     point+=1
     dot13.destroy()
     Hpoint()
     
def H21point():
     global point
     print(vvv)
     point+=1
     dot21.destroy()
     Hpoint()
     
def H22point():
     global point
     print(vvv)
     point+=1
     dot22.destroy()
     Hpoint()
     
def H1point():
     global point
     print(vvv)
     point+=1
     dot3.destroy()
     Hpoint()

def Hpoint():
     Label(window,text='Human points', width=17,height=3, bg='burlywood1').place(x=1250, y=400, anchor = W)
     Label(window,text=point, width=7,height=3, bg='burlywood1').place(x=1286, y=450, anchor = W)
     print('point',point)
     if point==6:
          window.destroy()
          import tkinter
          bot = Tk() 
          bot=Canvas(bot,width=400,height=250,bg='red')
          bot.pack() 
          bot.create_text(150,100,text='''
          GAME OVER!!
          YOU won :)
          ''',font=('courier',15),fill='black')
'''l=[]
def cfire():
    for i in range 9:'''
        
def command(*OPTIONS):
     global VV
     VV=variable.get()
     global C
     global n
     global he
     if VV=='Battleship':
          Lab=Label(window,text="Vertical or Horizontal :-").place(x=885,y=700)
          C=Text(window, height=1, width=10)
          C.place(x=1050, y=700)
          n=3
          #he=Button(window, height=1, width=10, text="Place", command=lambda: fire()).place(x=1080,y=658)
     elif VV=='Submarine':
          Lab=Label(window,text="Vertical or Horizontal :-").place(x=885,y=700)
          C=Text(window, height=1, width=10)
          C.place(x=1050, y=700)
          n=2
          #he=Button(window, height=1, width=10, text="Place", command=lambda: fire()).place(x=1080,y=658)
     elif VV=='Patrol Boat':
          Lab=Label(window,text="One block so type one- :-").place(x=885,y=700)
          C=Text(window, height=1, width=10)
          C.place(x=1050, y=700)
          n=1

     he=Button(window, height=1, width=10, text="Place", command=lambda: fire())
     he.place(x=1050, y=750)
     #print(VV)
     
def fire():
     global des
     f2=f.get("1.0","end-1c")
     h2=h.get("1.0","end-1c")     
     #print('f2',f2)
     des+=1
     print(des,'des')
     #print("des",des)
     CC=C.get("1.0","end-1c")
     #print('CC',CC)
     #print('h2',h2)
     if int(des)>=4:
         he.destroy()
     else:
         if str(CC)=='Vertical':
               for i in range(n):
                    dot=Button(window, text="*", width=8,height=4,bg='red').grid(row=int(h2)+1+i, column=f2, columnspan=1)
                    t=[int(h2)+i,int(f2)]
                    addlis.append(t)
                    #dot=IntVar()
                    #dot.set(1)
         elif str(CC)=='Horizontal':
               for i in range(n):
                    dot=Button(window, text="*", width=8,height=4,bg='red').grid(row=int(h2)+1, column=int(f2)+i, columnspan=1)
                    t=[int(h2),int(f2)+i]
                    addlis.append(t)
                    dot=IntVar()
                    dot.set(1)
         else:
               for i in range(n):
                    dot=Button(window, text="*", width=8,height=4,bg='red').grid(row=int(h2)+1+i, column=f2, columnspan=1)
                    t=[int(h2)+i,int(f2)]
                    addlis.append(t)
                    dot=IntVar()
                    dot.set(1)
         print('addlis',addlis)
         complace()

def Cfire():
     global cpoint
     rowno=r.randint(1,8)
     colno=r.randint(1,8)
     our=[rowno,colno]
     print('our',our)
     if our in addlis:
          cpoint+=1
          Label(window,text='Computer points', width=17,height=3, bg='burlywood1').place(x=1250, y=500, anchor = W)
          Label(window,text=cpoint, width=7,height=3, bg='burlywood1').place(x=1286, y=550, anchor = W)
          print('cpoint',cpoint)
          if cpoint==6:
               print('delete')
               window.destroy()
               import tkinter
               bot = Tk() 
               bot=Canvas(bot,width=500,height=500,bg='red')
               bot.pack() 
               bot.create_text(200,200,text='''
               GAME OVER!!

               Oopsy doopsy!

               Computer won :)
               ''',font=('courier',15),fill='black')

'''def command(*OPTIONS):
     VV=variable.get()
     if VV=='Battleship':
          Lab=Label(window,text="Vertical or horizontal :-").place(x=440,y=500)
          C=Text(window, height=1, width=10)
          print(C.get("1.0","end-1c"))
          C.place(x=550, y=500)
          n=3
     elif VV=='Submarine':
          Lab=Label(window,text="Vertical or horizontal :-").place(x=440,y=550)
          C=Text(window, height=1, width=10)
          C.place(x=550, y=455)
          n=2
     elif VV=='ship':
          n=1
     print(VV)
     f2=f.get("1.0","end-1c")
     h2=h.get("1.0","end-1c")
     print(f2)
     if C.get("1.0","end-1c")=='Vertical':
          for i in range(n):
               Button(window, text="*", width=8,height=4,bg='red').grid(row=int(h2)+1+i, column=f2, columnspan=1)
     elif C.get("1.0","end-1c")=='Horizontal':
          for i in range(n):
               Button(window, text="*", width=8,height=4,bg='red').grid(row=int(h2)+1, column=f2+i, columnspan=1)
     else:
          for i in range(n):
               Button(window, text="*", width=8,height=4,bg='red').grid(row=int(h2)+1+i, column=f2, columnspan=1)'''
 

'''def showcolour():
     colour=['red','pink','yellow','burlywood1','pink3']
     b.configure(background=random.choice(colour))
     import tkinter
     
     f1=f.get("1.0","end-1c")
     h1=h.get("1.0","end-1c")
     
     #but=(b.grid(row=int(f1)+1, column=h1)).get()
     print('f1',f1)
     print('h1',h1)
     sky='red'
     global x
     global y
     y=f1
     x=h1
          
     print('red')
     print(x)
     if int(x)==1:
          screen4=Tk() 
          screen4=Canvas(screen4,width=380,height=200,bg='red') 
          screen4.pack() 
          screen4.create_text(190,110,text=Your Out of the sea!!,font=('courier',15),fill='black')
          screen4.mainloop()
     elif int(y)==0:
          screen4=Tk() 
          screen4=Canvas(screen4,width=380,height=200,bg='red') 
          screen4.pack() 
          screen4.create_text(190,110,text=Your Out of the sea!!,font=('courier',15),fill='black')
          screen4.mainloop()
     elif int(y)==6:
          screen4=Tk() 
          screen4=Canvas(screen4,width=380,height=200,bg='red') 
          screen4.pack() 
          screen4.create_text(190,110,text=Your Out of the sea!!,font=('courier',15),fill='black')
          screen4.mainloop()
     elif int(y)==7:
          screen4=Tk() 
          screen4=Canvas(screen4,width=380,height=200,bg='red') 
          screen4.pack() 
          screen4.create_text(190,110,text=Your Out of the sea!!,font=('courier',15),fill='black')
          screen4.mainloop()
     else:
          Button(window, text="*", width=8,height=4,bg=sky).grid(row=int(x)+1, column=y, columnspan=1)'''

 
def about(): 
     screen1=Tk() 
     screen1.title("About The Game") 
     screen1=Canvas(screen1,width=1500,height=800,bg='light green') 
     screen1.pack()
     screen1.create_text(640,300,text='''\t\tDescription of the game:
               The game of Battleship is played on two square grids, one for each player. 
               The grids are typically 8x8, and each square is identified by a letter and 
               number coordinate. Before the game  begins, each player secretly  arranges 
               their ships on their grid. The ships come in three different types: 
               Battleship (3 squares), Submarine (2 squares), and  Patrol Boat (1 square). 
               The number of ships of each type is the same for both players.
               The ships must be placed so that they do not overlap, and each ship occupies
               a consecutive set of  squares  either  horizontally  or vertically. Once all 
               ships are placed, the  game begins  with  each player taking turns trying to 
               guess the location of their opponent's ships by  calling out  coordinates on 
               the grid. A hit is scored if the guess lands on a square occupied  by a ship, 
               and the player who sinks all of their opponent's ships first wins the game.
    ''',font=('courier',20),fill='black') 

     
     
def play(): 
    screen1=Tk() 
    screen1.title("How To Play") 
    screen1=Canvas(screen1,width=1500,height=800,bg='light green') 
    screen1.pack()
    screen1.create_text(640,300,text='''\t\tHow To Play: 
             After the ships have been positioned, the game proceeds in a series of rounds.
             In  each  round, each  player takes a turn to announce a target square in the
             opponent's grid which is to be shot at. When all of the squares of a ship have 
             been hit, the ship's owner announces the sinking of the BATTLESHIP, SUBMARINE/
             PATROL BOAT, or the titular Battleship. If a player's ships have been sunk,the 
             game is over and their opponent wins. the who gets 6 points first wins the game.''',font=('courier',20),fill='black') 

def main_screen(): 
    global screen
    screen=Tk() 
    screen.geometry("1500x1500") 
    screen.title("BATTLESHIP")
    screen.configure(background='maroon')         

    Label(text = "**SHIPS ON FIRE**",bg="orange",width= '300',height= '2',font= ("Algerian",20)).pack() 
    Label(text = "",bg="maroon").pack() 
    Button(text = "Login",height= '2',width= "30",bg="pink",command = Login).pack() 
    Label(text = "",bg="maroon").pack() 
    Button(text = "Register",height= '2',width= '30',bg="pink", command = Register).pack() 
    Label(text = "",bg="maroon").pack() 
    Button(text = "About The Game",height= '2',width= "30",bg="pink",command = about).pack() 
    Label(text = "",bg="maroon").pack() 
    Button(text ="How To Play",width ='30',height = '2',bg="pink",command=play).pack() 
    #Label(text = "",bg="maroon").pack() 

    '''global photol 
    photol=Toplevel(screen) 
    photol.geometry("1500x800") '''
    '''photol=PhotoImage(file="I:/Screenshot (2).png") 
    labelphotol=Label(screen,image=photol) 
    labelphotol.image=photol 
    labelphotol.pack()'''

    screen.mainloop() 
main_screen()

     
'''
op = 'y'
while op == 'y':
     print('1. Register')
     print('2. LOgin')
     a = int(input('Enter option'))
     if a == 1:
          Register()
     else:
          Login()
     op=input('y to continue')
Button(tk, height=1, width=10, text="Sign Up", 
                    command=lambda: Register()).place(x=200,y=130)
     
Button(tk, height=1, width=10, text="Login",
       
                    command=lambda: Login()).place(x=200,y=180)
Button(tk, height=1, width=11, text="ABOUT THE GAME", 
                    command=lambda: about()).place(x=200,y=230)
     
Button(tk, height=1, width=10, text="HOW TO PLAY", 
                    command=lambda: play()).place(x=200,y=280)'''