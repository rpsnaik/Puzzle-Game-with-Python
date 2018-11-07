from tkinter import *
from random import *
from datetime import datetime
import sqlite3
import os
global str
connection = sqlite3.connect('users.db')
c = connection.cursor()
#c.execute('CREATE TABLE user(id number, score number)')
class game:
    def __init__(self,g):
        self.g = g
        if(self.g == 1):
            logfile.writelines(time() + "Got inside of class and If condition \n")
            os.popen("cd game1 && npm start") 
        elif(self.g == 2):
            logicx = ""
            logicy = ""
            logicxlist = []
            logicylist = []
            coll = [];
            def bg1f():
                logicx = "1"
                logicy = "1"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg1.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg2f():
                logicx = "1"
                logicy = "2"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg2.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg3f():
                logicx = "1"
                logicy = "3"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg3.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg4f():
                logicx = "1"
                logicy = "4"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg4.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg5f():
                logicx = "1"
                logicy = "5"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg5.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg6f():
                logicx = "1"
                logicy = "6"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg6.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg7f():
                logicx = "1"
                logicy = "7"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg7.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg8f():
                logicx = "1"
                logicy = "8"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg8.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg9f():
                logicx = "2"
                logicy = "1"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg9.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg10f():
                logicx = "2"
                logicy = "2"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg10.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg11f():
                logicx = "2"
                logicy = "3"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg11.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg12f():
                logicx = "2"
                logicy = "4"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg12.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg13f():
                logicx = "2"
                logicy = "5"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg13.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg14f():
                logicx = "2"
                logicy = "6"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg14.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg15f():
                logicx = "2"
                logicy = "7"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg15.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg16f():
                logicx = "2"
                logicy = "8"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg16.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg17f():
                logicx = "3"
                logicy = "1"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg17.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg18f():
                logicx = "3"
                logicy = "2"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg18.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg19f():
                logicx = "3"
                logicy = "3"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg19.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg20f():
                logicx = "3"
                logicy = "4"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg20.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg21f():
                logicx = "3"
                logicy = "5"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg21.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg22f():
                logicx = "3"
                logicy = "6"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg22.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg23f():
                logicx = "3"
                logicy = "7"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg23.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg24f():
                logicx = "3"
                logicy = "8"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg24.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg25f():
                logicx = "4"
                logicy = "1"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg25.cget('text'))
                print(coll)
                wrds.configure(text = "Words : "+ str(coll))
                wrds1.configure(text="")

            def bg26f():
                logicx = "4"
                logicy = "2"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg26.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg27f():
                logicx = "4"
                logicy = "3"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg27.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg28f():
                logicx = "4"
                logicy = "4"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg28.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg29f():
                logicx = "4"
                logicy = "5"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg29.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg30f():
                logicx = "4"
                logicy = "6"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg30.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg31f():
                logicx = "4"
                logicy = "7"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg31.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg32f():
                logicx = "4"
                logicy = "8"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg32.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg33f():
                logicx = "5"
                logicy = "1"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg33.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg34f():
                logicx = "5"
                logicy = "2"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg34.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
            
            def bg35f():
                logicx = "5"
                logicy = "3"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg35.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg36f():
                logicx = "5"
                logicy = "4"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg36.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg37f():
                logicx = "5"
                logicy = "5"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg37.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg38f():
                logicx = "5"
                logicy = "6"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg38.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg39f():
                logicx = "5"
                logicy = "7"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg39.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg40f():
                logicx = "5"
                logicy = "8"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg40.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg41f():
                logicx = "6"
                logicy = "1"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg41.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg42f():
                logicx = "6"
                logicy = "2"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg42.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg43f():
                logicx = "6"
                logicy = "3"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg43.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg44f():
                logicx = "6"
                logicy = "4"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg44.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg45f():
                logicx = "6"
                logicy = "5"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg45.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg46f():
                logicx = "6"
                logicy = "6"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg46.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg47f():
                logicx = "6"
                logicy = "7"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg47.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg48f():
                logicx = "6"
                logicy = "8"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg48.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg49f():
                logicx = "7"
                logicy = "1"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg49.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg50f():
                logicx = "7"
                logicy = "2"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg50.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg51f():
                logicx = "7"
                logicy = "3"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg51.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg52f():
                logicx = "7"
                logicy = "4"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg52.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg53f():
                logicx = "7"
                logicy = "5"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg53.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg54f():
                logicx = "7"
                logicy = "6"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg54.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg55f():
                logicx = "7"
                logicy = "7"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg55.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg56f():
                logicx = "7"
                logicy = "8"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg56.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg57f():
                logicx = "8"
                logicy = "1"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg57.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg58f():
                logicx = "8"
                logicy = "2"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg58.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg59f():
                logicx = "8"
                logicy = "3"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg59.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg60f():
                logicx = "8"
                logicy = "4"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg60.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg61f():
                logicx = "8"
                logicy = "5"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg61.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg62f():
                logicx = "8"
                logicy = "6"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg62.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")
            
            def bg63f():
                logicx = "8"
                logicy = "7"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg63.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            def bg64f():
                logicx = "8"
                logicy = "8"
                logicxlist.append(logicx)
                logicylist.append(logicy)
                coll.append(bg64.cget('text'))
                print(coll)
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")



            logfile.writelines(time() + "Got inside the class and the If condition \n")
            game2 = Tk()
            game2.geometry('1920x1080')
            game2.configure(background="#59a79a")
            lr1 = Label(game2, text="THE PUZZLE GAME", bg="#4285F4", width="125", fg="#fff", padx="20", pady="20")
            lr1.configure(font=("segoe ui", 15, 'bold'))
            lr1.grid(row=0, columnspan=12)
            bg1 = Button(game2,text="Z", command=bg1f, fg="#fff",bg="#006dcc",padx="25", pady="10", border="1",relief=GROOVE)
            bg1.config(font=("segoe ui", 13))
            bg1.grid(row=1,column=1)
            bg2 = Button(game2,text="B", fg="#fff", command=bg2f, bg="#006dcc",padx="26", pady="10", border="1",relief=GROOVE)
            bg2.config(font=("segoe ui", 13))
            bg2.grid(row=1,column=2)
            bg3 = Button(game2,text="P", fg="#fff", command=bg3f, bg="#006dcc",padx="26", pady="10", border="1",relief=GROOVE)
            bg3.config(font=("segoe ui", 13))
            bg3.grid(row=1,column=3)
            bg4 = Button(game2,text="Y", fg="#fff" , command=bg4f,bg="#006dcc",padx="26", pady="10", border="1",relief=GROOVE)
            bg4.config(font=("segoe ui", 13))
            bg4.grid(row=1,column=4)
            bg5 = Button(game2,text="T", fg="#fff", command=bg5f, bg="#006dcc",padx="25", pady="10", border="1",relief=GROOVE)
            bg5.config(font=("segoe ui", 13))
            bg5.grid(row=1,column=5)
            bg6 = Button(game2,text="H", fg="#fff", command=bg6f,bg="#006dcc",padx="25", pady="10", border="1",relief=GROOVE)
            bg6.config(font=("segoe ui", 13))
            bg6.grid(row=1,column=6)
            bg7 = Button(game2,text="O", fg="#fff", command=bg7f,bg="#006dcc",padx="25", pady="10", border="1",relief=GROOVE)
            bg7.config(font=("segoe ui", 13))
            bg7.grid(row=1,column=7)
            bg8 = Button(game2,text="N", fg="#fff", command=bg8f,bg="#006dcc",padx="25", pady="10", border="1",relief=GROOVE)
            bg8.config(font=("segoe ui", 13))
            bg8.grid(row=1,column=8)

            bg9 = Button(game2,text="A", fg="#fff",command=bg9f,bg="#006dcc",padx="24", pady="10", border="1",relief=GROOVE)
            bg9.config(font=("segoe ui", 13))
            bg9.grid(row=2,column=1)
            bg10 = Button(game2,text="M", fg="#fff",command=bg10f,bg="#006dcc",padx="25", pady="10", border="1",relief=GROOVE)
            bg10.config(font=("segoe ui", 13))
            bg10.grid(row=2,column=2)
            bg11 = Button(game2,text="T", fg="#fff",command=bg11f,bg="#006dcc",padx="25", pady="10", border="1",relief=GROOVE)
            bg11.config(font=("segoe ui", 13))
            bg11.grid(row=2,column=3)
            bg12 = Button(game2,text="B", fg="#fff",command=bg12f,bg="#006dcc",padx="25", pady="10", border="1",relief=GROOVE)
            bg12.config(font=("segoe ui", 13))
            bg12.grid(row=2,column=4)
            bg13 = Button(game2,text="O", fg="#fff",bg="#006dcc",command=bg13f,padx="25", pady="10", border="1",relief=GROOVE)
            bg13.config(font=("segoe ui", 13))
            bg13.grid(row=2,column=5)
            bg14 = Button(game2,text="O", fg="#fff",bg="#006dcc",padx="25",command=bg14f, pady="10", border="1",relief=GROOVE)
            bg14.config(font=("segoe ui", 13))
            bg14.grid(row=2,column=6)
            bg15 = Button(game2,text="K", fg="#fff",bg="#006dcc",padx="25",command=bg15f, pady="10", border="1",relief=GROOVE)
            bg15.config(font=("segoe ui", 13))
            bg15.grid(row=2,column=7)
            bg16 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25",command=bg16f, pady="10", border="1",relief=GROOVE)
            bg16.config(font=("segoe ui", 13))
            bg16.grid(row=2,column=8)

            bg17 = Button(game2,text="J", fg="#fff",bg="#006dcc",padx="27",command=bg17f, pady="10", border="1",relief=GROOVE)
            bg17.config(font=("segoe ui", 13))
            bg17.grid(row=3,column=1)
            bg18 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25",command=bg18f ,pady="10", border="1",relief=GROOVE)
            bg18.config(font=("segoe ui", 13))
            bg18.grid(row=3,column=2)
            bg19 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25",command=bg19f , pady="10", border="1",relief=GROOVE)
            bg19.config(font=("segoe ui", 13))
            bg19.grid(row=3,column=3)
            bg20 = Button(game2,text="Q", fg="#fff",bg="#006dcc",padx="25",command=bg20f , pady="10", border="1",relief=GROOVE)
            bg20.config(font=("segoe ui", 13))
            bg20.grid(row=3,column=4)
            bg21 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25",command=bg21f ,pady="10", border="1",relief=GROOVE)
            bg21.config(font=("segoe ui", 13))
            bg21.grid(row=3,column=5)
            bg22 = Button(game2,text="D", fg="#fff",bg="#006dcc",padx="25",command=bg22f ,pady="10", border="1",relief=GROOVE)
            bg22.config(font=("segoe ui", 13))
            bg22.grid(row=3,column=6)
            bg23 = Button(game2,text="L", fg="#fff",bg="#006dcc",padx="25",command=bg23f ,pady="10", border="1",relief=GROOVE)
            bg23.config(font=("segoe ui", 13))
            bg23.grid(row=3,column=7)
            bg24 = Button(game2,text="I", fg="#fff",bg="#006dcc",padx="25",command=bg24f ,pady="10", border="1",relief=GROOVE)
            bg24.config(font=("segoe ui", 13))
            bg24.grid(row=3,column=8)

            bg25 = Button(game2,text="E", fg="#fff",bg="#006dcc",padx="25",command=bg25f ,pady="10", border="1",relief=GROOVE)
            bg25.config(font=("segoe ui", 13))
            bg25.grid(row=4,column=1)
            bg26 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg26f ,border="1",relief=GROOVE)
            bg26.config(font=("segoe ui", 13))
            bg26.grid(row=4,column=2)
            bg27 = Button(game2,text="C", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg27f ,border="1",relief=GROOVE)
            bg27.config(font=("segoe ui", 13))
            bg27.grid(row=4,column=3)
            bg28 = Button(game2,text="O", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg28f ,border="1",relief=GROOVE)
            bg28.config(font=("segoe ui", 13))
            bg28.grid(row=4,column=4)
            bg29 = Button(game2,text="D", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg29f ,border="1",relief=GROOVE)
            bg29.config(font=("segoe ui", 13))
            bg29.grid(row=4,column=5)
            bg30 = Button(game2,text="E", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg30f ,border="1",relief=GROOVE)
            bg30.config(font=("segoe ui", 13))
            bg30.grid(row=4,column=6)
            bg31 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg31f,border="1",relief=GROOVE)
            bg31.config(font=("segoe ui", 13))
            bg31.grid(row=4,column=7)
            bg32 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg32f,border="1",relief=GROOVE)
            bg32.config(font=("segoe ui", 13))
            bg32.grid(row=4,column=8)

            bg33 = Button(game2,text="T", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg33f, border="1",relief=GROOVE)
            bg33.config(font=("segoe ui", 13))
            bg33.grid(row=5,column=1)
            bg34 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg34f, border="1",relief=GROOVE)
            bg34.config(font=("segoe ui", 13))
            bg34.grid(row=5,column=2)
            bg35 = Button(game2,text="P", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg35f, border="1",relief=GROOVE)
            bg35.config(font=("segoe ui", 13))
            bg35.grid(row=5,column=3)
            bg36 = Button(game2,text="E", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg36f,border="1",relief=GROOVE)
            bg36.config(font=("segoe ui", 13))
            bg36.grid(row=5,column=4)
            bg37 = Button(game2,text="N", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg37f,border="1",relief=GROOVE)
            bg37.config(font=("segoe ui", 13))
            bg37.grid(row=5,column=5)
            bg38 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg38f,border="1",relief=GROOVE)
            bg38.config(font=("segoe ui", 13))
            bg38.grid(row=5,column=6)
            bg39 = Button(game2,text="R", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg39f, border="1",relief=GROOVE)
            bg39.config(font=("segoe ui", 13))
            bg39.grid(row=5,column=7)
            bg40 = Button(game2,text="H", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg40f,border="1",relief=GROOVE)
            bg40.config(font=("segoe ui", 13))
            bg40.grid(row=5,column=8)
            
            bg41 = Button(game2,text="S", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg41f, border="1",relief=GROOVE)
            bg41.config(font=("segoe ui", 13))
            bg41.grid(row=6,column=1)
            bg42 = Button(game2,text="H", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg42f, border="1",relief=GROOVE)
            bg42.config(font=("segoe ui", 13))
            bg42.grid(row=6,column=2)
            bg43 = Button(game2,text="L", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg43f,border="1",relief=GROOVE)
            bg43.config(font=("segoe ui", 13))
            bg43.grid(row=6,column=3)
            bg44 = Button(game2,text="I", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg44f, border="1",relief=GROOVE)
            bg44.config(font=("segoe ui", 13))
            bg44.grid(row=6,column=4)
            bg45 = Button(game2,text="O", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg45f, border="1",relief=GROOVE)
            bg45.config(font=("segoe ui", 13))
            bg45.grid(row=6,column=5)
            bg46 = Button(game2,text="E", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg46f, border="1",relief=GROOVE)
            bg46.config(font=("segoe ui", 13))
            bg46.grid(row=6,column=6)
            bg47 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg47f, border="1",relief=GROOVE)
            bg47.config(font=("segoe ui", 13))
            bg47.grid(row=6,column=7)
            bg48 = Button(game2,text="N", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg48f, border="1",relief=GROOVE)
            bg48.config(font=("segoe ui", 13))
            bg48.grid(row=6,column=8)

            bg49 = Button(game2,text="Y", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg49f, border="1",relief=GROOVE)
            bg49.config(font=("segoe ui", 13))
            bg49.grid(row=7,column=1)
            bg50 = Button(game2,text="I", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg50f, border="1",relief=GROOVE)
            bg50.config(font=("segoe ui", 13))
            bg50.grid(row=7,column=2)
            bg51 = Button(game2,text="Q", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg51f, border="1",relief=GROOVE)
            bg51.config(font=("segoe ui", 13))
            bg51.grid(row=7,column=3)
            bg52 = Button(game2,text="K", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg52f, border="1",relief=GROOVE)
            bg52.config(font=("segoe ui", 13))
            bg52.grid(row=7,column=4)
            bg53 = Button(game2,text="X", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg53f, border="1",relief=GROOVE)
            bg53.config(font=("segoe ui", 13))
            bg53.grid(row=7,column=5)
            bg54 = Button(game2,text="M", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg54f, border="1",relief=GROOVE)
            bg54.config(font=("segoe ui", 13))
            bg54.grid(row=7,column=6)
            bg55 = Button(game2,text="A", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg55f, border="1",relief=GROOVE)
            bg55.config(font=("segoe ui", 13))
            bg55.grid(row=7,column=7)
            bg56 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg56f, border="1",relief=GROOVE)
            bg56.config(font=("segoe ui", 13))
            bg56.grid(row=7,column=8)

            bg57 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg57f, border="1",relief=GROOVE)
            bg57.config(font=("segoe ui", 13))
            bg57.grid(row=8,column=1)
            bg58 = Button(game2,text="A", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg58f, border="1",relief=GROOVE)
            bg58.config(font=("segoe ui", 13))
            bg58.grid(row=8,column=2)
            bg59 = Button(game2,text="C", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg59f, border="1",relief=GROOVE)
            bg59.config(font=("segoe ui", 13))
            bg59.grid(row=8,column=3)
            bg60 = Button(game2,text="K", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg60f, border="1",relief=GROOVE)
            bg60.config(font=("segoe ui", 13))
            bg60.grid(row=8,column=4)
            bg61 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg61f, border="1",relief=GROOVE)
            bg61.config(font=("segoe ui", 13))
            bg61.grid(row=8,column=5)
            bg62 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg62f, border="1",relief=GROOVE)
            bg62.config(font=("segoe ui", 13))
            bg62.grid(row=8,column=6)
            bg63 = Button(game2,text="G", fg="#fff",bg="#006dcc",padx="25", pady="10", command=bg63f,border="1",relief=GROOVE)
            bg63.config(font=("segoe ui", 13))
            bg63.grid(row=8,column=7)
            bg64 = Button(game2,text="B", fg="#fff",bg="#006dcc",padx="25", pady="10",command=bg64f, border="1",relief=GROOVE)
            bg64.config(font=("segoe ui", 13))
            bg64.grid(row=8,column=8)

            dash = Label(game2, text="Dashboard : ", fg="#fff",bg="#59a79a", padx="50")
            dash.config(font=("segoe ui", 20))
            dash.grid(row=1,column=10)

            wrds = Label(game2, text="Words : ", fg="#fff",bg="#59a79a",width="60")
            wrds.config(font=("segoe ui", 14))
            wrds.grid(row=2,column=10)

            wrds3 = Label(game2, text="Score : ", fg="#fff", bg="#59a79a", padx="50")
            wrds3.config(font=("segoe ui", 14))
            wrds3.grid(row=3, column=10)
            wrds4 = Label(game2, text="", fg="#fff", bg="#59a79a", padx="50")
            wrds4.config(font=("segoe ui", 14))
            wrds4.grid(row=4, column=10)

            def checking():
                str=""
                c.execute('SELECT score FROM user')
                data=c.fetchall()
                print(data)
                for datascore in data:
                    for finaldata in datascore:
                        print(finaldata)
                        score = finaldata


                for i in coll:
                    str=str+i
                print(str)
                coll.clear()
                print(logicxlist)
                print(logicylist)
                strlogicxlist = ''.join(logicxlist)
                strlogicylist = ''.join(logicylist)
                if((strlogicxlist == "2222" or strlogicxlist == "111111" or strlogicxlist=="555" or strlogicxlist=="4444" or strlogicxlist=="8888") or (strlogicylist == "777" or strlogicylist == "111")):
                    strlogicxlist = ""
                    logicxlist.clear()
                    if str == "BOOK":
                        wrds1.configure(text="Response : Correct")
                        str == ""
                        coll.clear()
                        score = score+10
                        print(score)
                        listdata = [score, 0]
                        c.execute('UPDATE user SET score=? WHERE id=?',listdata)
                        connection.commit()
                        wrds4.configure(text=score)
                        logicxlist.clear()
                        logicylist.clear()


                    elif str == "PYTHON":
                        wrds1.configure(text="Response : Correct")
                        str == ""
                        coll.clear()
                        score = score + 10
                        print(score)
                        listdata = [score, 0]
                        c.execute('UPDATE user SET score=? WHERE id=?', listdata)
                        connection.commit()
                        wrds4.configure(text=score)
                        logicxlist.clear()
                        logicylist.clear()

                    elif str == "BAG":
                        wrds1.configure(text="Response : Correct")
                        str == ""
                        coll.clear()
                        score = score + 10
                        print(score)
                        listdata = [score, 0]
                        c.execute('UPDATE user SET score=? WHERE id=?', listdata)
                        connection.commit()
                        wrds4.configure(text=score)
                        logicxlist.clear()
                        logicylist.clear()

                    elif str == "JET":
                        wrds1.configure(text="Response : Correct")
                        str == ""
                        coll.clear()
                        score = score + 10
                        print(score)
                        listdata = [score, 0]
                        c.execute('UPDATE user SET score=? WHERE id=?', listdata)
                        connection.commit()
                        wrds4.configure(text=score)
                        logicxlist.clear()
                        logicylist.clear()

                    elif str == "PEN":
                        wrds1.configure(text="Response : Correct")
                        str == ""
                        coll.clear()
                        score = score + 10
                        print(score)
                        listdata = [score, 0]
                        c.execute('UPDATE user SET score=? WHERE id=?', listdata)
                        connection.commit()
                        wrds4.configure(text=score)
                        logicxlist.clear()
                        logicylist.clear()

                    elif str == "CODE":
                        wrds1.configure(text="Response : Correct")
                        str == ""
                        coll.clear()
                        score = score + 10
                        print(score)
                        listdata = [score, 0]
                        c.execute('UPDATE user SET score=? WHERE id=?', listdata)
                        connection.commit()
                        wrds4.configure(text=score)
                        logicxlist.clear()
                        logicylist.clear()

                    elif str == "BACK":
                        wrds1.configure(text="Response : Correct")
                        str == ""
                        coll.clear()
                        score = score + 10
                        print(score)
                        listdata = [score, 0]
                        c.execute('UPDATE user SET score=? WHERE id=?', listdata)
                        connection.commit()
                        wrds4.configure(text=score)
                        logicxlist.clear()
                        logicylist.clear()
                else:
                    strlogicxlist = ""
                    logicxlist.clear()
                    logicylist.clear()
                    wrds1.configure(text="Response : Not of Same Line or Correct word")


                
            def reset():
                str == ""
                coll.clear()
                wrds.configure(text="Words : " + str(''.join(coll)))
                wrds1.configure(text="")

            chb = Button(game2,text="Check",fg="#fff", command=checking, bg="#333",padx="5", pady="5",relief=GROOVE, border="1",width="10" )
            chb.config(font=("segoe ui", 14))
            chb.grid(row=5,column=10)
            chb1 = Button(game2, text="Reset", fg="#fff", command=reset, bg="red", padx="5", pady="5", relief=GROOVE,border="1", width="10")
            chb1.config(font=("segoe ui", 14))
            chb1.grid(row=6, column=10)

            wrds1 = Label(game2, text="Response : Not Checked Yet", fg="#fff",bg="#59a79a", padx="50")
            wrds1.config(font=("segoe ui", 14))
            wrds1.grid(row=7,column=10)

            game2.mainloop()
            

            
    


