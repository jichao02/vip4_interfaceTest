#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/29 0029  16:01
#Author:chao
import myfun
import unittest
class testMyfun(unittest.TestCase):
    def test_divide(self):
        result = myfun.divide(2, 1)
        self.assertEqual(1,result)

if __name__ == '__main__':
    unittest.main()


