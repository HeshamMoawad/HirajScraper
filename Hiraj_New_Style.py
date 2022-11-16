from datetime import datetime
import sys
from PyQt5.QtCore import QRect , Qt
from PyQt5.QtWidgets import ( QCheckBox, QComboBox, 
QGroupBox,  QLabel, QVBoxLayout,QPushButton,QAbstractItemView, QGridLayout ,

QWidget)
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
from mainclass import Hiraj
from MyPyQt5 import MyQTreeWidget , QSideMenuNewStyle , AnimatedToggle
import pyperclip
from styles import Styles
import sqlite3
from sqlite3 import IntegrityError, OperationalError



class Ui_MainWindow(object):
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

        self.Menu = QSideMenuNewStyle(
            self.centralwidget,
            ButtonsCount=2,
            ExitButtonIconPath="Data/Icons/reject.png" ,
            DefultIconPath="Data/Icons/list.png",
            ClickIconPath="Data/Icons/arrowheads-of-thin-outline-to-the-left.png",
            MaxButtonIconPath="Data\Icons\maximize.png",
            Mini_MaxButtonIconPath="Data\Icons\minimize.png",
            MiniButtonIconPath="Data\Icons\delete.png",

        )   
        # Stytles -----------
        self.Menu.TopFrame.setStyleSheet(Styles.PALET)
        self.Menu.ButtonsFrame.setStyleSheet(Styles.PALET)


        MainWindow.setFont(self.font)
        self.page1 = self.Menu.GetPage(0)
        # self.page1.setStyleSheet(Styles.PALET2)
        self.Menu.setCurrentPage(1)
        self.page2 = self.Menu.GetPage(1)
        self.ButtonDashBoard = self.Menu.GetButton(0)
        self.ButtonDashBoard.setText("DashBoard")
        self.Menu.setButtonIcon(0,"Data/Icons/dashboard.png")
        # self.Menu.GetButton(0).setIconSize(QtCore.QSize(20,20))
        # self.Menu.GetButton(1).setIconSize(QtCore.QSize(20,20))
        self.Menu.setButtonIcon(1,"Data/Icons/setting.png")
        self.ButtonSetting = self.Menu.GetButton(1)
        self.ButtonSetting.setText("Setting")
        self.gridLayout = QGridLayout(self.page2)
        self.treewidget = MyQTreeWidget(self.page2)

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
        # self.comboboxfont.setBold(True)
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
        self.treewidget.setColumns(["Username","Phone number","Location","Date","Time"])
        self.treewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ButtonStart.setDisabled(True)
        self.treewidget.customContextMenuRequested.connect(self.menu)
        self.handles_list = []
        ## Connection 
        self.ButtonDashBoard.clicked.connect(lambda : self.Menu.setCurrentPage(1))
        self.ButtonSetting.clicked.connect(lambda : self.Menu.setCurrentPage(0))
        self.comboBox_4.currentIndexChanged.connect(self.setcombo)

        self.treewidget.onLengthChanged.connect(self.counter)
        # self.treewidget.childChanged.connect(self.commentcount)
        
        self.lineEdit_2.textChanged.connect(self.disabledlink)

        self.lineEdit.textChanged.connect(self.disabled)
        self.spinBox.valueChanged.connect(self.disabled)
        # KeyWord Thread
        self.thread = Thread()
        self.thread.statues.connect(self.Menu.MainLabel.setText)
        self.thread.lead.connect(self.lead)
        self.thread.message.connect(self.messagebox)
        self.ButtonStart.clicked.connect(self.start_thread)
        self.ButtonStop.clicked.connect(self.kill)

        # Sec Thread 
        self.thread_link = ThreadLink()
        self.thread_link.statues.connect(self.Menu.MainLabel.setText)
        self.thread_link.lead.connect(self.lead)
        self.thread_link.message.connect(self.messagebox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.LeadsInThread = []
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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


    def lead(self,data:list):
        try:
            data = self.reshape_data(data)
            con= True
        except :
            con = False
            pass
        if con:
            if len(data[1]) > 0:
                ui.treewidget.appendData(items=data[0],childs=data[1])
                self.LeadsInThread.append([data])
            elif len(data[1]) == 0 and len(data[0]) != 0 :
                ui.treewidget.appendData(items=data[0])
                self.LeadsInThread.append([data])




    def reshape_data(self,data):
        data[1] = [datachild for datachild in data[1] if datachild[1] != None and self.searchDb(str(datachild[1])) == [] ]
        for datachild in data[1]:
            db_datachild = {"handle":datachild[0],"phone":datachild[1],"address":data[0][2],"timescrape":datachild[4],"comment":data[0][0]}
            self.add_to_db(**db_datachild)
            datachild[1] = f"+966{str(datachild[1])[1:]}" if len(datachild[1]) == 10 else  "+9665"+ datachild[1].split("05",1)[1:][0]
            ##############
            search = self.searchDb(str(data[0][1]))
            if data[0][1] != None : 
                data[0][1] = f"+966{str(data[0][1])[1:]}" if len(data[0][1]) == 10 else  "+9665"+ data[0][1].split("05",1)[1:][0]
                if search == [] :
                    db_data = {"handle":data[0][0],"phone":f"{data[0][1]}","address":data[0][2],"timeadded":data[0][3],"timescrape":data[0][4]}
                    self.add_to_db(**db_data)
        if len(data[1]) == 0 :
            search = self.searchDb(str(data[0][1]))
            if data[0][1] != None and search == [] :
                db_data = {"handle":data[0][0],"phone":f"{data[0][1]}","address":data[0][2],"timeadded":data[0][3],"timescrape":data[0][4]}
                self.add_to_db(**db_data)
                data[0][1] = f"+966{str(data[0][1])[1:]}" if len(data[0][1]) == 10 else  "+9665"+ data[0][1].split("05",1)[1:][0]
            else:
                data[0].clear()
        return data


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

    def searchDb(self,val):
        self.curser.execute(f"""SELECT * FROM maindata WHERE phone = '{val}'; """)
        return self.curser.fetchall()


    def messagebox(self,text:str ,type=QMessageBox.Information)->None: # that mean this Function not working outside Class
        messagebox = QMessageBox()
        messagebox.setIcon(type)
        messagebox.setText(f"\t{text}\t")
        messagebox.setWindowTitle("Information")
        messagebox.exec_()

    def menu(self):
        def copylist(index):
            pyperclip.copy(ui.treewidget.extract_data_to_string(index)) 
            
        def copy(index):
            try:
                item = ui.treewidget.currentItem().text(index)
                pyperclip.copy(item)
            except:
                pass

        def export(msg:bool=False , name:str=""):
            dataframe = ui.treewidget.extract_data_to_DataFrame()
            if dataframe.empty :
                self.messagebox(" Empty Data Please add any thing")
            else:
                dataframe.to_excel(f"Data\Exports/Export[{name}-{datetime.now().date()}].xlsx",index=False)
                if msg:
                    self.messagebox(text=f" Saved Succecfuly In Data Folder as \n Exports\Export[{name}-{datetime.now().date()}].xlsx")

        def delete_():
            try:
                index = ui.treewidget.indexOfTopLevelItem(ui.treewidget.currentItem())
                ui.handles_list.remove([ui.treewidget.currentItem().text(0),ui.treewidget.currentItem().text(1)])
                ui.treewidget.takeTopLevelItem(index)
            except Exception as e:
                print(e)
                pass


        def copycolumn():
            users = ui.treewidget.extract_data_to_list(0)
            handles= ui.treewidget.extract_data_to_list(1)
            result = " UserName  :  Phones \n"
            if len(users)== 0 or len(handles) == 0 :
                self.messagebox(text=" Empty Data Please add any thing")
            for row in range(ui.treewidget._ROW_INDEX):
                result = result+ f"\t{users[row]}  :  {handles[row]} \t\n"
            pyperclip.copy(result)


        def clear():
            ui.treewidget.clear()
            ui.handles_list.clear()
            

        menu = QtWidgets.QMenu()

        copyname = menu.addAction("Copy Name")
        copyname.triggered.connect(lambda:copy(0))##########
        
        copyhandle = menu.addAction("Copy Phone")
        copyhandle.triggered.connect(lambda:copy(1))##############

        delete = menu.addAction("Delete Row")
        delete.triggered.connect(delete_)###############

        export_ = menu.addAction("Export All To Excel")
        export_.triggered.connect(lambda : export(True , ui.thread.name))############

        copynamelist = menu.addAction("Copy Names List")
        copynamelist.triggered.connect(lambda:copylist(0))##########
        
        copyhandlelist = menu.addAction("Copy Phones List")
        copyhandlelist.triggered.connect(lambda:copylist(1))##############


        result = menu.addAction("Copy UserNames and Phones")
        result.triggered.connect(copycolumn)#########

        clear_ = menu.addAction("Clear Results")
        clear_.triggered.connect(clear)#########

        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())


