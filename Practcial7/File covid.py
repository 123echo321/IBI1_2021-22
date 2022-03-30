#import the full_data .csv file
os.chdir("C:\Users\DELL\Desktop\practical7")
#read the content of the .csv file into a dataframe object
covid_data=pd.read_csv("full_data.csv")

#show the first three rows, but only the first, third, and fifth column
covid_data.iloc[0:3,[0.2.4]]

#use a Boolean to show "total_cases" for all rows corresponding to Afghanistan 
covid_data.loc[covid_data["location"]=="Afghanistan","total_cases"]

#compute the mean number of new cases and new deaths in China
#access the specific row and column values by loc- and iloc-function
china_new_cases=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_deaths']]
china_dates=china_new_data.iloc[:,0]
#calculate the mean number and print them
new_cases_mean=np.mean(china_new_cases["new_cases"])
print(new_cases_mean)
new_deaths_mean=np.mean(china_new_cases["new_deaths"])
print(new_deaths_mean)

#creat a boxplot of new cases in China worldwide
china_data=covid_data.loc[covid_data['location']=='China',["date",'new_cases','new_deaths']]
china_dates=china_data.loc[:,"date"]
plt.boxplot(china_data.loc[:,"new_cases"],whis=1.5,patch_artist=True)
plt.show()

#creat a boxplot of new deaths in China worldwide
china_data=covid_data.loc[covid_data['location']=='China',["date",'new_cases','new_deaths']]
china_dates=china_data.loc[:,"date"]
plt.boxplot(china_data.loc[:,"new_deaths"],whis=1.5,patch_artist=True)
plt.show()

#plot both new cases and new deaths in China over time
china_data=covid_data.loc[covid_data["location"]=="China",["date","new_cases","new_deaths"]]
china_dates=china_data.loc[:,"date"]
new_cases=china_data.loc[:,"new_cases"]
new_deaths=china_data.loc[:,"new_deaths"]
plt.plot(china_dates,new_cases,"b*")
plt.plot(china_dates,new_deaths,"ro")
plt.xlabel("date")
plt.ylabel("number of people")
plt.legend(["new_cases","new_deaths"])
#make the x axis more clear and the code is from Practical7
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.title("New cases and new deaths in China over time")
plt.show()
