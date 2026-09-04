# https://matplotlib.org/stable/users/explain/quick_start.html

import matplotlib.pyplot as plt #pyplot is module inside matplotlib used for creating graphs
import numpy as np

# year = [2025,2026,2027,2028]
# cgpa = [8.56,9.0,9.5,8.96]

# plt.plot(year,cgpa,
#          marker = "o",
#          markersize = 6,
#          markerfacecolor = "black",
#          linestyle = "solid",
#          linewidth= 3,
#          color = "green")

# lne_style = dict(marker = "o",
#          markersize = 6,
#          markerfacecolor = "black",
#          linestyle = "solid",
#          linewidth= 3,
#          color = "green")

# cgpa_std2 = [6.7,8.9,9.4,4.0]

# plt.plot(year,cgpa_std2,**lne_style) #double * used to unpack dict

# plt.xticks(year)#this will only show the given tick in x-axis

##________________________________________________________________________________________________________________________

# x = np.array(["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7"])
# y1 = np.array([2400,2380,2390,2700,2790,2300,2500])

# plt.plot(x,y1,
#          marker = "o",
#          markerfacecolor = "green")

# plt.title("Diet track",
#           fontsize = 18,
#           family = "times new roman",
#           fontweight = "bold",
#           color = "red")

# txt_style = dict(fontsize = 18,
#           family = "times new roman",
#           fontweight = "bold")

# plt.xlabel("Days",color = "blue",**txt_style)
# plt.ylabel("Calories",color = "green",**txt_style)

# plt.tick_params(axis="y",
#                 colors = "blue")

##________________________________________________________________________________________________________________________

# x = [0,1,2,3,4,5]
# y = [0,1,4,9,16,25]

# plt.grid(axis="both",
#          linestyle = "dotted",
#          color="gray",
#          linewidth = 2)
 
# plt.plot(x,y,
#          marker = "o")

# plt.xticks(rotation=45) # this rotate ticks in x-axis

##________________________________________________________________________________________________________________________

# Bar chart (used to compare categories of data by representing each category with bar)

# categories = ["mobile","laptop","pc","projector","vr"]
# value = [100,59,44,29,4]

# bars = plt.bar(categories,value)
# plt.title("Gadget usage")
# plt.xlabel("Gadgets")
# plt.ylabel("No:of users")

# plt.bar_label(bars) #this labels the bar in the chart



##________________________________________________________________________________________________________________________

# Pie chart (circular chart divided into slices )

# x = ["childrens","youngster","men","women","scenior citizen"] 
# y = [30000,17000,4600,4800,1890]


# plt.pie(y,labels = x,
#         autopct="%.1f%%",
#         explode=[0,0.1,0,0,0.2],# make the slice out from the pice 
#         startangle=180,#rotate 180 deg
#         )#autopct -- auto percent 

##________________________________________________________________________________________________________________________

# Scatter graph (graph made by individual dots) 

# x = [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
# y = [10,12,11,14,14,18,24,23,25,39]

# plt.scatter(x,y,
#             color = "blue",
#             s = 100,
#             alpha = 0.6,#opacity
#             )

# y2 = [13,14,18,8,7,9,28,30,28,29]

# plt.scatter(x,y2,
#             color = "green",
#             s = 100,
#             alpha = 0.6)

# plt.title("Profit char")
# plt.xlabel("Year")
# plt.ylabel("Income in LPA")

# plt.xticks(x)

##________________________________________________________________________________________________________________________

# Histogram (show distribution of data)

# marks = [35, 42, 45, 48, 51, 53, 55, 56, 58, 60,
#          62, 65, 67, 70, 72, 75, 78, 82, 85, 90]

# plt.hist(marks) #this graph say how many std score how much mark

# scores = np.random.normal(#normal used for normal distribution(belly curve)
#     loc=80, #loc is mean(avg) of the distribution here 80 is avg 
#     scale=10,#scale is standard deviation (how spread value is from mean)
#     size=100,#size tell sample space
#      )
# print(scores)
# scores = np.clip(scores,0,100)#this make all generated number below zero as 0 and above 100 as 100

# plt.hist(scores,
#          bins=10,#no:of bar
#          color = "lightblue",
#          edgecolor = "black"
#          )

##________________________________________________________________________________________________________________________

#Subplots (multiple separate graph inside one figure)

# Figure = the entire canvas
# Axes = a subplot

# x= np.array([1,2,3,4,5])

# fig,axs = plt.subplots(2,2) #2 row 2 col total 4 axis(subplot)

# axs[0,0].plot(x,x,color = "green")
# axs[0,0].set_title("y = x")

# axs[0,1].bar(x,x**2,color = "blue")
# axs[0,1].set_title("y = x^2")

# axs[1,0].pie(x**3,labels = x)
# axs[1,0].set_title("y = x^3")

# axs[1,1].scatter(x,x**4,color = "red")
# axs[1,1].set_title("y = x^4")


##________________________________________________________________________________________________________________________

plt.show() # this show the plot(graph)