def time():
    return("[" + str(datetime.now()) + "] : ")

logfile = open("log.txt","w")
logfile.writelines(time()+"Starting the Game \n")

def randgame():
    randval = int(random()*10)
    if(randval < 3 and randval > 0):
        print("Got it its "+ str(randval))
        logfile.writelines(time()+"Got it its "+ str(randval) + "\n")
        print("Launching Game no : " + str(randval))
        logfile.writelines(time()+ "Launching Game no : " + str(randval) + "\n")
        ga = game(randval)
        print(ga.g)
    else:
        print("Not Got ... Finding again ... ")
        logfile.writelines(time()+"Not Got ... Finding again ... \n")
        randgame()
def startnew():
    print("Starting a new Game")
    logfile.writelines(time()+"Starting a new Game \n")
    print("Getting a Random Game")
    logfile.writelines(time()+"Getting a Random Game \n")
    score = 0
    listdata = [score, 0]
    c.execute('UPDATE user SET score=? WHERE id=?', listdata)
    connection.commit()
    randgame()


def contin():
    print("Continuing the Exisiting Game .. ")
    ga4 = game(2)

def allgames():
    print("All Games")
    allgamesgui = Tk()
    allgamesgui.geometry("1920x1080")
    allgamesgui.configure(background='#333')
    lr12 = Label(allgamesgui, text="THE PUZZLE GAME", bg="#4285F4", width="125", fg="#fff", padx="20", pady="20")
    lr12.configure(font=("segoe ui", 15, 'bold'))
    lr12.grid(row=0, columnspan=12)
    def pygame():
        ga1 = game(2)
    def elgame():
        ga2 = game(1)
    g1 = Button(allgamesgui, text="Python Game", command=pygame)
    g1.configure(font=('segoe ui', 30, 'bold') , bg="#59a79a")
    g1.grid(row=4, column=3)

    g2 = Button(allgamesgui, text="Electron Game")
    g2.configure(font=('segoe ui', 30, 'bold'), bg="#59a79a", command=elgame)
    g2.grid(row=4, column=6)
    allgamesgui.mainloop()

