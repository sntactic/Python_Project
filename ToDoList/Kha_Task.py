from PyQt5.QtWidgets import QApplication 
from Login import LoginWindow
import sys

app = QApplication(sys.argv)

login_window = LoginWindow()
login_window.show()

sys.exit(app.exec_())
