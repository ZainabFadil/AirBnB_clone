#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
import unittest
from models.base_model import BaseModel



class testBaseModel(unittest.TestCase):
    def testInit(self):
        parentClass = BaseModel()

        self.assertIsNotNone(parentClass.id)
        self.assertIsNotNone(parentClass.created_at)
        self.assertIsNotNone(parentClass.updated_at)


    def testsave(self):
        parentClass = BaseModel()

        old = parentClass.updated_at

        new = parentClass.save()

        self.assertNotEqual(old, new)


    def test_to_dict(self):
        """
        Test for to_dict method
        """
        parentClass = BaseModel()

        temp = parentClass.to_dict()
        
        self.assertIsInstance(temp, dict)

        self.assertEqual(temp["__class__"], "BaseModel")
        self.assertEqual(temp["id"], parentClass.id)
        self.assertEqual(temp["created_at"], parentClass.created_at.isoformat())
        self.assertEqual(temp["updated_at"], parentClass.updated_at.isoformat())


    def test_str(self):
        parentClass = BaseModel()

        self.assertTrue(str(parentClass).startswith("[BaseModel]"))
        self.assertIn(parentClass.id, str(parentClass))
        self.assertIn(str(parentClass.__dict__), str(parentClass))

if __name__ == "__main__":
    unittest.main()