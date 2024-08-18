from PyQt5.Qt import Qt #мобилизируем Qt из PyQt5
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel,  QHBoxLayout, QVBoxLayout, QButtonGroup, QTextEdit

menu_window = QWidget()
menu_window.resize(400, 300) 
menu_window.setWindowTitle("Memory card")
menu_window.move(700, 300)