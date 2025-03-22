from tkinter import *




" " "  CREATION OF THE TKINTER WINDOW  " " "
window = Tk()
window.title("TO DO LIST")
window.geometry("1080x720")
window.config(background = "white")




" " "  CREATION DE L' ARRIERE PLAN  " " "
largeur = 940
longueur = 530
image = PhotoImage(file = "bf_to_do.png").zoom(35).subsample(32)
planche = Canvas(window , width = largeur , height = longueur , bg = "white" , bd = 0 , highlightthickness = 0)
planche.create_image(largeur/2 , longueur/2  , image = image)
planche.place(x = 520 , y = 75) 





" " "  CREATION OF THE ENTRY FRAME FOR TASKS  " " "
task_frame = Frame(window , bg = "blue" , width = 900 , height = 50 )
task_frame.place(x = 0 , y = 20)

" " "          CREATION OF LABEL FOR TASK NAME       " " "
task_name = Label(task_frame , text = "intitulé :".upper() , bg = "blue" , fg = "white" , font = ("Courrier" , 20))
task_name.place(x = 0 , y = 10)

" " "          CREATION OF ENTRY FOR TASK NAME       " " "
task_entry = Entry(task_frame, bg="black", font=("Courrier", 28), fg="white", highlightthickness = 0, bd=0 , relief=SUNKEN ,
                                                         width = 18 , border=1)
task_entry.place(x = 110 , y = 8)

" " "          CREATION OF LABEL FOR TASK DATE       " " "
task_date = Label(task_frame , text = "echeance :".upper() , bg = "blue" , fg = "white" , font = ("Courrier" , 20))
task_date.place(x = 460 , y = 8)

" " "          CREATION OF ENTRY FOR TASK DATE       " " "
date_entry = Entry(task_frame, bg="black", font=("Courrier", 28), fg="green", highlightthickness = 0, bd=0 , relief=SUNKEN ,
                                                         width = 10 , border=1)
date_entry.place(x = 590 , y = 8)

" " "          CREATION OF BUTTON FOR CREATING TASK       " " "
task_button = Button(task_frame , text = "CRÉER" , borderwidth = 0 , fg = "dark blue" , highlightthickness = 0 , relief = SUNKEN ,
                                                        width = 5 , height = 2 )
task_button.place(x= 815 , y = 8 )








" " "  CREATION OF TASK CLASS  " " "

class Task() :
    frame = Frame(window , bg = "blue" , width = 20 , height = 50 )




























window.mainloop()