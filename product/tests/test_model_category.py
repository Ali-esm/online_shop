from django.test import TestCase
from ..models import Category


class CategoryTest(TestCase):

    def setUp(self) -> None:
        self.men_category = Category.objects.create(name='men')
        self.child_category = Category.objects.create(name='child')
        self.shirt_category = Category.objects.create(name='shirt', parent=self.men_category, is_sub=True)
        self.shoe_category = Category.objects.create(name='shoe', parent=self.child_category)

    def test_parent(self):
        self.assertEqual(self.men_category.parent, None)
        self.assertEqual(self.child_category.parent, None)
        self.assertEqual(self.shirt_category.parent.name, 'men')
        self.assertEqual(self.shoe_category.parent.name, 'child')

    def test_is_sub_not_set(self):
        self.assertEqual(self.shoe_category.is_sub, True)
        self.assertEqual(self.men_category.is_sub, False)

    def test_model_str(self):
        self.assertEqual(self.men_category, 'men')
        self.assertEqual(self.shirt_category, 'shirt')

