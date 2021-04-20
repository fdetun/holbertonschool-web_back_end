#!/usr/bin/env python3
"""import unittest file"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """class testted nested"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """access_nested_map test"""
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ access_nested_map exception"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        err = error.exception
        self.assertEqual(err.args[0], path[len(path) - 1])


class TestGetJson(unittest.TestCase):
    """class TestGetJson unittest"""

    @parameterized.expand([("http://example.com",
                            {"payload": True}),
                           ("http://holberton.io",
                            {"payload": False}),
                           ])
    @patch('test_utils.get_json')
    def test_get_json(self, url, payload, mok):
        """ test_get_json methode"""
        mok.return_value = payload
        resp = get_json(url)
        self.assertEqual(resp, payload)
