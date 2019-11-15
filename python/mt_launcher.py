# NOTE
# Launching MT4 via subprocess
# subprocess.Popen([path_to_mt4launcher.exe, path_to_configuration_file,"/portable"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

# Launching MT5 via subprocess
# subprocess.Popen([path_to_mt5launcher.exe,"/config:",path_to_configuration_file,"/portable"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

# Launching MT4 via pywinauto
#app = Application().start(path_to_mt4launcher.exe +" "+path_to_configuration_file+" /portable")

# Launching MT5 via pywinauto
#app = Application().start(path_to_mt5launcher.exe +" /config:"+ path_to_configuration_file+" /portable")


################################ SYSTEM IMPORTS ################################
#from pywinauto.application import Application # print(app.windows()) displays all windows
import subprocess
import time





################################ CUSTOM IMPORTS ################################
from config_generator import ConfigGenerator

class MTLauncher():
    
    def __init__(self):
        self.config_generator=ConfigGenerator()

        # Path to MT4 launcher
        self.mt4_demo_launcher = r"C:\MT4\mt4_demo\terminal.exe"
        self.mt4_live_launcher = r"C:\MT4\mt4_live\terminal.exe"

        # Path to MT5 launcher
        self.mt5_demo_launcher = r"C:\MT5\mt5_demo\terminal64.exe"
        self.mt5_live_launcher = r"C:\MT5\mt5_live\terminal64.exe"

    
    def launchMT4(self,mt4_type,mode):
        
        # 0 means first time launch during installation (blocking mode)
        # 1 means launch during strategy testing (blocking mode)
        # 2 means persistent launch (non-blocking mode)
        # mt_version = Account:mt4_demo, Account:mt4_live
        time.sleep(5)

        if(mode==0):    # During Installation. No need of configuration file here

            # Launch MT4 in portable mode for the first time without configuration file
            mt4_demo_process = subprocess.Popen([self.mt4_demo_launcher,"/portable"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    
            # For debugging
            print("[Debug] MT4 process id is "+str(mt4_demo_process.pid) + ". Please continue to wait...")
            # TODO: Launch MT4 Live account for the first time
    
            # Sleep for 30 seconds to allow default directories to be created
            # within portable MT4 directory
            time.sleep(30)
            mt4_demo_process.kill()
            # TODO: Kill MT4 Live account launched for the first time
    
            # Sleep for 60 seconds more to allow safe deletion of default directories
            time.sleep(60)
        
        elif(mode==1):  # During Strategy Testing. Uses existing configuration file with shutdown set to true
            mt4_demo_process = subprocess.call([self.mt4_demo_launcher,self.config_generator.config_file,"/portable"])
            
        else:   # During normal launch of MT4. Uses configuration file with shutdown set to false
            self.config_generator.generateConfigFile(mt4_type)
            mt4_demo_process = subprocess.Popen([self.mt4_demo_launcher,self.config_generator.config_file,"/portable"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)



    def launchMT5(self,mt5_type,mode):
        # 0 means first time launch during installation (blocking mode)
        # 1 means launch during strategy testing (blocking mode)
        # 2 means persistent launch (non-blocking mode)
        # mt_version =Account:mt5_demo, Account:mt5_live

        # Sleep a little before and after launchig the application
        time.sleep(5)

        if(mode==0):    # During Installation. No need of configuration file here
            # Launch MT5 in portable mode for the first time without configuration file for mt5
            mt5_demo_process = subprocess.Popen([self.mt5_demo_launcher,"/portable"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    
            # For debugging
            print("[Debug] MT5 process id is "+str(mt5_demo_process.pid) + ". Please continue to wait...")
            # TODO: Launch MT5 Live account for the first time
    
            # Sleep for 30 seconds to allow default directories to be created
            # within portable MT5 directory
            time.sleep(30)
            mt5_demo_process.kill()
            # TODO: Kill MT5 Live account launched for the first time
    
            # Sleep for 60 seconds more to allow safe deletion of default directories
            time.sleep(60)

        elif(mode==1):  # During Strategy Testing. Uses existing configuration file with shutdown set to true
            mt5_demo_process = subprocess.call([self.mt5_demo_launcher,"/config:",self.config_generator.config_file,"/portable"])

        else:   # During normal launch of MT5. Uses configuration file with shutdown set to false
            self.config_generator.generateConfigFile(mt5_type)
            mt5_demo_process = subprocess.Popen([self.mt5_demo_launcher,"/config:",self.config_generator.config_file,"/portable"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)






if __name__ == "__main__":
    mt_launcher=MTLauncher()
    #mt_launcher.launchMT4("Account:mt4_demo",2)
    mt_launcher.launchMT5("Account:mt5_demo",2)