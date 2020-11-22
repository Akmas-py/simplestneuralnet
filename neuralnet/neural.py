import random
from tkinter import *
window = Tk()  
window.title("Perciptron")  
window.geometry('400x300')
p = 0
while p == 0:
    p = p + 1
    a = int(input("First data: "))
    b = int(input("Second data: "))


    i = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0


    x1 = random.randint(-5, 5)
    y1 = random.randint(-5, 5)
    z1 = random.randint(-5, 5)
    c1 = random.randint(-5, 5)

    x2 = random.randint(-5, 5)
    y2 = random.randint(-5, 5)
    z2 = random.randint(-5, 5)
    c2 = random.randint(-5, 5)

    x3 = random.randint(-5, 5)
    y3 = random.randint(-5, 5)
    z3 = random.randint(-5, 5)
    c3 = random.randint(-5, 5)

    #1 simulation
    while i < 10:
        g1 = a*x1 + b*z1
        h1 = a*y1 + b*c1
        x1 = random.randint(-5, 5)
        y1 = random.randint(-5, 5)
        z1 = random.randint(-5, 5)
        c1 = random.randint(-5, 5)
        counter1 = counter1 + 1
        if g1 > h1:
            i = i+1
        print(i,".", g1, " ", h1)

    i = 0

    #2 simulation   
    while i < 10:
        g2 = a*x2 + b*z2
        h2 = a*y2 + b*c2
        x2 = random.randint(-5, 5)
        y2 = random.randint(-5, 5)
        z2 = random.randint(-5, 5)
        c2 = random.randint(-5, 5)
        counter2 = counter2 + 1
        if g2 > h2:
            i = i+1
        print(i,".", g2, " ", h2)

    i = 0
    #3 simulation

    while i < 10:
        g3 = a*x3 + b*z3
        h3 = a*y3 + b*c3
        x3 = random.randint(-5, 5)
        y3 = random.randint(-5, 5)
        z3 = random.randint(-5, 5)
        c3 = random.randint(-5, 5)
        counter3 = counter3 + 1
        if g3 > h3:
            i = i+1
        print(i,".", g3, " ", h3)
     

    #if counter1 < counter2 and counter1 < counter3:
     #   lbl = Label(window, text="Симуляция 1 оказалaсь лучшие")
      #  lbl.pack()
    #elif counter2 < counter1 and counter2 < counter3:
     #   lb1 = Label(window, text="Симуляция 2 оказалaсь лучшие")
      #  lb1.pack()
    #elif counter3 < counter1 and counter3 < counter2:
     #   lb1 = Label(window, text="Симуляция 3 оказалaсь лучшие")
      #  lb1.pack()
    lbl = Label(window, text="Первая симуляция: ")
    lbl1 = Label(window, text=counter1)
    lbl2 = Label(window, text="Вторая симуляция: ")
    lbl3 = Label(window, text=counter2)
    lbl4 = Label(window, text="Третья симуляция: ")
    lbl5 = Label(window, text=counter3)
    entr = Entry(window, width=40)








    
    lbl.pack()
    lbl1.pack()
    lbl2.pack()
    lbl3.pack()
    lbl4.pack()
    lbl5.pack()
    entr.pack()
 
    def save():
        f = open("notes.txt", 'w')
        f.write(entr.get())
        f.close()


    btnsave = Button(window, text="Save", command=save)
    btn = Button(window, text="Выйти", command=quit)
    btn.pack()
    btnsave.pack()
    print(counter1)
    print(counter2)
    print(counter3)

    window.mainloop()
window.mainloop()
input()













