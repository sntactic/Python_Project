from datetime import timedelta
from PyQt5.QtWidgets import (QWidget , QListWidget , QLabel , QLineEdit ,QListWidgetItem,
                              QPushButton , QDateTimeEdit , QVBoxLayout , QHBoxLayout)
from PyQt5.QtCore import QTimer , QDateTime , Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush 
from datetime import datetime , timedelta
import csv , os , sys
from mail import send_mail




def resource_path(relative_path):
    """Donne le chemin correct vers un fichier, même dans une app PyInstaller"""
    try:
        base_path = sys._MEIPASS  
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

image_path = resource_path("background1.png")
csv_path = resource_path("taches.csv")




tasks = []

" " "             CREATION DE L' OBJET TASK        """   
class Tache:
    def __init__(self , Frame , intitule , echeance ) :

        self.frame = QHBoxLayout()
        self.wframe = QWidget()
        self.wframe.setLayout(self.frame)

        self.intit = QLabel(text = intitule)
        self.intit.setStyleSheet("color : blue ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
        self.frame.addWidget(self.intit)

        self.eche = QLabel(text = "--------")
        self.eche.setStyleSheet("color : blue ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
        self.frame.addWidget(self.eche)

        item = QListWidgetItem()
        item.setSizeHint(self.wframe.sizeHint())
        Frame.addItem(item)
        Frame.setItemWidget(item, self.wframe)

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
                if restime > timedelta(days = 0, hours = 0, minutes = 0, seconds = -0.1)  :
                    send_mail(intitule)

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
            global tasks 
            self.intit.deleteLater()
            self.eche.deleteLater()
            self.sup.deleteLater()
            self.timer.deleteLater()
            self.frame.deleteLater()
            Frame.takeItem(Frame.row(item))
            self.wframe.deleteLater()

            " " "             SUPPRESSION DE TACHE DANS LE FICHIER DE SAUVEGARDE       """
            with open(csv_path , "r") as sauvetaches :
                taches = csv.DictReader(sauvetaches)
                new_taches = []
                for tache in taches :
                    if tache['intitu'] != intitule or tache['echea'] != echeance :
                        new_taches.append(tache['intitu']+","+tache['echea']+"\n")

                with open(csv_path , "w") as sauvetaches :
                    sauvetaches.write("intitu,echea\n")
                    for dico in new_taches :
                        sauvetaches.write(dico)

        " " "             CREATION DU BOUTTON DE SUPPRESSION       """   
        self.sup = QPushButton(text ="supprimer")
        self.sup.setStyleSheet("color : red ; font-size : 20px ; background : white ;")
        self.sup.clicked.connect(supp)
        self.frame.addWidget(self.sup)




" " "             DEFINITION DA LA FONCTION D'AFFICHAGE LES TACHES PRECEDENTES        """  
def majTaches(scroll_win) :
    global tasks

    if os.path.exists(csv_path) :
        with open(csv_path , "r") as sauvetaches :
            taches = csv.DictReader(sauvetaches)
            for tache in taches : 
                tache = Tache(scroll_win , tache['intitu'] , tache['echea'] )
                tasks.append(tache)
    else :
        with open(csv_path , "a") as sauvetaches :
            sauvetaches.write("intitu,echea\n")



" " "             CREATION DE LA FENETRE PRINCIPALE        """    
class mywindow(QWidget) :
    def __init__(self) :
        super().__init__()
        global tasks
        self.taches = []
        """ STYLE DE BASE SE LA FENETRE """
        self.setWindowTitle("TO DO LIST")
        self.move(200 , 100)
        self.resize(1080 , 720)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        palette = QPalette()
        pixmap = QPixmap(image_path) 
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

        """mise en place des elements fonctionnels"""

        self.frame = QHBoxLayout()
        self.frame.setSpacing(20)
        layout.addLayout(self.frame)

        """ ENTRE DE L' INTITULÉ """
        self.entre_intit = QLineEdit()
        self.entre_intit.setPlaceholderText("Entrez une tache")
        self.entre_intit.setStyleSheet("color : black ;background: white ; font-size : 17px ;border: 2px solid #000000;border-radius: 6px;padding: 4px;")
        self.entre_intit.setMinimumHeight(35)
        self.frame.addWidget(self.entre_intit)

        """ ENTRE DE L' ECHEANCE """
        self.entre_eche = QDateTimeEdit()
        self.entre_eche.setFixedHeight(35)
        self.entre_eche.setStyleSheet("font-size: 27px;padding: 4px;")
        self.entre_eche.setCalendarPopup(True)
        self.entre_eche.setDateTime(QDateTime.currentDateTime().addDays(1))
        self.frame.addWidget(self.entre_eche)

        self.message_vide = QLabel(self)
        self.message_vide.setGeometry(0,0,0,0)

        """ CREATION DU CHAMP DE DEROULEMENT """ 
        win_task =  QListWidget(self)
        win_task.setStyleSheet("background-color: rgba(0, 0, 0, 0); ")
        layout.addWidget(win_task) 

        """ MISE A JOUR DES TACHES SAUVEGARDEES"""  

        majTaches(win_task)

        " " "             CREATION DE LA D' AJOUT D' AJOUT DE TACHES       """   
        def ajout() :
            tex_intit = self.entre_intit.text()
            tex_eche = self.entre_eche.dateTime().toString("yyyy-MM-dd HH:mm:ss")
            self.message_vide.setGeometry(0,0,0,0)
            
            if tex_intit.strip() == "":
                self.message_vide.setText("vous devez saisir une tache !!!!!!!!!")
                self.message_vide.setStyleSheet("color : red ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
                self.message_vide.setGeometry(350 , 5 , 300 , 20)
            else :
                self.message_vide.setGeometry(0,0,0,0)
                tache = Tache(win_task , tex_intit , tex_eche )
                tasks.append(tache)
                self.taches.append(tache)
                self.entre_eche.clear()
                self.entre_intit.clear()
                with open(csv_path , "a") as sauvetaches :
                    sauvetaches.write(tex_intit+","+tex_eche+"\n")

        " " "          BOUTTON DE CREATION """
        self.boutton_creer = QPushButton(text = "ajouter✅")
        self.boutton_creer.setStyleSheet("color : green ; font-size : 20px ; background-color: rgba(0, 0, 0, 0) ;")
        self.boutton_creer.clicked.connect(ajout)
        self.frame.addWidget(self.boutton_creer)

        self.installEventFilter(self)
    def eventFilter(self, obj, event):
        if event.type() == event.KeyPress and event.key() == Qt.Key_Return:
            self.boutton_creer.click() 
            return True 
        return super().eventFilter(obj, event)