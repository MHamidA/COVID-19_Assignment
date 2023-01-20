# Q2
What is the correlation between the number of deaths with age for the US, China, France and Germany?

## Main Idea
In this folder, it aim to explore the correlation between the number of deaths and age for the US, China, France, and Germany. To do so, I preprocessed the data by filtering and filling any missing values. I then utilized the corr function to calculate the correlation. The python script used for this analysis can be found on our GitHub repository at [Correlation.py](https://github.com/MHamidA/COVID-19_Assignment/blob/main/Q2/correlation.py)

All the walkthrough of the approach can be seen here in the [Notebook](https://github.com/MHamidA/COVID-19_Assignment/blob/main/Q2/Q2%20Notebook.ipynb)

However, an important thing to note is that the correlation obtained illustrates a nan value. While this can often be attributed to missing data, in this instance, it is not a result of missing data as we have already replaced any missing values.

The reason for the nan correlation is that the values do not vary. This can happen due to the formula used to calculate correlation, which is 

cor(i,j) = cov(i,j)/[stdev(i)*stdev(j)]

As we can see, the formula is divided by the standard deviation of both variables. If the values do not vary, the standard deviation will be zero, resulting in a division by zero and ultimately producing a nan value. In this case, all the median age data is homogenous or stagnant, resulting in a standard deviation of zero.
