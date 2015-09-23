from PyQt4        import QtCore,QtGui,uic
from PyQt4.QtCore import SIGNAL,Qt,QVariant
import logging
import sys
import csv 

logging.basicConfig(level=logging.DEBUG)


class GelmaGui(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent=parent)
        uic.loadUi('gui.ui',self)
        self.logger = logging.getLogger('GelmaGui')
        self.my_model = GelmaModel()
        self.tableView.setModel(self.my_model)


class GelmaModel(QtCore.QAbstractTableModel):
    
    def __init__(self,parent=None,*args):
        super(GelmaModel,self).__init__(parent,*args)
        self.header = ['id','link','value']
        self.data_model = [
            [1,2,3],
            [4,6,7],
            [5,6,8],
            [9,1,4]
        ]
    
    def data(self,index,role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        if self.data_model != None:
            keys = self.header
            info = self.data_model[index.row()][index.column()]
            return QVariant(info)
        return QVariant()

    def rowCount(self,parent):
        return len(self.data_model)

    def columnCount(self,parent):
#        self.logger.debug("Model is %s"%self.model)
#        return len(self.model[0].keys())
        return len(self.header)

    def headerData(self,col,orientation,role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
#            return QVariant(self.model[0].keys()[col])
            return QVariant(self.header[col])



app = QtGui.QApplication(sys.argv)
issueGui = GelmaGui()
issueGui.show()
logging.info(issueGui.tableView)
app.exec_()
