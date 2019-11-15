import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import os

#jsonReport = r"C:\MT5\mt5_demo\report\report.txt"
jsonReport = os.path.join(os.getcwd(),"report.txt")


with open(jsonReport) as json_file:
    data = json.load(json_file)

currency_pairs = data["currency_pairs"]
H1_results = data["H1_results"]
D1_results = data ["D1_results"]

data_H1 = []
data_D1 = []

inputs_list = None
outputs_list = None

for i in range(len(currency_pairs)):
    if(H1_results):

        temp_H1 = pd.DataFrame.from_dict(H1_results[i]) 
        
        # Drop the pass and Custom columns
        temp_H1=temp_H1.drop(columns="Pass")
        temp_H1=temp_H1.drop(columns="Custom")
        
        

        # Convert True to 1 and False to -1
        temp_H1[temp_H1.columns.values]*=1
        
        # Add the data to list
        data_H1.append(temp_H1)
        
    if(D1_results):

        temp_D1 = pd.DataFrame.from_dict(D1_results[i]) 
        
        # Drop the pass and Custom columns
        temp_D1=temp_D1.drop(columns="Pass")
        temp_D1=temp_D1.drop(columns="Custom")
        
        

        # Convert True to 1 and False to -1
        temp_D1[temp_D1.columns.values]*=1
        
        data_D1.append(temp_D1)
        
# Get the inputs and outputs

if(H1_results):
    outputs_list=data_H1[0].loc[:, 'Result':'Trades']
    inputs_list=data_H1[0].loc[:, 'Trades':]
    inputs_list = inputs_list.drop(columns="Trades")
elif(D1_results):
    outputs_list=data_D1[0].loc[:, 'Result':'Trades']
    inputs_list=data_D1[0].loc[:, 'Trades':]
    inputs_list = inputs_list.drop(columns="Trades")

outputs_list    = outputs_list.columns.tolist()
inputs_list     = inputs_list.columns.tolist()
    

currency_pair_choice = None
period_choice = None
first_input_choice = None
second_input_choice = None
output_choice = None


print("Select a currency pair then press Enter")
    
for i in range(len(currency_pairs)):
    print(i,": "+currency_pairs[i] )
    
currency_pair_choice = int(input())


print("Select a period then press Enter")
print("0 : H1")
print("1 : D1")
period_choice = int(input())



print("Select FIRST input then press Enter")
for i in range(len(inputs_list)):
    print(i, ": "+inputs_list[i])
    
first_input_choice = int(input())

idx_to_delete = first_input_choice

first_input_choice = inputs_list[first_input_choice]

del inputs_list[int(idx_to_delete)]


print("Select SECOND input then press Enter")
for i in range(len(inputs_list)):
    print(i, ": "+inputs_list[i])
    
second_input_choice = int(input())

second_input_choice = inputs_list[second_input_choice]

print("Select output then press Enter")
for i in range(len(outputs_list)):
    print(i, ": "+outputs_list[i])
    
output_choice = int(input())
output_choice = outputs_list[output_choice]



data = None

print("---------------------------")
print("Summary")
print("---------------------------")
print("Currency pair:",currency_pairs[currency_pair_choice])
if(period_choice ==0):
    print("Period: H1")
    data = data_H1[currency_pair_choice]
elif(period_choice ==1):
    print("Period: D1")
    data = data_D1[currency_pair_choice]
print("First input choice:",first_input_choice)
print("Second input choice:",second_input_choice)
print("Output: ",output_choice)


fig = px.scatter_3d(data, x=first_input_choice, y=second_input_choice, z=output_choice, color=output_choice, color_continuous_scale=px.colors.sequential.Viridis,width=800, height=800)
fig.show()
