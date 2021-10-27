import string_ops


class TestStringOps:
    def test_remove_vowels(self):
        assert 'Jkm' == string_ops.remove_vowels('Joakim')

    def test_reversed_string(self):
        assert 'mikaoJ' == string_ops.reversed_string('Joakim')