from datetime import datetime
import sys,typing
from PyQt5.QtCore import QRect , Qt
from PyQt5.QtWidgets import ( QCheckBox, QComboBox, 
QGroupBox,  QLabel, QVBoxLayout,QPushButton,QAbstractItemView, QGridLayout ,

QWidget)
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
from mainclass import Hiraj
from MyPyQt5 import MyQTreeWidget ,MyMessageBox, MyThread,AnimatedToggle ,QSideMenuEnteredLeaved ,MyCustomContextMenu
import pyperclip
from styles import Styles
import sqlite3
from sqlite3 import IntegrityError, OperationalError



class Ui_MainWindow(object):
    Name = ""
    msg = MyMessageBox()
    CATEGORIES = ['حراج السيارات', 'حراج العقار', 'حراج الأجهزة', 'مواشي وحيوانات وطيور', 'اثاث', 'مستلزمات شخصية', 'خدمات', 'وظائف', 'اطعمة ومشروبات', 'برمجة وتصاميم', 'مكتبة وفنون', 'صيد ورحلات']
    SUBCATEGORY = [['', 'هونشي', 'زوتي', 'ماهيندرا', 'ساوايست', 'تسلا', 'بايك', 'جاك JAC', 'ماكلارين', 'ماكسيس', 'ليفان', 'فيكتوري اوتو', 'فوتون', 'سي ام سي', 'جيتور', 'جى ام سي JMC', 'تاتا', 'الفا روميو', 'BYD', 'فاو FAW', 'جريت وول Great Wall', 'جي ايه سي GAC', 'هافال', 'بروتون', 'استون مارتن', 'سانج يونج', 'فيات', 'ساب', 'دايو', 'سيات', 'تشيري', 'سيتروين', 'فيراري', 'سكودا', 'اوبل', 'لامبورجيني', 'رولز رويس', 'مازيراتي', 'بيوك', ' رينو', 'شانجان', 'ZXAUTO', 'MG', 'سوبارو', 'جاكوار', 'بنتلي', 'بيجو', 'فولفو', 'ميركوري', 'جيلي', 'ديهاتسو', 'فولكس واجن', 'لنكولن', 'همر', 'انفنيتي', 'سوزوكي', 'اودي', 'بورش', 'كاديلاك', 'ايسوزو', 'لاند روفر', 'مازدا', 'ميتسوبيشي', 'جيب','كرايزلر', 'دودج', 'كيا', 'دبابات', 'بي ام دبليو', 'هوندا', 'مرسيدس', 'شاحنات ومعدات ثقيلة', 'جي ام سي', 'لكزس', 'جنسس', 'هونداي', 'نيسان', 'قطع غيار وملحقات', 'شيفروليه', 'فورد', 'تويوتا'], ['', 'بيوت للايجار', 'ادوار للايجار', 'مزارع للبيع', 'فلل للايجار', 'استراحات للبيع', 'عماره للايجار', 'محلات للايجار', 'محلات للتقبيل', 'استراحات للايجار', 'عمارة للبيع', 'اراضي تجارية للبيع', 'بيوت للبيع', 'شقق للبيع', 'فلل للبيع', 'شقق للايجار', 'اراضي للبيع'], ['', 'غسالة سامسونج', 'ثلاجة سامسونج', 'اجهزة غير مصنفة', 'هيتاشي Hitachi', 'باناسونيك Panasonic', 'مايكروسوفت Microsoft', 'ال جي LG', 'أرقام مميزة', 'حسابات واشتراكات', 'كاميرات تصوير', 'تلفزيونات وصوتيات', 'ألعاب إلكترونية', 'أجهزة كمبيوتر', 'أجهزة تابلت', 'جوالات'], ['', 'وبر', 'هامستر', 'سناجب', 'بط', 'ارانب', 'أسماك وسلاحف', 'بقر', 'كلاب', 'خيل', 'أبل', 'دجاج', 'قطط', 'حمام', 'ببغاء', 'ماعز', 'غنم'], ['', 'مجالس ومفروشات', 'طاولات وكراسي', 'خزائن ودواليب', 'تحف وديكور', 'أسرة ومراتب', 'أدوات منزلية', 'أثاث مكتبي', 'أثاث خارجي'], ['', 'ملابس أطفال', 'ملابس نسائية', 'ملابس رجالية', 'نظارات', 'مستلزمات رياضية', 'عطورات', 'ساعات'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات','زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفروسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['']]
    AREAS = ["كل المناطق","الرياض","الشرقيه","جده","مكه","ينبع","حفر الباطن","المدينة","الطايف","تبوك","القصيم","حائل","أبها","عسير","الباحة","جيزان","نجران","الجوف","عرعر","الكويت","الإمارات","البحرين"]
    WIDTH = 550
    HIGHT = 400
    def setupUi(self, MainWindow:QMainWindow):
        self.font = QtGui.QFont()
        self.font.setFamily("Poor Richard")
        self.font.setPointSize(12)
        self.con = sqlite3.connect("Data/DataBase.db")
        self.curser = self.con.cursor()

        MainWindow.setFixedWidth(self.WIDTH)
        MainWindow.setFixedHeight(self.HIGHT)
        
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.Menu = QSideMenuEnteredLeaved(
            self.centralwidget,
            ButtonsCount=2,
            ExitButtonIconPath="Data/Icons/reject.png" ,
            DefultIconPath="Data/Icons/list.png",
            ClickIconPath="Data/Icons/arrowheads-of-thin-outline-to-the-left.png",
            MaxButtonIconPath="Data\Icons\maximize.png",
            Mini_MaxButtonIconPath="Data\Icons\minimize.png",
            MiniButtonIconPath="Data\Icons\delete.png",
            ButtonsFixedHight=40 ,
            ButtonsFrameFixedwidthMini= 40 ,
        )   
        # Stytles -----------
        self.Menu.TopFrame.setStyleSheet(Styles.PALET)
        self.Menu.ButtonsFrame.setStyleSheet(Styles.PALET)
        MainWindow.setFont(self.font)
        self.page1 = self.Menu.GetPage(0)
        self.Menu.setCurrentPage(1)
        self.page2 = self.Menu.GetPage(1)
        self.ButtonDashBoard = self.Menu.GetButton(0)
        self.ButtonDashBoard.setText("DashBoard")
        self.Menu.setButtonIcon(0,"Data/Icons/dashboard.png")
        self.Menu.setButtonIcon(1,"Data/Icons/setting.png")
        self.ButtonSetting = self.Menu.GetButton(1)
        self.ButtonSetting.setText("Setting")
        self.gridLayout = QGridLayout(self.page2)
        self.treewidget = MyQTreeWidget(self.page2,counterLabel=None)
        self.treewidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treewidget.customContextMenuRequested.connect(self.menu)###
        self.framecounts = QtWidgets.QFrame(self.page2)
        self.Hframecount = QtWidgets.QHBoxLayout(self.framecounts)
        self.countlabel = QLabel(self.framecounts)
        self.countlabel.setText("Count : 0 ")
        self.Hframecount.addWidget(self.countlabel,1,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.countchildlabel = QLabel(self.framecounts)
        self.countchildlabel.setText("Comment: 0 ")
        self.Hframecount.addWidget(self.countchildlabel,1,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.countotalabel = QLabel(self.framecounts)
        self.countotalabel.setText("Total: 0 ")
        self.Hframecount.addWidget(self.countotalabel,1,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Menu.MainLabel.setText("Statues")
        self.frameButtons = QtWidgets.QFrame(self.page1)
        self.Hframe = QtWidgets.QHBoxLayout(self.frameButtons)
        self.Hframe.setContentsMargins(0,0,0,0)
        self.ButtonStart = QtWidgets.QPushButton(self.frameButtons)
        self.ButtonStop = QtWidgets.QPushButton(self.frameButtons)
        self.ButtonStart.setText("Start")
        self.ButtonStop.setText("Stop")
        self.ButtonStop.setIcon(QtGui.QIcon("Data/Icons/no-stopping.png"))
        self.ButtonStart.setIcon(QtGui.QIcon("Data/Icons/play.png"))
        self.ButtonStart.setFlat(True)
        self.ButtonStop.setFlat(True)
        self.Hframe.addWidget(self.ButtonStart)
        self.Hframe.addWidget(self.ButtonStop)
        self.gridLayout.addWidget(self.frameButtons)
        self.gridLayout.addWidget(self.treewidget)
        self.gridLayout.addWidget(self.framecounts)
        self.verticalLayout_main = QVBoxLayout(self.page1)
        self.groupBox = QtWidgets.QGroupBox(self.page1)
        self.groupBox.setTitle("Link Only")
        self.verticalLayout_main.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page1)
        self.groupBox_2.setTitle("Normal")
        self.verticalLayout_main.addWidget(self.groupBox_2)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setStretch(0,3)
        self.verticalLayout.setStretch(1,1)
        self.verticalLayout.setStretch(2,1)
        self.verticalLayout.setStretch(3,1)
        self.frame = QtWidgets.QFrame(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("KeyWord")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setText("Category")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.comboboxfont = QtGui.QFont()
        self.comboboxfont.setFamily("Arabic Typesetting")
        self.comboboxfont.setPointSize(18)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setFont(self.comboboxfont)
        self.comboBox_4.addItems(["كل الاقسام"]+self.CATEGORIES)
        self.horizontalLayout_3.addWidget(self.comboBox_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.groupBox_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setText("SubCategory")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_5.setFont(self.comboboxfont)
        self.horizontalLayout_4.addWidget(self.comboBox_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.groupBox_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setText("Area")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_6.setFont(self.comboboxfont)
        self.comboBox_6.addItems(self.AREAS)
        self.horizontalLayout_5.addWidget(self.comboBox_6)
        self.verticalLayout.addWidget(self.frame_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.page1)
        self.groupBox_3.setTitle("Setting")
        self.verticalLayout_main.addWidget(self.groupBox_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.frame_7 = QtWidgets.QFrame(self.groupBox_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setText("Limit Of Results")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.frame_7)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(2000)
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.groupBox_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.frame_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_5)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setText("Scrape Comments")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.togglecomnt = AnimatedToggle(self.frame_5)
        self.horizontalLayout_9.addWidget(self.togglecomnt)
        self.horizontalLayout_7.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_8)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setText("Hide Browser")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.togglehide = AnimatedToggle(self.frame_6)
        self.horizontalLayout_8.addWidget(self.togglehide)
        self.horizontalLayout_7.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.verticalLayout_main.setContentsMargins(0,0,0,0)
        self.horizontalLayout.setContentsMargins(6,6,6,6)
        self.horizontalLayout_2.setContentsMargins(0,0,0,0)
        self.horizontalLayout_3.setContentsMargins(3,0,6,0)
        self.horizontalLayout_4.setContentsMargins(3,0,6,0)
        self.horizontalLayout_5.setContentsMargins(3,0,6,0)
        self.horizontalLayout_6.setContentsMargins(20,0,50,0)
        self.horizontalLayout_6.setStretch(0,3)
        self.horizontalLayout_6.setStretch(1,1)
        self.horizontalLayout_7.setContentsMargins(0,0,0,0)
        self.horizontalLayout_8.setContentsMargins(0,0,0,0)
        self.horizontalLayout_9.setContentsMargins(0,0,0,0)
        self.horizontalLayout_9.setStretch(0,3)
        self.horizontalLayout_9.setStretch(1,1)
        self.horizontalLayout_8.setStretch(0,3)
        self.horizontalLayout_8.setStretch(1,1)
        self.verticalLayout.setContentsMargins(6,6,6,6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(6,6,6,6)
        self.verticalLayout_main.setStretch(0,2)
        self.verticalLayout_main.setStretch(1,4)
        self.verticalLayout_main.setStretch(2,3)
        self.verticalLayout_main.setSpacing(5)
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.treewidget.setColumns(["Username","Phone number","Location"])
        self.treewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ButtonStart.setDisabled(True)
        self.handles_list = []
        ## Connection 
        self.ButtonDashBoard.clicked.connect(lambda : self.Menu.setCurrentPage(1))
        self.ButtonSetting.clicked.connect(lambda : self.Menu.setCurrentPage(0))
        self.comboBox_4.currentIndexChanged.connect(self.setcombo)
        self.treewidget.onLengthChanged.connect(self.counter)
        self.lineEdit_2.textChanged.connect(self.disabledlink)
        self.lineEdit.textChanged.connect(self.disabled)
        self.spinBox.valueChanged.connect(self.disabled)
        # KeyWord Thread
        self.thread = Thread()
        self.thread.statues.connect(self.Menu.MainLabel.setText)
        self.thread.lead.connect(self.treewidget.appendData)
        self.thread.message.connect(self.messagebox)
        self.ButtonStart.clicked.connect(self.start_thread)
        self.ButtonStop.clicked.connect(self.kill)
        # Sec Thread 
        self.thread_link = ThreadLink()
        self.thread_link.statues.connect(self.Menu.MainLabel.setText)
        self.thread_link.lead.connect(self.treewidget.appendData)
        self.thread_link.message.connect(self.messagebox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.LeadsInThread = []
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def shadow(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(-10,10)
        shadow.setColor(QtGui.QColor("black"))
        return shadow

    def menu(self):
        menu = MyCustomContextMenu([
            "Copy User",
            "Copy PhoneNumber" ,
            "Copy PhoneNumber List" ,
            "Export To Excel" ,
            "Delete Row" ,
            "Clear"
        ])
        menu.multiConnect([
            lambda: self.copy(0) ,
            lambda: self.copy(1) ,
            lambda : pyperclip.copy(self.treewidget.extract_data_to_string(1)) if self.treewidget._ROW_INDEX != 0 else self.msg.showWarning(text="No Data In Column !") ,
            lambda : self.export(self.Name) ,
            lambda : self.delete() ,
            lambda : self.treewidget.clear() ,
        ])
        menu.show()

    def copy(self , index:int):
        try :
            pyperclip.copy(self.treewidget.currentItem().text(index))
        except :
            self.msg.showWarning(text="No Item Selected please Select one !")

    def delete(self):
        try:
            self.treewidget.takeTopLevelItem(self.treewidget.indexOfTopLevelItem(self.treewidget.currentItem()))
        except:
            self.msg.showWarning(text="No Item Selected please Select one !")

    def export(self,name:typing.Optional[str]):
        if self.treewidget._ROW_INDEX > 0 :
            self.treewidget.extract_data_to_DataFrame().to_excel(f"Data/Exports/{name}[{datetime.now().date()}].xlsx",index=False)
            self.msg.showInfo(text=f"Exported Succecfully to 'Data/Exports/{name}[{datetime.now().date()}].xlsx'")
        else :
            self.msg.showWarning(text="No Data In App Please Try Again Later")


    def disabledlink(self):
        if "https://haraj.com.sa" in self.lineEdit_2.text():
            self.groupBox_2.setDisabled(True)
            self.groupBox.setDisabled(False)
            self.ButtonStart.setDisabled(False)
        else :
            self.groupBox_2.setDisabled(False)
            self.groupBox.setDisabled(False)
            self.ButtonStart.setDisabled(False)

    def disabled(self):
        if len(self.lineEdit.text()) >= 1 :
            self.groupBox.setDisabled(True)
            self.groupBox_2.setDisabled(False)
            if self.spinBox.value() != 0 :
                self.ButtonStart.setDisabled(False)
        else :
            self.groupBox_2.setDisabled(False)
            self.groupBox.setDisabled(False)
            self.ButtonStart.setDisabled(True)

    def counter(self,count):
        self.countlabel.setText("\tCount : "+f"{count}")
        self.countotalabel.setText(f"Total: {count + ui.treewidget._CHILD_COUNT} ")
        self.countchildlabel.setText(f"Comment: {ui.treewidget._CHILD_COUNT} ")        


    def kill(self):
        if self.thread.isRunning():
            self.thread.kill()
        elif self.thread_link.isRunning():
            self.thread_link.kill()
        else:
            pass

    def start_thread(self):
        if self.lineEdit.isEnabled():
            self.thread.start()
        elif self.lineEdit_2.isEnabled():
            self.thread_link.start()
        


    def setcombo(self):
        index = self.comboBox_4.currentIndex()
        if index == 0 :
            self.comboBox_5.clear()
        self.comboBox_5.clear()
        self.comboBox_5.addItems(self.SUBCATEGORY[index-1])


        





    def add_to_db(self , **kwargs):
        try:
            self.curser.execute(f"""
            INSERT INTO maindata {str(tuple(kwargs.keys())).replace("'","")}
            VALUES {tuple(kwargs.values())}; """)
            self.con.commit()
        except IntegrityError:
            return False
        except OperationalError:
            return False



    def messagebox(self,text:str ,type=QMessageBox.Information)->None: # that mean this Function not working outside Class
        messagebox = QMessageBox()
        messagebox.setIcon(type)
        messagebox.setText(f"\t{text}\t")
        messagebox.setWindowTitle("Information")
        messagebox.exec_()


############################# ---------------------- Link Thread -------------------------




class ThreadLink(QThread):
    lead = pyqtSignal(list)
    statues = pyqtSignal(str)
    message = pyqtSignal(str)

    def run(self) -> None:
        ui.LeadsInThread.clear()
        self.name = ""
        link = ui.lineEdit_2.text()
        self.statues.emit("Opening Browser")
        self.hiraj = Hiraj()
        self.hiraj.start_browser(ui.togglehide.isChecked())
        self.hiraj.driver.get(link)
        self.statues.emit("Scraping Comments Users ")
        self.name = self.hiraj.get_title()
        self.owner = self.hiraj.scrape_info()
        self.lead.emit([self.owner,[]])
        QThread.msleep(100)
        comntusersdata = []
        comment_users = self.hiraj.scrape_comments_users()
        QThread.sleep(10)
        print(len(comment_users))
        if comment_users != None :
            for user in comment_users:
                self.statues.emit(f"Scraping {user} Info ... ")
                infocomntuser = self.hiraj.scrape_user_info(user)
                comntusersdata.append(infocomntuser[:4])
                self.lead.emit([infocomntuser,[]])
        self.hiraj.exit()
        self.message.emit(" Scrape Ending ^_^ ")
        self.statues.emit(" Scrape Ending ^_^ ")
        
    def kill(self):
        if self.isRunning() :
            self.hiraj.exit()
            self.terminate()
            self.wait()
            self.statues.emit("Stopped")
            self.message.emit(f" Stopped ")






############################# ---------------------- KeyWord Thread -------------------------

class Thread(QThread):
    lead = pyqtSignal(list)
    statues = pyqtSignal(str)
    message = pyqtSignal(str)

    def run(self):
        ui.LeadsInThread.clear()
        keyword = ui.lineEdit.text()
        self.name = keyword
        if keyword == "" or keyword == " ":
            self.message.emit(" Please Enter KeyWord ")
        else:
            self.statues.emit("Opening Browser")
            keyword , limit , commentscrape , hidebrowser = ui.lineEdit.text() , ui.spinBox.value() , ui.togglecomnt.isChecked() , ui.togglehide.isChecked()
            print(keyword , limit , commentscrape , hidebrowser )
            self.hiraj = Hiraj(
                url= "https://haraj.com.sa/",
                DBconnect = "Data\DataBase.db",
                darkMode = True , 
                headless = hidebrowser ,
            ) ##################
            self.hiraj.LeadSignal.connect(self.lead.emit)
            self.hiraj.Status.connect(self.statues.emit)
            self.hiraj.search(
                keyword = keyword ,
                **self.ai_search(keyword)
            )    
            self.statues.emit("Scrape Links ...")
            links = self.hiraj.scrape_links(limit=limit)
            self.statues.emit("Scrape Info ...")
            for link in links:
                print(f'{len(ui.LeadsInThread) == limit-1}-------------\n')
                if len(ui.LeadsInThread) == limit-1 :
                    break
                self.statues.emit("Scrape Ad Info ...")
                ################
                self.hiraj.get_Ad_Info (
                    link= link ,
                    scrapeComent= ui.togglecomnt.isChecked() ,
                )

            self.hiraj.exit()
            self.message.emit(" Scrape Ending ^_^ ")
            self.statues.emit(" Scrape Ending ^_^ ")




    def ai_search(self,keyword):
        area = ui.comboBox_6.currentText()
        category = ui.comboBox_4.currentText()
        subcate = ui.comboBox_5.currentText()
        result = {}
        if ui.comboBox_4.currentIndex() :
            if ui.comboBox_5.currentIndex():
                result.update({"tagname":subcate})
            else:
                result.update({"tagname":category})
        if ui.comboBox_6.currentIndex():
            result.update({"city":area}) 
        print(result)
        self.name = f"{keyword}-{list(result.values())}".replace("]","").replace("[","")
        ui.Name = self.name
        return result

    def kill(self,msg:bool= False):
        """Method to kill Thread when it Running"""
        if self.isRunning():
            try:
                self.hiraj.exit()
            except :
                pass
            self.terminate()
            self.wait()
            if msg:
                ui.msg.showInfo(text="سيبونا ناخد فرصتنا بقى")




if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(16,16))
    app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(24,24))
    app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(32,32))
    app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(48,48))
    app_icon.addFile('Data\Icons\logo.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)
    MainWindow = QtWidgets.QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
