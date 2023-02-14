from MyPyQt5 import (MyQMainWindow,
                    MyMessageBox,
                    MyThread,
                    QSideMenuEnteredLeaved , 
                    QIcon ,
                    QSize,
                    QShortcut,
                    QKeySequence ,
                    pyqtSignal ,
                    )

from pages import Page1 , Page2


class Window(MyQMainWindow):
    msg = MyMessageBox()
    def SetupUi(self):
        self.resize(600,550)
        #self.setFrameLess()
        self.Menu = QSideMenuEnteredLeaved(
            parent= self.mainWidget ,
            ButtonsCount = 2 ,
            PagesCount = 2 ,
            ButtonsFixedHight = 50 ,
            ButtonsFrameFixedwidthMini = 50 , 
            ButtonsFrameFixedwidth = 130 ,
            ExitButtonIconPath = "Data\Icons\\reject.png" ,
            MaxButtonIconPath = "Data\Icons\maximize.png",
            Mini_MaxButtonIconPath = "Data\Icons\minimize.png",
            MiniButtonIconPath = "Data\Icons\delete.png",
        )
        page1 =  self.Menu.getPage(0)
        page2 = self.Menu.getPage(1)
        self.Page1 = Page1(page1)
        self.Page2 = Page2(page2)
        self.hideBrowser = self.Menu.setToggleText(0,"HideBrowser")
        self.darkMode = self.Menu.setToggleText(1,"Dark Mode")
        self.dashboard = self.Menu.getButton(0)
        self.dashboard.setIcon(QIcon("Data\Icons\dashboard.png"))
        self.dashboard.setIconSize(QSize(30,30))
        self.dashboard.setTexts("","  Dash Board")
        self.Menu.connect_Button_Page(btn = self.dashboard,pageIndex = 0 ,)
        self.exports = self.Menu.getButton(1)
        self.exports.setIcon(QIcon("Data\Icons\icons8-export-excel-96.png"))
        self.exports.setIconSize(QSize(35,35))
        self.exports.setTexts("","  Exports")
        self.Menu.connect_Button_Page(btn = self.exports,pageIndex = 1 ,)
        self.startShort = QShortcut(QKeySequence("enter"),self)
        self.startShort.activated.connect(self.op)
        
        self.Thread = MainThread()
        self.Thread.setMainClass(self)
        self.Thread.statues.connect(self.Menu.MainLabel.setText)
        self.Thread.lead.connect(self.Page1.treeWidget.appendData)


        self.Menu.setCurrentPage(0)
        return super().SetupUi()

    def op(self):
        print("hi")

class MainThread(MyThread):
    lead = pyqtSignal(list)

    def run(self) -> None:
        pass
        #self.setMainClass(Window)
        
        #return super().run()

    




w = Window()
w.show()










