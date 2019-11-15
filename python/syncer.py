################################ SYSTEM IMPORTS ################################
import shutil # When using copytree the destination directory MUST NOT exist beforehand
import os

################################ CUSTOM IMPORTS ################################
from mt_installer import MetaTraderInstaller

class FileSyncer():
# For syncing scripts and experts in portable MT4 and MT5
# with ones available in forex/experts/mt<X> and forex/scripts/mt<X>

    def __init__(self):
        
        # Directories for Custom Scripts, Experts and Indicators for MT4
        self.mt4_custom_experts_dir = r"C:\forex\experts\mt4"
        self.mt4_custom_scripts_dir = r"C:\forex\scripts\mt4"
        self.mt4_custom_indicators_dir = r"C:\forex\indicators\mt4"

        # Directories for Custom Scripts, Experts and Indicators for MT5
        self.mt5_custom_experts_dir = r"C:\forex\experts\mt5"
        self.mt5_custom_scripts_dir = r"C:\forex\scripts\mt5"
        self.mt5_custom_indicators_dir = r"C:\forex\indicators\mt5"

        # Locations where names of all Experts, Scripts and Indicators
        # for both MT4 and MT5 are saved

        self.mt4_custom_experts_list=r"C:\forex\nameLists\mt4_custom_experts_list.txt"
        self.mt4_custom_scripts_list=r"C:\forex\nameLists\mt4_custom_scripts_list.txt"
        self.mt4_custom_indicators_list=r"C:\forex\nameLists\mt4_custom_indicators_list.txt"

        self.mt5_custom_experts_list=r"C:\forex\nameLists\mt5_custom_experts_list.txt"
        self.mt5_custom_scripts_list=r"C:\forex\nameLists\mt5_custom_scripts_list.txt"
        self.mt5_custom_indicators_list=r"C:\forex\nameLists\mt5_custom_indicators_list.txt"

        self.mt_installer = MetaTraderInstaller()


    def SyncFiles(self, *mt_type): # mt_type = mt4 || mt5
        for i in mt_type:
            if(i=="mt4"):
                self.SyncMT4()
                self.generateMT4FileList()
                print("MT4 Files Synced successfully")
            if(i=="mt5"):
                self.SyncMT5()
                self.generateMT5FileList()
                print("MT5 Files Synced successfully")



    def SyncMT4(self):
        # Purge and Copy Custom MT4 Experts, Scripts and Indicators to mt4_demo
        self.mt_installer.RemoveDefaultMT4Directories()
        shutil.copytree(self.mt4_custom_experts_dir,self.mt_installer.mt4_demo_experts_dir)
        shutil.copytree(self.mt4_custom_scripts_dir,self.mt_installer.mt4_demo_scripts_dir)
        shutil.copytree(self.mt4_custom_indicators_dir,self.mt_installer.mt4_demo_indicators_dir)
        #TODO: Purge and Copy Custom MT4 Experts, Scripts and Indicators to mt4_live
        
    def SyncMT5(self):
        # Purge and Copy Custom MT4 Experts, Scripts and Indicators to mt4_demo
        self.mt_installer.RemoveDefaultMT5Directories()
        shutil.copytree(self.mt5_custom_experts_dir,self.mt_installer.mt5_demo_experts_dir)
        shutil.copytree(self.mt5_custom_scripts_dir,self.mt_installer.mt5_demo_scripts_dir)
        shutil.copytree(self.mt5_custom_indicators_dir,self.mt_installer.mt5_demo_indicators_dir)
        #TODO: Purge and Copy Custom MT5 Experts, Scripts and Indicators to mt5_live

    def generateMT4FileList(self):
        # Generates files containing names of MT4 Experts, Scripts and Indicators

        # Generate list of MT4 Experts
        f = open(self.mt4_custom_experts_list,"w")
        for i in os.listdir(self.mt4_custom_experts_dir):
            f.write(i.split(".")[0]+"\n")
        f.close()

        # Generate list of MT4 Scripts
        f = open(self.mt4_custom_scripts_list,"w")
        for i in os.listdir(self.mt4_custom_scripts_dir):
            f.write(i.split(".")[0]+"\n")
        f.close()

        # Generate list of MT4 Indicators
        f = open(self.mt4_custom_indicators_list,"w")
        for i in os.listdir(self.mt4_custom_indicators_dir):
            f.write(i.split(".")[0]+"\n")
        f.close()


    def generateMT5FileList(self):
        # Generates files containing names of MT5 Experts, Scripts and Indicators

        # Generate list of MT5 Experts
        f = open(self.mt5_custom_experts_list,"w")
        for i in os.listdir(self.mt5_custom_experts_dir):
            f.write(i.split(".")[0]+"\n")
        f.close()

        # Generate list of MT5 Scripts
        f = open(self.mt5_custom_scripts_list,"w")
        for i in os.listdir(self.mt5_custom_scripts_dir):
            f.write(i.split(".")[0]+"\n")
        f.close()

        # Generate list of MT5 Indicators
        f = open(self.mt5_custom_indicators_list,"w")
        for i in os.listdir(self.mt5_custom_indicators_dir):
            f.write(i.split(".")[0]+"\n")
        f.close()


        

        

if __name__ == "__main__":
    fileSyncer = FileSyncer()
    fileSyncer.SyncFiles("mt4","mt5")