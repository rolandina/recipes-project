from recipebook.data import Data

class Recipe(Data):

    def __init__(self):
        super().__init__()
        self.__recipes_scored = self.__create_recipe_scored_table()

    def __create_recipe_scored_table(self):
        
        recipes = self._Data__data['recipe']
        ingredients = self._Data__data['ingredient']
        items = self._Data__data['recipe_items'] 

        recipes_scored = recipes.copy()
        joint1 = items[['ingredient_id', 'recipe_id']].join(ingredients[['Id', 'Score']].set_index('Id'), on="ingredient_id", how='left')
        joint2 = joint1.join(recipes[['Id','name']].set_index('Id'), on = 'recipe_id', how = 'left')

        recipes_scored['score'] = joint2[['name', 'Score']].groupby(by = ['name']).mean()['Score'].to_list()
       
        return recipes_scored[['name', 'score']]
        
    def get_scored_recipes(self):
        return self.__recipes_scored

    