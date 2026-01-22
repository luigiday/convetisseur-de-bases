try:
    from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PyQt6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGroupBox,
        QLabel, QMainWindow, QPushButton, QSizePolicy,
        QSpinBox, QTabWidget, QWidget, QMessageBox, QStyleFactory)
    import sys
except ImportError as e:
    print(f"Erreur d'importation de module PyQt6 : {e}")
    import sys
    sys.exit(1)

def complementa2(n):
    nb = bin(n)
    if n >= 0:
        nb = nb[2:]
        if len(nb) < 8:
            nblist = []
            for i in range(8-len(nb)):
                nblist.append(0)
        elif len(nb) < 16:
            nblist = []
            for i in range(16-len(nb)):
                nblist.append(0)
        elif len(nb) < 32:
            nblist = []
            for i in range(32-len(nb)):
                nblist.append(0)
        elif len(nb) < 64:
            nblist = []
            for i in range(64-len(nb)):
                nblist.append(0)
        for x in nb:
            nblist.append(int(x))
        detail = "Conversion normale en binaire"
        return(nblist, detail)
    else:
        nb = nb[3:]
        detail = "Nombre negatif :"
        if len(nb) < 8:
            nblist = []
            for i in range(8-len(nb)):
                nblist.append(0)
            for x in nb:
                nblist.append(int(x))
            detail += f"\nConversion en binaire sur 8 bits : {nblist}"
            for i, e in enumerate(nblist):
                nblist[i] = 1 - e
            detail += f"\nInversion des bits : {nblist}"
            carry = 1
            for i in range(7, -1, -1):
                if nblist[i] == 1 and carry == 1:
                    nblist[i] = 0
                elif nblist[i] == 0 and carry == 1:
                    nblist[i] = 1
                    carry = 0
            detail += f"\nAjout de 1 : {nblist}\n"
        elif len(nb) < 16:
            nblist = []
            for i in range(16-len(nb)):
                nblist.append(0)
            for x in nb:
                nblist.append(int(x))
            detail += f"\nConversion en binaire sur 16 bits : {nblist}"
            for i, e in enumerate(nblist):
                nblist[i] = 1 - e
            detail += f"\nInversion des bits : {nblist}"
            carry = 1
            for i in range(15, -1, -1):
                if nblist[i] == 1 and carry == 1:
                    nblist[i] = 0
                elif nblist[i] == 0 and carry == 1:
                    nblist[i] = 1
                    carry = 0
            detail += f"\nAjout de 1 : {nblist}\n"
        elif len(nb) < 32:
            nblist = []
            for i in range(32-len(nb)):
                nblist.append(0)
            for x in nb:
                nblist.append(int(x))
            detail += f"\nConversion en binaire sur 32 bits : {nblist}"
            for i, e in enumerate(nblist):
                nblist[i] = 1 - e
            detail += f"\nInversion des bits : {nblist}"
            carry = 1
            for i in range(31, -1, -1):
                if nblist[i] == 1 and carry == 1:
                    nblist[i] = 0
                elif nblist[i] == 0 and carry == 1:
                    nblist[i] = 1
                    carry = 0
            detail += f"\nAjout de 1 : {nblist}\n"
        elif len(nb) < 64:
            nblist = []
            for i in range(64-len(nb)):
                nblist.append(0)
            for x in nb:
                nblist.append(int(x))
            detail += f"\nConversion en binaire sur 64 bits : {nblist}"
            for i, e in enumerate(nblist):
                nblist[i] = 1 - e
            detail += f"\nInversion des bits : {nblist}"
            carry = 1
            for i in range(63, -1, -1):
                if nblist[i] == 1 and carry == 1:
                    nblist[i] = 0
                elif nblist[i] == 0 and carry == 1:
                    nblist[i] = 1
                    carry = 0
            detail += f"\nAjout de 1 : {nblist}\n"
        else:
            raise ValueError("Le nombre est trop grand pour être représenté en complément à 2 sur 64 bits")
        return(nblist, detail)

