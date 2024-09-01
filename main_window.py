from PyQt5.Qt import Qt #мобилизируем Qt из PyQt5
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QRadioButton, QSpinBox, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup
#загальна мобілізація
main_window = QWidget() #призвали вікно до військомату

main_window.resize(600, 500) #додали розмір(видали зарплату)
main_window.setWindowTitle("Memory Card")#дали ім'я
main_window.move(300, 300)# дає кординати для вікна

btn_menu = QPushButton("Меню")#меню
btn_sleep = QPushButton("Відпочити")#кнопка відпочинку

box_minutes = QSpinBox()#створення лічильника хвилин
box_minutes.setValue(30)#
box_minutes_lbl = QLabel("хвилин")#

lbl_question = QLabel("Question")#

answer_group_box = QGroupBox("Варіанти відповідей")#створення групи віджитів
radion_buttons_group = QButtonGroup()#створення групи для кнопок
#додаємо кнопки в групу
r_btn1 = QRadioButton("1")#
r_btn2 = QRadioButton("2")#
r_btn3 = QRadioButton("3")#
r_btn4 = QRadioButton("4")#
#
radion_buttons_group.addButton(r_btn1)#
radion_buttons_group.addButton(r_btn2)#
radion_buttons_group.addButton(r_btn3)#
radion_buttons_group.addButton(r_btn4)#

v_line1 = QVBoxLayout()#
v_line2 = QVBoxLayout()#
h_line = QHBoxLayout()#

v_line1.addWidget(r_btn1)#
v_line1.addWidget(r_btn2)#

v_line2.addWidget(r_btn3)#
v_line2.addWidget(r_btn4)#

h_line.addLayout(v_line1)#
h_line.addLayout(v_line2)
answer_group_box.setLayout(h_line)

result_group_box = QGroupBox("Результат теста")#створення групи віджетів
lbl_correct = QLabel("правильно")
lbl_right = QLabel("правильна відповідь")

result_line = QVBoxLayout()
result_line.addWidget(lbl_correct, alignment=(Qt.AlignLeft|Qt.AlignTop))
result_line.addWidget(lbl_right, alignment=Qt.AlignCenter, stretch=3)
result_group_box.setLayout(result_line)
result_group_box.hide()

btn_answer = QPushButton("відповісти")

line1 = QHBoxLayout()
line1.addWidget(btn_menu)
line1.addStretch(2)
line1.addWidget(btn_sleep)
line1.addWidget(box_minutes)
line1.addWidget(box_minutes_lbl)

main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addWidget(lbl_question, alignment=(Qt.AlignCenter|Qt.AlignCenter))

line2 = QHBoxLayout()
line2.addWidget(answer_group_box)
line2.addWidget(result_group_box)

main_line.addLayout(line2, stretch=4)
main_line.addWidget(btn_answer)
main_line.addStretch()
main_line.addWidget(btn_answer)


main_window.setLayout(main_line)