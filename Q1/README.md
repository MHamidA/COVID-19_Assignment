# Q1
What is the probability of dying from COVID infection in France in March 2023 for a 25 year old? Draw the relevant correlation projections.

## Main Idea
The goal of this analysis is to determine the probability of dying from COVID-19 infection in France in March 2023 for a 25 year old. To accomplish this, we need to consider three variables: total_deaths, total_cases, and age. However, the age variable is not provided in the data. Instead, we have median_age, percentage of individuals older than 65, and percentage of individuals older than 70. These variables are not a perfect representation of the age variable and may introduce bias, but we will begin by assuming that median_age can be used as a proxy.

After further examination, it was determined that using median_age as a proxy is not a viable solution, as the median_age in France is stagnant and cannot be used for forecasting. Therefore, the question being addressed in this analysis is: What is **"the probability of dying from COVID infection in France in March 2023?"**

All the walkthrough of the approach can be seen here in the [Notebook](https://github.com/MHamidA/COVID-19_Assignment/blob/main/Q1/Q1%20Notebook.ipynb)

The approach taken to this problem is unique in that:
1. Since data is not available until March 2023, a model was created to forecast the data until that date. The Python script for the first model, which forecasts total_deaths, can be found here: [Model1.py](https://github.com/MHamidA/COVID-19_Assignment/blob/main/Q1/Model1.py)
2. A second model was created to forecast total_cases. The Python script for this model can be found here: [Model2.py](https://github.com/MHamidA/COVID-19_Assignment/blob/main/Q1/Model2.py)
3. The probability of dying from COVID-19 is calculated by dividing total_deaths by total_cases. The Python script for this calculation can be found here: [Probability.py](https://github.com/MHamidA/COVID-19_Assignment/blob/main/Q1/Probability.py)

To address the question **"Draw the relevant correlation projections"**, a Jupyter notebook was created to interactively visualize the correlation between total_deaths and total_cases with age, commodities, healthcare access and availability, and socio-economic status. These factors were chosen as they are assumed to have a significant correlation to total_cases and total_deaths. The notebook can be accessed here: [Notebook](https://github.com/MHamidA/COVID-19_Assignment/blob/main/Q1/Q1%20Notebook.ipynb)
