import sys
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton, 
    QTextEdit, 
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.resize(300,300)
        
        mainWidget = QWidget()
        
        self.line_edit = QLineEdit(parent=self)
        
        button = QPushButton("Hey")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        
        self.label = QLabel(parent=self)
        self.line_edit.textEdited.connect(self.update_label)
        
        button.clicked.connect(self.theButtonWasToggled)

    
        layout = QVBoxLayout(self)
        
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)
        layout.addWidget(button)
        
        self.setLayout(layout)
    def the_button_was_clicked(self):
        self.label.setText(self.line_edit.text())
        print(self.line_edit.text())
    def theButtonWasToggled(self, checked):
        print("TOGGLE", checked)
        
    def update_label(self):
        self.label.setText(self.line_edit.text())

app = QApplication()

window = MainWindow()
window.show()

app.exec()
