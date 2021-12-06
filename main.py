import pandas as pd
import tabulate as tb


data = pd.read_csv(r"D:\Documents\Work\python\pandas\data25-visualisations\top10s.csv", encoding='latin-1')
data = pd.DataFrame(data)
data = data.rename(columns={"nrgy": "energy", "dnce": "danceability", "live": "liveness", "val": "positivity",
                            "dur": "duration", "acous": "acousticness", "spch": "speechiness",
                            "pop": "popularity"})
#print(tb.tabulate(data, headers=data))
grouped_by_year = data.groupby(data.year)
year_2010 = grouped_by_year.get_group(2010)
year_2011 = grouped_by_year.get_group(2011)
year_2012 = grouped_by_year.get_group(2012)
year_2013 = grouped_by_year.get_group(2013)
year_2014 = grouped_by_year.get_group(2014)
year_2015 = grouped_by_year.get_group(2015)
year_2016 = grouped_by_year.get_group(2016)
year_2017 = grouped_by_year.get_group(2017)
year_2018 = grouped_by_year.get_group(2018)
year_2019 = grouped_by_year.get_group(2019)
print(tb.tabulate(year_2019, headers=data))