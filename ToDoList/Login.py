from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel , QHBoxLayout , QVBoxLayout
import json , os


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Page de Connexion")
        self.setStyleSheet("background : white;")
        self.move(200 , 100)
        self.resize(1080 , 720)
        

        vlayout = QVBoxLayout()
        vlayout.setSpacing(100)
        self.setLayout(vlayout)

        hlayout1 = QHBoxLayout()
        vlayout.addLayout(hlayout1)

        hlayout2 = QHBoxLayout()
        vlayout.addLayout(hlayout2)

        hlayout3 = QHBoxLayout()
        vlayout.addLayout(hlayout3)


        vlayout.addLayout(hlayout2)
        
        self.username_input = QLineEdit()
        self.username_input.setMinimumHeight(35)
        self.username_input.setPlaceholderText("Entrez votre adresse e-mail ")
        self.username_input.setStyleSheet("color : black ; font-size : 18px ; background : white ;border: 2px solid #000000;border-radius: 6px;padding: 4px;")
        hlayout1.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setMinimumHeight(35)
        self.password_input.setPlaceholderText("Entrez votre mot de passe de utilisateur")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("color : black ; font-size : 18px ; background : white ;border: 2px solid #000000;border-radius: 6px;padding: 4px;")
        hlayout2.addWidget(self.password_input)

        
        self.message_label = QLabel(self)
        self.message_label.setStyleSheet("color : red ; font-size : 20px ; background : white ;")

        def handle_login():
            from Main import mywindow
            global log
            username = self.username_input.text()
            password = self.password_input.text()
            
            with open("Logs.json" , "r", encoding = 'utf-8') as log :
                if os.path.getsize("Logs.json") == 0 :
                    jregis = {}
                else :
                    jregis = json.load(log)

                try :
                    self.username_input.clear()
                    self.password_input.clear()
                    assert jregis[username][0] == password 
                    window = mywindow(jregis[username][1])
                    window.show()
                    self.deleteLater()
                except :
                    self.message_label.setText("Nom d'utilisateur ou mot de passe incorrect !!!!!!!!!")
                    self.message_label.setGeometry(300 , 230 , 450 , 25)

        
            

        # Connexion du bouton à la méthode de connexion
        self.login_button = QPushButton(text = "Se connecter")
        self.login_button.setStyleSheet("color : white ; font-size : 20px ; background : green ;border: 2px solid green;border-radius: 6px;padding: 4px;")
        self.login_button.clicked.connect(handle_login)

        hlayout3.addWidget(self.login_button)

        def handle_subs():
            from Subscribe import subs
            subs_window = subs()
            subs_window.show()
            self.deleteLater()


        self.subs_button = QPushButton(text = " Creer un compte ")
        self.subs_button.setStyleSheet("color : white ; font-size : 20px ; background : blue ;border: 2px solid blue ;border-radius: 6px;padding: 4px;")
        self.subs_button.clicked.connect(handle_subs)
        hlayout3.addWidget(self.subs_button)

        