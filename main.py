from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()


mainLine = QVBoxLayout()
window.resize(500, 500)

menu8tn = QPushButton("меню")
rest8tn = QPushButton("Відпочити від ігора")
timeSpn = QSpinBox()
timeLbl = QLabel("хвилини до до нападу ігора з кавою на жопі")

hyra = QLabel("Яблуко")

firstLine = QHBoxLayout()
firstLine.addWidget(menu8tn)
firstLine.addWidget(rest8tn)
firstLine.addWidget(timeSpn)
firstLine.addWidget(timeLbl)
firstLine.addWidget(hyra)
mainLine.addLayout(firstLine)

answersGroup = QGroupBox("Варіанти відповідей")
answer1 = QRadioButton("1")
answer2 = QRadioButton("2")
answer3 = QRadioButton("3")
answer4 = QRadioButton("4")
answersLine = QVBoxLayout()
answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)
answersGroup.setLayout(answersLine)
mainLine.addWidget(answersGroup)


window.setLayout(mainLine)
window.show()
app.exec()