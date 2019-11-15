################################ SYSTEM IMPORTS ################################
import pandas as pd
import os
import time
import win32com.client as win32
import pythoncom

################################ CUSTOM IMPORTS ################################



class ReportGenerator():
    
    def __init__(self,symbol,expert_name,inputs,platform):
        
        pythoncom.CoInitialize()
        
        # MT4 or MT5
        self.platform=platform
        
        print("Initializing new report for:",expert_name)
        
        self.mt4_report_dir = r"C:\MT4\mt4_demo\report"
        self.mt5_report_dir = r"C:\MT5\mt5_demo\report"

        if(platform=="mt4"):
            self.xml_report=r"C:\MT4\mt4_demo\report\report.xml"
            self.csv_report=r"C:\MT4\mt4_demo\report\report.csv"
            self.json_report = r"C:\MT4\mt4_demo\report\report.txt"
        
        elif(platform=="mt5"):
            self.xml_report=r"C:\MT5\mt5_demo\report\report.xml"
            self.csv_report=r"C:\MT5\mt5_demo\report\report.csv"
            self.json_report = r"C:\MT5\mt5_demo\report\report.txt"


        self.expert_name=expert_name
        self.inputs=inputs




        # For regular report
        #######################################################################
        self.no_tables=0
        self.summary=["Bars in test","Ticks modelled","Modelling quality",
                      "Initial deposit",
                      "Total net profit","Gross profit","Gross loss",
                      "Profit factor","Expected payoff",
                      "Absolute drawdown","Maximal drawdown","Relative drawdown",

                     ]
        

        index = pd.MultiIndex.from_product([[symbol], self.summary],
                                   names=['Symbol', 'Summary'])
        
        columns = pd.MultiIndex.from_product([["H1","D1"], self.inputs])
    
        self.custom_report = pd.DataFrame(index=index, columns=columns)
        time.sleep(1)
        #######################################################################
        # For optimized report
        self.first_time=1
        
        # For best results
        self.best_values = None
        self.optimized_report=None
        
        # For heatmap visualization
        self.visualization_data = {}
        self.visualization_data["currency_pairs"] = []
        self.visualization_data["H1_results"] = []
        self.visualization_data["D1_results"] = []


    def updateReport(self,current_symbol,period,input_link):
        
        print("Updating report")
        
        if(self.platform=="mt4"):
            try:
                data=pd.read_html(os.path.join(self.mt4_report_dir,"report.htm"))
            except:
                self.no_tables=1

                # If it is first time reading report, create new dataframe
                if(self.first_time==1):
                    self.initializeOptimizedReport()
                
                self.xml2csv()
                self.csv2lst(current_symbol,period)
                self.csv2VisualizationData(current_symbol, period)
                self.optimized_report.loc[len(self.optimized_report)] = self.best_values

        elif(self.platform=="mt5"):

            try:
                data=pd.read_html(os.path.join(self.mt5_report_dir,"report.htm"))
            except:
                self.no_tables=1

                # If it is first time reading report, create new dataframe
                if(self.first_time==1):
                    self.initializeOptimizedReport()
                
                self.xml2csv()
                self.csv2lst(current_symbol,period)
                self.csv2VisualizationData(current_symbol, period)
                self.optimized_report.loc[len(self.optimized_report)] = self.best_values

        if(self.no_tables!=1):
            data=data[0]

            if(self.platform=="mt4"):
                self.custom_report.loc[(current_symbol,"Bars in test"),(period,input_link)]=data.iloc[5,1]
                self.custom_report.loc[(current_symbol,"Ticks modelled"),(period,input_link)]=data.iloc[5,3]
                self.custom_report.loc[(current_symbol,"Modelling quality"),(period,input_link)]=data.iloc[5,5]
                self.custom_report.loc[(current_symbol,"Initial deposit"),(period,input_link)]=data.iloc[8,1]
                self.custom_report.loc[(current_symbol,"Total net profit"),(period,input_link)]=data.iloc[9,1]
                self.custom_report.loc[(current_symbol,"Gross profit"),(period,input_link)]=data.iloc[9,3]
                self.custom_report.loc[(current_symbol,"Gross loss"),(period,input_link)]=data.iloc[9,5]
                self.custom_report.loc[(current_symbol,"Profit factor"),(period,input_link)]=data.iloc[10,1]
                self.custom_report.loc[(current_symbol,"Expected payoff"),(period,input_link)]=data.iloc[10,3]
                self.custom_report.loc[(current_symbol,"Absolute drawdown"),(period,input_link)]=data.iloc[11,1]
                self.custom_report.loc[(current_symbol,"Maximal drawdown"),(period,input_link)]=data.iloc[11,3]
                self.custom_report.loc[(current_symbol,"Relative drawdown"),(period,input_link)]=data.iloc[11,5]
    
            if(self.platform=="mt5"):
                data=data.tail(35).reset_index(drop=True)
                self.custom_report.loc[(current_symbol,"Bars in test"),(period,input_link)]=data.iloc[7,3]
                self.custom_report.loc[(current_symbol,"Ticks modelled"),(period,input_link)]=data.iloc[7,7]
                self.custom_report.loc[(current_symbol,"Modelling quality"),(period,input_link)]=data.iloc[6,3]
                self.custom_report.loc[(current_symbol,"Initial deposit"),(period,input_link)]=data.iloc[2,3]
                self.custom_report.loc[(current_symbol,"Total net profit"),(period,input_link)]=data.iloc[8,3]
                self.custom_report.loc[(current_symbol,"Gross profit"),(period,input_link)]=data.iloc[9,3]
                self.custom_report.loc[(current_symbol,"Gross loss"),(period,input_link)]=data.iloc[10,3]
                self.custom_report.loc[(current_symbol,"Profit factor"),(period,input_link)]=data.iloc[12,3]
                self.custom_report.loc[(current_symbol,"Expected payoff"),(period,input_link)]=data.iloc[12,7]
                self.custom_report.loc[(current_symbol,"Absolute drawdown"),(period,input_link)]=data.iloc[8,7]
                self.custom_report.loc[(current_symbol,"Maximal drawdown"),(period,input_link)]=data.iloc[9,7]
                self.custom_report.loc[(current_symbol,"Relative drawdown"),(period,input_link)]=data.iloc[10,7]


    def saveReport(self):

        print("Saving report")

        if(self.no_tables!=1):

            if(self.platform=="mt4"):
                # Save as h5
                #self.custom_report.to_hdf(os.path.join(self.mt4_report_dir,self.expert_name+".h5"),key="df",mode="w")
                #Save as HTML
                self.custom_report.to_html(os.path.join(self.mt4_report_dir,self.expert_name+".html"))
            elif(self.platform=="mt5"):
                # Save as h5
                #self.custom_report.to_hdf(os.path.join(self.mt5_report_dir,self.expert_name+".h5"),key="df",mode="w")
                #Save as HTML
                self.custom_report.to_html(os.path.join(self.mt5_report_dir,self.expert_name+".html"))
        
        else:
            if(self.platform=="mt4"):
                # Save as h5
                #self.optimized_report.to_hdf(os.path.join(self.mt4_report_dir,self.expert_name+".h5"),key="df",mode="w")
                #Save as HTML
                self.optimized_report.to_html(os.path.join(self.mt4_report_dir,self.expert_name+".html"))
            elif(self.platform=="mt5"):
                # Save as h5
                #self.optimized_report.to_hdf(os.path.join(self.mt5_report_dir,self.expert_name+".h5"),key="df",mode="w")
                #Save as HTML
                self.optimized_report.to_html(os.path.join(self.mt5_report_dir,self.expert_name+".html"))
        
        print("Report Successfully saved")



