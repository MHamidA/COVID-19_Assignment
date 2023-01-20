import pandas as pd

class CorrelationCalculator:
    def __init__(self, file_path, countries):
        self.file_path = file_path
        self.countries = countries
        self.df = pd.read_csv(file_path)
        
    def filter_countries(self):
        self.df = self.df[self.df['location'].isin(self.countries)]
        
    def calculate_correlations(self):
        self.correlations = {}
        for country in self.countries:
            country_df = self.df[self.df['location'] == country][['total_deaths', 'median_age']].fillna(0)
            corr = country_df.corr()
            self.correlations[country] = corr
        
    def print_interpretation(self):
        with open('corr_interpretation.txt', 'w') as f:
            for country, corr in self.correlations.items():
                interpretation = f"Correlation between total deaths and median age for {country}:\n{corr}"
                print(interpretation)
                f.write(interpretation + '\n')

if __name__ == '__main__':
    calculator = CorrelationCalculator("Assets/owid-covid-data.csv", ["United States", "China", "France", "Germany"])
    calculator.filter_countries()
    calculator.calculate_correlations()
    calculator.print_interpretation()
