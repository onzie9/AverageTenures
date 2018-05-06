import pandas as pd
from collections import Counter


def weird_division(n, d):
    return n / d if d else 0

nums1 = [4, .5, 1, 3, 2, 10, 9, 5, 7, 6, 8]
nums2 = [4, .5, 1, 3, 2, 20, 9, 5, 7, 6, 8]

df1 = pd.read_csv('RejectStatsA.csv')
df = pd.read_csv('LoanStats3a.csv')

states = df1.State
tenure = df.Tenure
statecodes = []
for key in Counter(states).keys():
    statecodes.append(key)

tenurecount = {}
for code in statecodes:
    tenurecount[code] = Counter(df[df['State'] == code].Tenure)

tenurecount1 = {}
for code in statecodes:
    tenurecount1[code] = Counter(df1[df1['State'] == code].Tenure)

tenurekeys = Counter(tenure).keys()


for code in statecodes:
    step = []
    for key in tenurekeys:
        temp = []
        temp.append(code)
        temp.append(key)
        temp.append(tenurecount[code][key])
        temp.append(tenurecount1[code][key])
        step.append(temp)
    num1 = 0
    num2 = 0
    tot = 0
    for i in range(11):
        num1 += nums1[i]*(step[i][2] + step[i][3])
        num2 += nums2[i]*(step[i][2] + step[i][3])
        tot += step[i][2] + step[i][3]
        if i == 10:
            avg1 = weird_division(num1, tot)
            avg2 = weird_division(num2, tot)
            print("The average tenure for " + str(code) + " is between " + "{0:.2f}".format(avg1) + " and " +
                  "{0:.2f}".format(avg2))