############################# ---------------------- Link Thread -------------------------




class ThreadLink(QThread):
    lead = pyqtSignal(list)
    statues = pyqtSignal(str)
    message = pyqtSignal(str)

    def run(self) -> None:
        ui.LeadsInThread.clear()
        self.name = ""
        link = ui.lineEdit_2.text()
        # ui.lineEdit_2.clear()
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
            self.hiraj = Hiraj()
            self.hiraj.start_browser(hidebrowser=hidebrowser)
            self.ai_search(keyword)
            self.statues.emit("Scrape Links ...")
            links = self.hiraj.scrape_links(limit=limit)
            self.statues.emit("Scrape Info ...")
            for link in links:
                if len(ui.LeadsInThread) == limit-1 :
                    break
                self.hiraj.driver.get(link)
                self.statues.emit("Scrape Ad Info ...")
                infoauthor = self.hiraj.scrape_info()
                comntusersdata = []
                if commentscrape:
                    self.statues.emit("Scrape Comments ...")
                    comment_users = self.hiraj.scrape_comments_users()
                    # print(comment_users)
                    if comment_users != None :
                        for user in comment_users:
                            self.statues.emit(f"Scrape {user} info ...")
                            infocomntuser = self.hiraj.scrape_user_info(user)
                            comntusersdata.append(infocomntuser)
                self.lead.emit([infoauthor,comntusersdata])
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
        self.hiraj.search(keyword=keyword,**result)
        self.name = f"{keyword}-{list(result.values())}".replace("]","").replace("[","")

    def kill(self):
        if self.isRunning() :
            self.hiraj.exit()
            self.terminate()
            self.wait()
            self.statues.emit("Stopped")
            self.message.emit(f" Stopped ")


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
