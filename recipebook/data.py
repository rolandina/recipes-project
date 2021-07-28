import pandas as pd

class Data:
    
    def __init__(self):
        self.__data = dict()
        self.__read_data()

    def __read_table(self, table_name):
        path = "../data/csv/" + table_name
        cols = list(pd.read_csv(path, sep = ';', nrows =1))
        return pd.read_csv(path, sep = ';', usecols =[i for i in cols if i.split(':')[0] != 'Unnamed'])

    def __read_data(self):
        self.__data['recipe'] = self.__read_table('recipes.csv')
        self.__data['ingredient'] = self.__read_table('ingredients.csv')
        self.__data['recipe_items'] = self.__read_table('recipe_items.csv')

    def get_data(self):
        return self.__data