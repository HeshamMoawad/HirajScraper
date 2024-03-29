from PyQt5 import QtCore, QtWidgets
from Packages import (
    QObject , 
    MyQTreeWidget , 
    QIcon, 
    QSize , 
    MyCustomContextMenu,
    MyMessageBox ,
    QFont ,
    AnimatedToggle ,
    pyqtSignal
)

import os , openpyxl,pandas,pyperclip,typing
from datetime import datetime
import subprocess
from styles import Styles


class Search(QObject):
    msg = MyMessageBox()
    Name = ""
    def __init__(self, parent):
        super().__init__()
        # ['UserName','PhoneNumber','Title','LastSeen']
        self.keyword = ''
        self.ExportRange = {'UserName':0,'PhoneNumber':1,'Title':2,'LastSeen':3 }
        self.gridLayout = QtWidgets.QGridLayout(parent)
        self.MainFrame = QtWidgets.QFrame(parent)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainFrame)
        self.TitleFrame = QtWidgets.QFrame(self.MainFrame)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.TitleFrame)
        self.TitleLabel = QtWidgets.QLabel(self.TitleFrame)
        self.TitleLabel.setText('Search')
        font = QFont()
        font.setPointSize(14)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.TitleLabel, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.TitleFrame)
        self.ExportNameFrame = QtWidgets.QFrame(self.MainFrame)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ExportNameFrame)
        self.ExportNameLabel = QtWidgets.QLabel(self.ExportNameFrame)
        self.ExportNameLabel.setText('Export Name')
        self.horizontalLayout.addWidget(self.ExportNameLabel, 0, QtCore.Qt.AlignHCenter)
        self.ExportNameLineEdit = QtWidgets.QLineEdit(self.ExportNameFrame)
        self.ExportNameLineEdit.setPlaceholderText('Enter Export Name ...')
        self.horizontalLayout.addWidget(self.ExportNameLineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.ExportNameFrame)
        self.StartStopFrame = QtWidgets.QFrame(self.MainFrame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.StartStopFrame)
        self.horizontalLayout_2.setSpacing(20)
        self.StartBtn = QtWidgets.QToolButton(self.StartStopFrame)
        self.StartBtn.setText("Start")
        self.StartBtn.setAutoRaise(False)
        self.StartBtn.setShortcut('enter')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.StartBtn.setSizePolicy(sizePolicy)
        self.horizontalLayout_2.addWidget(self.StartBtn)
        self.StopBtn = QtWidgets.QToolButton(self.StartStopFrame)
        self.StopBtn.setText('Stop')
        self.StopBtn.setAutoRaise(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.StopBtn.setSizePolicy(sizePolicy)
        self.horizontalLayout_2.addWidget(self.StopBtn)
        self.verticalLayout_2.addWidget(self.StartStopFrame)
        self.frame_2 = QtWidgets.QFrame(self.MainFrame)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.counterLabel = QtWidgets.QLabel(self.frame_2)
        self.counterLabel.setText('Count : 0')
        self.treeWidget = MyQTreeWidget(self.frame_2,counterLabel=self.counterLabel)
        self.treeWidget.setStyleSheet(Styles.TreeWidget.Normal)
        self.treeWidget.setColumns(['UserName','PhoneNumber','Title','LastSeen'])
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.menu)
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.counterLabel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(3, 15)
        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)

    def menu (self):
        menu = MyCustomContextMenu(
            Actions_arg=[
                "Copy UserName", 
                "Copy PhoneNumber", 
                "Delete Row", 
                "Export To Excel", 
                "Clear Data" ,
            ])
        menu.multiConnect(functions=[
            lambda: self.copy(0) ,
            lambda: self.copy(1) ,
            lambda: self.delete() ,
            lambda : self.export(f"{self.ExportNameLineEdit.text()}-'{self.keyword}'",self.ExportRange),
            lambda : self.treeWidget.clear()
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

    def export(self,name:typing.Optional[str],values:dict):
        if name == "-''" or name == "-''":
            name = f"Hour{datetime.now().hour}Minute{datetime.now().minute}"
        if self.treeWidget._ROW_INDEX > 0 :
            self.treeWidget.getCustomDataFrame(values).to_excel(f"Data/Exports/{name}[{datetime.now().date()}].xlsx",index=False)
            self.msg.showInfo(text=f"Exported Succecfully to 'Data/Exports/{name}[{datetime.now().date()}].xlsx'")
        else :
            self.msg.showWarning(text="No Data In App Please Try Again Later")

    def setkeyword(self , keyword):
        self.keyword = keyword

    def setExportRange(self,values:dict):
        self.ExportRange = values



class Setting(QObject):
    CATEGORIES = ['كل الحراج','حراج السيارات', 'حراج العقار', 'حراج الأجهزة', 'مواشي وحيوانات وطيور', 'اثاث', 'مستلزمات شخصية', 'خدمات', 'وظائف', 'اطعمة ومشروبات', 'برمجة وتصاميم', 'مكتبة وفنون', 'صيد ورحلات']
    SUBCATEGORY = [['', 'هونشي', 'زوتي', 'ماهيندرا', 'ساوايست', 'تسلا', 'بايك', 'جاك JAC', 'ماكلارين', 'ماكسيس', 'ليفان', 'فيكتوري اوتو', 'فوتون', 'سي ام سي', 'جيتور', 'جى ام سي JMC', 'تاتا', 'الفا روميو', 'BYD', 'فاو FAW', 'جريت وول Great Wall', 'جي ايه سي GAC', 'هافال', 'بروتون', 'استون مارتن', 'سانج يونج', 'فيات', 'ساب', 'دايو', 'سيات', 'تشيري', 'سيتروين', 'فيراري', 'سكودا', 'اوبل', 'لامبورجيني', 'رولز رويس', 'مازيراتي', 'بيوك', ' رينو', 'شانجان', 'ZXAUTO', 'MG', 'سوبارو', 'جاكوار', 'بنتلي', 'بيجو', 'فولفو', 'ميركوري', 'جيلي', 'ديهاتسو', 'فولكس واجن', 'لنكولن', 'همر', 'انفنيتي', 'سوزوكي', 'اودي', 'بورش', 'كاديلاك', 'ايسوزو', 'لاند روفر', 'مازدا', 'ميتسوبيشي', 'جيب','كرايزلر', 'دودج', 'كيا', 'دبابات', 'بي ام دبليو', 'هوندا', 'مرسيدس', 'شاحنات ومعدات ثقيلة', 'جي ام سي', 'لكزس', 'جنسس', 'هونداي', 'نيسان', 'قطع غيار وملحقات', 'شيفروليه', 'فورد', 'تويوتا'], ['', 'بيوت للايجار', 'ادوار للايجار', 'مزارع للبيع', 'فلل للايجار', 'استراحات للبيع', 'عماره للايجار', 'محلات للايجار', 'محلات للتقبيل', 'استراحات للايجار', 'عمارة للبيع', 'اراضي تجارية للبيع', 'بيوت للبيع', 'شقق للبيع', 'فلل للبيع', 'شقق للايجار', 'اراضي للبيع'], ['', 'غسالة سامسونج', 'ثلاجة سامسونج', 'اجهزة غير مصنفة', 'هيتاشي Hitachi', 'باناسونيك Panasonic', 'مايكروسوفت Microsoft', 'ال جي LG', 'أرقام مميزة', 'حسابات واشتراكات', 'كاميرات تصوير', 'تلفزيونات وصوتيات', 'ألعاب إلكترونية', 'أجهزة كمبيوتر', 'أجهزة تابلت', 'جوالات'], ['', 'وبر', 'هامستر', 'سناجب', 'بط', 'ارانب', 'أسماك وسلاحف', 'بقر', 'كلاب', 'خيل', 'أبل', 'دجاج', 'قطط', 'حمام', 'ببغاء', 'ماعز', 'غنم'], ['', 'مجالس ومفروشات', 'طاولات وكراسي', 'خزائن ودواليب', 'تحف وديكور', 'أسرة ومراتب', 'أدوات منزلية', 'أثاث مكتبي', 'أثاث خارجي'], ['', 'ملابس أطفال', 'ملابس نسائية', 'ملابس رجالية', 'نظارات', 'مستلزمات رياضية', 'عطورات', 'ساعات'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات','زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفر وسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['', 'مفقودات', 'قسم غير مصنف', 'سفروسياحة', 'حفلات ومناسبات', 'زراعة وحدائق', 'العاب وترفيه'], ['']]
    AREAS = ["","الرياض","الشرقيه","جده","مكه","ينبع","حفر الباطن","المدينة","الطايف","تبوك","القصيم","حائل","أبها","عسير","الباحة","جيزان","نجران","الجوف","عرعر","الكويت","الإمارات","البحرين"]
    msg = MyMessageBox()
    ExportRangeSignal = pyqtSignal(dict)
    keywordSignal = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__()
        self.gridLayout = QtWidgets.QGridLayout(parent)
        self.MainFrame = QtWidgets.QFrame(parent)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainFrame)
        self.SettingFrame = QtWidgets.QFrame(self.MainFrame)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.SettingFrame)
        self.SettingLabel = QtWidgets.QLabel(self.SettingFrame)
        font = QFont()
        font.setPointSize(14)
        self.SettingLabel.setFont(font)
        self.SettingLabel.setText('Setting')
        self.gridLayout_2.addWidget(self.SettingLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.SettingFrame)
        self.keywordLimitMainFrame = QtWidgets.QFrame(self.MainFrame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.keywordLimitMainFrame)
        self.KeyWordFrame = QtWidgets.QFrame(self.keywordLimitMainFrame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.KeyWordFrame)
        self.KeyWordLabel = QtWidgets.QLabel(self.KeyWordFrame)
        self.KeyWordLabel.setText('KeyWord')
        self.horizontalLayout_2.addWidget(self.KeyWordLabel, 0, QtCore.Qt.AlignHCenter)
        self.KeyWordLineEdit = QtWidgets.QLineEdit(self.KeyWordFrame)
        self.KeyWordLineEdit.textChanged.connect(self.keywordSignal.emit)
        self.KeyWordLineEdit.setPlaceholderText('Enter KeyWord Here ...')
        self.horizontalLayout_2.addWidget(self.KeyWordLineEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_3.addWidget(self.KeyWordFrame)
        self.LimitFrame = QtWidgets.QFrame(self.keywordLimitMainFrame)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.LimitFrame)
        self.LimitLabel = QtWidgets.QLabel(self.LimitFrame)
        self.LimitLabel.setText('Limit Pages')
        self.horizontalLayout.addWidget(self.LimitLabel, 0, QtCore.Qt.AlignHCenter)
        self.LimitSpinbox = QtWidgets.QSpinBox(self.LimitFrame)
        self.LimitSpinbox.setMinimum(1)
        self.LimitSpinbox.setMaximum(200)
        self.LimitSpinbox.setValue(200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.LimitSpinbox.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.LimitSpinbox)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addWidget(self.LimitFrame)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.keywordLimitMainFrame)
        self.CategorySubMainFrame = QtWidgets.QFrame(self.MainFrame)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.CategorySubMainFrame)
        self.CategoryFrame = QtWidgets.QFrame(self.CategorySubMainFrame)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.CategoryFrame)
        self.CategoryLabel = QtWidgets.QLabel(self.CategoryFrame)
        self.CategoryLabel.setText('Category')
        self.horizontalLayout_4.addWidget(self.CategoryLabel, 0, QtCore.Qt.AlignHCenter)
        self.CategoryCombobox = QtWidgets.QComboBox(self.CategoryFrame)
        self.CategoryCombobox.setFixedHeight(30)
        self.CategoryCombobox.addItems(self.CATEGORIES)
        self.CategoryCombobox.currentIndexChanged.connect(self.changeComboBox)
        self.horizontalLayout_4.addWidget(self.CategoryCombobox)
        self.horizontalLayout_6.addWidget(self.CategoryFrame)
        self.SubCategoryFrame = QtWidgets.QFrame(self.CategorySubMainFrame)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.SubCategoryFrame)
        self.SubCategoryLabel = QtWidgets.QLabel(self.SubCategoryFrame)
        self.SubCategoryLabel.setText('SubCategory')
        self.SubCategoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_5.addWidget(self.SubCategoryLabel)
        self.SubCategoryCombobox = QtWidgets.QComboBox(self.SubCategoryFrame)
        self.SubCategoryCombobox.setFixedHeight(30)
        self.SubCategoryCombobox.setFixedWidth(150)
        self.horizontalLayout_5.addWidget(self.SubCategoryCombobox)
        self.horizontalLayout_6.addWidget(self.SubCategoryFrame)
        self.verticalLayout_2.addWidget(self.CategorySubMainFrame)
        self.CityCommentMainFrame = QtWidgets.QFrame(self.MainFrame)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.CityCommentMainFrame)
        self.CityFrame = QtWidgets.QFrame(self.CityCommentMainFrame)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.CityFrame)
        self.CityLabel = QtWidgets.QLabel(self.CityFrame)
        self.CityLabel.setText('City')
        self.horizontalLayout_7.addWidget(self.CityLabel, 0, QtCore.Qt.AlignHCenter)
        self.CityCombobox = QtWidgets.QComboBox(self.CityFrame)
        self.CityCombobox.setFixedHeight(30)
        self.CityCombobox.addItems(self.AREAS)
        self.horizontalLayout_7.addWidget(self.CityCombobox)
        self.horizontalLayout_9.addWidget(self.CityFrame)
        self.CommentsFrame = QtWidgets.QFrame(self.CityCommentMainFrame)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.CommentsFrame)
        self.CommentsLabel = QtWidgets.QLabel(self.CommentsFrame)
        self.CommentsLabel.setText('Scrape Comments')
        self.horizontalLayout_8.addWidget(self.CommentsLabel, 0, QtCore.Qt.AlignHCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.CommentsToggle = AnimatedToggle(self.CommentsFrame)
        self.CommentsToggle.setSizePolicy(sizePolicy)
        self.horizontalLayout_8.addWidget(self.CommentsToggle)
        self.horizontalLayout_9.addWidget(self.CommentsFrame)
        self.verticalLayout_2.addWidget(self.CityCommentMainFrame)
        self.ExportGroupBox = QtWidgets.QGroupBox(self.MainFrame)
        self.ExportGroupBox.setTitle('Export Options')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ExportGroupBox)
        self.UserPhoneMainFrame = QtWidgets.QFrame(self.ExportGroupBox)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.UserPhoneMainFrame)
        self.UserNameFrame = QtWidgets.QFrame(self.UserPhoneMainFrame)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.UserNameFrame)
        self.UserNameLabel = QtWidgets.QLabel(self.UserNameFrame)
        self.UserNameLabel.setText('UserName')
        self.horizontalLayout_10.addWidget(self.UserNameLabel, 0, QtCore.Qt.AlignHCenter)
        self.UserNameToggle = AnimatedToggle(self.UserNameFrame)
        self.UserNameToggle.setSizePolicy(sizePolicy)
        self.UserNameToggle.setChecked(True)
        self.horizontalLayout_10.addWidget(self.UserNameToggle)
        self.horizontalLayout_15.addWidget(self.UserNameFrame)
        self.PhoneNumberFrame = QtWidgets.QFrame(self.UserPhoneMainFrame)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.PhoneNumberFrame)
        self.PhoneNumberLabel = QtWidgets.QLabel(self.PhoneNumberFrame)
        self.PhoneNumberLabel.setText('PhoneNumber')
        self.horizontalLayout_11.addWidget(self.PhoneNumberLabel, 0, QtCore.Qt.AlignHCenter)
        self.PhoneNumberToggle = AnimatedToggle(self.PhoneNumberFrame)
        self.PhoneNumberToggle.setSizePolicy(sizePolicy)
        self.PhoneNumberToggle.setChecked(True)
        self.horizontalLayout_11.addWidget(self.PhoneNumberToggle)
        self.horizontalLayout_15.addWidget(self.PhoneNumberFrame)
        self.verticalLayout.addWidget(self.UserPhoneMainFrame)
        self.TitleLastMainFrame = QtWidgets.QFrame(self.ExportGroupBox)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.TitleLastMainFrame)
        self.TitleFrame = QtWidgets.QFrame(self.TitleLastMainFrame)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.TitleFrame)
        self.TitleLabel = QtWidgets.QLabel(self.TitleFrame)
        self.TitleLabel.setText('Title')
        self.horizontalLayout_12.addWidget(self.TitleLabel, 0, QtCore.Qt.AlignHCenter)
        self.TitleToggle = AnimatedToggle(self.TitleFrame)
        self.TitleToggle.setSizePolicy(sizePolicy)
        self.TitleToggle.setChecked(True)
        self.horizontalLayout_12.addWidget(self.TitleToggle)
        self.horizontalLayout_14.addWidget(self.TitleFrame)
        self.LastSeenFrame = QtWidgets.QFrame(self.TitleLastMainFrame)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.LastSeenFrame)
        self.LastSeenLabel = QtWidgets.QLabel(self.LastSeenFrame)
        self.LastSeenLabel.setText('LastSeen')
        self.horizontalLayout_13.addWidget(self.LastSeenLabel, 0, QtCore.Qt.AlignHCenter)
        self.LastSeenToggle = AnimatedToggle(self.LastSeenFrame)
        self.LastSeenToggle.setSizePolicy(sizePolicy)
        self.LastSeenToggle.setChecked(True)
        self.horizontalLayout_13.addWidget(self.LastSeenToggle)
        self.horizontalLayout_14.addWidget(self.LastSeenFrame)
        self.verticalLayout.addWidget(self.TitleLastMainFrame)
        self.verticalLayout_2.addWidget(self.ExportGroupBox)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(3, 3)
        self.verticalLayout_2.setStretch(4, 6)
        self.gridLayout.addWidget(self.MainFrame, 1, 0, 1, 1)



    def changeComboBox(self):
        index = self.CategoryCombobox.currentIndex()
        if index == 0 :
            self.SubCategoryCombobox.clear()
        self.SubCategoryCombobox.clear()
        self.SubCategoryCombobox.addItems(self.SUBCATEGORY[index-1])


    def exportrange(self):
        # ['UserName','Title','PhoneNumber','LastSeen']
        result = {}
        result['UserName'] = 0 if self.UserNameToggle.isChecked() else None
        result['PhoneNumber'] = 1 if self.PhoneNumberToggle.isChecked() else None
        result['Title'] = 2  if self.TitleToggle.isChecked() else None
        result['LastSeen'] = 3  if self.LastSeenToggle.isChecked() else None
        self.ExportRangeSignal.emit(result)



