#!/usr/bin/python3
"""
A test suite for BaseModel
"""
import unittest
from datetime import datetime
import models
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """
    Contains series of test cases for BaseModel class
    """

    def test_if_id_attribute_is_present(self):
        """
        Checks if BaseModel has the id attribute
        """
        a = BaseModel()
        self.assertTrue(hasattr(a, 'id'))

    def test_if_created_at_attribute_is_present(self):
        """
        Checks if the BaseModel has the created_at attribute
        """
        a = BaseModel()
        self.assertTrue(hasattr(a, 'created_at'))

    def test_if_updated_at_attribute_is_present(self):
        """
        Checks if the BaseModel has the updated_at attribute
        """
        a = BaseModel()
        self.assertTrue(hasattr(a, 'updated_at'))

    def test_if_id_is_unique(self):
        """
        Checks if id attribute is unique
        """
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_if_id_is_str(self):
        """
        Checks if id is a string
        """
        a = BaseModel()
        self.assertTrue(type(a.id), str)

    def test_if_str_has_correct_output(self):
        """
        Checks if __str__ has appropriate output
        """
        a = BaseModel()
        self.assertEqual(str(a), f"[BaseModel] ({a.id}) {a.__dict__}")

    def test_if_to_dict_returns_dict(self):
        """
        Checks if to_dict method returns a dict
        """
        a = BaseModel()
        self.assertTrue(type(a.to_dict()), dict)

    def test_if_key_class_is_in_dict(self):
        """Checks if the key __class__ is in o.to_dict"""
        a = BaseModel()
        self.assertIn('__class__', a.to_dict())

    def test_if_created_at_is_datetime_object(self):
        """Checks if created_at is a datetime obj """
        a = BaseModel()
        self.assertTrue(type(a.created_at), datetime)

    def test_if_updated_at_is_datetime_object(self):
        """Checks if updated_at is a datetime obj"""
        a = BaseModel()
        self.assertTrue(type(a.updated_at), datetime)

    def test_if_created_at_and_updated_at_is_same_initially(self):
        """Tests if created_at & updated_at attr have same values
        initially"""
        a = BaseModel()
        self.assertEqual(a.created_at, a.updated_at)

    def test_two_objects_created_at(self):
        """Compares the created_at time of two class instances"""
        a = BaseModel()
        sleep(0.2)
        b = BaseModel()
        self.assertLess(a.created_at, b.created_at)

    def test_if_save_method_updates_updated_at_attr(self):
        """Checks if calling save method updated the updated_at attr"""
        a = BaseModel()
        a.save()
        self.assertNotEqual(a.created_at, a.updated_at)
        self.assertGreater(a.updated_at.microsecond, a.created_at.microsecond)


if __name__ == "__main__":
    unittest.main()
