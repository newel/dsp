from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
import main


if __name__ == '__main__':
    app = QApplication(sys.argv) 
    mainWindow = main.Main()
    mainWindow.show()
    sys.exit(app.exec_())