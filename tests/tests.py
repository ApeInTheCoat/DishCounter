import unittest
from app.common import *

recipes = [
    {
        "name": "Бутерброд с сыром",
        "components": [
            {
                "item": "хлеб",
                "q": 50
            },
            {
                "item": "сыр",
                "q": 25
            }
        ]
    },
    {
        "name": "Бутерброд с мясом",
        "components": [
            {
                "item": "мясо",
                "q": 25
            },
            {
                "item": "хлеб",
                "q": 50
            }
        ]
    }
]


class TestCountDishes(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(count_dishes(recipes, {}), [])

    def test_zero(self):
        self.assertEqual(count_dishes(recipes, {'мясо': 0, 'хлеб': 0, 'сыр': 0}), [])

    def test_irrelevant(self):
        self.assertEqual(count_dishes(recipes,
                                      {'свекла': 100, 'рыба': 100, 'огурец': 100, 'картофель': 100, 'яйцо': 100}), [])

    def test_no_bread(self):
        self.assertEqual(count_dishes(recipes,
                                      {'мясо': 100, 'сыр': 100}), [])

    def test_no_cheese(self):
        self.assertEqual(count_dishes(recipes,
                                      {'мясо': 100, 'хлеб': 100}), [{'Бутерброд с мясом': 2}])

    def test_no_meat(self):
        self.assertEqual(count_dishes(recipes,
                                      {'сыр': 100, 'хлеб': 100}), [{'Бутерброд с сыром': 2}])

    def test_abundance(self):
        self.assertEqual(count_dishes(recipes,
                                      {'сыр': 2000, 'хлеб': 2000, 'мясо': 2000}),
                         [{'Бутерброд с сыром': 40}, {'Бутерброд с мясом': 40}])


class TestAssertFridgeIsValid(unittest.TestCase):

    def test_invalid(self):
        with self.assertRaises(TypeError):
            assert_fridge_is_valid(None)

    def test_invalid_name(self):
        with self.assertRaises(TypeError):
            assert_fridge_is_valid({'рыба': 100, 'огурец': 100, 250: 'грибы', 'сыр': 25})

    def test_invalid_count(self):
        with self.assertRaises(TypeError):
            assert_fridge_is_valid({'сыр': 2000, 'хлеб': 2000, 'мясо': '100'})

    def test_valid(self):
        assert_fridge_is_valid({'молоко': 5, 'мясо': 250, 'авокадо': 7})


if __name__ == '__main__':
    unittest.main()
