from datetime import datetime
import sys
from PyQt5.QtCore import QRect , Qt
from PyQt5.QtWidgets import ( QCheckBox, QComboBox, 
QGroupBox,  QLabel, QVBoxLayout,QPushButton,QAbstractItemView,
QWidget)
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
from mainclass import Hiraj
from MyPyQt5 import MyQTreeWidget , QSideMenuNewStyle
import pyperclip
from styles import Styles
import sqlite3
from sqlite3 import IntegrityError, OperationalError


class Ui_MainWindow(object):
    CATEGORIES = ['حراج السيارات', 'حراج العقار', 'حراج الأجهزة', 'مواشي وحيوانات وطيور', 'اثاث', 'مستلزمات شخصية', 'خدمات', 'وظائف', 'اطعمة ومشروبات', 'برمجة وتصاميم', 'مكتبة وفنون', 'صيد ورحلات']
    SUBCATEGORY = [['', 'هونشي', 'زوتي', 'ماهيندرا', 'ساوايست', 'تسلا', 'بايك', 'جاك JAC', 'ماكلارين', 'ماكسيس', 'ليفان', 'فيكتوري اوتو', 'فوتون', 'سي ام سي', 'جيتور', 'جى ام سي JMC', 'تاتا', 'الفا روميو', 'BYD', 'فاو FAW', 'جريت وول Great Wall', 'جي ايه سي GAC', 'هافال', 'بروتون', 'استون مارتن', 'سانج يونج', 'فيات', 'ساب', 'دايو', 'سيات', 'تشيري', 'سيتروين', 'فيراري', 'سكودا', 'اوبل', 'لامبورجيني', 'رولز رويس', 'مازيراتي', 'بيوك', ' رينو', 'شانجان', 'ZXAUTO', 'MG', 'سوبارو', 'جاكوار', 'بنتلي', 'بيجو', 'فولفو', 'ميركوري', 'جيلي', 'ديهاتسو', 'فولكس واجن', 'لنكولن', 'همر', 'انفنيتي', 'سوزوكي', 'اودي', 'بورش', 'كاديلاك', 'ايسوزو', 'لاند روفر', 'مازدا', 'ميتسوبيشي', 'جيب','كرايزلر', 'دودج', 'كيا', 'دبابات', 'بي ام دبليو', 'هوندا', 'مرسيدس', 'شاحنات ومعدات ثقيلة', 'جي ام سي', 'لكزس', 'جنسس', 'هونداي', 'نيسان', 'قطع غيار وملحقات', 'شيفروليه', 'فورد', 'تويوتا'], ['', 'بيوت للايجار', 'ادوار للايجار', 'مزارع للبيع', 'فلل للايجار', 'استراحات للبيع', 'عماره للايجار', 'محلات للايجار', 'محلات للتقبيل', 'استراحات للايجار', 'عمارة للبيع', 'اراضي تجارية للبيع', 'بيوت للبيع', 'شقق للبيع', 'فلل للبيع', 'شقق للايجار', 'اراضي للبيع'], ['', 'غسالة سامسونج', 'ثلاجة سامسونج', 'اجهزة غير مصنفة', 'هيتاشي Hitachi', 'باناسونيك Panasonic', 'مايكروسوفت Microsoft', 'ال جي LG', 'أرقام مميزة', 'حسابات واشتراكات', 'كاميرات تصوير', 'تلفزيونات وصوتيات', 'ألعاب إلكترونية', 'أجهزة كمبيوتر', 'أجهزة تابلت', 'جوالات'], ['', 'وبر', 'هامستر', 'سناجب', 'بط', 'ارانب', 'أسماك وسلاحف', 'بقر', 'كلاب', 'خيل', 'أبل', 'دجاج', 'قطط', 'حمام', 'ببغاء', 'ماعز', 'غنم'], ['', 'مجالس ومفروشات', 'طاولات وكراسي', 'خزائن ودواليب', 'تحف وديكور', 'أسرة ومراتب', 'أدوات منزلية', 'أثاث مكتبي', 'أثاث خارجي'], ['', 'ملابس أطفال', 'ملابس نسائية', 'ملابس رجالية', 'نظارات', 'مستلزمات رياضية', 'عطورات', 'ساعات'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات','زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفروسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['']]
    AREAS = ["كل المناطق","الرياض","الشرقيه","جده","مكه","ينبع","حفر الباطن","المدينة","الطايف","تبوك","القصيم","حائل","أبها","عسير","الباحة","جيزان","نجران","الجوف","عرعر","الكويت","الإمارات","البحرين"]
    def show(self):
        ui.MainWindow.show()

    def messagebox(self,text:str ,type=QMessageBox.Information)->None: # that mean this Function not working outside Class
        messagebox = QMessageBox()
        messagebox.setIcon(type)
        messagebox.setText(f"\t{text}\t")
        messagebox.setWindowTitle(" Warning ")
        messagebox.exec_()



    def setupUi(self):
        self.con = sqlite3.connect("Data/DataBase.db")
        self.curser = self.con.cursor()
        MainWindow = QMainWindow()
        self.MainWindow = MainWindow
        self.rootwidth = 600
        self.roothight = 500
        MainWindow.setWindowTitle("HirajScraper \tProducer : Hesham")
        MainWindow.resize(self.rootwidth,self.roothight)
        # MainWindow.setMaximumWidth(self.rootwidth)
        # MainWindow.setMaximumHeight(self.roothight)
        MainWindow.setWindowIcon(QtGui.QIcon("Icons\logo.png"))
        MainWindow.setStyleSheet(Styles.APP)


        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.Menu = QSideMenuNewStyle(
            self.centralwidget,
            
            )

        page1 = self.Menu.GetPage(0)
        # self.Button

        self.Menu.setCurrentPage(1)

        page2 = self.Menu.GetPage(1)

        # self.tabs = QtWidgets.QTabWidget(self.Menu)

        # self.tabs.setGeometry(QtCore.QRect(0, 0,self.rootwidth , self.roothight))#MainWindow.width()MainWindow.height(

        self.pushButton = QtWidgets.QPushButton(page1)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 370, 30))
        self.pushButton.setStyleSheet(Styles.BUTTON)
        self.pushButton.setText("Start")

        self.spinBox = QtWidgets.QSpinBox(page1)
        self.spinBox.setGeometry(QtCore.QRect(310, 10, 80, 21))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(1000)

        self.spinBox.setStyleSheet(Styles.SPINBOX)
        self.label = QtWidgets.QLabel(page1)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label.setStyleSheet(Styles.LABEL)
        self.label.setText("KeyWord")

        self.lineEdit = QtWidgets.QLineEdit(page1)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 150, 21))
        self.lineEdit.setStyleSheet(Styles.LINEDIT)

        self.label3 = QtWidgets.QLabel(page1)
        self.label3.setGeometry(QtCore.QRect(9, 40, 121, 21))
        self.label3.setStyleSheet(Styles.LABEL)
        self.label3.setText("Categories")

        self.catbox = QComboBox(page1)
        self.catbox.setGeometry(QtCore.QRect(80, 40, 120, 21))
        self.catbox.setCurrentIndex(0)
        self.catbox.addItems(["كل الاقسام"]+self.CATEGORIES)
        self.catbox.setStyleSheet(Styles.COMPOBOX)
        self.catbox.currentIndexChanged.connect(self.setitemsforsub)

        self.label4 = QtWidgets.QLabel(page1)
        self.label4.setGeometry(QtCore.QRect(210, 40, 121, 21))
        self.label4.setStyleSheet(Styles.LABEL)
        self.label4.setText("SubCate")
        self.subcatbox = QComboBox(page1)
        self.subcatbox.setGeometry(QtCore.QRect(280, 40, 110, 21))
        self.subcatbox.setStyleSheet(Styles.COMPOBOX)

        self.label4 = QtWidgets.QLabel(page1)
        self.label4.setGeometry(QtCore.QRect(9, 70, 121, 21))
        self.label4.setStyleSheet(Styles.LABEL)
        self.label4.setText("Area")

        self.areabox = QComboBox(page1)
        self.areabox.setGeometry(QtCore.QRect(80, 70, 110, 21))
        self.areabox.setStyleSheet(Styles.COMPOBOX)
        self.areabox.addItems(self.AREAS)
        self.areabox.setCurrentIndex(0)

        self.comntcheck = QCheckBox(page1)
        self.comntcheck.setGeometry(QRect(220, 100, 160, 21))
        self.comntcheck.setText("Scrape Comments")
        self.comntcheck.setStyleSheet(Styles.CHECKBOX)

        self.hidecheck = QCheckBox(page1)
        self.hidecheck.setGeometry(QRect(40, 100, 160, 21))
        self.hidecheck.setText("Hide Browser")
        self.hidecheck.setStyleSheet(Styles.CHECKBOX)

        self.label2 = QtWidgets.QLabel(page1)
        self.label2.setGeometry(QtCore.QRect(260, 10, 30, 21))
        self.label2.setObjectName("label")
        self.label2.setStyleSheet(Styles.LABEL)
        self.label2.setText("Limit")


        self.label_tab2 = QtWidgets.QLabel(page2,text="Link")
        self.label_tab2.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label_tab2.setStyleSheet(Styles.LABEL)

        self.link_tab2 = QtWidgets.QLineEdit(page2)
        self.link_tab2.setGeometry(QtCore.QRect(80, 10, self.rootwidth - 100, 21))
        self.link_tab2.setStyleSheet(Styles.LINEDIT)

        self.hidecheck_tab2 = QCheckBox(page2)
        self.hidecheck_tab2.setGeometry(QRect(40, 50, 160, 21))
        self.hidecheck_tab2.setText("Hide Browser")
        self.hidecheck_tab2.setStyleSheet(Styles.CHECKBOX)

        self.pushButton_tab2 = QtWidgets.QPushButton(page2)
        self.pushButton_tab2.setGeometry(QtCore.QRect(10, 80, self.rootwidth-20, 30))
        self.pushButton_tab2.setStyleSheet(Styles.BUTTON)
        self.pushButton_tab2.setText("Start")

        MainWindow.setCentralWidget(self.centralwidget)

        contanier = QGroupBox("Exports")
        #contanier.setFixedWidth(self.centralwidget.width())
        contanier.setFixedHeight(60)

        # self.app = App()
        # self.app.setStyleSheet(Styles.APP)
        # self.app.show()
        self.statues = QLabel(contanier)
        self.statues.setGeometry(QRect(270,20 ,180, 31))
        self.statues.setText("dasdasd")
        self.statues.setStyleSheet(Styles.LABEL)

        # thread
        self.thread = Thread()
        self.thread.statues.connect(self.statues.setText)
        self.thread.lead.connect(self.lead)
        self.thread.message.connect(self.messagebox)
        self.pushButton.clicked.connect(self.thread.start)

        # Sec Thread 
        self.thread_link = ThreadLink()
        self.thread_link.statues.connect(self.statues.setText)
        self.thread_link.lead.connect(self.lead)
        self.thread_link.message.connect(self.messagebox)
        self.pushButton_tab2.clicked.connect(self.thread_link.start)