class Sheets(QObject):
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
        self.toolButton.setShortcut('enter')
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
        self.treeWidget.setStyleSheet(Styles.TreeWidget.Normal)
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
            try:
                wb = openpyxl.load_workbook(f"Data\Exports\{file}")#, use_iterators=True
                sheet = wb.worksheets[0]
                row_count = sheet.max_row
                self.treeWidget.appendDataAsList(
                    items = [file,str(row_count-1)] ,
                    Icon = "Data\Icons\icons8-export-excel-100.png" ,
                )
            except Exception as e :
                self.msg.showCritical("Can't Open Sheets\nPlease Make Sure you are Closed All Sheet in Directory")
        self.label_2.setText(f"NumbersCount : {self.totalNumbers()}")

    def Menu(self):
        menu = MyCustomContextMenu(
            Actions_arg=[
                "Open Excel Sheet",
                "Copy Sheet Numbers" ,
                "Copy All Sheet Numbers" ,
                "Delete sheet" ,
            ]
        )
        menu.multiConnect(functions=[
            lambda : self.openexcelsheet() ,
            lambda : self.copyNumbersFromExcel() ,
            lambda : self.copyNumbersFromExcelAll(),
            lambda : self.deleteSheet(),
        ])
        menu.show()

    def openexcelsheet(self):
        try :
            file = f"Data\Exports\{self.treeWidget.currentItem().text(0)}"
            subprocess.Popen([file], shell=True)
        except Exception as e :
            self.msg.showWarning('No sheet Selected')

    def copyNumbersFromExcel(self):
        file = self.treeWidget.currentItem().text(0)
        wb = openpyxl.load_workbook(f"Data\Exports\{file}")
        ws = wb['Sheet1']
        df = pandas.DataFrame(ws.values)
        df.dropna(inplace=True)
        df = df[1:]
        try:
            pyperclip.copy(df["Phone number"].to_string(index=False)) 
        except:
            pyperclip.copy(df[df.columns[1]].to_string(index=False)) 

    def copyNumbersFromExcelAll(self):
        self.refresh()
        result = ""
        for sheet in range(self.treeWidget._ROW_INDEX):
            file = self.treeWidget.topLevelItem(sheet).text(0)
            wb = openpyxl.load_workbook(f"Data\Exports\{file}")
            ws = wb['Sheet1']
            df = pandas.DataFrame(ws.values)
            df.dropna(inplace=True)
            df = df[1:]
            try:
                string = df[1].to_string(index=False)#index=False
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
        self.refresh()

    def totalNumbers(self)-> int :
        total = 0
        for sheet in range(self.treeWidget._ROW_INDEX):
            total += int(self.treeWidget.topLevelItem(sheet).text(1))
        return total
        


