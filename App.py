from Packages import (
    MyQMainWindow,
    QSideMenuEnteredLeaved ,
    QIcon,
    QSize
)
from mainclass import HirajSlots
from pages import (
    Search ,
    Setting ,
    Sheets ,
    Similar
    )



class Window(MyQMainWindow):
    def SetupUi(self):
        self.resize(650,550)
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
        self.SearchBtn.setIcon(QIcon('Data\Icons\dashboard.png'))
        self.SearchBtn.setIconSize(QSize(30,30))
        # Setting Button in Side Menu 
        self.SettingBtn = self.Menu.getButton(1)
        self.SettingBtn.setIcon(QIcon('Data\Icons\setting.png'))
        self.SettingBtn.setIconSize(QSize(30,30))
        self.SettingBtn.setTexts(entred=' Setting',leaved='')
        # Sheets Button in Side Menu 
        self.SheetsBtn = self.Menu.getButton(2)
        self.SheetsBtn.setIcon(QIcon('Data\Icons\setting.png'))
        self.SheetsBtn.setIconSize(QSize(30,30))
        self.SheetsBtn.setTexts(entred=' Sheets',leaved='')
        # Similar Button in Side Menu 
        self.SimilarBtn = self.Menu.getButton(3)
        self.SimilarBtn.setIcon(QIcon('Data\Icons\setting.png'))
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










w = Window()
w.show()


