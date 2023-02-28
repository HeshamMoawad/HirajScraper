####################################################

# MIT License

# Copyright (c) 2023 HeshamMoawad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Contact Me 
# GitHub : github.com/HeshamMoawad
# Gmail : HeshamMoawad120120@gmail.com
# Whatsapp : +201111141853

####################################################


class Styles():


    @property
    def main(self)->str:
        return self.Widget.Normal + self.Label.Normal+ self.LineEdit.Normal + self.ComboBox.Normal + self.SpinBox.Normal + self.PushButton.Normal + self.GroupBox.Normal + self.Frame.Normal

    class Colors():
        Orange = "rgb(255, 112, 16)"
        DarkOrangeToggle = "#ff7010"

    class Backgrounds():
        Transparent = f"background-color:transparent;"
        Orange = "background-color:rgb(255, 112, 16);color:black;"
        DarkOrange = """background-color:black;color:white;"""
        LineEdit = """"background-color:gray;color:black;"""
        Blue = "background-color:blue;color:white;"
        gradiant = """background-color:qlineargradient(spread:pad, x1:0.943, y1:0.733591, x2:0.131, y2:0.500227, stop:0 rgba(0, 0, 0, 210), stop:1 rgba(0, 68, 150, 255));"""
        Black = """background-color:black;color:white;"""
        White = """background-color:lightgray;color:black;"""

    class LineEdit():
        Normal = """
        QLineEdit{
            font:14px;
            border-radius:4px;
            background-color:white;
            color:black;
        }
        """

    class Label():
        Normal = """        
        QLabel{
            background-color:transparent;
        }  
        """
    class Widget():
        Normal = """
        QWidget{
            font:16px;
            color:white;
            background-color:qlineargradient(spread:pad, x1:0.943, y1:0.733591, x2:0.131, y2:0.500227, stop:0 rgba(0, 0, 0, 210), stop:1 rgba(0, 68, 150, 255));
        }
        """
    class ComboBox():
        Normal = """
        QComboBox{
            border-radius:4px;
            background-color:white;
            color:black;
        }
        QComboBox QListView{
            border-radius:4px;
            background-color:white;
            color:black;
        }
        """
    class SpinBox():
        Normal = """
        
        QSpinBox{
            background-color:white;
            border-radius:4px;
            color:black;
        }
        """

    class GroupBox():
        Normal = """
        QGroupBox{
            /*
            border:2px;
            border-radius:2px;*/
            background-color:transparent;
        }
        """

    class PushButton():
        Normal = """
        QToolButton{
            background-color:transparent;
            border-radius:6px;
        }
        QToolButton:hover{
            background-color:darkgray;
            color:black;
        }
        QPushButton{
            background-color:transparent;
            border-radius:6px;
        }
        QPushButton:hover{
            background-color:darkgray;
            color:black;
        }
        
        """
    class Frame():
        Normal = """
        MyQFrame{
            background-color:transparent;
        }
        QFrame{
            background-color:transparent;
        }
        """
        custom = """
        MyQFrame{
            background-color:blue;
        }
        QFrame{
            background-color:blue;
        }
        """
    class TreeWidget():
        Normal = """
        MyQTreeWidget{
            color:black;
            background-color:white;
        }
        MyQTreeWidget QHeaderView{
            color:black;
            background-color:white;
        }
        """


