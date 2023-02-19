from PyQt5 import QtCore, QtWidgets
from Packages import QObject , MyQTreeWidget , QIcon, QSize , MyCustomContextMenu,MyMessageBox
import os , openpyxl,pandas,pyperclip,typing
from datetime import datetime


class Page1(QObject):
    msg = MyMessageBox()
    CATEGORIES = ['حراج السيارات', 'حراج العقار', 'حراج الأجهزة', 'مواشي وحيوانات وطيور', 'اثاث', 'مستلزمات شخصية', 'خدمات', 'وظائف', 'اطعمة ومشروبات', 'برمجة وتصاميم', 'مكتبة وفنون', 'صيد ورحلات']
    SUBCATEGORY = [['', 'هونشي', 'زوتي', 'ماهيندرا', 'ساوايست', 'تسلا', 'بايك', 'جاك JAC', 'ماكلارين', 'ماكسيس', 'ليفان', 'فيكتوري اوتو', 'فوتون', 'سي ام سي', 'جيتور', 'جى ام سي JMC', 'تاتا', 'الفا روميو', 'BYD', 'فاو FAW', 'جريت وول Great Wall', 'جي ايه سي GAC', 'هافال', 'بروتون', 'استون مارتن', 'سانج يونج', 'فيات', 'ساب', 'دايو', 'سيات', 'تشيري', 'سيتروين', 'فيراري', 'سكودا', 'اوبل', 'لامبورجيني', 'رولز رويس', 'مازيراتي', 'بيوك', ' رينو', 'شانجان', 'ZXAUTO', 'MG', 'سوبارو', 'جاكوار', 'بنتلي', 'بيجو', 'فولفو', 'ميركوري', 'جيلي', 'ديهاتسو', 'فولكس واجن', 'لنكولن', 'همر', 'انفنيتي', 'سوزوكي', 'اودي', 'بورش', 'كاديلاك', 'ايسوزو', 'لاند روفر', 'مازدا', 'ميتسوبيشي', 'جيب','كرايزلر', 'دودج', 'كيا', 'دبابات', 'بي ام دبليو', 'هوندا', 'مرسيدس', 'شاحنات ومعدات ثقيلة', 'جي ام سي', 'لكزس', 'جنسس', 'هونداي', 'نيسان', 'قطع غيار وملحقات', 'شيفروليه', 'فورد', 'تويوتا'], ['', 'بيوت للايجار', 'ادوار للايجار', 'مزارع للبيع', 'فلل للايجار', 'استراحات للبيع', 'عماره للايجار', 'محلات للايجار', 'محلات للتقبيل', 'استراحات للايجار', 'عمارة للبيع', 'اراضي تجارية للبيع', 'بيوت للبيع', 'شقق للبيع', 'فلل للبيع', 'شقق للايجار', 'اراضي للبيع'], ['', 'غسالة سامسونج', 'ثلاجة سامسونج', 'اجهزة غير مصنفة', 'هيتاشي Hitachi', 'باناسونيك Panasonic', 'مايكروسوفت Microsoft', 'ال جي LG', 'أرقام مميزة', 'حسابات واشتراكات', 'كاميرات تصوير', 'تلفزيونات وصوتيات', 'ألعاب إلكترونية', 'أجهزة كمبيوتر', 'أجهزة تابلت', 'جوالات'], ['', 'وبر', 'هامستر', 'سناجب', 'بط', 'ارانب', 'أسماك وسلاحف', 'بقر', 'كلاب', 'خيل', 'أبل', 'دجاج', 'قطط', 'حمام', 'ببغاء', 'ماعز', 'غنم'], ['', 'مجالس ومفروشات', 'طاولات وكراسي', 'خزائن ودواليب', 'تحف وديكور', 'أسرة ومراتب', 'أدوات منزلية', 'أثاث مكتبي', 'أثاث خارجي'], ['', 'ملابس أطفال', 'ملابس نسائية', 'ملابس رجالية', 'نظارات', 'مستلزمات رياضية', 'عطورات', 'ساعات'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات','زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفروسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['']]
    AREAS = ["كل المناطق","الرياض","الشرقيه","جده","مكه","ينبع","حفر الباطن","المدينة","الطايف","تبوك","القصيم","حائل","أبها","عسير","الباحة","جيزان","نجران","الجوف","عرعر","الكويت","الإمارات","البحرين"]
    Name = ""
    def __init__(self, parent):
        super().__init__()
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(parent)
        self.groupBox = QtWidgets.QGroupBox(parent)
        self.groupBox.setTitle("Setting")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(0, 3, 3, 3)
        self.verticalLayout_4.setSpacing(3)
        self.frame_kw_lim = QtWidgets.QFrame(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_kw_lim)
        self.label_kw = QtWidgets.QLabel(self.frame_kw_lim)
        self.label_kw.setText("KeyWord")
        self.label_kw.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label_kw)
        self.lineEdit_kw = QtWidgets.QLineEdit(self.frame_kw_lim)
        self.horizontalLayout.addWidget(self.lineEdit_kw)
        self.label_lim = QtWidgets.QLabel(self.frame_kw_lim)
        self.label_lim.setText("Limit")
        self.label_lim.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label_lim)
        self.spinBox_lim = QtWidgets.QSpinBox(self.frame_kw_lim)
        self.spinBox_lim.setMinimum(5)
        self.spinBox_lim.setMaximum(10000)
        self.horizontalLayout.addWidget(self.spinBox_lim)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_4.addWidget(self.frame_kw_lim)
        self.frame_5 = QtWidgets.QFrame(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 5)
        self.horizontalLayout_2.setSpacing(10)
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.label_cat = QtWidgets.QLabel(self.frame_2)
        self.label_cat.setText("Category")
        self.label_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_cat)
        self.comboBox_cat = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_cat.addItems( ["كل الاقسام"] + self.CATEGORIES)
        self.comboBox_cat.currentIndexChanged.connect(self.changeComboBox )
        self.verticalLayout.addWidget(self.comboBox_cat)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.label_sub = QtWidgets.QLabel(self.frame_3)
        self.label_sub.setText("SubCategory")
        self.label_sub.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label_sub)
        self.comboBox_sub = QtWidgets.QComboBox(self.frame_3)
        self.verticalLayout_2.addWidget(self.comboBox_sub)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(3)
        self.label_city = QtWidgets.QLabel(self.frame_4)
        self.label_city.setText("City")
        self.label_city.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_city)
        self.comboBox_city = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_city.addItems(self.AREAS)
        self.verticalLayout_3.addWidget(self.comboBox_city)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.label_count = QtWidgets.QLabel(parent)
        self.label_count.setText("Count : 0")
        self.label_count.setAlignment(QtCore.Qt.AlignCenter)
        self.treeWidget = MyQTreeWidget(
            parent ,
            counterLabel = self.label_count ,
            )
        self.treeWidget.setColumns(["Name","Phone Number","City"])
        self.treeWidget.setColumnWidth(0,150)
        self.treeWidget.setColumnWidth(1,200)        
        self.treeWidget.setColumnWidth(2,150) 
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.Menu)  
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.verticalLayout_5.addWidget(self.label_count)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 3)

    def changeComboBox(self):
        index = self.comboBox_cat.currentIndex()
        if index == 0 :
            self.comboBox_sub.clear()
        self.comboBox_sub.clear()
        self.comboBox_sub.addItems(self.SUBCATEGORY[index-1])

    def Menu(self):
        menu = MyCustomContextMenu(
            Actions_arg=[
                "Copy Number", # 1
                "Copy Number List",  # 2
                "Delete Row", # 3
                "Export To Excel", # 4
            ]
        )
        menu.multiConnect(functions=[
            lambda: self.copy(1) ,
            lambda : pyperclip.copy(self.treeWidget.extract_data_to_string(1)) if self.treeWidget._ROW_INDEX != 0 else self.msg.showWarning(text="No Data In Column !") ,
            lambda: self.delete() ,
            lambda : self.export(self.Name),
        ])
        menu.show()

    def copy(self , index:int):
        try :
            pyperclip.copy(self.treeWidget.currentItem().text(index))
        except :
            self.msg.showWarning(text="No Item Selected please Select one !")

    def delete(self):
        try:
            self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(self.treeWidget.currentItem()))
        except:
            self.msg.showWarning(text="No Item Selected please Select one !")

    def export(self,name:typing.Optional[str]):
        if self.treeWidget._ROW_INDEX > 0 :
            self.treeWidget.extract_data_to_DataFrame().to_excel(f"Data/Exports/{name}[{datetime.now().date()}].xlsx",index=False)
            self.msg.showInfo(text=f"Exported Succecfully to 'Data/Exports/{name}[{datetime.now().date()}].xlsx'")
        else :
            self.msg.showWarning(text="No Data In App Please Try Again Later")





