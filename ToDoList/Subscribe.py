from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel , QHBoxLayout , QVBoxLayout , QApplication
from Main import mywindow
import json , os , sys

def resource_path(relative_path):
    """Donne le chemin correct vers un fichier, même dans une app PyInstaller"""
    try:
        base_path = sys._MEIPASS  
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

log_path = resource_path("Logs.json")

class subs(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Page de Connexion")
        self.setStyleSheet("background : white;")
        self.move(200 , 100)
        self.resize(1080 , 720)
        

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


        vlayout.addLayout(hlayout2)
        
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

        self.message_label = QLabel(self)
        self.message_label.setStyleSheet("color : red ; font-size : 20px ; background : white ;")

        def subs_login():
            self.message_label.setGeometry(0 , 0 , 0 , 0)
            from Login import LoginWindow
            global log
            mail = self.mail_input.text()
            password = self.password_input.text()
            username = self.username_input.text()

            
            with open(log_path  , "r", encoding = 'utf-8') as log :
                if os.path.getsize("Logs.json") == 0 :
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
                        with open(log_path  , "w", encoding = 'utf-8') as log :
                            json.dump(jregis , log , indent = 4)
                        self.message_label.setText("Vous etes inscrit, Vous pouvez retourner vous connecter")
                        self.message_label.setStyleSheet("color : green ; font-size : 20px ; background : white ;")
                        self.message_label.setGeometry(300 , 30 , 500 , 25)
                    
                        self.username_input.clear()
                        self.password_input.clear()
                        self.mail_input.clear()
                except AssertionError:
                    self.message_label.setText("Donnees incorrecte !!!")
                    self.message_label.setStyleSheet("color : red ; font-size : 20px ; background : white ;")
                    self.message_label.setGeometry(300 , 30 , 450 , 25)



                    


        self.subs_button = QPushButton(text = " S' inscrire ")
        self.subs_button.setStyleSheet("color : white ; font-size : 20px ; background : blue ;border: 2px solid blue;border-radius: 6px;padding: 4px;")
        self.subs_button.clicked.connect(subs_login)
        hlayout3.addWidget(self.subs_button)
        hlayout3.addWidget(self.login_button)

