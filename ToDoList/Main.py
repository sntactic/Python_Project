from datetime import date
from PyQt5.QtWidgets import QWidget , QScrollArea , QLabel , QLineEdit , QPushButton , QFrame , QVBoxLayout , QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from datetime import datetime , timedelta
import csv , os

tasks = []
yposi = 5

" " "             CREATION DE L' OBJET TASK        """   
class Tache:
    def __init__(self , Frame , intitule , echeance , ypos) :
        self.ypos = ypos

        self.frame = QHBoxLayout()

        self.intit = QLabel(text = intitule)
        self.intit.setStyleSheet("color : blue ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
        self.frame.addWidget(self.intit)

        self.eche = QLabel(text = "--------")
        self.eche.setStyleSheet("color : blue ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
        self.frame.addWidget(self.eche)
        

        def update_time() :
            temps = datetime.strptime(echeance, "%Y-%m-%d %H:%M:%S")
            restime = temps - datetime.now()
            jours = (restime.total_seconds() // 3600) // 24
            heures = (restime.total_seconds() - (jours * 24 * 3600)) // 3600
            minutes = (restime.total_seconds() - (jours * 24 * 3600 + heures * 3600)) // 60
            secondes = restime.total_seconds() % 60 

            if restime > timedelta(days = 0, hours = 0, minutes = 0, seconds = 0) :
                self.eche.setText("expire dans : {}j {}h {}mn {}s".format(int(jours) , int(heures) , int(minutes) , int(secondes)))
                if restime > timedelta(days = 0, hours = 2, minutes = 0, seconds = 0) :
                    self.eche.setStyleSheet("color : green ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
                else :
                    self.eche.setStyleSheet("color : orange ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ") 
            else :
                self.eche.setText("expirée")
                self.eche.setStyleSheet("color : red ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")


        def est_date(chaine, format_date="%Y-%m-%d %H:%M:%S"):
            try:
                datetime.strptime(chaine, format_date)
                return True
            except ValueError:
                return False


        self.timer = QTimer(self.frame)
        if est_date(echeance) :
            self.timer.timeout.connect(update_time)
            self.timer.start(100)
        



        " " "             DEFINITION DE LA METHODE DE SUPPRESSION DE TACHES      """   
        def supp() :
            global yposi , tasks 
            self.intit.deleteLater()
            self.eche.deleteLater()
            self.sup.deleteLater()
            self.timer.deleteLater()
            self.frame.deleteLater()

            " " "             MISE A JOUR DES TACHES      """
            for task in tasks[tasks.index(self) : ] :
                task.ypos -= 50
            tasks.remove(self)
            yposi = 5 + 50*len(tasks)

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
        self.sup = QPushButton(text ="supprimer")
        self.sup.setStyleSheet("color : red ; font-size : 20px ; background : white ;")
        self.sup.clicked.connect(supp)
        self.frame.addWidget(self.sup)
        Frame.addLayout(self.frame)



" " "             DEFINITION DA LA FONCTION D'AFFICHAGE LES TACHES PRECEDENTES        """  
def majTaches(scroll_win) :
    global yposi , tasks

    if os.path.exists("taches.csv") :
        with open("taches.csv" , "r") as sauvetaches :
            taches = csv.DictReader(sauvetaches)
            for tache in taches : 
                tache = Tache(scroll_win , tache['intitu'] , tache['echea'] ,yposi)
                tasks.append(tache)
                yposi = 5 + 50*len(tasks)
    else :
        with open("taches.csv" , "a") as sauvetaches :
            sauvetaches.write("intitu,echea\n")



" " "             CREATION DE LA FENETRE PRINCIPALE        """    
class mywindow(QWidget) :
    def __init__(self, color = "white") :
        super().__init__()
        global tasks
        self.taches = []
        """ STYLE DE BASE SE LA FENETRE """
        self.setWindowTitle("TO DO LIST")

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        palette = QPalette()
        pixmap = QPixmap("background1.png") 
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

        """mise en place des elements fonctionnels"""

        self.frame = QHBoxLayout()
        layout.addLayout(self.frame)

        """ ECRIRE L' INTITULÉ """
        self.texte_intit = QLabel(text= "INTITULÉ : ".lower())
        self.texte_intit.setStyleSheet("color : black ; font-size : 25px ; background-color: rgba(0, 0, 0, 0) ;")
        self.frame.addWidget(self.texte_intit)

        """ ENTRE DE L' INTITULÉ """
        self.entre_intit = QLineEdit()
        self.entre_intit.setStyleSheet("color : black ;  background : white ; font-size : 20px ;")
        self.frame.addWidget(self.entre_intit)
        

        """ ECRIRE DA DATE DE L' ECHEANCE """
        self.texte_eche = QLabel(text= "ÉCHÉANCE : ".lower())
        self.texte_eche.setStyleSheet("color : black ; font-size : 25px ; background-color: rgba(0, 0, 0, 0) ;")
        self.frame.addWidget(self.texte_eche)

        """ ENTRE DE L' ECHEANCE """
        self.entre_eche = QLineEdit()
        self.entre_eche.setStyleSheet("color : black ; font-size : 20xp ; background : white ; font-size : 18px ;")
        self.frame.addWidget(self.entre_eche)

        self.message_vide = QLabel(self)
        self.message_vide.setGeometry(0,0,0,0)

        """ MISE A JOUR DES TACHES SAUVEGARDEES"""  
        scroll_win = QWidget()
        win_layout = QVBoxLayout(scroll_win)
        win_layout.setSpacing(20)
        #scroll_win.setStyleSheet("background-image: url('/Users/macbookair/Documents/github/Python_project_evo/ToDoList/background.png')"
                                # ";background-repeat: no-repeat;background-position: center;background-size: cover; ")

    

        majTaches(win_layout)

        """ CREATION DU CHAMP DE DEROULEMENT """        
        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(scroll_win)
        
        layout.addWidget(self.scroll_area)


        " " "             CREATION DE LA D' AJOUT D' AJOUT DE TACHES       """   
        def ajout() :
            global yposi
            tex_intit = self.entre_intit.text()
            tex_eche = self.entre_eche.text()
            self.message_vide.setGeometry(0,0,0,0)
            
            if tex_intit.strip() == "":
                self.message_vide.setText("vous devez saisir une tache !!!!!!!!!")
                self.message_vide.setStyleSheet("color : red ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
                self.message_vide.setGeometry(350 , 5 , 300 , 20)
            else :
                self.message_vide.setGeometry(0,0,0,0)
                tache = Tache(win_layout , tex_intit , tex_eche ,yposi)
                tasks.append(tache)
                self.taches.append(tache)
                self.entre_eche.clear()
                self.entre_intit.clear()
                yposi = 5 + 50*len(tasks)
                with open("taches.csv" , "a") as sauvetaches :
                    sauvetaches.write(tex_intit+","+tex_eche+"\n")

        " " "          BOUTTON DE CREATION """
        self.boutton_creer = QPushButton(text = "ajouter✅")
        self.boutton_creer.setStyleSheet("color : green ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
        self.boutton_creer.clicked.connect(ajout)
        self.frame.addWidget(self.boutton_creer)