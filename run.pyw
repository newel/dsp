import sys,os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import main_window


if __name__ == '__main__':
    app = QApplication(sys.argv) 
    mainWindow = main_window.Main_window()
    mainWindow.show()
    sys.exit(app.exec_())