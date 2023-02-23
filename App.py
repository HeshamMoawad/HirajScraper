from Packages import (
    MyQMainWindow,
    QSideMenuEnteredLeaved ,
    QIcon,
    QSize ,
    MyThread ,
    pyqtSignal
)
from mainclass import Hiraj , RequestKeys
from pages import (
    Search ,
    Setting ,
    Sheets ,
    Similar )
from styles import Styles


class Window(MyQMainWindow):
    def SetupUi(self):
        self.resize(650,550)
        # self.mainWidget.setStyleSheet(Styles().main)
        # Define Animated Side Menu 
        self.Menu = QSideMenuEnteredLeaved(
            parent = self.mainWidget ,
            Title = "Welcome " ,
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
        # Connect Export Range With Other Pages
        self.SettingPage.ExportRangeSignal.connect(self.SearchPage.setExportRange)
        self.SettingPage.ExportRangeSignal.connect(self.SimilarPage.setExportRange)
        # Connect Side Menu Buttons With Pages
        self.Menu.connect_Button_Page(btn = self.SearchBtn ,pageIndex = 0)
        self.Menu.connect_Button_Page(btn = self.SettingBtn ,pageIndex = 1)
        self.Menu.connect_Button_Page(btn = self.SheetsBtn ,pageIndex = 2)
        self.Menu.connect_Button_Page(btn = self.SimilarBtn ,pageIndex = 3)


        return super().SetupUi()



class SearchThread(MyThread):
    LeadSignal = pyqtSignal(dict)


    def setMainClass(self,window:Window):
        self.MainClass = window

    def run(self) -> None:

        # Block Of Code
        tag = self.MainClass.SettingPage.SubCategoryCombobox.currentText() if self.MainClass.SettingPage.SubCategoryCombobox.currentIndex() != 0 else self.MainClass.SettingPage.CategoryCombobox.currentText()
        city = [self.MainClass.SettingPage.CityCombobox.currentText()] if self.MainClass.SettingPage.CityCombobox.currentIndex() != 0 else []
        key = self.MainClass.SettingPage.KeyWordLineEdit.text()
        keyword = key if key != '' and key != ' ' else ''
        hiraj = Hiraj()
        hiraj.LeadSignal.connect(self.LeadSignal.emit)
        hiraj.msg.connect(self.msg.emit)
        args = {
                RequestKeys.Search.tag: tag ,
                RequestKeys.Search.cities:city ,
                RequestKeys.Search.search:keyword ,
            }
        print(args)
        # hiraj.Search(
        #     limitPage = self.MainClass.SettingPage.LimitSpinbox.value() ,
        #     comments = hiraj.HirajBase.Flags.Yes if self.MainClass.SettingPage.CommentsToggle.isChecked() else hiraj.HirajBase.Flags.No
        #     **args
        #     )



        






w = Window()
w.show()