#-------------------------------------------------------------------
        self.dataGroupBox = QGroupBox("Inbox")
        self.dataView = MyQTreeWidget(self.dataGroupBox)
        
        dataLayout = QVBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)
        
        self.dataView.setColumns(["Username","Phone number","Location","Date","Time"])
        self.dataView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.dataView.setContextMenuPolicy(Qt.CustomContextMenu)
        
        self.dataView.customContextMenuRequested.connect(self.menu)
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        page2.setLayout(mainLayout)


        listbox = QComboBox(contanier)
        listbox.setGeometry(QRect(180,20 ,80, 30))
        listbox.setObjectName("listbox")
        listbox.addItem("Excel")
        listbox.setStyleSheet(Styles.COMPOBOX)
        
        self.stopbtn = QPushButton(contanier)
        self.stopbtn.setGeometry(QRect(470,20 ,120, 31))
        self.stopbtn.setText("Stop")
        self.stopbtn.setObjectName("stopbtn")
        self.stopbtn.setStyleSheet(Styles.BUTTON)
        self.stopbtn.setDisabled(True)
        # Thread part
        self.stopbtn.clicked.connect(self.kill)
        
        self.exportbtn = QPushButton(contanier)
        mainLayout.addWidget(contanier)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def menu(self):
        menu = QtWidgets.QMenu()

        copyhanph = menu.addAction("Copy Handles and Phones")
        copyhanph.triggered.connect(self.copycolumn)
        
        copyphones = menu.addAction("Copy Phones")
        copyphones.triggered.connect( lambda:pyperclip.copy(self.dataView.extract_data_to_string(1)))

        export = menu.addAction("Export All To Excel")
        export.triggered.connect(lambda:self.export(msg=True))

        user = menu.addAction("Copy Username")
        user.triggered.connect(lambda: self.copy(0))

        phone = menu.addAction("Copy Phone number")
        phone.triggered.connect(lambda: self.copy(1))

        delete_ = menu.addAction("Delete Row")
        delete_.triggered.connect(self.delete_)

        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())



    def copycolumn(self):
        handles = self.dataView.extract_data_to_list(0)
        phones= self.dataView.extract_data_to_list(1)
        result = " Username  :  Password \n"
        for row in range(self.dataView.ROW_INDEX):
            result = result+ f"\t{handles[row]}  :  {phones[row]} \t\n"
        pyperclip.copy(result)



