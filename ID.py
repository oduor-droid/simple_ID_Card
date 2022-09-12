from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Kenya National ID.")
root.geometry('500x280')
root.resizeable(False, False)


heading = Label(root, font=('Terminal', 15), text='Republic of Kenya')
heading.pack()

serial = Label(root, font=('Terminal', 10), text='Serial number: 304567', )
serial.place(x=30, y=30)

Id = Label(root, font=('Terminal', 10), text='Id number: 304567')
Id.place(x=350, y=30)

fnLabel = Label(root, font=('Terminal', 7), text='Full name;', pady=3)
fnLabel.place(x=30, y=45)

name = Label(root, font=('Terminal', 10), text='Bill Clinton Jordan')
name.place(x=30, y=60)

photo =ImageTk.PhotoImage(Image.open("/home/oduor/Pictures/e2.jpg").resize((150, 180), Image.ANTIALIAS))
photoLabel = Label(image=photo)
photoLabel.place(x=30, y=80)

seal = ImageTk.PhotoImage(Image.open("/home/oduor/Pictures/coat-of-arms-of-kenya.jpg").resize((50, 50), Image.ANTIALIAS))
seaLabel = Label(image=seal)
seaLabel.place(x=250, y=25)

thumb = ImageTk.PhotoImage(Image.open("/home/oduor/Pictures/thumb.jpeg").resize((70, 70), Image.ANTIALIAS))
thumbLabel = Label(image=thumb)
thumbLabel.place(x=420, y=200)

DoB = Label(root, font=('Terminal', 7), text='Date of Birth;', pady=3)
DoB.place(x=200, y=80)
Date = Label(root, font=('Terminal', 10), text='07-02-2000 ')
Date.place(x=200, y=100)

Sex = Label(root, font=('Terminal', 7), text='Sex;', pady=3)
Sex.place(x=200, y=120)
SAB = Label(root, font=('Terminal', 10), text='MALE')
SAB.place(x=200, y=140)

DistOB = Label(root, font=('Terminal', 7), text='District of Birth;', pady=3)
DistOB.place(x=200, y=160)
District = Label(root, font=('Terminal', 10), text='HOMABAY')
District.place(x=200, y=180)

POI = Label(root, font=('Terminal', 7), text='Place Of Issue;', pady=3)
POI.place(x=200, y=200)
PlaceI = Label(root, font=('Terminal', 10), text='EMBAKASI')
PlaceI.place(x=200, y=220)

DoI = Label(root, font=('Terminal', 7), text='Date Of Issue;', pady=3)
DoI.place(x=200, y= 240)
date = Label(root, font=('Terminal', 10), text='29.01.2019')
date.place(x=200, y=260)


root.mainloop()
