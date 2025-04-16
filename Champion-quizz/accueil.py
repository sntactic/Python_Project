from PyQt5.QtWidgets import (QWidget , QListWidget , QLabel , QLineEdit ,QListWidgetItem, QApplication ,
                              QPushButton , QDateTimeEdit , QVBoxLayout , QHBoxLayout , QCheckBox)
import sys


#"""""""""""""""""""""""""""""""""""""""""""""CREATION D'UNE CLASSE D'ENTREES DE NOMS D' UTILISATEURS"""""""""""""""""""""""""""""""""""""""""""""""
class my_entry(QLineEdit):
    def __init__(self) :
        super().__init__()
        self.setStyleSheet("background: white ; border: 1px solid black ; border-radius : 6px ; font-size : 20px ; color : black")
        self.setPlaceholderText("veillez saisir le nom du joueur")
        self.setFixedHeight(40)

#""""""""""""""""""""""""""""""""""""""""""""""""""""CREATION DE LA CLASSE DE LA FENETRE D'ACCUEIL"""""""""""""""""""""""""""""""""""""""""""""""""""
class win_accueil(QWidget) :
    def __init__(self) :
        super().__init__()

        self.setWindowTitle("Accueil Quizz")
        self.setStyleSheet("background : white")
        self.resize(820 , 530)

        #"""""""""""""""""""""""""""CREATION D' UN LAYOUT POUR ORGANISER VERTICALEMENT LA FENETRE D' ACCUEIL""""""""""""""""""""""""""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(150 , 0 , 150 , 0)
        self.setLayout(layout)

        #""""""""""""""""""""""""""""""""""""""""""""INSTANCIATION DES ENTREES UTILISATEURS""""""""""""""""""""""""""""""""""""""""""""
        self.line1 , self.line2 , self.line3 , self.line4 = my_entry() , my_entry() , my_entry() , my_entry()

        #""""""""""""""""""""""""""""""""""""""""""CREATION DU BOUTTON POUR COMMENCER LE JEUX""""""""""""""""""""""""""""""""""""""""""
        self.boutton_commencer = QPushButton("commencer le Quizz")
        self.boutton_commencer.setStyleSheet("color : white ; font-size : 20px ; background : blue ;border: 2px solid blue ;border-radius: 6px;")
        self.boutton_commencer.setFixedHeight(30)

        #""""""""""""""""""""""""""""""""""""AJOUT DES ENTREES DE NOM D'UTILISATEURS DANS LE LAYOUT""""""""""""""""""""""""""""""""""""
        layout.addWidget(self.line1)
        layout.addWidget(self.line2)
        layout.addWidget(self.line3)
        layout.addWidget(self.line4)
        layout.addWidget(self.boutton_commencer)
    
    def recupe_nom_joueurs(self) :
        nom_joueurs = [self.line1.text() , self.line2.text() , self.line3.text() , self.line4.text()]


app = QApplication(sys.argv)

accueil = win_accueil()
accueil.show()

sys.exit(app.exec_())