from Packages import (
    MyQMainWindow,
    QSideMenuEnteredLeaved ,
    QIcon,
    QSize ,
    MyThread ,
    pyqtSignal ,
    Checking
)
from mainclass import Hiraj , RequestKeys
from pages import (
    Search ,
    Setting ,
    Sheets ,
    Similar 
    )

from styles import Styles


class Window(MyQMainWindow):
    def SetupUi(self):
        self.resize(650,550)
        self.setFrameLess()
        self.mainWidget.setStyleSheet(Styles().main)
        self.checker = Checking()
        if self.checker.haveInternet():
            # Define Animated Side Menu 
            self.Menu = QSideMenuEnteredLeaved(
                parent = self.mainWidget ,
                Title = "Welcome يا اخوياااااا" ,
                ButtonsCount = 4 ,
                PagesCount = 4 ,
                ToggleCount = 0 ,
                ButtonsFixedHight = 50 ,
                ButtonsFrameFixedwidthMini = 50 , 
                ButtonsFrameFixedwidth = 120 ,
                ExitButtonIconPath = "Data\Icons\\reject.png" ,
                MaxButtonIconPath = "Data\Icons\maximize.png",
                Mini_MaxButtonIconPath = "Data\Icons\minimize.png",
                MiniButtonIconPath = "Data\Icons\delete.png",
            )
            # Search Button in Side Menu 
            self.SearchBtn = self.Menu.getButton(0)
            self.SearchBtn.setTexts(entred=' Search',leaved='')
            self.SearchBtn.setIcon(QIcon('Data\Icons\icons8-search-100.png'))
            self.SearchBtn.setIconSize(QSize(30,30))
            # Setting Button in Side Menu 
            self.SettingBtn = self.Menu.getButton(1)
            self.SettingBtn.setIcon(QIcon('Data\Icons\setting.png'))
            self.SettingBtn.setIconSize(QSize(30,30))
            self.SettingBtn.setTexts(entred=' Setting',leaved='')
            # Sheets Button in Side Menu 
            self.SheetsBtn = self.Menu.getButton(2)
            self.SheetsBtn.setIcon(QIcon('Data\Icons\icons8-microsoft-excel-100.png'))
            self.SheetsBtn.setIconSize(QSize(30,30))
            self.SheetsBtn.setTexts(entred=' Sheets',leaved='')
            # Similar Button in Side Menu 
            self.SimilarBtn = self.Menu.getButton(3)
            self.SimilarBtn.setIcon(QIcon('Data\Icons\icons8-child-64.png'))
            self.SimilarBtn.setIconSize(QSize(30,30))
            self.SimilarBtn.setTexts(entred=' Similar',leaved='')
            # Define All Pages
            self.SearchPage = Search(self.Menu.getPage(0))
            self.SettingPage = Setting(self.Menu.getPage(1))
            self.SheetsPage = Sheets(self.Menu.getPage(2))
            self.SimilarPage = Similar(self.Menu.getPage(3))
            self.SettingPage.keywordSignal.connect(self.SearchPage.setkeyword)
            # Connect Export Range With Other Pages
            self.SettingPage.ExportRangeSignal.connect(self.SearchPage.setExportRange)
            self.SettingPage.ExportRangeSignal.connect(self.SimilarPage.setExportRange)
            # Connect Side Menu Buttons With Pages
            self.Menu.connect_Button_Page(btn = self.SearchBtn ,pageIndex = 0)
            self.Menu.connect_Button_Page(btn = self.SettingBtn ,pageIndex = 1)
            self.Menu.connect_Button_Page(btn = self.SheetsBtn ,pageIndex = 2)
            self.Menu.connect_Button_Page(btn = self.SimilarBtn ,pageIndex = 3)
            # SearchThread Part 
            self.SearchThread = SearchThread()
            self.SearchThread.setMainClass(self)
            self.SearchThread.msg.connect(self.msg.showInfo)
            self.SearchThread.status.connect(self.Menu.MainLabel.setText)
            self.SearchThread.hiraj.msg.connect(self.msg.showInfo)
            self.SearchThread.hiraj.status.connect(self.Menu.MainLabel.setText)
            self.SearchThread.hiraj.LeadSignal.connect(self.SearchPage.treeWidget.appendDataAsDict)
            self.SearchPage.StartBtn.clicked.connect(self.SearchThread.start)
            self.SearchPage.StopBtn.clicked.connect(lambda : self.SearchThread.kill(msg='Stopped Search Succecfully'))
            # SimilarThread Part 
            self.SimilarThread = SimilarThread() 
            self.SimilarThread.setMainClass(self)
            self.SimilarThread.msg.connect(self.msg.showInfo)
            self.SimilarThread.status.connect(self.Menu.MainLabel.setText)
            self.SimilarThread.hiraj.msg.connect(self.msg.showInfo)
            self.SimilarThread.hiraj.status.connect(self.Menu.MainLabel.setText)
            self.SimilarThread.hiraj.LeadSignal.connect(self.SimilarPage.treeWidget.appendDataAsDict)
            self.SimilarPage.StartButton.clicked.connect(self.SimilarThread.start)
            self.SimilarPage.StopButton.clicked.connect( lambda :self.SimilarThread.kill(msg='Stopped Similar Search Succecfully') )
            # styles
            self.Menu.TopFrame.setStyleSheet(Styles.Backgrounds.White)
            self.setAppIcon("Data\Icons\hiraj.png")
            return super().SetupUi()