class UserInterface(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(490, 380)
        MainWindow.setMinimumSize(QSize(490, 380))
        MainWindow.setMaximumSize(QSize(490, 380))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 441, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 481, 18))
        self.btn_infos = QPushButton(self.centralwidget)
        self.btn_infos.setObjectName(u"btn_infos")
        self.btn_infos.setGeometry(QRect(442, 10, 40, 34))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 70, 491, 301))
        self.input_complement_a_2 = QSpinBox(self.frame)
        self.input_complement_a_2.setObjectName(u"input_complement_a_2")
        self.input_complement_a_2.setGeometry(QRect(11, 10, 471, 32))
        self.input_complement_a_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.input_complement_a_2.setMinimum(-999999999)
        self.input_complement_a_2.setMaximum(999999999)
        self.input_complement_a_2.setDisplayIntegerBase(10)
        self.btn_complement_a_2 = QPushButton(self.frame)
        self.btn_complement_a_2.setObjectName(u"btn_complement_a_2")
        self.btn_complement_a_2.setGeometry(QRect(11, 50, 471, 41))
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 100, 471, 61))
        self.sortie_complement_a_2 = QLabel(self.groupBox_2)
        self.sortie_complement_a_2.setObjectName(u"sortie_complement_a_2")
        self.sortie_complement_a_2.setGeometry(QRect(17, 27, 439, 26))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.sortie_complement_a_2.setFont(font1)
        self.sortie_complement_a_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sortie_complement_a_2.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 170, 471, 131))
        self.details_label = QLabel(self.groupBox_3)
        self.details_label.setObjectName(u"details_label")
        self.details_label.setGeometry(QRect(17, 30, 431, 81))
        self.details_label.setScaledContents(True)
        self.details_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.details_label.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Complement a 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Complement a 2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Calcule le complement a 2 pour un nombre donn\u00e9", None))
#if QT_CONFIG(tooltip)
        self.btn_infos.setToolTip(QCoreApplication.translate("MainWindow", u"A propos", None))
#endif // QT_CONFIG(tooltip)
        self.btn_infos.setText(QCoreApplication.translate("MainWindow", u"\u2139\ufe0f", None))
        self.btn_complement_a_2.setText(QCoreApplication.translate("MainWindow", u"Complement a 2", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"R\u00e9sultat", None))
        self.sortie_complement_a_2.setText(QCoreApplication.translate("MainWindow", u"[0,0,0,0,0,0,0,0]", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"D\u00e9tails", None))
        self.details_label.setText(QCoreApplication.translate("MainWindow", u"Attente d'une entr\u00e9e", None))
    # retranslateUi


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.btn_complement_a_2.clicked.connect(self.convert_complement_a_2)
        self.btn_infos.clicked.connect(self.convertir_les_bases)

    def convert_complement_a_2(self):
        try:
            n = int(self.input_complement_a_2.text())
            binary_list, details = complementa2(n)
            s = ''.join(map(str, binary_list))
            grouped = ' '.join(s[i:i+4] for i in range(0, len(s), 4))
            self.sortie_complement_a_2.setText(grouped)
            self.details_label.setText(details)
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Veuillez entrer un nombre entier valide.")
    def convertir_les_bases(self):
        QMessageBox.information(self, "A propos", "Appli codé avec 🧡 par Luigiday\nhttps://github.com/luigiday\nVersion 1.0")

if __name__ == "__main__":
    debug_allow = False
    app = QApplication(sys.argv)
    # Prefer Breeze if available, otherwise fall back to Fusion and warn.
    try:
        available = QStyleFactory.keys()
        if 'Breeze' in available:
            app.setStyle('Breeze')
        else:
            print('Breeze style not installed; available styles:', available)
            try:
                QMessageBox.information(None, 'Style',
                    'Breeze not installed; using fallback (Fusion).\nAvailable: ' + ', '.join(available))
            except Exception:
                pass
            try:
                app.setStyle('Fusion')
            except Exception:
                pass
    except Exception as e:
        print('Error while setting style:', e)
    mainwin = UserInterface()
    mainwin.show()
    sys.exit(app.exec())