#---------------------------------------------------------------------



        

    def messagebox(self,text:str ,type=QMessageBox.Information)->None: # that mean this Function not working outside Class
        messagebox = QMessageBox()
        messagebox.setIcon(type)
        messagebox.setText(f"\t{text}\t")
        messagebox.setWindowTitle(" Warning ")
        messagebox.exec_()

        
    def setall(self,ch):
        if ch ==1:
            ui.pushButton.setDisabled(True)
            ui.app.stopbtn.setDisabled(False)
            ui.app.exportbtn.setDisabled(False)
        elif ch ==2:
            ui.pushButton.setDisabled(False)
            ui.app.stopbtn.setDisabled(True)
            ui.app.exportbtn.setDisabled(False)

    def setitemsforsub(self):
        index = self.catbox.currentIndex()
        self.subcatbox.clear()
        self.subcatbox.addItems(self.SUBCATEGORY[index-1])  

    def lead(self,data:list):
        data = self.reshape_data(data)
        #print(data)
        if len(data[1]) > 0:
            self.app.dataView.appendData(items=data[0],childs=data[1])
        elif len(data[1]) == 0 and len(data[0]) != 0 :
            self.app.dataView.appendData(items=data[0])


    def reshape_data(self,data):
        print("-----------before filter----------------")
        print(data)
        #print("-----------end----------------")
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

        print("-------------after filters--------------")
        print(data)
        print("------------------------------------------- end --------------------------------------------------")
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

    def kill(self)-> None:
        self.thread.kill()
        self.thread_link.kill()
        