class SearchThread(MyThread):
    LeadSignal = pyqtSignal(dict)
    msg = pyqtSignal(str)
    status = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.hiraj = Hiraj()

    def setMainClass(self,window:Window):
        self.MainClass = window

    def run(self) -> None:
        self.statues.emit('Starting Search')
        category = self.MainClass.SettingPage.CategoryCombobox.currentText()
        subcategory = self.MainClass.SettingPage.SubCategoryCombobox.currentText()
        tag = category if subcategory == '' else subcategory
        city = [self.MainClass.SettingPage.CityCombobox.currentText()] if self.MainClass.SettingPage.CityCombobox.currentText() != '' else []
        key = self.MainClass.SettingPage.KeyWordLineEdit.text()
        keyword = key if key != '' and key != ' ' else ''
        self.statues.emit(f'Starting Search with keyword {keyword}')
        self.hiraj.Search(
            limitPage = self.MainClass.SettingPage.LimitSpinbox.value() ,
            comments = self.hiraj.HirajBase.Flags.Yes if self.MainClass.SettingPage.CommentsToggle.isChecked() else self.hiraj.HirajBase.Flags.No ,
            **{
                RequestKeys.Search.tag : tag ,
                RequestKeys.Search.cities : city ,
                RequestKeys.Search.search : keyword ,
            })

        self.statues.emit('Ending good luck ^_^')
        self.msg.emit('Ending good luck ^_^')

    def kill(self, msg: str = None):
        if self.isRunning():
            self.status.emit("Stopped Succecfully")
        return super().kill(msg)

class SimilarThread(MyThread):
    LeadSignal = pyqtSignal(dict)
    status = pyqtSignal(str)
    msg = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.hiraj = Hiraj()


    def setMainClass(self,window:Window):
        self.MainClass = window

    def run(self) -> None:
        self.statues.emit('Starting with Similar ')
        self.hiraj.msg.connect(self.msg.emit)
        self.hiraj.status.connect(self.status.emit)
        self.hiraj.LeadSignal.connect(self.LeadSignal.emit)
        self.hiraj.Similar(
            self.MainClass.SimilarPage.plainTextEdit.toPlainText().splitlines(),
            comments = self.hiraj.HirajBase.Flags.Yes if self.MainClass.SettingPage.CommentsToggle.isChecked() else self.hiraj.HirajBase.Flags.No
            )
        self.statues.emit('Ending good luck ^_^')
        self.msg.emit('Ending good luck ^_^')

        

w = Window()
w.show()


