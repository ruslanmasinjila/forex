

################################ SYSTEM IMPORTS ################################
import win32com.client as win32
import pandas as pd



################################ CUSTOM IMPORTS ################################


class XML_CSV_LST():
    
    
    def __init__(self):
        
        self.xml_report=r"C:\MT5\mt5_demo\report\report.xml"
        self.csv_report=r"C:\MT5\mt5_demo\report\report.csv"
        
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
        

    def csv2lst(self):
        # Read the csv file
        data = pd.read_csv(self.csv_report)
        
        data=data.sort_values(by=data.columns.tolist())
        
        print(data["Equity DD %"])


        # Drop the pass column
        data=data.drop(columns="Pass")
        #print(data.columns.tolist())

        # Get best results
        lst=[1,2]
        highest_ = lst+list(data.loc[data['Profit'].idxmax()].values)
        
        print(highest_)


if __name__ == "__main__":
    xml2csv2lst = XML_CSV_LST()
    xml2csv2lst.xml2csv( )
    xml2csv2lst.csv2lst()