class ThreadLink(QThread):
    lead = pyqtSignal(list)
    statues = pyqtSignal(str)
    message = pyqtSignal(str)

    def run(self) -> None:
        self.name = ""
        link = ui.link_tab2.text()
        if link == "" and link == " " or "https://haraj.com.sa/" not in link:
            print(link)
            self.message.emit(" Please Enter Hiraj Link ")
        else:
            # try:
            self.statues.emit("Opening Browser")
            ui.app.dataView.clear()
            ui.link_tab2.clear()
            ui.setall(1)
            ui.pushButton_tab2.setDisabled(True)
            self.hiraj = Hiraj()
            self.hiraj.start_browser(ui.hidecheck_tab2.isChecked())
            self.hiraj.driver.get(link)
            self.statues.emit("Scraping Comments Users ")
            self.name = self.hiraj.get_title()
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
            ui.setall(2)
            ui.pushButton_tab2.setDisabled(False)
            self.message.emit(" Scrape Ending ^_^ ")
            self.statues.emit(" Scrape Ending ^_^ ")
            
    def kill(self):
        if self.isRunning() :
            self.hiraj.exit()
            self.terminate()
            self.wait()
            ui.pushButton_tab2.setDisabled(False)
            self.statues.emit("Stopped")
            self.message.emit(f" Stopped ")
            ui.app.stopbtn.setDisabled(True)


