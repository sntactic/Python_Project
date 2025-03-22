from random import randint
from tkinter import *

x = 10
tentative = x
minValue = 0
maxValue = 100

justprix = randint(minValue , maxValue)

#creation de la fenetre principale

window = Tk()
window.title("jeu juste prix")
window.geometry("1080x720")
window.config(background = "grey")



def fermer() :
    window.quit()

    #affice d' un message de description

message = Label(window , text = "BIENVENUE SUR LE JEU DU JUSTE PRIX \n \n Deviner un nombre ou un chiffre "
                                "comprix entre {} et {} en {} tantatives".format(minValue , maxValue , x) ,
                                    bg ="grey" , font = ("Courrier" , 25) , fg = "black" )

message.pack()

    # creation du menu du jeu

frameMenue = Frame(window , bg = "blue" , width = 220 , height = 720 )
frameMenue.place(x = -300 , y = 0)

fermeture = Button(frameMenue , text = "FERMER" , borderwidth = 0 , fg = "black" , highlightthickness = 0 , relief = SUNKEN ,
                                                        width = 18 , height = 1 , command = fermer )
fermeture.place(x = 10 , y = 30)

activeperso = False

def translationperso() :

    global activeperso

    if activeperso == False :

        for i in range(-300 , 0) :
            frameperso.place(x = i , y = 100)
            activeperso = True

    else :

        for i in range(300) :
            frameperso.place(x= -i , y = 100)
            activeperso = False


personnaliser = Button(frameMenue , text = "PERSONNALISER" , borderwidth = 0 , fg = "black" , highlightthickness = 0 , relief = SUNKEN ,
                                                        width = 18 , height = 1  , command = translationperso )
personnaliser.place(x = 10 , y = 70)

frameperso = Frame(frameMenue , bg = "dark blue" , width = 220 , height = 200 )
frameperso.place(x = -300 , y = 100)

mintexte = Label(frameperso , text = "minimum : " , bg = "blue" , fg = "white" , font = ("Courrier" , 20))
mintexte.place(x = 0 , y = 5)

minentry = Entry(frameperso, bg="black", font=("Courrier", 25), fg="green", highlightthickness = 0, bd=2 , relief=SUNKEN , width = 5)
minentry.place(x = 100 , y = 5)

maxtexte = Label(frameperso , text = "maximum : " , bg = "blue" , fg = "white" , font = ("Courrier" , 20))
maxtexte.place(x = 0 , y = 50)

maxentry = Entry(frameperso, bg="black", font=("Courrier", 25), fg="green", highlightthickness = 0, bd=2 , relief=SUNKEN , width = 5)
maxentry.place(x = 100 , y = 50)

tentativetexte = Label(frameperso , text = "tentatives : " , bg = "blue" , fg = "white" , font = ("Courrier" , 20))
tentativetexte.place(x = 0 , y = 95)

tentativeentry = Entry(frameperso, bg="black", font=("Courrier", 25), fg="green", highlightthickness = 0, bd=2 , relief=SUNKEN , width = 5)
tentativeentry.place(x = 100 , y = 95)

def appliquer_() :

    global minValue , maxValue , tentative , x

    try :
        minValue = int(minentry.get())
    except :
        minentry.delete(0, END)
        #minentry.config(fg="red")
        minentry.insert(0, "!!!")

    try :
        maxValue = int(maxentry.get())
    except :
        maxentry.delete(0 , END)
        #maxentry.config(fg="red")
        maxentry.insert(0, "!!!")

    try :
        x = int(tentativeentry.get())
    except ValueError :
        tentativeentry.delete(0 , END)
        #tentativeentry.config(fg = "red")
        tentativeentry.insert(0 , "!!!")

    message.config(text = "BIENVENUE SUR LE JEU DU JUSTE PRIX \n \n Deviner un nombre ou un chiffre "
                                "comprix entre {} et {} en {} tantatives".format(minValue , maxValue , x))

    afficheTentative.config(text= "{}".format(tentative))
    
    texteSaisi.delete(0, END)

    relancer()




appliquer = Button(frameperso , text = "APPLIQUER : " ,  fg = "blue" , font = ("Courrier" , 20) , activebackground = "green" , activeforeground = "white" ,
                   highlightthickness = 0 , relief = SUNKEN , borderwidth = 0 , command = appliquer_)
appliquer.place(x = 35 , y = 140)

        #glissement du menu

active = False

def translation() :

    global active

    if active == False :

        for i in range(-300 , 0) :
            frameMenue.place(x = i , y = 0)
            active = True
            menu.place(x= -100, y=10)

    else :

        for i in range(0,300) :
            frameMenue.place(x= -i , y = 0)
            active = False
            menu.place(x = 10, y = 10)



