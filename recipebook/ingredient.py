from recipebook.data import Data

class Ingredient:

    def __init__(self):
        self.__data_dict = Data().get_data()
        self.__ingredient_popularities = self.__create_popularities_table()

    def __create_popularities_table(self):
        
        ingredients = self.__data_dict['ingredient']
        items = self.__data_dict['recipe_items'] 

        ingredient_popularities = ingredients.copy()
        ingredient_popularities['polularity'] = items[['ingredient_id','recipe_id']].groupby(by = ['ingredient_id']).count()['recipe_id'].to_list()
        ingredient_popularities['is_popular'] = [1 if i >1 else 0 for i in ingredient_popularities['polularity']]
        return ingredient_popularities

    def get_with_popularities(self):
        return self.__ingredient_popularities