class Thread(QThread):
    lead = pyqtSignal(list)
    statues = pyqtSignal(str)
    message = pyqtSignal(str)

    def run(self):
        self.name = ""
        keyword = ui.lineEdit.text()
        if keyword == "" or keyword == " ":
            self.message.emit(" Please Enter KeyWord ")
        else:
            # try:
            self.statues.emit("Opening Browser")
            ui.app.dataView.clear()
            ui.setall(1)
            keyword , limit , commentscrape , hidebrowser = ui.lineEdit.text() , ui.spinBox.value() , ui.comntcheck.isChecked() , ui.hidecheck.isChecked()
            self.hiraj = Hiraj()
            self.hiraj.start_browser(hidebrowser=hidebrowser)
            self.ai_search(keyword)
            self.statues.emit("Scrape Links ...")
            links = self.hiraj.scrape_links(limit=limit)
            self.statues.emit("Scrape Info ...")
            try:
                links = links[:limit]
            except:
                pass
            for link in links:
                QThread.msleep(100)
                self.hiraj.driver.get(link)
                self.statues.emit("Scrape Ad Info ...")
                infoauthor = self.hiraj.scrape_info()
                QThread.msleep(100)
                comntusersdata = []
                if commentscrape:
                    self.statues.emit("Scrape Comments ...")
                    comment_users = self.hiraj.scrape_comments_users()
                    print(comment_users)
                    if comment_users != None :
                        for user in comment_users:
                            self.statues.emit(f"Scrape {user} info ...")
                            infocomntuser = self.hiraj.scrape_user_info(user)
                            comntusersdata.append(infocomntuser)

                self.lead.emit([infoauthor,comntusersdata])
            self.hiraj.exit()
            ui.setall(2)
            self.message.emit(" Scrape Ending ^_^ ")
            self.statues.emit(" Scrape Ending ^_^ ")
            # except Exception as e :
            #     ui.app.export(name=self.name)
            #     ui.setall(2)
            #     self.message.emit(f" Sorry Data exported Automaticlly for Error {e}!! ")




    def ai_search(self,keyword):
        area = ui.areabox.currentText()
        category = ui.catbox.currentText()
        subcate = ui.subcatbox.currentText()
        result = {}
        if ui.catbox.currentIndex() :
            if ui.subcatbox.currentIndex() :
                result.update({"tagname":subcate})
            else:
                result.update({"tagname":category})
        if ui.areabox.currentIndex():
            result.update({"city":area}) 
        self.hiraj.search(keyword=keyword,**result)
        self.name = f"{keyword}-{list(result.values())}".replace("]","").replace("[","")


    def kill(self):
        if self.isRunning():
            print("1")
            self.hiraj.exit()
            self.terminate()
            self.wait()
            ui.pushButton.setDisabled(False)
            self.statues.emit("Stopped")
            self.message.emit(f" Stopped ")
            ui.app.stopbtn.setDisabled(True)

class App(QWidget):
    USERNAME, PHONE, LOCATION,DATE = range(4)
    row_data_count = 0
    def __init__(self):
        super().__init__()
        self.title = 'HirajScraper \tProducer: ProfitWay.Co'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 500
        self.initUI()
        
    def messagebox(self,text:str ,type=QMessageBox.Information)->None: # that mean this Function not working outside Class
        messagebox = QMessageBox()
        messagebox.setIcon(type)
        messagebox.setText(f"\t{text}\t")
        messagebox.setWindowTitle(" Warning ")
        messagebox.exec_()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("Icons\logo.png"))

    def menu(self):
        menu = QtWidgets.QMenu()

        copyhanph = menu.addAction("Copy Handles and Phones")
        copyhanph.triggered.connect(self.copycolumn)
        
        copyphones = menu.addAction("Copy Phones")
        copyphones.triggered.connect( lambda:pyperclip.copy(self.dataView.extract_data_to_string(1)))

        export = menu.addAction("Export All To Excel")
        export.triggered.connect(lambda:self.export(msg=True))

        user = menu.addAction("Copy Username")
        user.triggered.connect(lambda: self.copy(0))

        phone = menu.addAction("Copy Phone number")
        phone.triggered.connect(lambda: self.copy(1))

        delete_ = menu.addAction("Delete Row")
        delete_.triggered.connect(self.delete_)

        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())



    def copycolumn(self):
        handles = self.dataView.extract_data_to_list(0)
        phones= self.dataView.extract_data_to_list(1)
        result = " Username  :  Password \n"
        for row in range(self.dataView.ROW_INDEX):
            result = result+ f"\t{handles[row]}  :  {phones[row]} \t\n"
        pyperclip.copy(result)

            




    def delete_(self):
        try:
            index = self.dataView.indexOfTopLevelItem(self.dataView.currentItem())
            self.dataView.takeTopLevelItem(index)
        except:
            pass


    def copy(self,index):
        try:
            item = self.dataView.currentItem().text(index)
            pyperclip.copy(item)
        except:
            pass


    def export(self,msg:bool=False , name:str=""):
        dataframe = self.dataView.extract_data_to_DataFrame()
        if dataframe.empty :
            self.messagebox(" Empty Data Please add any thing")
        else:
            dataframe.to_excel(f"Data\Export[{name}-{datetime.now().date()}].xlsx",index=False)
            if msg:
                self.messagebox(text=f" Saved Succecfuly In Data Folder as \n Data\Export[{name}-{datetime.now().date()}].xlsx")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    app_icon.addFile('Icons\logo.png', QtCore.QSize(16,16))
    app_icon.addFile('Icons\logo.png', QtCore.QSize(24,24))
    app_icon.addFile('Icons\logo.png', QtCore.QSize(32,32))
    app_icon.addFile('Icons\logo.png', QtCore.QSize(48,48))
    app_icon.addFile('Icons\logo.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)

    MainWindow = QtWidgets.QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi()

    ui.show()
    sys.exit(app.exec_())