class Page2(QObject):
    msg = MyMessageBox()
    def __init__(self, parent):
        super().__init__()
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(parent)
        self.frame = QtWidgets.QFrame(parent)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setIcon(QIcon("Data\Icons\icons8-repeat-64.png"))
        self.toolButton.setIconSize(QSize(50,50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.clicked.connect(self.refresh)
        self.verticalLayout.addWidget(self.toolButton)

        self.frame_2 = QtWidgets.QFrame(parent)
        self.horizontLayout = QtWidgets.QHBoxLayout(self.frame_2)
        
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setText("Count : 0")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontLayout.addWidget(self.label)
        self.treeWidget = MyQTreeWidget(
            self.frame_2,
            counterLabel = self.label ,
            )

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setText("NumbersCount : 0")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontLayout.addWidget(self.label_2)
        self.treeWidget.setColumns(["Sheet Name","Numbers Count"])
        self.treeWidget.setColumnWidth(0,250)
        self.treeWidget.setColumnWidth(1,150)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.Menu)
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout_1.addWidget(self.frame)

    def refresh(self):
        files = [file for file in os.listdir("Data\Exports") if ".xlsx" in file]
        self.treeWidget.clear()
        for file in files:
            wb = openpyxl.load_workbook(f"Data\Exports\{file}")#, use_iterators=True
            sheet = wb.worksheets[0]
            row_count = sheet.max_row
            self.treeWidget.appendData(
                items = [file,str(row_count-1)] ,
                Icon = "Data\Icons\icons8-export-excel-100.png" ,
            )
        self.label_2.setText(f"NumbersCount : {self.totalNumbers()}")

    def Menu(self):
        menu = MyCustomContextMenu(
            Actions_arg=[
                #"Open Excel Sheet",
                "Copy Sheet Numbers" ,
                "Copy All Sheet Numbers" ,
                "Delete sheet" ,
            ]
        )
        menu.multiConnect(functions=[
            lambda : self.copyNumbersFromExcel() ,
            lambda : self.copyNumbersFromExcelAll(),
            lambda : self.deleteSheet(),
        ])
        menu.show()

    def copyNumbersFromExcel(self):
        file = self.treeWidget.currentItem().text(0)
        df = pandas.read_excel(f"Data\Exports\{file}")
        try:
            pyperclip.copy(df["Phone number"].to_string(index=False)) 
        except:
            pyperclip.copy(df[df.columns[1]].to_string(index=False)) 

    def copyNumbersFromExcelAll(self):
        result = ""
        for sheet in range(self.treeWidget._ROW_INDEX):
            file = self.treeWidget.topLevelItem(sheet).text(0)
            df = pandas.read_excel(f"Data\Exports\{file}")
            try:
                string = df["Phone number"].to_string(index=False)#index=False
            except KeyError:
                try:
                    string = df[df.columns[1]].to_string(index=False)#
                except IndexError :
                    string = ""
            result = (result + "\n" + string ) if string != "" else result
        pyperclip.copy(result)
        

    def deleteSheet(self):
        file = self.treeWidget.currentItem().text(0)
        try:
            os.remove(f"Data\Exports\{file}")
        except :
            self.msg.showCritical(
                text="Can't delete this excel sheet :\n please make sure you don't open this file currently" ,
                title = "Delete Faild" ,
            )

    def totalNumbers(self)-> int :
        total = 0
        for sheet in range(self.treeWidget._ROW_INDEX):
            total += int(self.treeWidget.topLevelItem(sheet).text(1))
        return total
        
