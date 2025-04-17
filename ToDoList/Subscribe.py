from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel , QHBoxLayout , QVBoxLayout , QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import json , os , sys

class subs(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Page de Connexion")
        self.setStyleSheet("background : white;")
        self.move(200 , 100)
        self.resize(1080 , 720)
        self.setWindowIcon(QIcon("icon.png"))

        vlayout = QVBoxLayout()
        vlayout.setSpacing(100)
        self.setLayout(vlayout)

        hlayout11 = QHBoxLayout()
        vlayout.addLayout(hlayout11)

        hlayout1 = QHBoxLayout()
        vlayout.addLayout(hlayout1)

        hlayout2 = QHBoxLayout()
        vlayout.addLayout(hlayout2)

        hlayout3 = QHBoxLayout()
        vlayout.addLayout(hlayout3)

        
        # Création des éléments de l'interface

        self.mail_input = QLineEdit()
        self.mail_input.setMinimumHeight(35)
        self.mail_input.setPlaceholderText("Entrez votre adresse e-mail ")
        self.mail_input.setStyleSheet("color : black ; font-size : 18px ; background : white ;border: 2px solid #000000;border-radius: 6px;padding: 4px;")
        hlayout11.addWidget(self.mail_input)



        self.username_input = QLineEdit()
        self.username_input.setMinimumHeight(35)
        self.username_input.setPlaceholderText("Entrez votre nom d' utilisateur ")
        self.username_input.setStyleSheet("color : black ; font-size : 18px ; background : white ;border: 2px solid #000000;border-radius: 6px;padding: 4px;")
        hlayout1.addWidget(self.username_input)


        self.password_input = QLineEdit()
        self.password_input.setMinimumHeight(35)
        self.password_input.setPlaceholderText("Entrez votre mot de passe utilisateur ")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("color : black ; font-size : 21px ; background : white ;border: 2px solid #000000;border-radius: 6px;padding: 4px;")
        hlayout2.addWidget(self.password_input)

        
        self.message_label = QLabel(self)
        self.message_label.setStyleSheet("color : red ; font-size : 20px ; background : white ;")

        def handle_login():
            from Login import LoginWindow
            window = LoginWindow()
            window.show()
            self.deleteLater()

        # Connexion du bouton à la méthode de connexion
        self.login_button = QPushButton(text = "Retour")
        self.login_button.setStyleSheet("color : white ; font-size : 20px ; background : green ;border: 2px solid green;border-radius: 6px;padding: 4px;")
        self.login_button.clicked.connect(handle_login)


        def subs_login():
            self.message_label.setGeometry(0 , 0 , 0 , 0)
            from Login import LoginWindow
            global log
            mail = self.mail_input.text()
            password = self.password_input.text()
            username = self.username_input.text()

            from Login import json_path
            if os.path.exists(json_path) :
                    pass
            else :
                open(json_path , "w").close()
            
            with open(json_path  , "r", encoding = 'utf-8') as log :
                if os.path.getsize(json_path) == 0 :
                    jregis = {}
                else :
                    jregis = json.load(log)
                
                try :
                    assert mail !="" and username !="" and password !=""

                    if mail in jregis.keys() :
                        self.message_label.setText("Cet utilisateur existe deja !!!")
                        self.message_label.setStyleSheet("color : red ; font-size : 20px ; background : white ;")
                        self.message_label.setGeometry(300 , 30 , 450 , 25)
                    else :
                        jregis[mail] = [password , "{}.csv".format(mail)]
                        with open(json_path  , "w", encoding = 'utf-8') as log :
                            json.dump(jregis , log , indent = 4)
                        self.message_label.setText("Vous etes inscrit, Vous pouvez retourner vous connecter")
                        self.message_label.setStyleSheet("color : green ; font-size : 20px ; background : white ;")
                        self.message_label.setGeometry(300 , 30 , 500 , 25)
                    
                        self.username_input.clear()
                        self.password_input.clear()
                        self.mail_input.clear()
                except :
                    self.message_label.setText("Donnees incorrecte !!!")
                    self.message_label.setStyleSheet("color : red ; font-size : 20px ; background : white ;")
                    self.message_label.setGeometry(300 , 30 , 450 , 25)



                    


        self.subs_button = QPushButton(text = " S' inscrire ")
        self.subs_button.setStyleSheet("color : white ; font-size : 20px ; background : blue ;border: 2px solid blue;border-radius: 6px;padding: 4px;")
        self.subs_button.clicked.connect(subs_login)
        hlayout3.addWidget(self.subs_button)
        hlayout3.addWidget(self.login_button)

        self.installEventFilter(self)
    def eventFilter(self, obj, event):
        if event.type() == event.KeyPress and event.key() == Qt.Key_Return:
            self.subs_button.click() 
            return True 
        return super().eventFilter(obj, event)

