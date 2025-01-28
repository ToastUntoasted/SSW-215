import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
Robert Galletta
11/18/2024
SSW 215
"""

data = pd.read_csv("sales_data.csv")

print(data.iloc[:5,:])

for date in data.Date:
    data = data.replace(to_replace=date,value=date[5:7]) #replaces the dates with only the month

Sales_Dict_month={'Months':['January','February','March','April','May','June','July',
                      'August','September','October','November','December'],
                      'Sales':[np.sum(data.loc[data['Date']=='01'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='02'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='03'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='04'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='05'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='06'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='07'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='08'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='09'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='10'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='11'].iloc[:,3]),
                     np.sum(data.loc[data['Date']=='12'].iloc[:,3])]}

Sales_month= pd.DataFrame(Sales_Dict_month)

Sales_Dict_product={'Product':['A','B','C','D'],
                      'Sales':[np.sum(data.loc[data['Product']=='Product A'].iloc[:,3]),
                     np.sum(data.loc[data['Product']=='Product B'].iloc[:,3]),
                     np.sum(data.loc[data['Product']=='Product C'].iloc[:,3]),
                     np.sum(data.loc[data['Product']=='Product D'].iloc[:,3])]}

Sales_product=pd.DataFrame(Sales_Dict_product)

Sales_Dict_region={'Region':['North','South','East','West'],
                      'Sales':[np.sum(data.loc[data['Region']=='North'].iloc[:,3]),
                     np.sum(data.loc[data['Region']=='South'].iloc[:,3]),
                     np.sum(data.loc[data['Region']=='East'].iloc[:,3]),
                     np.sum(data.loc[data['Region']=='West'].iloc[:,3])]}

Sales_region = pd.DataFrame(Sales_Dict_region)

Revenue_dict_month={'Months':['January','February','March','April','May','June','July',
                      'August','September','October','November','December'],
                      'Revenue':[np.sum(data.loc[data['Date']=='01'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='02'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='03'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='04'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='05'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='06'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='07'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='08'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='09'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='10'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='11'].iloc[:,4]),
                     np.sum(data.loc[data['Date']=='12'].iloc[:,4])]}

Revenue_month = pd.DataFrame(Revenue_dict_month)

Revenue_Dict_region={'Region':['North','South','East','West'],
                      'Revenue':[np.sum(data.loc[data['Region']=='North'].iloc[:,4]),
                     np.sum(data.loc[data['Region']=='South'].iloc[:,4]),
                     np.sum(data.loc[data['Region']=='East'].iloc[:,4]),
                     np.sum(data.loc[data['Region']=='West'].iloc[:,4])]}

Revenue_region = pd.DataFrame(Revenue_Dict_region)

Profit_dict_month={'Months':['January','February','March','April','May','June','July',
                      'August','September','October','November','December'],
                      'Profit':[np.sum(data.loc[data['Date']=='01'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='02'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='03'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='04'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='05'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='06'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='07'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='08'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='09'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='10'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='11'].iloc[:,5]),
                     np.sum(data.loc[data['Date']=='12'].iloc[:,5])]}

Profit_month = pd.DataFrame(Profit_dict_month)

plt.figure(1)
plt.plot(Revenue_month.Months,Revenue_month.Revenue,color='green')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Revenue by Month')
plt.grid()
plt.savefig("Assignment_7_1.png")

plt.figure(2)
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Sales by Product')
plt.bar(Sales_product.Product,Sales_product.Sales,color=['Green','blue','red','yellow'])
plt.savefig("Assignment_7_2.png")

plt.figure(3)
plt.pie(Revenue_region.Revenue,labels=Revenue_region.Region)
plt.title("Distribution of Revenue Across Regions")
plt.savefig("Assignment_7_3.png")

plt.figure(4)
plt.scatter(data.loc[data['Region']=='North'].iloc[:,3],data.loc[data['Region']=='North'].iloc[:,5],color=['blue'])
plt.scatter(data.loc[data['Region']=='South'].iloc[:,3],data.loc[data['Region']=='South'].iloc[:,5],color=['green'])
plt.scatter(data.loc[data['Region']=='East'].iloc[:,3],data.loc[data['Region']=='East'].iloc[:,5],color=['red'])
plt.scatter(data.loc[data['Region']=='West'].iloc[:,3],data.loc[data['Region']=='West'].iloc[:,5],color=['yellow'])
plt.grid()
plt.xlabel('Units Sold')
plt.ylabel('Profit')
plt.title('Profits from Units Sold by Region')
plt.legend(['North','South','East','West'])
plt.savefig("Assignment_7_4.png")
plt.show()





