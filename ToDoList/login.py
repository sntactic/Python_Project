from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel , QHBoxLayout , QVBoxLayout
from to_do_list import mywindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Page de Connexion")
        self.setStyleSheet("background : white;")
        self.move(220 , 100)
        

        vlayout = QVBoxLayout()
        vlayout.setSpacing(100)
        vlayout.setContentsMargins(0, 200, 0, 200)
        self.setLayout(vlayout)

        hlayout1 = QHBoxLayout()
        hlayout1.setContentsMargins(200, 0, 200, 0)
        hlayout1.setSpacing(20)
        vlayout.addLayout(hlayout1)

        hlayout2 = QHBoxLayout()
        hlayout2.setContentsMargins(250, 0 , 250, 0)
        hlayout2.setSpacing(30)
        vlayout.addLayout(hlayout2)

        hlayout3 = QHBoxLayout()
        hlayout3.setContentsMargins(440, 0, 440, 0)
        vlayout.addLayout(hlayout3)


        vlayout.addLayout(hlayout2)
        
        # Création des éléments de l'interface
        self.username_label = QLabel(text = "Nom d'utilisateur")
        self.username_label.setStyleSheet("color : black ; font-size : 20px ; background : white ;")
        hlayout1.addWidget(self.username_label)

        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("color : black ; font-size : 18px ; background : grey ;")
        hlayout1.addWidget(self.username_input)

        self.password_label = QLabel(text = "Mot de passe")
        self.password_label.setStyleSheet("color : black ; font-size : 20px ; background : white ;")
        hlayout2.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("color : black ; font-size : 25px ; background : grey ;")
        hlayout2.addWidget(self.password_input)

        
        self.message_label = QLabel(self)
        self.message_label.setStyleSheet("color : red ; font-size : 20px ; background : white ;")

        def handle_login():
            global log
            username = self.username_input.text()
            password = self.password_input.text()
            if username != "" or password != "":
                self.message_label.setText("Nom d'utilisateur ou mot de passe incorrect !!!!!!!!!")
                self.message_label.setGeometry(300 , 140 , 450 , 25)
            else :
                window = mywindow().show()
                self.deleteLater()

        # Connexion du bouton à la méthode de connexion
        self.login_button = QPushButton(text = "Se connecter")
        self.login_button.setStyleSheet("color : blue ; font-size : 20px ; background : white ;")
        self.login_button.clicked.connect(handle_login)

        hlayout3.addWidget(self.login_button)
        