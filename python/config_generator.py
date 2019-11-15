################################ SYSTEM IMPORTS ################################
from datetime import datetime


################################ CUSTOM IMPORTS ################################

class ConfigGenerator():
# Generates configuration file

    def __init__(self):
        
        # mt4_demo account
        self.mt4_demo_login = "2088958353"
        self.mt4_demo_password = "B8IPdCW"
        self.mt4_demo_server = "Darwinex-Demo"
        
        # mt5_demo account
        self.mt5_demo_login = "3000011005"
        self.mt5_demo_password = "9Lt3bifmH6e"
        self.mt5_demo_server = "Darwinex-Demo"
        
        self.testFromDateD1="2016.01.01"
        self.testFromDateH1="2017.01.01"

#        self.testFromDateD1="2019.09.09"
#        self.testFromDateH1="2019.09.09"
        
        self.symbol = ""
        self.expert=""
        self.period=""
        self.input=""
        
        self.config_file = "C:\\forex\\configuration files\\configuration.ini"
        # Populate configuration file parameters for MT4
        self.config_parametersMT4 =    {
                                # Common Settings
                                # [Protocol example] "Account:account_name"
                                # account_name = mt4_demo||mt4_live||mt5_demo||mt5_lives
                                "Common": "[Common]",
                                "Profile": "Profile=",
                                "MarketWatch": "MarketWatch=",
                                "Login": "Login=",
                                "Password": "Password=",
                                "Server": "Server=",
                                "AutoConfiguration": "AutoConfiguration=",
                                "DataServer": "DataServer=",
                                "EnableDDE": "EnableDDE=",
                                "EnableNews": "EnableNews="+"\n",
                                
                                
                                # Proxy Settings
                                "Proxy": "[Proxy]",
                                "ProxyServer": "ProxyServer=",
                                "ProxyType": "ProxyType=",
                                "ProxyLogin": "ProxyLogin=",
                                "ProxyPassword": "ProxyPassword="+"\n",
                                
                                # FTP Settings
                                "FTP": "[FTP]",
                                "FTPEnable": "FTPEnable=",
                                "FTPPassiveMode": "FTPPassiveMode=",
                                "FTPAccount": "FTPAccount=",
                                "FTPServer": "FTPServer=",
                                "FTPLogin": "FTPLogin=",
                                "FTPPassword": "FTPPassword=",
                                "FTPPath": "FTPPath=",
                                "FTPPeriod": "FTPPeriod="+"\n",
                                
                                # EA Settings
                                "Experts": "[Experts]",
                                "ExpertsEnable": "ExpertsEnable=true",
                                "ExpertsDllImport": "ExpertsDllImport=true",
                                "ExpertsExpImport": "ExpertsExpImport=true",
                                "ExpertsTrades": "ExpertsTrades=true"+"\n",
                                
                                # EA and Scripts startup
                                "Startup": "[Startup]",
                                "Symbol": "Symbol=",  #[Protocol example] "Symbol:EURUSD"
                                "Period": "Period= ", #[Protocol example] "Period:H1"
                                "Template": "Template=",
                                "Expert": "Expert=",  #[Protocol example] "Expert:expert_name"
                                "ExpertParameters": "ExpertParameters=",
                                "Script": "Script=",  #[Protocol example] "Script:script_name"
                                "ScriptParameters  ": "ScriptParameters="+"\n",
                                
                                # Strategy Tester
                                "StrategyTester": "[Strategy Tester]",
                                "TestExpert" : "TestExpert=",
                                "TestExpertParameters": "TestExpertParameters=",
                                "TestSymbol": "TestSymbol=", #[Protocol example] "TestSymbol:EURUSD"
                                "TestPeriod": "TestPeriod=", #[Protocol example] "TestPeriod:H1"
                                "TestModel": "TestModel=0",
                                "TestSpread": "TestSpread=",
                                "TestOptimization ": "TestOptimization=false",
                                "TestDateEnable": "TestDateEnable=true",
                                "TestFromDate": "TestFromDate=",
                                "TestToDate": "TestToDate="+datetime.today().strftime('%Y.%m.%d'),
                                "TestReport": "TestReport= report",
                                "TestReplaceReport": "TestReplaceReport=true",
                                "TestShutdownTerminal": "TestShutdownTerminal=false", # By default terminal does not close (mode 2)
                                "TestVisualEnable": "TestVisualEnable=false",
                                }

