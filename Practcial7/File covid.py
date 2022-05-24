import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#The code for importing the .csv file works
filepath="C:\\Users\\INTL\\Desktop\\python\\practical 7\\full_data(2).csv"
covid_data = pd.read_csv(filepath,header=0,encoding="gbk")

#4
#print(covid_data.head(5))
#print(type(covid_data))
#print(covid_data.info())

#print(covid_data.iloc[2,0])
#There is correct code for showing the first and third columns from rows 10-20 (inclusive)
print(covid_data.iloc[10:21,[1,3]])
#print(covid_data.iloc[0:10:2,0:5])

my_columns = [True, True, False, True, False,True] 
#print(covid_data.iloc[0:3,my_columns])
#Python will go through the list and show me the columns where the value is True.

print(covid_data.loc[2:4,"date"])# loc 若用：则range是前闭后闭
print(covid_data.iloc[10:15,[1,3]])# iloc 若用：则range是前闭后开

#to Afghanistan.

country = ""
list_country = []
for index in range(7996):
    country = covid_data.iloc[index,1]
    if country == "Afghanistan":
        list_country.append(True)
    else:
        list_country.append(False)
        
print(covid_data.iloc[list_country,1])

#5
country = ""
list_country = []
for index in range(7996):
    country = covid_data.iloc[index,1]
    if country == "China":
        list_country.append(True)
    else:
        list_country.append(False)
        
china_new_data = covid_data.iloc[list_country,0:4]
china_new_cases = covid_data.iloc[list_country,2]
china_new_death = covid_data.iloc[list_country,3]
mean_newcases = china_new_data['new_cases'].mean()
mean_newdeath = china_new_data['new_deaths'].mean()
china_dates = covid_data.iloc[list_country,0]
#You have correctly computed the mean number of new cases and new deaths in China.
print(mean_newcases)
print(mean_newdeath)
rate = mean_newdeath/mean_newcases
print(rate)
fig1 = plt.figure(num='china_cases', figsize=(9, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
#You have successfully plotted both new cases and new deaths in China over time.

plt.plot(china_dates,china_new_cases,c = 'r',marker = 'o')
plt.plot(china_dates,china_new_death,c = 'b',marker = 'x')
plt.xlabel('Dates')
plt.ylabel('Daily additions') 
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.show()


#You have successfully created a boxplot of new cases and new deaths in China worldwide.
country = ""
list_country = []
for index in range(7996):
    country = covid_data.iloc[index,1]
    if country == "China":
        list_country.append(True)
    else:
        list_country.append(False)

china_new_data = covid_data.iloc[list_country,0:4]
china_new_cases = covid_data.iloc[list_country,2]
china_new_death = covid_data.iloc[list_country,3]
mean_newcases = china_new_data['new_cases'].mean()
mean_newdeath = china_new_data['new_deaths'].mean()
china_dates = covid_data.iloc[list_country,0]
data_all = [china_new_cases,china_new_death]

plt.boxplot(data_all,showmeans=True,patch_artist=True,vert=False,sym='b+',labels=('newcases','newdeath'))  #patch_artist represents the default background; sym means:Outlier patterns;Vert controls the direction of the box diagram. The default value is True, indicating a vertical box diagram




plt.title("china_newcases",color = "blue")
plt.xlabel("",color = "red")
plt.savefig("a.png")
plt.show()

plt.boxplot(china_new_death,showmeans=True,patch_artist=True,vert=False,sym='b+') #patch_artist represents the default background; sym means:Outlier patterns;Vert controls the direction of the box diagram. The default value is True, indicating a vertical box diagram

plt.title("china_newdeaths",color = "blue")
plt.xlabel("",color = "red")
plt.savefig("a.png")
plt.show()

plt.plot(china_dates, china_new_cases, 'r+')# b+ equals to blue and the shape is +; r+ equals to red and the shape is +; bo equals to blue and the shape is o
plt.title("china_new_cases")
plt.xticks(china_dates.iloc[0:len(china_dates):3],rotation=-90)
plt.show()


#6
#Austria
'''
country = ""
list_country = []
for index in range(7996):
    country = covid_data.iloc[index,1]
    if country == "Austria":
        list_country.append(True)
    else:
        list_country.append(False)
        
print(covid_data.iloc[list_country,1])
Austria_new_data = covid_data.iloc[list_country,0:6]
Austria_total_cases = covid_data.iloc[list_country,4]
Austria_total_death = covid_data.iloc[list_country,5]
Austria_dates = covid_data.iloc[list_country,0]
fig1 = plt.figure(num='Austria', figsize=(9, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
plt.plot(Austria_dates,Austria_total_cases,c = 'b',marker = 'o')
plt.plot(Austria_dates,Austria_total_death,c = 'r',marker = 'x')
plt.xlabel('date')
plt.ylabel('number') 
plt.xticks(Austria_dates.iloc[0:len(Austria_dates):4],rotation=-90)
plt.show()
'''
#Korea

country = ""
list_country = []
for index in range(7996):
    country = covid_data.iloc[index,1]
    if country == "South Korea":
        list_country.append(True)
    else:
        list_country.append(False)
        
print(covid_data.iloc[list_country,1])

korea_new_data = covid_data.iloc[list_country,0:6]
korea_total_cases = covid_data.iloc[list_country,4]
korea_total_death = covid_data.iloc[list_country,5]
korea_dates = covid_data.iloc[list_country,0]

fig2 = plt.figure(num='Korea', figsize=(9, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
plt.plot(korea_dates,korea_total_cases,c = 'b',marker = 'o')
plt.plot(korea_dates,korea_total_death,c = 'r',marker = 'x')
plt.xlabel('date')
plt.ylabel('number') 
plt.xticks(korea_dates.iloc[0:len(korea_dates):4],rotation=-90)

#plt.show()


#Kenya

country = ""
list_country = []
for index in range(7996):
    country = covid_data.iloc[index,1]
    if country == "Kenya":
        list_country.append(True)
    else:
        list_country.append(False)
        
print(covid_data.iloc[list_country,1])

kenya_new_data = covid_data.iloc[list_country,0:6]
kenya_total_cases = covid_data.iloc[list_country,4]
kenya_total_death = covid_data.iloc[list_country,5]
kenya_dates = covid_data.iloc[list_country,0]

fig3 = plt.figure(num='Kenya', figsize=(9, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
plt.plot(kenya_dates,kenya_total_cases,c = 'b',marker = 'o')
plt.plot(kenya_dates,kenya_total_death,c = 'r',marker = 'x')
plt.xlabel('date')
plt.ylabel('number') 
plt.xticks(kenya_dates.iloc[0:len(kenya_dates):4],rotation=-90)

#colombia
country = ""
list_country = []
for index in range(7996):
    country = covid_data.iloc[index,1]
    if country == "Colombia":
        list_country.append(True)
    else:
        list_country.append(False)
        
print(covid_data.iloc[list_country,1])

colombia_new_data = covid_data.iloc[list_country,0:6]
colombia_total_cases = covid_data.iloc[list_country,4]
colombia_total_death = covid_data.iloc[list_country,5]
colombia_dates = covid_data.iloc[list_country,0]

fig3 = plt.figure(num='Colombia', figsize=(9, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
plt.plot(colombia_dates,colombia_total_cases,c = 'b',marker = 'o')
plt.plot(colombia_dates,colombia_total_death,c = 'r',marker = 'x')
plt.xlabel('date')
plt.ylabel('number') 
plt.xticks(colombia_dates.iloc[0:len(colombia_dates):4],rotation=-90)
plt.show()
'''
