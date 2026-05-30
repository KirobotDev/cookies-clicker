from tkinter import *


clicks = []
puissance = 1

def click():
    global puissance
    clicks.append(puissance) 
    click_number.config(text="Vous avez actuellement " + str(sum(clicks)))


def retire_click(): # all retire_click is AI :)
    global puissance

    if sum(clicks) >= 100:
        puissance += 1

        restant_a_enlever = 100

        while restant_a_enlever > 0 and clicks:
            val = clicks.pop()   
            restant_a_enlever -= val

        click_number.config(text="Amélioration achetée" + str(puissance))
    else:
        click_number.config(text="Pas assez de cookies")

window = Tk()

window.title("Cookies clicker")
window.geometry("720x480")
window.iconbitmap("logo.ico")
window.configure(background="black")

# On va crée notre frame
frame = Frame(window, bg="black")

# On crée le text d'affichage
click_number = Label(frame, text="Vous avez actuelement", bg="#00FFFF", fg="black", width="20", height="5")
click_number.pack()

# cookies
cookie_img = PhotoImage(file="cookies.png")
cookie_img = cookie_img.subsample(2, 2)

# button 
button = Button(frame, image=cookie_img, command=click, borderwidth=0, bg="black", activebackground="black")
button.pack()

# on affiche la frame
frame.pack(expand=YES)

menu_bare = Menu(window)
# on crée le menu
file_menue = Menu(menu_bare, tearoff=0)
file_menue.add_command(label="Tu perdra 100 Cookies mais ca ameliore ta rapidité", command=retire_click)
menu_bare.add_cascade(label="Améliorations", menu=file_menue)

window.config(menu=menu_bare)

window.mainloop()