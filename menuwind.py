from PyQt5.QtWidgets import *

import base


def menuWind() :
    window = QDialog()
    window.resize(550,440)

    questLbl = QLabel("питання")
    questEdit = QLineEdit()


    rightAnswerLbl = QLabel("правильна відповідь")

    add8th = QPushButton("добавити")



    mainLine = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(questLbl)
    h1.addWidget(questEdit)
    mainLine.addLayout(mainLine)

    h2 = QHBoxLayout()
    h2.addWidget(rightAnswerLbl)

    def addFuns():
        base.qeust.appent(

            {
                "питання:": questEdit.text(),
                "правильеа відповідь": "ЯЛКВОМ",
                "неправильна1": "введіть текст",
                "неправильна2": "4",
                "неправильна3": "фісташки",

            },
        )


    mainLine.addLayout(add8th)


    window.setLayout(mainLine)
    window.show()
    window.exec()