from mock import patch
from service import Service
import pytest
import random
from unittest import TestCase

class ServiceTest(TestCase):

    def setUp(self):
        self.service = Service()

    def bad_random_mock(self):
        return 10

    @patch.object(Service, 'bad_random', bad_random_mock)
    def test_divide(self):
        assert self.service.divide(2) == 5
        assert self.service.divide(-1) == -10

    def test_abs_plus(self):
        assert self.service.abs_plus(-9) == 10
        assert self.service.abs_plus(0) == 1
        assert self.service.abs_plus(1) == 2

    @patch.object(Service, 'bad_random', bad_random_mock)
    def test_complicated_function(self):
        res1, res2 = self.service.complicated_function(10)
        assert res1 == 1
        assert res2 == 0

        res1, res2 = self.service.complicated_function(-1)
        assert res1 == -10
        assert res2 == 0