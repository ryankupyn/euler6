sumsquares = 0
sumtotal = 0
for x in range(1, 101):
    sumsquares += x*x
    sumtotal += x
squaredsum = sumtotal*sumtotal
print(squaredsum - sumsquares)