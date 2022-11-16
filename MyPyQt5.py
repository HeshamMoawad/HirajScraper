from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import typing,pandas


class MyQTreeWidget(QTreeWidget):
    ROW_INDEX = 0
    def __init__(self, parent: typing.Optional[QWidget] = ...) -> None:
        super().__init__(parent)
        
    def extract_data_to_DataFrame(self)-> pandas.DataFrame:
        self.COLUMN_NAMES = [self.headerItem().text(i) for i in range(self.columnCount())]
        self.df = pandas.DataFrame(columns=self.COLUMN_NAMES)
        for col_index in range(self.columnCount()):
            col_vals = []
            for row_index in range(self.topLevelItemCount()):
                text = self.topLevelItem(row_index).text(col_index)
                col_vals.append(text)
                for ch_index in range(self.topLevelItem(row_index).childCount()):
                    chtext = self.topLevelItem(row_index).child(ch_index).text(col_index)
                    col_vals.append(chtext)
            self.df[self.COLUMN_NAMES[col_index]] = col_vals
        return self.df

    def extract_data_to_list(self,index_of_column)->list:
        return self.extract_data_to_DataFrame()[self.COLUMN_NAMES[index_of_column]].to_list()
    
    def appendData(self,items:list=None,childs:list=None)->None:

        item_ = QTreeWidgetItem(self)
        for i in range(self.columnCount()):
            self.topLevelItem(self.ROW_INDEX).setText(i,items[i])
        if childs != None:
            childindex = 0
            if type(childs[0]) is list :
                for child in childs:
                    child_ = QTreeWidgetItem(item_)
                    for i in range(self.columnCount()):
                        self.topLevelItem(self.ROW_INDEX).child(childindex).setText(i, child[i])
                    childindex += 1
            else:
                child_ = QTreeWidgetItem(item_)
                for i in range(self.columnCount()):
                    self.topLevelItem(self.ROW_INDEX).child(childindex).setText(i, childs[i])
        self.ROW_INDEX += 1







    def setColumns(self, columns: list) -> None:
        for column in columns:
            self.headerItem().setText(columns.index(column),str(column))

    def takeTopLevelItem(self, index: int) -> QTreeWidgetItem:
        self.ROW_INDEX -= 1
        return super().takeTopLevelItem(index)

    def clear(self) -> None:
        self.ROW_INDEX = 0
        return super().clear()

