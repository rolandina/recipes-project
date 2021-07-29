from recipebook.data import Data

class Ingredient(Data):

    def __init__(self):
        super().__init__()
        self.__ingredient_popularities = self.__create_popularities_table()

    def __create_popularities_table(self):
        
        ingredients = self._Data__data['ingredient']
        items = self._Data__data['recipe_items'] 

        ingredient_popularities = ingredients.copy()
        ingredient_popularities['polularity'] = items[['ingredient_id','recipe_id']].groupby(by = ['ingredient_id']).count()['recipe_id'].to_list()
        ingredient_popularities['is_popular'] = [1 if i >1 else 0 for i in ingredient_popularities['polularity']]
        return ingredient_popularities

    def get_with_popularities(self):
        return self.__ingredient_popularities