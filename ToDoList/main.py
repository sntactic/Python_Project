from PyQt5.QtWidgets import QApplication , QWidget
from login import LoginWindow
import sys

app = QApplication(sys.argv)
scroll_win = QWidget()

login_window = LoginWindow()
login_window.show()

sys.exit(app.exec_())