###############################################################################

#   Uses the first generated xml file to create a dataframe
#   Containing Symbol, Period, and all columns of the xml file
    def initializeOptimizedReport(self):
        self.first_time=0

        # First convert the xml file to csv
        self.xml2csv()
        
        # Get the names of the columns
        data = pd.read_csv(self.csv_report)
        
        # Drop the Column called Pass
        data=data.drop(columns="Pass")
        optimized_columns = data.columns.tolist()
        
        # Create the dataframe
        self.optimized_report = pd.DataFrame(columns=["Symbol","Period"]+optimized_columns)


    # USes win32 API and Microsoft Excel to convert xml file to csv
    def xml2csv(self):

        # Open up Excel and make it invisible
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = False
        excel.DisplayAlerts = False

        # Open up the file
        reportxml=excel.Workbooks.Open(self.xml_report)
        
        # Save the report as CSV
        reportxml.SaveAs(self.csv_report, win32.constants.xlCSV)
        
        # Quit excel
        excel.Application.Quit()

    # Converts the csv file to a list with best results
    def csv2lst(self,current_symbol,period):
        # Read the csv file
        data = pd.read_csv(self.csv_report)
        
        # Drop the pass column
        data=data.drop(columns="Pass")
        
        # Get best results
        self.best_values = [current_symbol,period] + list(data.loc[data['Profit'].idxmax()].values)


    # Prepares data for visualization
    def csv2VisualizationData(self, current_symbol, period):
        
        data = pd.read_csv(self.csv_report)

        self.visualization_data["currency_pairs"].append(current_symbol)
        
        if(period == "H1"):
            self.visualization_data["H1_results"].append(data.to_dict())
        elif(period == "D1"):
            self.visualization_data["D1_results"].append(data.to_dict())



if __name__ == "__main__":
    pass
