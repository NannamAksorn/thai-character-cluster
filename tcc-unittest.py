import unittest
from tcc import TCC

class tcc_test(unittest.TestCase):
    def testSegment(self):
        self.assertCountEqual(TCC.segment('เจ้าเสือน้อยเหมือนแมว'), ['เจ้า', 'เสือ', 'น้', 'อ', 'ย', 'เหมือ' ,'น', 'แม', 'ว'])


if __name__ == "__main__":
    unittest.main()