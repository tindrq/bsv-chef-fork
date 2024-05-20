import pytest
import unittest.mock as mock
from unittest.mock import patch

from src.controllers.recipecontroller import RecipeController
from src.static.diets import from_string
@pytest.fixture
def sut(ListRecipes : list ):
    mockeList = mock.MagicMock()
    mockeList.get_readiness_of_recipes.return_value = ListRecipes
    mockedsut = RecipeController(dao=mockeList)
    return mockedsut


@pytest.mark.unit
@pytest.mark.parametrize('take, expected, ListRecipes', [(True, 'Banana Bread', ['Banana Bread']),
                                                            (False, 'Banana Bread', ['Banana Bread']),
                                                            (True, None, [])])
def optimal(sut, take, expected, ListRecipes):
    diet = from_string('vegetarian')
    with patch('random.randint') as mockrandint:
        mockrandint.return_value = 1
    validationresult = sut.get_recipe(diet=diet, take_best=take)
    print(validationresult)
    assert validationresult == expected 