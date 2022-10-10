import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''
    def test_register_params_check(self):
        dic = {}
        self.assertEqual(register_params_check(dic), ("username", False))
        dic['username'] = 'user'
        self.assertEqual(register_params_check(dic), ("error: username", False))
        dic['username'] = 'user12'
        self.assertEqual(register_params_check(dic), ("password", False))
        dic['password'] = 'asSD'
        self.assertEqual(register_params_check(dic), ("error: password", False))
        dic['password'] = 'Aa525__ass'
        self.assertEqual(register_params_check(dic), ("nickname", False))
        dic['nickname'] = 'boin'
        self.assertEqual(register_params_check(dic), ("url", False))
        dic['url'] = 'boinzz.com.123'
        self.assertEqual(register_params_check(dic), ("error: url", False))
        dic['url'] = 'https://www.baidu.123.com'
        self.assertEqual(register_params_check(dic), ("mobile", False))
        dic['mobile'] = '+285.9456546'
        self.assertEqual(register_params_check(dic), ("error: mobile", False))
        dic['mobile'] = '+25.654123456879'
        self.assertEqual(register_params_check(dic), ("magic_number", False))
        dic['magic_number'] = '-1'
        self.assertEqual(register_params_check(dic), ("error: magic_number", False))
        dic['magic_number'] = '1'
        self.assertEqual(register_params_check(dic), ("ck", True))

if __name__ == '__main__':
    unittest.main()
