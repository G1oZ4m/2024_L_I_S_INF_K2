from hello_world.formater import plain_text_upper_case
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        imie = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(imie.isupper())
        self.assertTrue(msg.isupper())
