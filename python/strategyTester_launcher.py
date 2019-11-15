################################ SYSTEM IMPORTS ################################
import shutil
import glob
import os
#import time
#from threading import Thread



################################ CUSTOM IMPORTS ################################
from config_generator import ConfigGenerator
from mt_launcher import MTLauncher
from report_generator import ReportGenerator
import json


#TODO: Default uses mt4_demo or mt5_demo
class StrategyTester():


    
    def __init__(self):
        
        # File containing the list of strategy tests.
        self.strategyTests = r"C:\forex\strategyTester\strategyTests.txt"
        
        # Custom Inputs directory
        self.mt4_custom_inputs_folder = r"C:\forex\inputs\mt4"
        self.mt5_custom_inputs_folder = r"C:\forex\inputs\mt5"
        
        # Inputs for testing directory
        self.mt4_inputs = r"C:\MT4\mt4_demo\tester"
        self.mt5_inputs = r"C:\MT5\mt5_demo\MQL5\Profiles\Tester"
        
        self.mtLauncher = MTLauncher()
        
        self.reportGenerator = None
        
        self.currentExpertName=""

        
    def launchStrategyTester(self):
        print("Strategy Tester Running")
        
        # Open and read all test cases
        f = open(self.strategyTests, "r")
        strategyTests= (f.read()).splitlines()
        
        count =1

        # Loop theough each test case and generate configuration files
        for i in strategyTests:
            platform = (i.split("|")[0]).lower()
            account = "Account:"+platform+"_demo"
            expert = "Expert:"+i.split("|")[1]
            period = "Period:"+i.split("|")[2]
            symbol = "Symbol:"+i.split("|")[3]
            mode =  "StrategyTester:-"


            # Source of input must be in .txt format.
            # Destination must be in .set format
            if(platform=="mt4"):
                # Get all inputs for current Expert
                custom_inputs=glob.glob(os.path.join(self.mt4_custom_inputs_folder,i.split("|")[1],"*.set"))
                # input file for testing
                test_input = os.path.join(self.mt4_inputs,i.split("|")[1]+".set")
            elif(platform=="mt5"):
                # Get all inputs for current Expert
                custom_inputs=glob.glob(os.path.join(self.mt5_custom_inputs_folder,i.split("|")[1],"*.set"))
                # input file for testing
                test_input = os.path.join(self.mt5_inputs,i.split("|")[1]+".set")

            if(self.currentExpertName != i.split("|")[1]):
                
                self.currentExpertName=i.split("|")[1]
                
                #Save the report
                if(self.reportGenerator!=None):
                    self.reportGenerator.saveReport()

                # Generate new report
                self.reportGenerator=ReportGenerator(i.split("|")[3],self.currentExpertName,custom_inputs,platform)




            for j in custom_inputs:
                
                shutil.copy(j,test_input)
                _input="Input: "+i.split("|")[1]
                print(_input)
                # Generate configuration file for current account, symbol, period and expert
                configGenerator = ConfigGenerator()
                configGenerator.generateConfigFile(account, period, expert, symbol,mode,_input,platform)
    
                # Now launch MT4 or MT5
                if(platform=="mt4"):
                    self.mtLauncher.launchMT4(account,1) # Launch MT4
                elif(platform=="mt5"):
                    self.mtLauncher.launchMT5(account,1) # Launch MT5



                # TODO: Update report
                self.reportGenerator.updateReport(i.split("|")[3],i.split("|")[2],j)
                
                print("Test "+str(count)+" of "+str(len(strategyTests))+" completed")
                count+=1

            # Move this out to save report only once.
            self.reportGenerator.saveReport()
        print("All tests complete...")
        
        repeated_list = self.reportGenerator.visualization_data["currency_pairs"]
        self.reportGenerator.visualization_data["currency_pairs"] = repeated_list[0:int(len(repeated_list)/2)]
        
        with open(self.reportGenerator.json_report, 'w') as outfile:
            json.dump(self.reportGenerator.visualization_data, outfile)


if __name__ == "__main__":
    strategyTester = StrategyTester()
    strategyTester.launchStrategyTester()
    

