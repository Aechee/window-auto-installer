from pywinauto.application import  Application
from pywinauto import Desktop
import subprocess
import os
import time
from distutils.dir_util import copy_tree


def start_wamp():
    os.startfile('C:\wamp64\wampmanager.exe')

def mysql_installation():

    app = Application(backend="uia").start("setups/wampserver.exe")
    Wizard = Desktop(backend='uia').Select_Setup_Language
    Wizard.OK.click_input()
    # app.InstallDialog.IAgreeRadioButton.wait('ready', timeout=30).click_input()

    Wizard2 = Desktop(backend='uia').Setup_Wampserver64
    Wizard2.i_accept_the_agreement.click_input()
    Wizard2.NextButton.click_input()
    Wizard2.NextButton.click_input()
    Wizard2.NextButton.click_input()
    Wizard2.Install.click_input()

    Wizard2.wait_not('visible')

    start_wamp()
    time.sleep(5)
    os.startfile(os.getcwd()+'/setups/database.bat')




def qgis_installation():
    # starting a qgis installation process
    app = Application().start("setups/QGIS-OSGeo4W-2.18.27-1-Setup-x86_64.exe")

    app.InstallDialog.NextButton.wait('ready', timeout=30).click_input()

    app.InstallDialog.IAgreeRadioButton.wait('ready', timeout=30).click_input()

    app.InstallDialog.NextButton.wait('ready', timeout=30).click_input()

    app.InstallDialog.InstallButton.wait('ready',timeout=30).click_input()

    # app.InstallDialog.wait_not('visible')
    copy_tree(os.getcwd()+"/setups/plugins", r"C:\Program Files\QGIS 2.18\apps\qgis-ltr\python\plugins")
    # copy_tree(os.getcwd() + "/setups/searchRescuePlugin", r"C:\Program Files\QGIS 2.18\apps\qgis-ltr\python\plugins\searchRescuePlugin")



def main():
    # qgis_installation()
    mysql_installation()
    qgis_installation()



if __name__=="__main__":
    main()