###############################################################################

        # Populate configuration file parameters for MT4
        self.config_parametersMT5 =    {
                                # Common Settings
                                # [Protocol example] "Account:account_name"
                                # account_name = mt4_demo||mt4_live||mt5_demo||mt5_lives
                                "Common": "[Common]",
                                "Login": "Login=",
                                "Password": "Password=",
                                "Server": "Server=",
#                                "CertPassword": "CertPassword=",
#                                "ProxyEnable": "ProxyEnable=0",
#                                "ProxyType": "ProxyType=",
#                                "ProxyAddress": "ProxyAddress=",
#                                "ProxyLogin": "ProxyLogin=",
#                                "ProxyPassword": "ProxyPassword=",
#                                "KeepPrivate": "KeepPrivate=",
#                                "NewsEnable": "NewsEnable=",
#                                "CertInstall": "CertInstall=",
#                                "MQL5Login": "MQL5Login=",
#                                "MQL5Password": "MQL5Password="+"\n",
                                
                                # CHARTS
#                                "Charts":"[Charts]",
#                                "ProfileLast": "ProfileLast=",
#                                "MaxBars": "MaxBars=",
#                                "PrintColor": "PrintColor=",
#                                "SaveDeleted": "SaveDeleted="+"\n",

                                # EXPERTS
#                                "Experts": "[Experts]",
#                                "AllowLiveTrading": "AllowLiveTrading=0",
#                                "AllowDllImport": "AllowDllImport=0",
#                                "Enabled": "Enabled=1",
#                                "Account": "Account=0",
#                                "Profile": "Profile=0"+"\n",

                                # OBJECTS
#                                "Objects": "[Objects]",
#                                "ShowPropertiesOnCreate": "ShowPropertiesOnCreate=",
#                                "SelectOneClick": "SelectOneClick=",
#                                "MagnetSens": "MagnetSens="+"\n",


                                # EA and Scripts startup
#                                "Startup": "[StartUp]",
#                                "Symbol": "Symbol=",  #[Protocol example] "Symbol:EURUSD"
#                                "Period": "Period=", #[Protocol example] "Period:H1"
#                                "Template": "Template=",
#                                "Expert": "Expert=",  #[Protocol example] "Expert:expert_name"
#                                "ExpertParameters": "ExpertParameters=",
#                                "Script": "Script=",  #[Protocol example] "Script:script_name"
#                                "ScriptParameters  ": "ScriptParameters="+"\n",

                                # Strategy Tester
                                "StrategyTester": "[Tester]",
                                "Expert" : "Expert=",
                                "ExpertParameters": "ExpertParameters=",
                                "Symbol": "Symbol=", #[Protocol example] "TestSymbol:EURUSD"
                                "Period": "Period=", #[Protocol example] "TestPeriod:H1"
                                "Model": "Model=2",
                                "FromDate": "FromDate=",
                                "ToDate": "ToDate="+datetime.today().strftime('%Y.%m.%d'),
                                "Report": "Report= report",
                                "ReplaceReport": "ReplaceReport=1",
                                "ShutdownTerminal": "ShutdownTerminal=0", # By default terminal does not close (mode 2)
                                "Deposit": "Deposit=10000",
                                
                                
                                "Login": "Login=",
                                "ExecutionMode": "ExecutionMode=0",
                                "Optimization": "Optimization=2",
                                "OptimizationCriterion": "OptimizationCriterion=0",
                                "ForwardMode": "ForwardMode=",
                                "ForwardDate": "ForwardDate=",
                                "Currency": "Currency=",
                                "Leverage": "Leverage=",
                                "UseLocal": "UseLocal=",
                                "UseRemote": "UseRemote=",
                                "UseCloud": "UseCloud=",
                                "Visual": "Visual=",
                                "Port": "Port="

                                }

###############################################################################
        # Generates a configuration file then saves the file
        # in the directory of the corresponding metatrader (mt4_live, mt4_demo, mt5_live, mt5_demo)
        
        # Input 
        # Array of strings of the form LHS:RHS
        # Compares LHS with the keys in dictionary, if the keys match,
        # sets the value of the key to RHS
        
        # Output
        # Text File self.config_file
    def generateConfigFile(self, *config_parametersMT4):

        platform = ""
        for i in config_parametersMT4:
