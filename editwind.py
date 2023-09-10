from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel

import base

def editwindow():
    window = QDialog()
    window.resize(380,380)
    editbut = QPushButton("Редагувати.")

    h3 = QHBoxLayout()
    editienqe = QLabel("питання")
    queedit