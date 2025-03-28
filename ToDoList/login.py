from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel
from to_do_list import mywindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Page de Connexion")
        self.setGeometry(150, 100, 1080, 720)
        self.setStyleSheet("background : white;")
        
        # Création des éléments de l'interface
        self.username_label = QLabel(self , text = "Nom d'utilisateur:")
        self.username_label.setStyleSheet("color : black ; font-size : 20px ; background : white ;")
        self.username_label.move(280 , 200)
        
        self.username_input = QLineEdit(self)
        self.username_input.setStyleSheet("color : black ; font-size : 25px ; background : grey ;")
        self.username_input.setGeometry(450 , 200 , 300 , 25)
        
        self.password_label = QLabel(self , text = "Mot de passe:")
        self.password_label.setStyleSheet("color : black ; font-size : 20px ; background : white ;")
        self.password_label.move(280 , 280)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("color : black ; font-size : 25px ; background : grey ;")
        self.password_input.setGeometry(450 , 280 , 300 , 25)
        
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
        self.login_button = QPushButton(self , text = "Se connecter")
        self.login_button.setGeometry(420 , 380 , 160 , 25)
        self.login_button.setStyleSheet("color : blue ; font-size : 20px ; background : white ;")
        self.login_button.clicked.connect(handle_login)

