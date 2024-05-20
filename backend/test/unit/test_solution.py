import pytest
import unittest.mock as mock

from src.controllers.recipecontroller import RecipeController
from src.static.diets import from_string
@pytest.fixture
def sut():
    mockeList = mock.MagicMock()
    mockeList.get_readiness_of_recipes.return_value = ['Banana Bread']
    mockedsut = RecipeController(dao=mockeList)
    return mockedsut


@pytest.mark.unit
@pytest.mark.parametrize('take, expected' [(1, 'Banana Bread', )])
def optimal(sut, take, expected):
    diet = from_string('vegetarian')
    validationresult = sut.get_recipe(diet=diet, take_best=take)
    print(validationresult)
    assert validationresult == expected 