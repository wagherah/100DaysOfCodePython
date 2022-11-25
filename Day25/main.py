import pandas
# gets dataFrama
data = pandas.read_csv('squirrel_census_data.csv')

# get series
fur_colors = data['Primary Fur Color']
gray_count = fur_colors.value_counts()['Gray']
black_count = fur_colors.value_counts()['Black']
cinnamon_count = fur_colors.value_counts()['Cinnamon']


# creating csv
squirrel_colors_dict = {
    'Fur Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [gray_count, black_count, cinnamon_count]
}

squirrel_colors = pandas.DataFrame(squirrel_colors_dict)
# saving the data frame in csv file
squirrel_colors.to_csv('squirrel_colors.csv')
