import string_ops


class TestStringOps:
    def test_remove_vowels(self):
        assert 'Jkm' == string_ops.remove_vowels('Joakim')

    def test_reversed_string(self):
        assert 'mikaoJ' == string_ops.reversed_string('Joakim')

    def test_translate_to_robber(self):
        assert string_ops.translate_to_robber('this is fun') == 'tothohisos isos fofunon'