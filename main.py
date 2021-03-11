from tkinter import *
import cv2
import threading
import time
from PIL import Image,ImageTk
import imutils
from functools import partial

HEIGHT=348
WIDTH=600

stream=cv2.VideoCapture('video.mp4')
def play(speed):
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame=stream.read()
    if not grabbed:
        exit(0)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor='nw')
    canvas.create_text(134,26,text='Decision Pending',fill='black',font='Times 26 bold')
def pending(decision):
    frame=cv2.cvtColor(cv2.imread('decision.png'),cv2.COLOR_RGB2YCrCb)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor='nw')
    time.sleep(2)
    frame=cv2.cvtColor(cv2.imread('sponser.png'),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor='nw')
    time.sleep(2)
    if decision=='OUT':
        decision_img='out.png'
    else:
        decision_img='not-out.png'
    frame=cv2.cvtColor(cv2.imread(decision_img),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=WIDTH,height=HEIGHT)
    frame=ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor='nw')
def out():
    thread=threading.Thread(target=pending,args=('OUT',))
    thread.daemon=1
    thread.start()
def notout():
    thread=threading.Thread(target=pending,args=('NOTOUT',))
    thread.daemon=1
    thread.start()

root=Tk()
root.title('Review System by Hiten')
frame1=cv2.cvtColor(cv2.imread('bg.png'),cv2.COLOR_BGR2RGB)
frame1=ImageTk.PhotoImage(image=Image.fromarray(frame1))
canvas=Canvas(root,width=WIDTH,height=HEIGHT)
img=canvas.create_image(0,0,image=frame1,anchor='nw')
canvas.pack()
Button(root,text='<< Previous(fast)',width=50,command=partial(play,-25)).pack()
Button(root,text='< Previous(slow)',width=50,command=partial(play,-5)).pack()
Button(root,text='Next(fast) >>',width=50,command=partial(play,25)).pack()
Button(root,text='Next(slow) >',width=50,command=partial(play,5)).pack()
Button(root,text='Out',width=50,command=out).pack()
Button(root,text='Not Out',width=50,command=notout).pack()

root.mainloop()