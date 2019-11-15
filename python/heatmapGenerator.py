import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

#jsonReport = r"C:\MT5\mt5_demo\report\report.txt"
jsonReport = r"report.txt"

with open(jsonReport) as json_file:
    data = json.load(json_file)

currency_pairs = data["currency_pairs"]
H1_results = data["H1_results"]
D1_results = data ["D1_results"]



first_pass_H1 = 1
first_pass_D1 = 1

concatenated_H1 = None
concatenated_D1 = None


for i in range(len(currency_pairs)):

    if(H1_results):
        data_H1 = pd.DataFrame.from_dict(H1_results[i])
    
        # Drop the pass and Custom columns
        data_H1=data_H1.drop(columns="Pass")
        data_H1=data_H1.drop(columns="Custom")
    
        # Convert True to 1 and False to -1
        data_H1[data_H1.columns.values]*=1
    
        yAxis_H1=data_H1.loc[:, 'Result':'Trades']
        xAxis_H1=data_H1.loc[:, 'Trades':]
        xAxis_H1 = xAxis_H1.drop(columns="Trades")
        
        xAxisList_H1 = xAxis_H1.columns.tolist()
        yAxisList_H1 = yAxis_H1.columns.tolist()
    
        #print(xAxisList)
        #print(yAxisList)
        #
        corr_H1 = data_H1.corr()
        #
        corr_H1=corr_H1.drop(xAxisList_H1,axis=0)
        corr_H1=corr_H1.drop(yAxisList_H1,axis=1)
        
        top = pd.DataFrame([[0]*len(corr_H1.columns)],columns=corr_H1.columns.values)
        corr_H1=pd.concat([top,corr_H1])
        corr_H1=corr_H1.rename(index={0: currency_pairs[i]+"*********"})
        
        if(first_pass_H1 == 1):
            first_pass_H1 = 0
            concatenated_H1 = corr_H1
        else:
            concatenated_H1 = pd.concat([concatenated_H1,corr_H1])

###############################################################################

    if (D1_results):
        data_D1 = pd.DataFrame.from_dict(D1_results[i])


        # Drop the pass and Custom columns
        data_D1=data_D1.drop(columns="Pass")
        data_D1=data_D1.drop(columns="Custom")
    
        # Convert True to 1 and False to -1
        data_D1[data_D1.columns.values]*=1

    
        yAxis_D1=data_D1.loc[:, 'Result':'Trades']
        xAxis_D1=data_D1.loc[:, 'Trades':]
        xAxis_D1 = xAxis_D1.drop(columns="Trades")
        
        xAxisList_D1 = xAxis_D1.columns.tolist()
        yAxisList_D1 = yAxis_D1.columns.tolist()
    
        #print(xAxisList)
        #print(yAxisList)
        #
        corr_D1 = data_D1.corr()
        #
        corr_D1=corr_D1.drop(xAxisList_D1,axis=0)
        corr_D1=corr_D1.drop(yAxisList_D1,axis=1)

        top = pd.DataFrame([[0]*len(corr_D1.columns)],columns=corr_D1.columns.values)
        corr_D1=pd.concat([top,corr_D1])
        corr_D1=corr_D1.rename(index={0: currency_pairs[i]+"*********"})

        if(first_pass_D1 == 1):
            first_pass_D1 = 0
            concatenated_D1 = corr_D1
        else:
            concatenated_D1 = pd.concat([concatenated_D1,corr_D1])

###############################################################################

plt.figure()
ax= sns.heatmap(concatenated_H1, 
            xticklabels=concatenated_H1.columns.values,
            yticklabels=concatenated_H1.index.values,
            annot=True,
            center=0,
            cmap="cool")

ax.set_title("Period: H1")

plt.figure()
ax= sns.heatmap(concatenated_D1, 
            xticklabels=concatenated_D1.columns.values,
            yticklabels=concatenated_D1.index.values,
            annot=True,
            center=0,
            cmap="cool")

ax.set_title("Period: D1")


