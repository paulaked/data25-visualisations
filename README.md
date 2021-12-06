# data25-visualisations

Task: 
- Create your own branch for this repo and commit & push your work to it frequently with good commit messages.
- Change this README.md to your own version on your branch, outlining what dataset you are using and notes about your data exploration/analysis.
- Pick a dataset from Kaggle, if you struggle pick one of the suggested ones below. 
- Clean and analyse the dataset using Pandas DataFrames and packages like seaborn and matplotlib to create visualisations.

## Dataset from Kaggle:

- Videogame Sales: https://www.kaggle.com/gregorut/videogamesales , contains info about videogames and sales in 4 different regions

- Firstly, clean up Year column, which was unneccessarily done as floats.
  This did require filling in N/A values with a 0 in order to convert the whole column.

- Next, make Publisher column uniform by changing all Unknown to N/A.
  This way, we can pick all rows with no value in a more efficient way.
