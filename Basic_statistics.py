import statistics as st
from collections import Counter
import matplotlib.pyplot as plt
import math

print(st.median([2,3,4,5]))
a = [1,2,3,4,45,5,0,-6,-8,8,8,-10]
print(max(a))
print(sorted(a))
print(st.mode(a))
print(math.sqrt(4))
####
# num_friends = [100,49,41,40,25]
# friend_counts = Counter(num_friends)
# xs=range(101)
# ys = [friend_counts[x] for x in xs]
# plt.bar(xs,ys)
# plt.axis([0,101,0,25])
# plt.title("Histogram of Friend Counts")
# plt.xlabel("# of Friends")
# plt.ylabel('# of People')
# plt.show()

def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

print(quantile([x for x in range(100)],0.40))

### Dispersion ###
def interquartile_range(x):
    return quantile(x,0.75) - quantile(x,0.25)

print(interquartile_range(a))





