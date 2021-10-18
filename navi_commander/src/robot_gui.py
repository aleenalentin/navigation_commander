#!/usr/bin/env python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import rospy
from std_msgs.msg import String

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
        rospy.init_node('ros_gui', anonymous=True)
        self.pub = rospy.Publisher('/chatter', String, queue_size=10)    

    def button_clicked0(self):
        self.label.setText("Move to table A")
        self.vel1 = String()
        self.vel1.data = "A"
        tableA= self.vel1.data
        rospy.loginfo("table A = %s",tableA)
        self.pub.publish(self.vel1)
        self.update()
    def button_clicked1(self):
        self.label.setText("Move to table B")
        self.vel1 = String()
        self.vel1.data = "B"
        tableB= self.vel1.data
        rospy.loginfo("table B = %s",tableB)
        self.pub.publish(self.vel1)
        self.update()
    def button_clicked2(self):
        self.label.setText("Move to table C")
        self.vel1 = String()
        self.vel1.data = "C"
        tableC= self.vel1.data
        rospy.loginfo("table C = %s",tableC)
        self.pub.publish(self.vel1)
        self.update()
    def button_clicked3(self):
        self.label.setText("Move to table D")
        self.vel1 = String()
        self.vel1.data = "D"
        tableD= self.vel1.data
        rospy.loginfo("table D = %s",tableD)
        self.pub.publish(self.vel1)
        self.update()
    def button_clicked4(self):
        self.label.setText("Move to table E")
        self.vel1 = String()
        self.vel1.data = "E"
        tableE= self.vel1.data
        rospy.loginfo("table E = %s",tableE)
        self.pub.publish(self.vel1)
        self.update()   
    def button_clicked5(self):
        self.label.setText("Move to table F")
        self.vel1 = String()
        self.vel1.data = "F"
        tableF= self.vel1.data
        rospy.loginfo("table F = %s",tableF)
        self.pub.publish(self.vel1)
        self.update() 
    def button_clicked6(self):
        self.label.setText("Move to table G")
        self.vel1 = String()
        self.vel1.data = "G"
        tableG= self.vel1.data
        rospy.loginfo("table G = %s",tableG)
        self.pub.publish(self.vel1)
        self.update()
    def button_clicked7(self):
        self.label.setText("Move to table H")
        self.vel1 = String()
        self.vel1.data = "H"
        tableH= self.vel1.data
        rospy.loginfo("table H = %s",tableH)
        self.pub.publish(self.vel1)
        self.update() 
    def button_clicked8(self):
        self.label.setText("Move to table I")
        self.vel1 = String()
        self.vel1.data = "I"
        tableI= self.vel1.data
        rospy.loginfo("table I = %s",tableI)
        self.pub.publish(self.vel1)
        self.update()   
    def button_clicked9(self):
        self.label.setText("Move to table HOME")
        self.vel1 = String()
        self.vel1.data = "HOME"
        tableI= self.vel1.data
        rospy.loginfo("table HOME = %s",tableI)
        self.pub.publish(self.vel1)
        self.update()  
    def initUI(self):
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("ROBOT-GUI")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("click a button ")
        self.label.move(200,300)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("G")
        self.b1.clicked.connect(self.button_clicked6)
        self.b1.move(10,10)
        
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("H")
        self.b2.clicked.connect(self.button_clicked7)
        self.b2.move(115,10)
        
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("I")
        self.b3.clicked.connect(self.button_clicked8)
        self.b3.move(220,10)
        
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("F")
        self.b4.clicked.connect(self.button_clicked5)
        self.b4.move(10,50)
        
        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setText("E")
        self.b5.clicked.connect(self.button_clicked4)
        self.b5.move(115,50)
        
        self.b6 = QtWidgets.QPushButton(self)
        self.b6.setText("D")
        self.b6.clicked.connect(self.button_clicked3)
        self.b6.move(220,50)
        
        self.b7 = QtWidgets.QPushButton(self)
        self.b7.setText("A")
        self.b7.clicked.connect(self.button_clicked0)
        self.b7.move(10,90)
      
        self.b8 = QtWidgets.QPushButton(self)
        self.b8.setText("B")
        self.b8.clicked.connect(self.button_clicked1)
        self.b8.move(115,90)
        
        self.b9 = QtWidgets.QPushButton(self)
        self.b9.setText("C")
        self.b9.clicked.connect(self.button_clicked2)
        self.b9.move(220,90)
        
        self.b10 = QtWidgets.QPushButton(self)
        self.b10.setText("HOME")
        self.b10.clicked.connect(self.button_clicked9)
        self.b10.move(115,130)
        
    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()

