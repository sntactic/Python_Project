from datetime import date
from PyQt5.QtWidgets import QWidget , QScrollArea , QLabel , QLineEdit , QPushButton , QFrame
import csv , os


tasks = []
yposi = 5


" " "             CREATION DE L' OBJET TASK        """   
class Tache:
    def __init__(self , Frame , intitule , echeance , ypos) :
        self.ypos = ypos
        self.frame = QFrame(Frame)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setStyleSheet("background : white;")
        self.frame.setGeometry(5 , yposi , 600 , 30)

        self.intit = QLabel(self.frame , text = intitule+" :")
        self.intit.setStyleSheet("color : blue ; font-size : 20px ; background : white ;")
        self.intit.move(2 , 4)
        
        
        self.eche = QLabel(self.frame , text = "---------" if echeance == "" else echeance)
        self.eche.setStyleSheet("color : green ; font-size : 20px ; background : white ;")
        self.eche.move(350 , 4)

        " " "             DEFINITION DE LA METHODE DE SUPPRESSION DE TACHES      """   
        def supp() :
            global yposi , tasks 
            self.frame.deleteLater()

            " " "             MISE A JOUR DES TACHES      """
            for task in tasks[tasks.index(self) : ] :
                task.ypos -= 50
                task.frame.setGeometry(5 , task.ypos , 600 , 30)
                task.frame.show()
            tasks.remove(self)
            yposi = 5 + 50*len(tasks)
            Frame.setMinimumHeight(50 * len(tasks))

            " " "             SUPPRESSION DE TACHE DANS LE FICHIER DE SAUVEGARDE       """
            with open("taches.csv" , "r") as sauvetaches :
                taches = csv.DictReader(sauvetaches)
                new_taches = []
                for tache in taches :
                    if tache['intitu'] != intitule or tache['echea'] != echeance :
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
def majTaches(scroll_win) :
    global yposi , tasks

    if os.path.exists("taches.csv") :
        with open("taches.csv" , "r") as sauvetaches :
            taches = csv.DictReader(sauvetaches)
            for tache in taches : 
                tache = Tache(scroll_win , tache['intitu'] , tache['echea'] ,yposi)
                tasks.append(tache)
                tache.frame.show()
                yposi = 5 + 50*len(tasks)
                scroll_win.setMinimumHeight(50 * len(tasks))
    else :
        with open("taches.csv" , "a") as sauvetaches :
            sauvetaches.write("intitu,echea\n")



" " "             CREATION DE LA FENETRE PRINCIPALE        """    
class mywindow(QWidget) :
    def __init__(self, color = "white") :
        super().__init__()

        """ STYLE DE BASE SE LA FENETRE """
        self.setWindowTitle("TO DO LIST")
        self.setGeometry(150 , 100 , 1080 , 720)
        self.setMinimumSize(1080 , 720)
        self.setStyleSheet("background :"+color+";")

        """ ECRIRE L' INTITULÉ """
        self.texte_intit = QLabel(self , text= "INTITULÉ : ".lower())
        self.texte_intit.setStyleSheet("color : black ; font-size : 25px ; background : white ;")
        self.texte_intit.move(100 , 30 )

        """ ENTRE DE L' INTITULÉ """
        self.entre_intit = QLineEdit(self)
        self.entre_intit.setGeometry(200 , 33 , 300 , 25)
        self.entre_intit.setStyleSheet("color : black ;  background : grey ; font-size : 20px ;")

        """ ECRIRE DA DATE DE L' ECHEANCE """
        self.texte_eche = QLabel(self , text= "ÉCHÉANCE : ".lower())
        self.texte_eche.setStyleSheet("color : black ; font-size : 25px ; background : white ;")
        self.texte_eche.move(550 , 30 )

        """ ENTRE DE L' ECHEANCE """
        self.entre_eche = QLineEdit(self)
        self.entre_eche.setGeometry(680 , 33 , 120 , 25)
        self.entre_eche.setStyleSheet("color : black ; font-size : 20xp ; background : grey ; font-size : 18px ;")

        self.message_vide = QLabel(self)

        """ MISE A JOUR DES TACHES SAUVEGARDEES"""  
        scroll_win = QWidget()
        majTaches(scroll_win)

        """ CREATION DU CHAMP DE DEROULEMENT """        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(220 , 80 , 630 , 650)
        self.scroll_area.setWidgetResizable(True)

        scroll_win.setMinimumHeight(50 * len(tasks))
        self.scroll_area.setWidget(scroll_win)


        " " "             CREATION DE LA D' AJOUT D' AJOUT DE TACHES       """   
        def ajout() :
            global tasks ,yposi
            tex_intit = self.entre_intit.text()
            tex_eche = self.entre_eche.text()
            self.message_vide.setGeometry(0,0,0,0)
            
            if tex_intit.strip() == "":
                self.message_vide.setText("vous devez saisir une tache !!!!!!!!!")
                self.message_vide.setStyleSheet("color : red ; font-size : 20px ; background : white ;")
                self.message_vide.setGeometry(350 , 5 , 300 , 20)
            else :
                self.message_vide.setGeometry(0,0,0,0)
                tache = Tache(scroll_win , tex_intit , tex_eche ,yposi)
                tasks.append(tache)
                self.entre_eche.clear()
                self.entre_intit.clear()
                tache.frame.show()
                yposi = 5 + 50*len(tasks)
                scroll_win.setMinimumHeight(50 * len(tasks)) 
                
                with open("taches.csv" , "a") as sauvetaches :
                    sauvetaches.write(tex_intit+","+tex_eche+"\n")

        " " "          BOUTTON DE CREATION """
        self.boutton_creer = QPushButton(self , text = "AJOUTER")
        self.boutton_creer.setGeometry(840 , 33 , 90 , 25)
        self.boutton_creer.setStyleSheet("color : green ; font-size : 20px ; background : white ;")
        self.boutton_creer.clicked.connect(ajout)


