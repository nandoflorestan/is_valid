from unittest import TestCase
import warnings

from is_valid import is_something, is_nothing, is_eq
from is_valid.utils import explain, Wrapper


class TestExplain(TestCase):

    def setUp(self):
        self.predicate = explain(1, 'valid', 'foo', 'bar')

    def test_explain_valid(self):
        with self.subTest('explain=True == explain=False'):
            self.assertEqual(
                self.predicate(1), self.predicate(1, explain=True).valid
            )
        with self.subTest('pred correct'):
            self.assertEqual(
                self.predicate(1, explain=True).dict(include_valid=True),
                {'valid': True, 'code': 'valid', 'message': 'foo'}
            )

    def test_explain_invalid(self):
        with self.subTest('explain=True == explain=False'):
            self.assertEqual(
                self.predicate(0), self.predicate(0, explain=True).valid
            )
        with self.subTest('pred correct'):
            self.assertEqual(
                self.predicate(0, explain=True).dict(include_valid=True),
                {'valid': False, 'code': 'not_valid', 'message': 'bar'}
            )


class TestWrapper(TestCase):

    def test_wrapper_predicate(self):
        wrapper = Wrapper()
        with self.assertRaises(AttributeError):
            wrapper(None)
        wrapper.wrap(is_something)
        self._test(wrapper, None, True)
        wrapper.wrap(is_nothing)
        self._test(wrapper, None, False)

    def test_wrapper_predicate_with_arg(self):
        wrapper = Wrapper(is_something)
        self._test(wrapper, None, True)
        wrapper.wrap(is_nothing)
        self._test(wrapper, None, False)

    def _test(self, predicate, value, expected):
        with self.subTest('explain=True == explain=False'):
            self.assertEqual(
                predicate(value),
                predicate.explain(value).valid
            )
        with self.subTest('pred correct'):
            self.assertEqual(predicate(value), expected)

    def test_warning_func(self):
        wrapper = Wrapper()
        with warnings.catch_warnings(record=True) as w:
            wrapper.func = is_eq(0)
        self.assertTrue(len(w) == 1)
        self.assertEqual(w[0].category, PendingDeprecationWarning)
        self._test(wrapper, 0, True)
        self._test(wrapper, 1, False)
        wrapper._value = 1
        self._test(wrapper, 0, False)
        self._test(wrapper, 1, True)
