from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download() / (10**6), 3)) + "Mbps"
    upload = str(round(sp.upload() / (10**6), 3)) + "Mbps"
    down_l.config(text=download)
    upload_l.config(text=upload)
    ping.config(text=ping)

sp = Tk()
sp.title("Internet Speed Checker")
sp.geometry("500x500")
sp.config(bg="skyblue")
label = Label(sp,
              text="Internet Speed Checker",
              font=("Time New Roman", 20, "bold"),
              bg="skyblue",
              fg="white")
label.place(x=60, y=40, height=50, width=380)

label = Label(sp, text="Download Speed", font=("Time New Roman", 20, "bold"))
label.place(x=60, y=130, height=50, width=380)

down_l = Label(sp, text="00", font=("Time New Roman", 20, "bold"))
down_l.place(x=60, y=200, height=50, width=380)

label = Label(sp, text="Upload Speed", font=("Time New Roman", 20, "bold"))
label.place(x=60, y=290, height=50, width=380)

upload_l = Label(sp, text="00", font=("Time New Roman", 20, "bold"))
upload_l.place(x=60, y=360, height=50, width=380)

button = Button(sp,
                text="Check Speed",
                font=("Time New Roman", 20, "bold"),
                bg="skyblue",
                relief=RAISED,
                cursor="hand2",
                command=speedcheck)
button.place(x=140, y=420, height=30, width=200)

sp.mainloop()
