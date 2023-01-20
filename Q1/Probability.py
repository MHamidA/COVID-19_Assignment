import pandas as pd

class DataProcessor:
    def __init__(self, deaths_file, cases_file):
        self.deaths_file = deaths_file
        self.cases_file = cases_file
        self.df_deaths = pd.read_csv(self.deaths_file)
        self.df_cases = pd.read_csv(self.cases_file)
        self.dfmerged = pd.merge(self.df_deaths, self.df_cases, on='date')
        self.dfmerged['date'] = pd.to_datetime(self.dfmerged['date'])
    
    def filter_by_month_year(self, year, month):
        mask = (self.dfmerged['date'].dt.year == year) & (self.dfmerged['date'].dt.month == month)
        self.df_march = self.dfmerged[mask]
        return self.df_march
    
    def calculate_probability(self):
        self.df_march['probability_of_death'] = self.df_march['total_deaths'] / self.df_march['total_cases']
    
    def save_csv(self, filename):
        self.df_march.to_csv(filename)
        print("Saving the CSV file")
    
    def save_interpretation(self, filename):
        max = round(self.df_march['probability_of_death'].max(), 4)
        min = round(self.df_march['probability_of_death'].min(), 4)
        average = round(self.df_march['probability_of_death'].mean(), 4)
        interpretation = (f'The least likelihood of fatalities caused by COVID-19 in March 2023 in France forecasted to be {min} or {min*100}%.\n'
                         f'The most significant probability of fatalities caused by COVID-19 in March 2023 in France forecasted to be {max*100} or {max*100}%.\n'
                         f'The average probability of fatalities caused by COVID-19 in March 2023 in France was calculated to be {average} or {average*100}%, providing a general overview of the risk level during that specific period.')
        print("Saving the Probability Interpretation (TXT) file")
        with open(filename, "w") as text_file:
            text_file.write(interpretation)

if __name__ == '__main__':
    data_processor = DataProcessor('tdeaths_forecasted.csv', 'tcases_forecasted.csv')
    data_processor.filter_by_month_year(2023, 3)
    data_processor.calculate_probability()
    data_processor.save_csv('march_2023.csv')
    data_processor.save_interpretation('prob interpretation.txt')