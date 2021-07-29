from recipebook.data import Data

class Recipe:

    def __init__(self):
        self.get_scored_recipes = []


    def __init__(self):
        self.__data_dict = Data().get_data()
        self.__recipes_scored = self.__create_recipe_scored_table()

    def __create_recipe_scored_table(self):
        
        recipes = self.__data_dict['recipe']
        ingredients = self.__data_dict['ingredient']
        items = self.__data_dict['recipe_items'] 

        recipes_scored = recipes.copy()
        joint1 = items[['ingredient_id', 'recipe_id']].join(ingredients[['Id', 'Score']].set_index('Id'), on="ingredient_id", how='left')
        joint2 = joint1.join(recipes[['Id','name']].set_index('Id'), on = 'recipe_id', how = 'left')

        recipes_scored['score'] = joint2[['name', 'Score']].groupby(by = ['name']).mean()['Score'].to_list()
       
        return recipes_scored[['name', 'score']]
        
    def get_scored_recipes(self):
        return self.__recipes_scored

    