class Similar(QObject):
    msg = MyMessageBox()

    def __init__(self, parent) -> None:
        super().__init__()
        self.ExportRange = {'UserName':0,'PhoneNumber':1,'Title':2,'LastSeen':3 }
        self.gridLayout = QtWidgets.QGridLayout(parent)
        self.frame = QtWidgets.QFrame(parent)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.Similar = QtWidgets.QFrame(self.frame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Similar)
        self.SimilarLabel = QtWidgets.QLabel(self.Similar)
        self.SimilarLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SimilarLabel.setText('Similar Leads')
        self.horizontalLayout_2.addWidget(self.SimilarLabel)
        self.verticalLayout_2.addWidget(self.Similar)
        self.NumbersFrame = QtWidgets.QFrame(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.NumbersFrame)
        self.NumbersLabel = QtWidgets.QLabel(self.NumbersFrame)
        self.NumbersLabel.setText('Numbers')
        self.horizontalLayout.addWidget(self.NumbersLabel, 0, QtCore.Qt.AlignHCenter)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.NumbersFrame)
        self.plainTextEdit.setPlaceholderText('Enter Numbers That you want to Scrape Similar \nEnter numbers(same Format)like This :-\n550011122\n550011122\n550011122')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.NumbersFrame)
        self.ExportNameFrame = QtWidgets.QFrame(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ExportNameFrame)
        self.ExportNameLabel = QtWidgets.QLabel(self.ExportNameFrame)
        self.ExportNameLabel.setText('Export Name')
        self.horizontalLayout_3.addWidget(self.ExportNameLabel, 0, QtCore.Qt.AlignHCenter)
        self.ExportNameLineEdit = QtWidgets.QLineEdit(self.ExportNameFrame)
        self.ExportNameLineEdit.setPlaceholderText('Enter Export Name ...')
        self.horizontalLayout_3.addWidget(self.ExportNameLineEdit)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.ExportNameFrame)
        self.ButtonsFrame = QtWidgets.QFrame(self.frame)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ButtonsFrame)
        self.horizontalLayout_4.setSpacing(20)
        self.StartButton = QtWidgets.QToolButton(self.ButtonsFrame)
        self.StartButton.setText('Start')
        self.StartButton.setAutoRaise(False)
        self.StartButton.setShortcut('enter')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.StartButton.setSizePolicy(sizePolicy)
        self.horizontalLayout_4.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QToolButton(self.ButtonsFrame)
        self.StopButton.setText('Stop')
        self.StopButton.setAutoRaise(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.StopButton.setSizePolicy(sizePolicy)
        self.horizontalLayout_4.addWidget(self.StopButton)
        self.verticalLayout_2.addWidget(self.ButtonsFrame)
        self.TreeWidgetFrame = QtWidgets.QFrame(self.frame)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.TreeWidgetFrame)
        self.CounterLabel = QtWidgets.QLabel(self.TreeWidgetFrame)
        self.CounterLabel.setText('Count : 0')
        self.treeWidget = MyQTreeWidget(self.TreeWidgetFrame,counterLabel=self.CounterLabel)
        self.treeWidget.setStyleSheet(Styles.TreeWidget.Normal)
        self.treeWidget.setColumns(['UserName','PhoneNumber','Title','LastSeen'])
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.menu)
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.CounterLabel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.TreeWidgetFrame)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 5)
        self.verticalLayout_2.setStretch(4, 20)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

    def menu (self):
        menu = MyCustomContextMenu(
            Actions_arg=[
                "Copy UserName", 
                "Copy PhoneNumber", 
                "Delete Row", 
                "Export To Excel", 
                "Clear Data" ,
            ])
        menu.multiConnect(functions=[
            lambda: self.copy(0) ,
            lambda: self.copy(1) ,
            lambda: self.delete() ,
            lambda : self.export(f"{self.ExportNameLineEdit.text()}-'Similar'",self.ExportRange),
            lambda : self.treeWidget.clear()
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

    def export(self,name:typing.Optional[str],values:dict):
        if name == '' or name == ' ':
            name = f"Hour{datetime.now().hour}Minute{datetime.now().minute}"
        if self.treeWidget._ROW_INDEX > 0 :
            self.treeWidget.getCustomDataFrame(values).to_excel(f"Data/Exports/{name}[{datetime.now().date()}].xlsx",index=False)
            self.msg.showInfo(text=f"Exported Succecfully to 'Data/Exports/{name}[{datetime.now().date()}].xlsx'")
        else :
            self.msg.showWarning(text="No Data In App Please Try Again Later")

    def setExportRange(self,values:dict):
        self.ExportRange = values