menu = Button(window , text = "⚙️" ,bd = 0 , borderwidth = 0 , width = 1 , height = 1 , highlightthickness = 0 , relief = SUNKEN , command = translation )
menu.place(x = 10 , y = 10)

fermermenu = Button(frameMenue , text = "❌" ,bd = 0 , borderwidth = 0 , width = 1 , height = 1 , highlightthickness = 0 , relief = SUNKEN , command = translation )
fermermenu.place(x = 170 , y = 0)

    # creation d' un frame contenue le coeur de jeu

boite = Frame(window , bg = "grey" , width= 600 , height= 600)

        #creation d' un entry pour l' affichage des tentatives

indicTentative = Label(boite , text = "tentatives restantes : " , bg = "black" , font = ("Courrier" , 25) , fg = "green" )
indicTentative.place(x = 150 , y = 50)


afficheTentative = Label(boite,text=str(tentative) ,bg="black", font=("Courrier", 25), fg="green")

afficheTentative.place(x = 420 , y = 51)


        # creation d'un entry pour afficher du texte

texteAfficher = Label(boite , bg = "black" , font = ("Courrier" , 25) , fg = "white" , width=35)
texteAfficher.config(text = "veillez saisir un nombre compris entre {} et {}".format(minValue , maxValue))
texteAfficher.place(x = 30 , y = 160)


        #crearion d' un entry pour la saisie dee l' utilisateur

texteSaisi = Entry(boite , bg = "black" , font = ("Courrier" , 25) , fg = "green" , highlightthickness = 0 , bd = 5 , relief = SUNKEN , width = 5 )
texteSaisi.place(x = 255 , y = 250)


        #fonction de fin de partie
def fin() :
    valider.place(x = -500)
    sousboite.place(x = 100 , y = 400)

# creation de la fonction de validation

def validation():
    global tentative

    prixentre = texteSaisi.get()
    try:
        prixentre = int(prixentre)

    except ValueError:
        texteAfficher.config(text= "vous devez saisir un entier")
        texteSaisi.delete(0, END)

    if tentative > 0:
        tentative -= 1

        afficheTentative.config(text=str(tentative))

        if prixentre == justprix:
            texteAfficher.config(fg = "green")
            texteAfficher.config(text = "felicitation vous avez trouver le juste prix : {} !".format(prixentre))
            texteSaisi.delete(0, END)
            fin()

        elif prixentre > justprix:
            texteAfficher.config(text= "c' est moins de {}".format(prixentre))
            texteSaisi.delete(0, END)

        else:
            texteAfficher.config(text= "c' est plus {}".format(prixentre))
            texteSaisi.delete(0, END)

    if tentative == 0 :
        texteAfficher.config(fg="red")
        texteAfficher.config(text= "vous avez perdu le juste prix etait : {}".format(justprix))
        texteSaisi.delete(0, END)
        fin()

valider = Button(boite , text = "VALIDER" , borderwidth = 0 , fg = "green" , highlightthickness = 0 , relief = SUNKEN ,
                                                width = 10 , height = 2 , activebackground = "green" , activeforeground = "white" , command = validation )

valider.place(x = 240 , y = 350)

# relancer le jeu

sousboite = Frame(boite , width = 400 , height = 60 , bg = "grey")

def relancer():
    global tentative , x , justprix , minValue , maxValue
    tentative = x
    afficheTentative.config(text= str(tentative))
    texteAfficher.config(fg="white")
    texteAfficher.config(text= " veillez saisir un nombre compris entre {} et {}".format(minValue , maxValue))
    sousboite.place(x= -500)
    valider.place(x=240, y=350)
    justprix = randint(minValue, maxValue)

recommencer = Button(sousboite , text = "RECOMMENCER" , borderwidth = 0, fg = "orange" , highlightthickness = 0 , relief = SUNKEN ,
                                                     width = 10 , height = 2 ,  activebackground = "orange" , activeforeground = "white" ,command = relancer)

recommencer.place(x = 30 , y = 10)

            #creation d' un bouton quitter
#commande de fermeture

quitter = Button(sousboite , text = "QUITTER" , borderwidth = 0 , fg = "red" , highlightthickness = 0 , relief = SUNKEN ,
                                                        width = 10 , height = 2 , activebackground = "red" , activeforeground = "white" , command = fermer )

quitter.place(x = 250 , y = 10)


boite.place(x = 250 , y = 100)

#main programme
window.mainloop()