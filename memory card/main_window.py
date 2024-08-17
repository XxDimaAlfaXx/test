from msilib.schema import RadioButton
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
app = QApplication([])

main_window = QWidget()

rbutton1 = QRadioButton("caterpillar")
rbutton2 = QRadioButton("application")
rbutton3 = QRadioButton("apple")
rbutton4 = QRadioButton("building")

minutes = QLabel("хвилини")
answer = QLabel("Відповісти")

menu_button = QPushButton('меню')
reset_button = QPushButton('відпочити')
answerbutton = QPushButton('яблуко')

box_minutes = QSpinBox()

radioGroup = QButtonGroup()

radioGroup.addButton(rbutton1)
radioGroup.addButton(rbutton2)
radioGroup.addButton(rbutton3)
radioGroup.addButton(rbutton4)

radioGroupBox = QGroupBox("варінти відповідей")

hlayaout1 = QHBoxLayout()
hlayaout2 = QHBoxLayout()
hlayaout3 = QHBoxLayout()
hlayaout4 = QHBoxLayout()

hlayaout1.addWidget(menu_button, alignment = (Qt.AlignLeft | Qt.AlignTop))
hlayaout1.addWidget(reset_button)
hlayaout1.addWidget(box_minutes)
hlayaout1.addWidget(minutes)

hlayaout2.addWidget(answer, alignment = Qt.AlignCenter)



vlayaout1 = QVBoxLayout()
vlayaout2 = QVBoxLayout()

vlayaout1.addWidget(rbutton1)
vlayaout1.addWidget(rbutton2)

vlayaout2.addWidget(rbutton3)
vlayaout2.addWidget(rbutton4)

hbuttonlayout = QHBoxLayout()
hbuttonlayout.addLayout(vlayaout1)
hbuttonlayout.addLayout(vlayaout2)



radioGroupBox.setLayout(hbuttonlayout)

hlayaout3.addWidget(radioGroupBox)

hlayaout4.addWidget(answerbutton)

main_layout = QVBoxLayout()

main_layout.addLayout(hlayaout1)
main_layout.addLayout(hlayaout2)
main_layout.addLayout(hlayaout3)
main_layout.addLayout(hlayaout4)

main_window.setLayout(main_layout)

main_window.show()
app.exec_()