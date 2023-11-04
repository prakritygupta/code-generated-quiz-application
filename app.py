import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QFrame, QLineEdit, QRadioButton, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Quiz'
        self.left = 350
        self.top = 80
        self.width = 560
        self.height = 700
        self.setFixedSize(self.width, self.height)
        with open("design.qss",'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.setObjectName("main-window")
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


    #create
        self.quiz_label = QLabel(self)
        self.quiz_label.setText("Quiz")
        self.quiz_label.setObjectName("quiz-label")
        self.quiz_label.move(200,110)

        self.create_btn = QFrame(self)
        self.create_btn.setObjectName("buttons")
        self.create_btn.move(100,300)
        self.create_btn.mousePressEvent = self.create_clicked

        self.create_label = QLabel(self.create_btn)
        self.create_label.setObjectName("frame-heading")
        self.create_label.setText("Create a Quiz")
        self.create_label.move(85,25)

        self.create_expanded = QLabel(self)
        self.create_expanded.setObjectName("frame-exp")
        self.create_expanded.move(100,100)
        self.create_expanded.setVisible(False)

        #second page
        self.back_button_c = QLabel(self.create_expanded)
        self.back_button_c.move(20,5)
        self.back_button_c.setTextFormat(Qt.RichText)
        self.back_button_c.setText("&#8592;")
        self.back_button_c.setObjectName("back_button")
        self.back_button_c.mousePressEvent = self.back_button_clicked

        self.deco = QLabel(self.create_expanded)
        self.deco.setObjectName("deco")
        self.deco.setText("ecmce")
        self.deco.move(155,12)

        self.welcome = QLabel(self.create_expanded)
        self.welcome.move(85,50)
        self.welcome.setText("Welcome!")
        self.welcome.setObjectName("welcome")

        self.qname = QLabel(self.create_expanded)
        self.qname.setText("Name your quiz*:")
        self.qname.setObjectName("input_prompts")
        self.qname.move(30,150)

        self.name_input = QLineEdit(self.create_expanded)
        self.name_input.setObjectName("input")
        self.name_input.move(170,150)
        self.name_input.textChanged.connect(self.disable_btn)

        self.time_prompt = QLabel(self.create_expanded)
        self.time_prompt.setText("Time required?*")
        self.time_prompt.setObjectName("input_prompts")
        self.time_prompt.move(30,200)

        self.ans_y = QRadioButton(self.create_expanded)
        self.ans_y.setText("Yes")
        self.ans_y.setObjectName("input_prompts")
        self.ans_y.move(170,200)

        self.ans_n = QRadioButton(self.create_expanded)
        self.ans_n.setText("No")
        self.ans_n.setObjectName("input_prompts")
        self.ans_n.move(220,200)

        self.seconds = QLabel(self.create_expanded)
        self.seconds.setText("How many seconds needed?:")
        self.seconds.setObjectName("input_prompts")
        self.seconds.move(30,250)

        self.time_input = QLineEdit(self.create_expanded)
        self.time_input.setObjectName("time_input")
        self.time_input.move(260,250)

        self.start_create_btn = QPushButton(self.create_expanded)
        self.start_create_btn.setText("Start Creating!")
        self.start_create_btn.setObjectName("push-buttons")
        self.start_create_btn.move(75,350)
        #self.start_create_btn.setDisabled(True)
        self.start_create_btn.clicked.connect(self.start_c_clicked)

        self.req = QLabel(self.create_expanded)
        self.req.setText("*:Required field")
        self.req.setObjectName("ps")
        self.req.move(120,390)

        self.create_q_frame = QLabel(self)
        self.create_q_frame.setObjectName("frame-exp")
        self.create_q_frame.move(100,100)
        self.create_q_frame.setVisible(False)

        self.q_frame = QLabel(self.create_q_frame)
        self.q_frame.setObjectName("q-frame")
        self.q_frame.move(5,30)

        self.question = QLabel(self.q_frame)
        self.question.setObjectName("input_prompts")
        self.question.setText("Question:")
        self.question.move(10,5)

        self.q_input = QTextEdit(self.q_frame)
        self.q_input.setObjectName("question")
        self.q_input.move(10,25)

        self.marks = QLabel(self.q_frame)
        self.marks.setObjectName("input_prompts")
        self.marks.setText("Marks:")
        self.marks.move(10,75)

        self.marks_input = QLineEdit(self.q_frame)
        self.marks_input.setObjectName("time_input")
        self.marks_input.move(65,75)

        #self.instructions = QLabel(self.q_frame)
        #self.instructions.setText("--Fill in  the answers and choose the right one--")
        #self.instructions.setWordWrap(True)
        #self.instructions.setObjectName("input_prompts")
        #self.instructions.move(20,95)




    #join
        self.join_btn = QFrame(self)
        self.join_btn.setObjectName("buttons")
        self.join_btn.move(100,420)
        self.join_btn.mousePressEvent = self.join_clicked

        self.join_label = QLabel(self.join_btn)
        self.join_label.setObjectName("frame-heading")
        self.join_label.setText("Take a Quiz")
        self.join_label.move(85,25)

        self.join_expanded = QLabel(self)
        self.join_expanded.setObjectName("frame-exp")
        self.join_expanded.move(100,100)
        self.join_expanded.setVisible(False)

        #second page
        self.back_button_j = QLabel(self.join_expanded)
        self.back_button_j.move(20,5)
        self.back_button_j.setTextFormat(Qt.RichText)
        self.back_button_j.setText("&#8592;")
        self.back_button_j.setObjectName("back_button")
        self.back_button_j.mousePressEvent = self.back_button_clicked

        self.deco = QLabel(self.join_expanded)
        self.deco.setObjectName("deco")
        self.deco.setText("ecmce")
        self.deco.move(125,12)

        self.welcome = QLabel(self.join_expanded)
        self.welcome.move(55,50)
        self.welcome.setText("Welcome!")
        self.welcome.setObjectName("welcome")

        self.show()

    def create_clicked(self, event):
        self.create_expanded.setVisible(True)
        self.join_btn.setVisible(False)
        self.create_btn.setVisible(False)

    def join_clicked(self, event):
        self.join_expanded.setVisible(True)
        self.join_btn.setVisible(False)
        self.create_btn.setVisible(False)

    def back_button_clicked(self, event):
        self.create_expanded.setVisible(False)
        self.join_expanded.setVisible(False)
        self.join_btn.setVisible(True)
        self.create_btn.setVisible(True)

    def start_c_clicked(self):
        self.create_expanded.setVisible(False)
        self.create_q_frame.setVisible(True)

        
    def disable_btn(self):
        if len(self.name_input.text()) > 0:
            if self.ans_y.isChecked or self.ans_n.isChecked:
                self.start_create_btn.setDisabled(False)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())