def ex():
    print("Exit")
    logfile.writelines(time()+"Exit \n")
    logfile.close()
    root.destroy()
root = Tk()

'''The Main Bar '''
root.geometry("1920x1080")
root.configure(background='#333')
lr = Label(root,text="THE PUZZLE GAME", bg="#4285F4",width="125", fg="#fff", padx="20", pady="20")
lr.configure(font=("segoe ui", 15,'bold'))
lr.grid(row=0,columnspan=12)

'''The Navigation Bar'''
l1r = Label(root,text="Game Options : ", fg="#fff",bg="#333", pady="30")
l1r.config(font=("segoe ui", 25))
l1r.grid(row=1,column=2)

c.execute('SELECT score FROM user')
data=c.fetchall()
print(data)
for datascore in data:
    for finaldata in datascore:
        print(finaldata)
        score = finaldata



l2r = Label(root,text="Score : ", fg="#fff",bg="#333", pady="30")
l2r.config(font=("segoe ui", 25))
l2r.grid(row=7,column=2)
l2r.configure(text="High Scores Till Now : "+str(score))

l3r = Label(root,text="\u00A9 Copy right Ashok,Rahul ,R P S Naik", fg="#fff",bg="#333", pady="30")
l3r.config(font=("segoe ui", 15))
l3r.grid(row=10,column=2)
l3r = Label(root,text="\u00AE All rights reserved 2018", fg="#fff",bg="#333", pady="30")
l3r.config(font=("segoe ui", 15))
l3r.grid(row=11,column=2)

b1 = Button(root,text="Start a New Game", command = startnew, fg="#fff",bg="#006dcc",padx="10", pady="10",relief=GROOVE, border="1",width="30" )
b1.config(font=("segoe ui", 13))
b1.grid(row=2,column=4)

b2 = Button(root,text="Continue", command = contin, fg="#fff",bg="#006dcc",padx="10", pady="10", border="1",relief=GROOVE,width="30")
b2.config(font=("segoe ui", 13))
b2.grid(row=3,column=4)

b3 = Button(root,text="All Random Games", command = allgames, fg="#fff",bg="#006dcc",padx="10", pady="10", border="1",relief=GROOVE,width="30")
b3.config(font=("segoe ui", 13))
b3.grid(row=4,column=4)

b4 = Button(root,text="Exit", command = ex, fg="#fff",bg="#006dcc",padx="10", pady="10", border="1",relief=GROOVE,width="30")
b4.config(font=("segoe ui", 13))
b4.grid(row=5,column=4)
root.mainloop()

