# AverageTenures
Analysis of LendingClub.com data self-reports of employment tenure from 2007 to 2011.

In this project, I downloaded [two public data sets from LendingClub.com](https://www.lendingclub.com/info/download-data.action).  One data set contains rejections from 2007 to 2012, and the other contains all loan data from 2007 to 2011, the early years of LendingClub.  Within those data, there is a self-reported employment tenure for each data point.  I parsed all the data (800,000 points) by state, and then looked at the average tenure for each state. The options for tenure were limited, with the largest option being "10+ years" and the smallest option "<1 year".  For these computations, I set "<1" to be .5 years, and I did two averages, one for exactly 10 years, and one for 20 years.  The two results were identical in many places, and only differed by a few days in most days; I used the average of the two values. This was all done in Python using pandas.

I used d3 and created two cartograms.  One image uses all the data, and the other image excludes 7 outlying states. The 7 outliers had very few data points. These images are in the form of the two html files.
