from pywinauto.application import Application
from pywinauto import Desktop
import subprocess
import os
import time
from distutils.dir_util import copy_tree


def start_wamp():
    os.startfile('C:\wamp64\wampmanager.exe')


def mysql_installation():
    # Loading the app exe file from the directory.

    '''

    pywinauto dialogue select best name for the dialgoue combination. more details can be found here.

    https://pywinauto.readthedocs.io/en/latest/getting_started.html#attribute-resolution-magic
    https://pywinauto.readthedocs.io/en/latest/wait_long_operations.html

    :return:
    '''

    app = Application(backend="uia").start("setups/wampserver.exe")

    # selecting  the language dialogue box.
    Wizard = Desktop(backend='uia').Select_Setup_Language
    Wizard.OK.click_input()
    # app.InstallDialog.IAgreeRadioButton.wait('ready', timeout=30).click_input()

    Wizard2 = Desktop(backend='uia').Setup_Wampserver64
    Wizard2.i_accept_the_agreement.click_input()
    Wizard2.NextButton.click_input()
    Wizard2.NextButton.click_input()
    Wizard2.NextButton.click_input()
    Wizard2.Install.click_input()

    # waiting for open dialogue to be closed
    Wizard2.wait_not('visible')

    # After installation, start the application from the windows installed directory
    start_wamp()
    time.sleep(5)
    # setup the database. This batch file created database in the db MySQL and improt all the sql file data into it.
    os.startfile(os.getcwd() + '/setups/database.bat')


def qgis_installation():
    # starting a qgis installation process
    app = Application().start("setups/QGIS-OSGeo4W-2.18.27-1-Setup-x86_64.exe")

    app.InstallDialog.NextButton.wait('ready', timeout=30).click_input()

    app.InstallDialog.IAgreeRadioButton.wait('ready', timeout=30).click_input()

    app.InstallDialog.NextButton.wait('ready', timeout=30).click_input()

    app.InstallDialog.InstallButton.wait('ready', timeout=30).click_input()

    # copy plugins into qgis instaleld directory.
    # app.InstallDialog.wait_not('visible')
    copy_tree(os.getcwd() + "/setups/plugins", r"C:\Program Files\QGIS 2.18\apps\qgis-ltr\python\plugins")
    # copy_tree(os.getcwd() + "/setups/searchRescuePlugin", r"C:\Program Files\QGIS 2.18\apps\qgis-ltr\python\plugins\searchRescuePlugin")


def main():
    # qgis_installation()
    mysql_installation()
    qgis_installation()


if __name__ == "__main__":
    main()
