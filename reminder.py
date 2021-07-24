#!/usr/bin/env python3

import sys
import os
import logging.config

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTranslator, QLocale, QLibraryInfo

from app_modules.views import AppView
from app_modules.controller import AppController


def main():
    # instance of 'QApplication'
    app = QtWidgets.QApplication(sys.argv)
    

    # render the view
    view = AppView()
    view.show()
    # instance of the controller
    ctrl = AppController(view=view)
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    
    
    
    
    
    main()
