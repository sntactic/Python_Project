from datetime import date
from PyQt5.QtWidgets import QWidget , QScrollArea , QLabel , QLineEdit , QPushButton , QFrame , QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from datetime import datetime , timedelta
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
        self.frame.setGeometry(15 , yposi , 700 , 30)

        self.intit = QLabel(self.frame , text = intitule)
        self.intit.setStyleSheet("color : blue ; font-size : 17px ; background : white ;")
        self.intit.move(2 , 4) 

        self.eche = QLabel(self.frame , text = "--------")
        self.eche.setStyleSheet("color : blue ; font-size : 15px ; background : white ;")
        self.eche.setGeometry(500 , 3 , 300 , 20) 
        


        def update_time() :
            temps = datetime.strptime(echeance, "%Y-%m-%d %H:%M:%S")
            restime = temps - datetime.now()
            jours = (restime.total_seconds() // 3600) // 24
            heures = (restime.total_seconds() - (jours * 24 * 3600)) // 3600
            minutes = (restime.total_seconds() - (jours * 24 * 3600 + heures * 3600)) // 60
            secondes = restime.total_seconds() % 60 

            if restime > timedelta(days = 0, hours = 0, minutes = 0, seconds = 0) :
                self.eche.setText("expire dans : {}j {}h {}mn {}s".format(int(jours) , int(heures) , int(minutes) , int(secondes)))
                self.eche.setGeometry(350 , 3 , 300 , 20) 
                if restime > timedelta(days = 0, hours = 2, minutes = 0, seconds = 0) :
                    self.eche.setStyleSheet("color : green ; font-size : 15px ; background : white ;")
                else :
                    self.eche.setStyleSheet("color : orange ; font-size : 15px ; background : white ") 
            else :
                self.eche.setText("expirée")
                self.eche.setGeometry(500 , 3 , 100 , 20)
                self.eche.setStyleSheet("color : red ; font-size : 17px ; background : white ;")


        def est_date(chaine, format_date="%Y-%m-%d %H:%M:%S"):
            try:
                datetime.strptime(chaine, format_date)
                return True
            except ValueError:
                return False

       
        if est_date(echeance) :
            self.timer = QTimer(self.frame)
            self.timer.timeout.connect(update_time)
            self.timer.start(100)
        



        " " "             DEFINITION DE LA METHODE DE SUPPRESSION DE TACHES      """   
        def supp() :
            global yposi , tasks 
            self.frame.deleteLater()

            " " "             MISE A JOUR DES TACHES      """
            for task in tasks[tasks.index(self) : ] :
                task.ypos -= 50
                task.frame.setGeometry(15 , task.ypos , 700 , 30)
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
        self.sup = QPushButton(self.frame , text ="supprimer")
        self.sup.setStyleSheet("color : red ; font-size : 20px ; background : white ;")
        self.sup.setGeometry(580 , 3 , 100 , 23)
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
        global tasks
        self.taches = []
        """ STYLE DE BASE SE LA FENETRE """
        self.setWindowTitle("TO DO LIST")
        self.setGeometry(150 , 100 , 1080 , 720)
        self.setMinimumSize(1080 , 720)
        self.setStyleSheet("background :"+color+";")

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

        label = QLabel(self)
        pixmap = QPixmap('background.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        
        layout.addWidget(label)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setStyleSheet("background : blue;")
        self.frame.setGeometry(40 , 30 , 1000 , 35)

        """ ECRIRE L' INTITULÉ """
        self.texte_intit = QLabel(self.frame , text= "INTITULÉ : ".lower())
        self.texte_intit.setStyleSheet("color : white ; font-size : 25px ; background : blue ;")
        self.texte_intit.move(10 , 2 )

        """ ENTRE DE L' INTITULÉ """
        self.entre_intit = QLineEdit(self.frame)
        self.entre_intit.setGeometry(100 , 5 , 350 , 25)
        self.entre_intit.setStyleSheet("color : black ;  background : white ; font-size : 20px ;")

        """ ECRIRE DA DATE DE L' ECHEANCE """
        self.texte_eche = QLabel(self.frame , text= "ÉCHÉANCE : ".lower())
        self.texte_eche.setStyleSheet("color : white ; font-size : 25px ; background : blue ;")
        self.texte_eche.move(500 , 2 )

        """ ENTRE DE L' ECHEANCE """
        self.entre_eche = QLineEdit(self.frame)
        self.entre_eche.setGeometry(620 , 5 , 250 , 25)
        self.entre_eche.setStyleSheet("color : black ; font-size : 20xp ; background : white ; font-size : 18px ;")

        self.message_vide = QLabel(self)
        self.message_vide.setGeometry(0,0,0,0)

        """ MISE A JOUR DES TACHES SAUVEGARDEES"""  
        scroll_win = QWidget()
        #scroll_win.setStyleSheet("background-image: url('/Users/macbookair/Documents/github/Python_project_evo/ToDoList/background.png')"
                                # ";background-repeat: no-repeat;background-position: center;background-size: cover; ")

    

        majTaches(scroll_win)

        """ CREATION DU CHAMP DE DEROULEMENT """        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.scroll_area.setGeometry(180 , 80 , 730 , 650)
        self.scroll_area.setWidgetResizable(True)

        scroll_win.setMinimumHeight(50 * len(tasks))
        self.scroll_area.setWidget(scroll_win)


        " " "             CREATION DE LA D' AJOUT D' AJOUT DE TACHES       """   
        def ajout() :
            global yposi
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
                self.taches.append(tache)
                self.entre_eche.clear()
                self.entre_intit.clear()
                tache.frame.show()
                yposi = 5 + 50*len(tasks)
                scroll_win.setMinimumHeight(50 * len(tasks)) 
                with open("taches.csv" , "a") as sauvetaches :
                    sauvetaches.write(tex_intit+","+tex_eche+"\n")

        " " "          BOUTTON DE CREATION """
        self.boutton_creer = QPushButton(self.frame , text = "ajouter✅")
        self.boutton_creer.setGeometry(900 , 5 , 90 , 25)
        self.boutton_creer.setStyleSheet("color : green ; font-size : 20px ; background : white ;")
        self.boutton_creer.clicked.connect(ajout)
