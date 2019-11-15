# NOTE: During installation, all directories must be closed

################################ SYSTEM IMPORTS ################################
import shutil
import os
from threading import Thread


################################ CUSTOM IMPORTS ################################
from mt_launcher import MTLauncher


class MetaTraderInstaller():
# Copies pre-installed Meta Trader to C directory
# Once installation completed, the following directories will be formed
# C:\MT4\mt4_demo
# C:\MT4\mt4_live
# C:\MT5\mt5_demo
# C:\MT5\mt5_live
# Deletes default Scripts, Experts and Indicators and creates fresh directories


    def __init__(self):

###############################################################################
        # Default installation directory for MT4
        self.mt4_original_dir = r"C:\Program Files (x86)\Darwinex MT4"

        # Default installation directory for MT5
        self.mt5_original_dir = r"C:\Program Files\Darwinex MetaTrader 5"
###############################################################################
        # Root directories for portable MT4
        self.mt4_demo_dir = r"C:\MT4\mt4_demo"
        self.mt4_live_dir = r"C:\MT4\mt4_live"
        
        # strategy tester report folder
        self.strategyTesterReport = "report"
        
        # Directories for Default MT4 Experts
        self.mt4_demo_experts_dir = r"C:\MT4\mt4_demo\MQL4\Experts"
        self.mt4_live_experts_dir = r"C:\MT4\mt4_live\MQL4\Experts"

        # Directories for Default MT4 Scripts
        self.mt4_demo_scripts_dir = r"C:\MT4\mt4_demo\MQL4\Scripts"
        self.mt4_live_scripts_dir = r"C:\MT4\mt4_live\MQL4\Scripts"

        # Directories for Default MT4 Indicators
        self.mt4_demo_indicators_dir = r"C:\MT4\mt4_demo\MQL4\Indicators"
        self.mt4_live_indicators_dir = r"C:\MT4\mt4_live\MQL4\Indicators"

###############################################################################
        # Root directories for portable  MT5
        self.mt5_demo_dir = r"C:\MT5\mt5_demo"
        self.mt5_live_dir = r"C:\MT5\mt5_live"
        
        # Directories for Default MT5 Experts
        self.mt5_demo_experts_dir = r"C:\MT5\mt5_demo\MQL5\Experts"
        self.mt5_live_experts_dir = r"C:\MT5\mt5_live\MQL5\Experts"

        # Directories for Default MT5 Scripts
        self.mt5_demo_scripts_dir = r"C:\MT5\mt5_demo\MQL5\Scripts"
        self.mt5_live_scripts_dir = r"C:\MT5\mt5_live\MQL5\Scripts"

        # Directories for Default MT5 Indicators
        self.mt5_demo_indicators_dir = r"C:\MT5\mt5_demo\MQL5\Indicators"
        self.mt5_live_indicators_dir = r"C:\MT5\mt5_live\MQL5\Indicators"
###############################################################################
        self.mt_launcher=MTLauncher()


    def installMetaTraders(self, *mt_type): # mt_type = "mt4" || "mt5"
        for i in mt_type:
            if(i=="mt4"):
                print("Installing MT4. Please wait...")
                Thread(target = self.InstallMT4).start()

            if(i=="mt5"):
                print("Installing MT5. Please wait...")
                Thread(target = self.InstallMT5).start()



    def InstallMT4(self):
        # Remove existing MT4 directory from C
        shutil.rmtree(self.mt4_demo_dir, ignore_errors=True, onerror=None)
        # Copy originally installed MT4 from Program Files to C
        shutil.copytree(self.mt4_original_dir, self.mt4_demo_dir)
        
        # Launch MT4 for the first time without configuration file (mode 0)
        self.mt_launcher.launchMT4("Account:mt4_demo",0)

        self.RemoveDefaultMT4Directories()
        self.CreateFreshMT4Directories()
        print(">>> MT4 installed successfully")

    def InstallMT5(self):

        # Remove existing MT5 directory from C
        shutil.rmtree(self.mt5_demo_dir, ignore_errors=True, onerror=None)

        # Copy originally installed MT5 from Program Files to C
        shutil.copytree(self.mt5_original_dir, self.mt5_demo_dir)

        # Launch MT5 for the first time without configuration file (mode 0)
        self.mt_launcher.launchMT5("Account:mt5_demo",0)

        self.RemoveDefaultMT5Directories()
        self.CreateFreshMT5Directories()
        print(">>> MT5 installed successfully")


    def RemoveDefaultMT4Directories(self):
        # Remove default Experts, Scripts and Indicators directories in portable demo MT4
        shutil.rmtree(self.mt4_demo_experts_dir, ignore_errors=True, onerror=None)
        shutil.rmtree(self.mt4_demo_scripts_dir, ignore_errors=True, onerror=None)
        shutil.rmtree(self.mt4_demo_indicators_dir, ignore_errors=True, onerror=None)
        # TODO: Remove default Experts, Scripts and Indicators directories in portable live MT4

    def RemoveDefaultMT5Directories(self):
        # Remove default Experts, Scripts and Indicators directories in portable demo MT5
        shutil.rmtree(self.mt5_demo_experts_dir, ignore_errors=True, onerror=None)
        shutil.rmtree(self.mt5_demo_scripts_dir, ignore_errors=True, onerror=None)
        shutil.rmtree(self.mt5_demo_indicators_dir, ignore_errors=True, onerror=None)
        # TODO: Remove default Experts, Scripts and Indicators directories in portable live MT5

    def CreateFreshMT4Directories(self):
        # Create fresh Experts, Scripts and Indicators directories in portable demo MT4
        os.mkdir(self.mt4_demo_experts_dir)
        os.mkdir(self.mt4_demo_scripts_dir)
        os.mkdir(self.mt4_demo_indicators_dir)
        os.mkdir(os.path.join(self.mt4_demo_dir,self.strategyTesterReport))
        # TODO: Create fresh Experts, Scripts and Indicators directories in portable live MT4

    def CreateFreshMT5Directories(self):
        # Create fresh Experts, Scripts and Indicators directories in portable live MT5
        os.mkdir(self.mt5_demo_experts_dir)
        os.mkdir(self.mt5_demo_scripts_dir)
        os.mkdir(self.mt5_demo_indicators_dir)
        os.mkdir(os.path.join(self.mt5_demo_dir,self.strategyTesterReport))
        # TODO: Create fresh Experts, Scripts and Indicators directories in portable live MT5


if __name__ == "__main__":
    installer = MetaTraderInstaller()
    installer.installMetaTraders("mt4","mt5")