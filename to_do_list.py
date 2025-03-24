from datetime import date
import sys
from PyQt5.QtWidgets import QApplication, QWidget , QLabel , QLineEdit , QPushButton , QFrame
import csv


tasks = []
yposi = 80 


" " "             CREATION DE L' OBJET TASK        """   
class Tache:
    def __init__(self , Frame , intitule , echeance , ypos) :
        self.ypos = ypos
        self.frame = QFrame(Frame)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setStyleSheet("background : blue;")
        self.frame.setGeometry(30 , yposi , 600 , 30)

        self.intit = QLabel(self.frame , text = intitule)
        self.intit.setStyleSheet("color : black ; font-size : 20px ; background : white ;")
        self.intit.move(2 , 4)
        
        self.eche = QLabel(self.frame , text = echeance)
        self.eche.setStyleSheet("color : green ; font-size : 20px ; background : white ;")
        self.eche.move(350 , 4)

        " " "             DEFINITION DE LA METHODE DE SUPPRESSION DE TACHES      """   
        def supp() :
            global yposi , tasks 
            self.frame.deleteLater()

            " " "             MISE A JOUR DES TACHES      """
            for task in tasks[tasks.index(self) : ] :
                task.ypos -= 50
                task.frame.setGeometry(30 , task.ypos , 600 , 30)
                task.frame.show()
            tasks.remove(self)
            yposi = 80 + 50*len(tasks)

            " " "             SUPPRESSION DE TACHE DANS LE FICHIER DE SAUVEGARDE       """
            with open("taches.csv" , "r") as sauvetaches :
                taches = csv.DictReader(sauvetaches)
                new_taches = []
                for tache in taches :
                    if tache['intitu'] != intitule :
                        new_taches.append(tache['intitu']+","+tache['echea']+"\n")

                with open("taches.csv" , "w") as sauvetaches :
                    sauvetaches.write("intitu,echea\n")
                    for dico in new_taches :
                        sauvetaches.write(dico)

        " " "             CREATION DU BOUTTON DE SUPPRESSION       """   
        self.sup = QPushButton(self.frame , text = "SUPRIMER")
        self.sup.setStyleSheet("color : red ; font-size : 20px ; background : white ;")
        self.sup.setGeometry(490 , 5 , 100 , 20)
        self.sup.clicked.connect(supp)



" " "             DEFINITION DA LA FONCTION D'AFFICHAGE LES TACHES PRECEDENTES        """  
def majTaches(win) :
    global yposi , tasks
    with open("taches.csv" , "r") as sauvetaches :
        taches = csv.DictReader(sauvetaches)
        for tache in taches : 
            tache = Tache(win , tache['intitu'] , tache['echea'] ,yposi)
            tasks.append(tache)
            tache.frame.show()
            yposi = 80 + 50*len(tasks)



" " "             CREATION DE LA FENETRE PRINCIPALE        """    
class mywindow(QWidget) :
    def __init__(self, window , color = "white") :
        super().__init__()

        """ STYLE DE BASE SE LA FENETRE """
        self.window = window
        self.window.setWindowTitle("TO DO LIST")
        self.window.setGeometry(150 , 100 , 1080 , 720)
        self.window.setStyleSheet("background :"+color+";")

        """ ECRIRE L' INTITULÉ """
        self.texte_intit = QLabel(self.window , text= "INTITULÉ : ")
        self.texte_intit.setStyleSheet("color : black ; font-size : 25px ; background : white ;")
        self.texte_intit.move(10 , 30 )

        """ ENTRE DE L' INTITULÉ """
        self.entre_intit = QLineEdit(self.window)
        self.entre_intit.setGeometry(140 , 33 , 300 , 25)
        self.entre_intit.setStyleSheet("color : black ;  background : grey ; font-size : 20px ;")

        """ ECRIRE DA DATE DE L' ECHEANCE """
        self.texte_eche = QLabel(self.window , text= "ECHEANCE : ")
        self.texte_eche.setStyleSheet("color : black ; font-size : 25px ; background : white ;")
        self.texte_eche.move(470 , 30 )

        """ ENTRE DE L' ECHEANCE """
        self.entre_eche = QLineEdit(self.window)
        self.entre_eche.setGeometry(620 , 33 , 120 , 25)
        self.entre_eche.setStyleSheet("color : black ; font-size : 20xp ; background : grey ; font-size : 18px ;")

        majTaches(self.window)

        " " "             CREATION DE LA D' AJOUT D' AJOUT DE TACHES       """   
        def ajout() :
            global tasks ,yposi
            tex_intit = self.entre_intit.text()
            tex_eche = self.entre_eche.text()
            tache = Tache(self.window , tex_intit , tex_eche ,yposi)
            tasks.append(tache)
            self.entre_eche.clear()
            self.entre_intit.clear()
            tache.frame.show()
            yposi = 80 + 50*len(tasks) 

            with open("taches.csv" , "a") as sauvetaches :
                sauvetaches.write(tex_intit+","+tex_eche+"\n")

        " " "          BOUTTON DE CREATION """
        self.boutton_creer = QPushButton(self.window , text = "AJOUTER")
        self.boutton_creer.setGeometry(780 , 33 , 90 , 25)
        self.boutton_creer.setStyleSheet("color : green ; font-size : 20px ; background : white ;")
        self.boutton_creer.clicked.connect(ajout)



" " "   L' APPELLE DU PRGRAMME   """
if __name__ == '__main__' :

    app = QApplication(sys.argv)

    root = QWidget()
    window = mywindow(root)
    root.show()
    
    sys.exit(app.exec_())
