import tkinter  
import datetime  
import time
import tkinter as tk
import vlc

Clock = tkinter.Tk()
Clock.title("Yourself")
Clock.geometry("400x300+1000+10")

WINwidth = 800  
WINcolor = 'pink'  
WINheight = WINwidth  

w = tkinter.Canvas(Clock, width=WINwidth, height=WINheight, background=WINcolor)
w.place(x=0, y=0)
w.pack()
p = vlc.MediaPlayer()

def wake():
    now = datetime.datetime.now()
    now += datetime.timedelta(seconds=10)
    return now

def drawing():
    btn1 = tkinter.Button(Clock, text='Sweet dreams',command=call_btn)
    btn1.place(x=70, y=190)
    btn2 = tkinter.Button(Clock, text="Don't Wake me up",command=delate_btn)
    btn2.place(x=200, y=190)


    while True:
            now = wake()  
            if now.hour > 24:  
                nowhour = now.hour - 24
            else:
                nowhour = now.hour

            FontSize=60
            nowhour = nowhour + now.minute / 60 + now.second / 3600  
            nowminute = now.minute + now.second / 60
            w.create_text(190,150, text = wake().strftime('%H:%M:%S'), font = ("", int(FontSize)), tag="Y")  #年月日時分秒
            w.create_text(190,100, text="Sweet dreams", font=("Helvetica", 50, "bold"), fill='#5e95ed')

            w.update()  
            w.delete("Y")
            time.sleep(0.1) 


def call_btn():
    get_up=wake()
    p.set_mrl("desktop/nemuke/Alone.mp3")
    print("設定しました！")
    flg = True
    while flg:
        if get_up == datetime.datetime.now():
            p.play()
            flg = False

def delate_btn():
    print("削除しました！")
    p.stop()


def main():
    drawing()

if __name__ == '__main__':
    main()
