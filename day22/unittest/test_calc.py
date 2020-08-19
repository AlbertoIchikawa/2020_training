#１．ファイル名は「test_対象のモジュール名.py」
import unittest
from unittest import calc


# ２．テストクラス名は「Testテスト対象のクラス名」
# ３．テストクラスはunittest.TestCaseを継承する
class TestCalc(unittest.TestCase):

    #４．テストメソッド名は「test_テスト対象のメソッド名」
    def test_add_num(self):
        self.assertEqual(10, calc.add_num(6, 4))

    def test_sub_num(self):
        self.assertEqual(2, calc.sub_num(6, 4))

    def test_mul_num(self):
        self.assertEqual(24, calc.mul_num(6, 4))

    def test_div_num(self):
        self.assertEqual(1.5, calc.div_num(6, 4))
