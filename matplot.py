###Visualizing the data

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3, 16000]

# plt.plot(years,gdp,color = "green", marker='o',linestyle='solid')
# plt.title("Nominal GDP")
# plt.ylabel("Billions of $")
# plt.show()

### Bar charts

# movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10]
#
# xs = [i +0.1 for i,_ in enumerate(movies)]
# plt.bar(xs,num_oscars)
# plt.ylabel("# of Academy Awards")
# plt.title("My Favourite Movies")
#
# plt.xticks([i+0.1 for i,_ in enumerate(movies)], movies)
# plt.show()

# mentions = [500,505]
# years = [2013,2014]
#
# plt.bar([2013,2014],mentions,0.5)
# plt.xticks(years)
# plt.ylabel("# of times i heard someone say Data Science")
# plt.ticklabel_format(useOffset=False)
#
# plt.axis([2013,2014,499,506])
# plt.title("Look at the huge Increase")
# plt.show()

##**** Line Charts

# variance = [1,2,4,8,16,32,64,128,256]
# bias_square = variance[::-1]#[256,128,64,32,16,8,4,2,1]
# total_error = [x+y for x,y in zip(variance,bias_square)]
# xs = [i for i, _ in enumerate(variance)]
# print(xs)
# plt.plot(xs, variance, 'g-', label = 'variance')
# plt.plot(xs,bias_square, 'r-', label = 'bias^2')
# plt.plot(xs,total_error, 'b:', label = 'Total error')
# plt.legend(loc = 9)
# plt.xlabel("model complexity")
# plt.title("The Bias Variance Tradeoff")
# plt.show()

###*** Scatter Plots

# friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#
# plt.scatter(friends,minutes)
#
# for label, friend_count, minute_count in zip(labels,friends, minutes):
#     plt.annotate(label,
#                  xy=(friend_count,minute_count),
#                  xytext=(5,-5),
#                  textcoords='offset points')
#
# plt.title("Daily Minutes vs Number of Friends")
# plt.xlabel("# of friends")
# plt.ylabel("daily minutes spent on the site")
# plt.show()

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.axis("equal")
plt.show()