import unittest

from ..util.SOMA.links import Create


class Test_Create(unittest.TestCase):
    def setUp(self) -> None:
        self.link_base = Create().date_context()

    def test_summary(self) -> None:
        expected = self.link_base + "&query=summary&format=json"
        result = Create().summary()
        self.assertEqual(expected, result)

    def test_holdings(self) -> None:
        types = ["bills", "agency debts", ["cmbs", "tips", "notesbonds"]]
        for _type in types:
            if isinstance(_type, str):
                expected = f"{self.link_base}&query=details&holdingTypes={_type}&format=json"
                result = Create().holdings(str(_type))
            else:
                _types = ','.join(_type)
                expected = f"{self.link_base}&query=details&holdingTypes={_types}&format=json"
                result = Create().holdings(list(_type))
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
