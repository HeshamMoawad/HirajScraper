from Packages import (
    MyQMainWindow,
    QSideMenuEnteredLeaved ,
    QIcon,
    QSize
)
from mainclass import HirajSlots


class Window(MyQMainWindow):
    def SetupUi(self):
        self.resize(650,550)
        self.Menu = QSideMenuEnteredLeaved(
            parent = self.mainWidget ,
            Title = "Welcome " ,
            ButtonsCount = 2 ,
            PagesCount = 2 ,
            ToggleCount = 0 ,
            ButtonsFixedHight = 50 ,
            ButtonsFrameFixedwidthMini = 50 , 
            ButtonsFrameFixedwidth = 120 ,
            ExitButtonIconPath = "Data\Icons\\reject.png" ,
            MaxButtonIconPath = "Data\Icons\maximize.png",
            Mini_MaxButtonIconPath = "Data\Icons\minimize.png",
            MiniButtonIconPath = "Data\Icons\delete.png",
        )

        self.DashBoardBtn = self.Menu.getButton(0)
        self.DashBoardBtn.setTexts(entred=' DashBoard',leaved='')
        self.DashBoardBtn.setIcon(QIcon('Data\Icons\dashboard.png'))
        self.DashBoardBtn.setIconSize(QSize(30,30))
        self.SettingBtn = self.Menu.getButton(1)
        self.SettingBtn.setIcon(QIcon('Data\Icons\setting.png'))
        self.SettingBtn.setIconSize(QSize(30,30))
        self.SettingBtn.setTexts(entred=' Setting',leaved='')
        # self.DashBoard = Page1(self.Menu.getPage(0))
        # self.Setting = Page2(self.Menu.getPage(1))
        # self.Setting.ExportRangeSignal.connect(self.DashBoard.setExportRange)
        self.Menu.connect_Button_Page(btn = self.DashBoardBtn ,pageIndex = 0)
        self.Menu.connect_Button_Page(btn = self.SettingBtn ,pageIndex = 1)





        return super().SetupUi()






w = Window()
w.show()


