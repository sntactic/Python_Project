from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel , QHBoxLayout , QVBoxLayout
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QIcon
import json , os 

def get_user_data_dir():
    """Retourne un dossier de sauvegarde persistant dans le home de l'utilisateur"""
    path = os.path.join(os.path.expanduser("~"), ".MonApp")
    os.makedirs(path, exist_ok=True)
    return path

def get_csv_path(file):
    return os.path.join(get_user_data_dir(), file)

def get_json_path():
    return os.path.join(get_user_data_dir(), "Logs.json")

# Utilisation :
json_path = get_json_path()


class LoginWindow(QWidget):
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
            try :
                with open(json_path , "r", encoding = 'utf-8') as log :
                    if os.path.getsize(json_path) == 0 :
                        jregis = {}
                    else :
                        jregis = json.load(log)

                        self.username_input.clear()
                        self.password_input.clear()
                        assert jregis[username][0] == password 
                        self.hide()
                        csv_path = get_csv_path(jregis[username][1])
                        window = mywindow(csv_path  , username)
                        window.show()
            except  :
                self.message_label.setText("Nom d'utilisateur ou mot de passe incorrect !!!!!!!!!")
                self.message_label.setGeometry(300 , 230 , 450 , 25)

        
            

        # Connexion du bouton à la méthode de connexion
        self.login_button = QPushButton(text = "Se connecter")
        self.login_button.setStyleSheet("color : white ; font-size : 20px ; background : green ;border: 2px solid green;border-radius: 6px;padding: 4px;")
        self.login_button.clicked.connect(handle_login)

        self.installEventFilter(self)

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

        self.installEventFilter(self)
    def eventFilter(self, obj, event):
        if event.type() == event.KeyPress and event.key() == Qt.Key_Return:
            self.login_button.click() 
            return True 
        return super().eventFilter(obj, event)

        