#------------------------------------------------------------------------------
            # Account Type (Account:account_type)
            if(i.split(":")[0] == "Account"):
                if(i.split(":")[1] == "mt4_demo"):
                    platform = "mt4_demo"
                    self.config_parametersMT4["Login"]     = "Login="+self.mt4_demo_login
                    self.config_parametersMT4["Password"]  = "Password="+self.mt4_demo_password
                    self.config_parametersMT4["Server"]    = "Server="+self.mt4_demo_server
                    print("Generating Configuration parameters for MT4 Demo")

                if(i.split(":")[1] == "mt5_demo"):
                    platform = "mt5_demo"
                    self.config_parametersMT5["Login"]     = "Login="+self.mt5_demo_login
                    self.config_parametersMT5["Password"]  = "Password="+self.mt5_demo_password
                    self.config_parametersMT5["Server"]    = "Server="+self.mt5_demo_server+"\n"
                    print("Generating Configuration parameters for MT5 Demo")
#------------------------------------------------------------------------------
            # Symbol (Symbol:symbol_name)
            if(i.split(":")[0] == "Symbol"):
                self.symbol = i.split(":")[1]
                if(platform == "mt4_demo"):
                    self.config_parametersMT4["Symbol"]="Symbol="+self.symbol
                    self.config_parametersMT4["TestSymbol"]="TestSymbol="+self.symbol
                else:
                    self.config_parametersMT5["Symbol"]="Symbol="+self.symbol
#------------------------------------------------------------------------------
            # Period (Period:period_name)
            if(i.split(":")[0] == "Period"):
                self.period = i.split(":")[1]
                if(platform == "mt4_demo"):
                    self.config_parametersMT4["Period"]="Period="+self.period
                    self.config_parametersMT4["TestPeriod"]="TestPeriod="+self.period
                else:
                    self.config_parametersMT5["Period"]="Period="+self.period
                
                #TODO: Change this in future
                # Set Default Test Periods
                if(self.period=="H1"):
                    self.config_parametersMT4["TestFromDate"] = "TestFromDate=" + self.testFromDateH1
                    self.config_parametersMT5["FromDate"] = "FromDate=" + self.testFromDateH1
                if(self.period=="D1"):
                    self.config_parametersMT4["TestFromDate"] = "TestFromDate=" + self.testFromDateD1
                    self.config_parametersMT5["FromDate"] = "FromDate=" + self.testFromDateD1
#------------------------------------------------------------------------------
            # Expert (Expert:expert_name)
            #
            if(i.split(":")[0] == "Expert"):
                self.expert = i.split(":")[1]
                if(platform == "mt4_demo"):
                    self.config_parametersMT4["Expert"]="Expert="+self.expert
                    self.config_parametersMT4["TestExpert"]="TestExpert="+self.expert
                else:
                    self.config_parametersMT5["Expert"]="Expert="+self.expert
#------------------------------------------------------------------------------
            # Inputs (Input:input_name)
            # Split after equal sign because path already contains full colons
            if(i.split(":")[0] == "Input"):
                self.input=i.split(":")[1]
                if(platform == "mt4_demo"):
                    self.config_parametersMT4["TestExpertParameters"]="TestExpertParameters="+self.input+".set"
                else:
                    self.config_parametersMT5["ExpertParameters"]="ExpertParameters="+self.input+".set"
#------------------------------------------------------------------------------
            # Check if the configuration file is meant for Strategy Tester
            if(i.split(":")[0]=="StrategyTester"):
                if(platform == "mt4_demo"):
                    self.config_parametersMT4["TestShutdownTerminal"] = "TestShutdownTerminal=true"
                if(platform == "mt5_demo"):
                    self.config_parametersMT5["ShutdownTerminal"] = "ShutdownTerminal=1"

            # Name of the report file
            if(platform == "mt4_demo"):
                self.config_parametersMT4["TestReport"] = "TestReport="+"report\\"+"report"

            if(platform == "mt5_demo"):
                self.config_parametersMT5["Report"] = "Report="+"report\\"+"report"



        # TODO: Remove this and instead save the config file
        # in r"C:\forex\configuration files\configuration.txt" 
        f = open(self.config_file,"w")
        
        if(platform == "mt4_demo"):
            for i in self.config_parametersMT4.keys():
                f.write(self.config_parametersMT4[i]+"\n")

        if(platform == "mt5_demo"):
            for i in self.config_parametersMT5.keys():
                f.write(self.config_parametersMT5[i]+"\n")

        f.close()



if __name__ == "__main__":
    configGenerator = ConfigGenerator()
    configGenerator.generateConfigFile("Account:mt5_demo","Symbol:EURUSD","Period:H1","Expert:MACD Sample")
