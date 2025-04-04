from PyQt5.QtWidgets import QApplication , QWidget
from Login import LoginWindow
from Main import mywindow
import sys

app = QApplication(sys.argv)

login_window = LoginWindow()
login_window.show()


sys.exit(app.exec_())
