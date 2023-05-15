import statistics as st
from fractions import Fraction as F
from decimal import Decimal

# mean
print("mean: ")
l = [1, 4, 3, 2, 1]  # (1 + 4 + 3 +2 + 1)/5 = 2.2
print(st.mean(l))
listF = [F(4, 5), F(2, 3), F(4, 5), F(1, 4)]  # (4/5 + 2/3 + 4/5 + 1/4)/ 5
print(st.mean(listF))
print("------------------")

# list = []
# print(st.mean(list)) # raise StatisticsError

# fmean
print("fmean: ")

l = [4, 8, 61, 1, 56]  # (4+8+61+1+56)/5
print(st.fmean(l))
l = [4.5, 8.1, 6.5, 1, 56]  # (4.5 + 8.1 +6.5 + 1 + 56)
print(st.fmean(l))
print("------------------")

# geometric_mean
print("geomtric_mean: ")
l = [15, 7, 1, 4]  # sqrt5(15,7,1,4)
print(st.geometric_mean(l))
# l = [-4, 7, 1, 4]
# print(st.geometric_mean(l)) # raise StatisticsError (negative Number is not allowed)
print("------------------")

# harmonic_mean
print("harmonic_mean: ")
l = [40, 60, 50]  # 3/(1/40 + 1/60 + 1/50)
print(st.harmonic_mean(l))
print(st.harmonic_mean(l, weights=[4, 30, 20]))
print("------------------")

# median
print("median: ")
print(st.median([1, 2, 4]))  # number of list is odd --> middle number is returned (2)
print(st.median([1, 2, 4, 5]))  # number of list is even --> (2 + 4)/2 = 3
print(st.median([6, 3, 4, 8, 9]))  # number of list is odd --> middle number is returned (6)
print("------------------")

# median_low
print("median_low: ")
print(st.median_low([1, 2, 4]))  # number of list is odd --> middle number is returned (2)
print(st.median_low([1, 2, 4, 5]))  # number of list is even --> lower middle number is returned (2)
print(st.median_low([6, 3, 4, 8, 9]))  # number of list is odd --> middle number is returned (6)
print("------------------")

# median_high
print("median_high: ")
print(st.median_high([1, 2, 4]))  # number of list is odd --> middle number is returned (2)
print(st.median_high([1, 2, 4, 5]))  # number of list is even --> greater number is returned (4)
print(st.median_high([2, 3, 6, 8, 9, 10]))  # number of list is even --> greater middle number is returned (8)
print("------------------")

# median_grouped
print("median_grouped: ")
print(st.median_grouped([1, 1, 2, 2, 4], interval=1))
print(st.median_grouped([1, 3, 5, 2, 4], interval=1))
print(st.median_grouped([34, 65, 1, 2, 4], interval=2))
print("------------------")

# mode
print("mode: ")
print(st.mode([1, 2, 4]))  # 1 (first number)
print(st.mode([1, 2, 3, 4, 3, 3, 3]))  # 3 (4 times repeated)
print(st.mode([1, 2, 4, 2, 2, 4, 1, 3]))  # 2 (3 times repeated)
print("------------------")

# multimode
print("multi_mode: ")
print(st.multimode([1, 1, 2, 2, 4]))  # 1,2 (2 times repeated)
print(st.multimode("tttpppabbb"))  # t,p,b (3 times repeated)
print(st.multimode([1, 2, 4, -1, -1, 2]))  # 2, -1 (2 times repeated)
print("------------------")

# quantiles
print("quantiles: ")
data1 = [1, 5, 6, 7, 18, 25, 26, 27, 27, 26]
print(st.quantiles(data1, n=4, method='exclusive'))
print(st.quantiles(data1, n=5, method='inclusive'))
print("------------------")

# pstdev
print("pstdev: ")
data1 = [1, 5, 6, 7, 18, 25, 26, 27, 27, 26]
print(st.pstdev(data1, st.mean(data1)))
print(st.pstdev(data1))
print("------------------")

# pvariance
print("pvariance: ")
data1 = [1, 5, 6, 7, 18, 25, 26, 27, 27, 26]
data2 = [F(1, 2), F(5, 6), F(7, 18)]
data3 = [Decimal("24.5"), Decimal("44.1"), Decimal("15.2")]

print(st.pvariance(data1, st.mean(data1)))
print(st.pvariance(data1, None))
print(st.pvariance(data2, st.mean(data2)))
print(st.pvariance(data2, None))
print(st.pvariance(data3, st.mean(data3)))
print(st.pvariance(data3, None))
print("------------------")

# stdev
print("stdev: ")
print(st.stdev(data1, st.mean(data1)))
print(st.stdev(data1, None))
print(st.stdev(data2, st.mean(data2)))
print(st.stdev(data2, None))
print(st.stdev(data3, st.mean(data3)))
print(st.stdev(data3, None))
print("------------------")

# variance
print("variance: ")
print(st.variance(data1, st.mean(data1)))
print(st.variance(data1, None))
print(st.variance(data2, st.mean(data2)))
print(st.variance(data2, None))
print(st.variance(data3, st.mean(data3)))
print(st.variance(data3, None))
print("------------------")

# covariance
print("covariance: ")
data1 = [1, 5, 6, 7, 18, 25, 26, 27, 27, 26]
data2 = [1, 5, 8, 15, 24, 31, 44, 32, 27, 26]
data3 = [45, 43, 42, 34, 33, 31, 29, 25, 24, 23]
print(st.covariance(data1, data2))
print(st.covariance(data1, data3))
print("------------------")

# correctlation
print("correctlation: ")
print(st.correlation(data1, data2))
print(st.correlation(data1, data3))
print("------------------")

# linear_regression
print("linear_regression: ")
x = [1964, 1985, 1987, 1999]
y = [1, 3, 5, 8]
a, b = st.linear_regression(x, y, proportional=False)  # y = ax + b
print(a, b)
a, b = st.linear_regression(x, y, proportional=True)  # y = ax
print(a, b)
