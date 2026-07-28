import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(200, 200, 500, 500)
        self.sonuc = 0
        self.initUI()




    def initUI(self):
        self.lbl_sayi1= QLabel(self)
        self.lbl_sayi1.setText("Sayı 1:")
        self.lbl_sayi1.move(50, 30)

        self.txt_sayi1= QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150, 30)
        self.txt_sayi1.resize(200, 32)

        self.lbl_sayi2= QLabel(self)
        self.lbl_sayi2.setText("Sayı 2:")
        self.lbl_sayi2.move(50, 80)

        self.txt_sayi2= QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150, 80)
        self.txt_sayi2.resize(200, 32)

        self.btn_toplama = QPushButton(self)
        self.btn_toplama.setText("Toplama")
        self.btn_toplama.move(150, 130)
        self.btn_toplama.clicked.connect(self.toplama)

        self.btn_cikarma = QPushButton(self)
        self.btn_cikarma.setText("Çıkarma") 
        self.btn_cikarma.move(150, 180)
        self.btn_cikarma.clicked.connect(self.cikarma)

        self.btn_carpma = QPushButton(self)
        self.btn_carpma.setText("Çarpma")   
        self.btn_carpma.move(150, 230)
        self.btn_carpma.clicked.connect(self.carpma)

        self.btn_bolme = QPushButton(self)
        self.btn_bolme.setText("Bölme")
        self.btn_bolme.move(150, 280)   
        self.btn_bolme.clicked.connect(self.bolme)

        self.lbl_sonuc = QLabel(self)
        self.lbl_sonuc.move(150, 330)
        self.lbl_sonuc.setText("Sonuç: " + str(self.sonuc))


    def toplama(self):
        result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç: " + str(result))
        

    def cikarma(self):
        result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç: " + str(result))

    def carpma(self):
        result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç: " + str(result))

    def bolme(self):
        result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç: " + str(result))


           

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()