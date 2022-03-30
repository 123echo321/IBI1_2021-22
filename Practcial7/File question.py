#answer the question: When the new cases and total cases were significantly increasing in Spain?
Spain_data=covid_data.loc[covid_data["location"]=="Spain",["date","new_cases","total_cases"]]
Spain_dates=Spain_data.loc[:,"date"]
new_cases=Spain_data.loc[:,"new_cases"]
total_cases=Spain_data.loc[:,"total_cases"]
plt.plot(Spain_dates,new_cases,"b*")
plt.plot(Spain_dates,total_cases,"ro")
plt.xlabel("date")
plt.ylabel("number of people")
plt.legend(["new_cases","total_cases"])
#make the x axis more clear and the code is from Practical7
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-90)
plt.title("New cases and total cases in Spain over time")
