################################ SYSTEM IMPORTS ################################
import socket
from threading import Thread
import subprocess
import time


################################ CUSTOM IMPORTS ################################
from tcp_killer import TCPKiller
from mt_installer import MetaTraderInstaller
from syncer import FileSyncer
from strategyTester_launcher import StrategyTester



class Controller():

    
    def __init__(self):

        # For Installation of Metatraders
        self.mt_installer = MetaTraderInstaller()
        
        # For launching strategy tester
        self.strategyTesterLauncher = StrategyTester()
        
        # For Syncing Experts, Scripts and Indicators
        self.syncer = FileSyncer()

        # Location for Java GUI launcher
        self.javaGUI_launcher = r"C:\forex\JAVA_GUI\dist\JAVA_GUI.jar"

##############################################################################
        # Local Host for TCP Communications
        self.HOST = '127.0.0.1'

        # Port for receiving data from Java GUI
        self.fromJavaGUIPort = 65431

        # Data  From Java GUI (string)
        self.dataFromJavaGUI = ""
################################ DATA ################################




    def launchThreads(self):
        # Get the latest list of experts, scripts and indicators for MT4
        self.syncer.generateMT4FileList()

        # Get the latest list of experts, scripts and indicators for MT5
        self.syncer.generateMT5FileList()
        
        # Kill Any Server and Client running at the ports
        tcp_killer = TCPKiller()
        tcp_killer.KillPorts()

        # Launch Python Server
        Thread(target = self.launchServer).start()
        
        # Launch Java GUI
        # The GUI launches a client that connects to the Server
        # The GUI also launches its own Server
        time.sleep(5)
        subprocess.Popen(['java', '-jar', self.javaGUI_launcher], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)


    def launchServer(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Server Listening to port:", self.fromJavaGUIPort)
            s.bind((self.HOST, self.fromJavaGUIPort))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print("Java GUI has Connected to Python Server")
                while True:
                    try:
                        data = conn.recv(65536)
                        self.dataFromJavaGUI = data.decode('utf-8')
                    except:
                        print("Java GUI closed unexpectedly...")
                        break
                    # Process the data here
                    self.processDataFromJavaGUI()
                    
                    if not data:
                        break

    def processDataFromJavaGUI(self):
        print("From Java GUI: " + self.dataFromJavaGUI)
        
        if(self.dataFromJavaGUI.split("-")[0]=="installMT4"):
            self.mt_installer.installMetaTraders("mt4")

        elif(self.dataFromJavaGUI.split("-")[0]=="installMT5"):
            self.mt_installer.installMetaTraders("mt5")

        elif(self.dataFromJavaGUI.split("-")[0]=="syncMT4"):
            self.syncer.SyncFiles("mt4")

        elif(self.dataFromJavaGUI.split("-")[0]=="syncMT5"):
            self.syncer.SyncFiles("mt5")
            
        elif(self.dataFromJavaGUI.split("-")[0]=="launchStrategyTester"):
            self.strategyTesterLauncher.launchStrategyTester()


if __name__ == "__main__":

    controller = Controller()
    controller.launchThreads()

