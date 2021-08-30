import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class TreeWidgetDemo(QMainWindow):
      
  def checkEdit(self, item, column):
    tmp = item.flags()
    if column == 0 :
        item.setFlags(tmp | Qt.ItemIsEditable)
    elif tmp & Qt.ItemIsEditable:
        item.setFlags(tmp ^ Qt.ItemIsEditable)

  def __init__(self, parent=None):
    super(TreeWidgetDemo, self).__init__(parent)
    self.setWindowTitle('TreeWidget 例子')

    self.tree=QTreeWidget()
    self.tree.setStyleSheet("QTreeWidget::item{border-right: 1px solid green;border-bottom: 1px solid green;}"
                            "QTreeView::item:hover{background-color:rgb(0,255,0,50)}"
                            "QTreeView::item:selected{background-color:rgb(255,0,0,100)}");
    self.tree.itemDoubleClicked.connect(self.checkEdit)  
    #设置树形控件头部的标题
    self.tree.setHeaderLabels(['Key','Value','tes','ddsd','ssdd'])
    #设置根节点
    root=QTreeWidgetItem(self.tree)    
    root.setText(0,'Root')  

    root2=QTreeWidgetItem(self.tree)
    root2.setText(0,'Root2')    
    #设置子节点1
    parent = root
    for x in range(1,4096):        
        child1=QTreeWidgetItem(parent)
        child1.setFlags(child1.flags() | Qt.ItemIsEditable)
        child1.setText(0,str(x))
        child1.setText(1,'ios')
        child1.setText(2,'ios')        
        parent = child1

    #加载根节点的所有属性与子控件
    self.tree.addTopLevelItem(root)

    #TODO 优化3 给节点添加响应事件
    self.tree.clicked.connect(self.onClicked)


    #节点全部展开
    self.tree.expandAll()
    self.setCentralWidget(self.tree)

  def onClicked(self,qmodeLindex):
    item=self.tree.currentItem()
    print('Key=%s,value=%s'%(item.text(0),item.text(1)))

if __name__ == '__main__':
  app = QApplication(sys.argv)
  tree = TreeWidgetDemo()
  tree.show()
  sys.exit(app.exec_())