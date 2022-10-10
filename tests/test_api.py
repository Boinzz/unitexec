import json
import unittest
from urllib import response

from app import create_app, db
from app.models.model import User
from app.utils.jwt import encrypt_password
from flask import current_app, url_for


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()
        me = User(username="test", password=encrypt_password(str("test")), nickname="test", mobile="+86.123456789012", magic_number=0, url="https://baidu.com")
        db.session.add(me)
        db.session.commit()

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        self.app_context.pop()

    def test_login(self):
        """
        TODO: 使用错误的信息进行登录，检查返回值为失败
        """
        data = {"username": "test", "password": "asd"}

        response = current_app.test_client().patch(
            url_for("user.login"),
            json = data
        )
        json_data = json.loads(response.data)
        self.assertEqual(json_data['message'], 'not found')
        self.assertEqual(response.status_code, 500)

        """
        TODO: 使用正确的信息进行登录，检查返回值为成功
        """
        data = {'username':'test', 'password':'test'}
        response = current_app.test_client().patch(
            url_for("user.login"),
            json = data
        )
        json_data = json.loads(response.data)
        self.assertEqual(json_data['username'], 'test')
        self.assertEqual(response.status_code, 200)
        
        """
        TODO: 进行登出，检查返回值为成功
        """
        response = current_app.test_client().patch(
            url_for("user.warperlogout"),
            headers = {"Authorization": json_data['jwt']}  
        )

        json_data = json.loads(response.data)
        self.assertEqual(json_data['message'],'ok')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        """
        Example: 使用错误信息进行注册，检查返回值为失败
        """
        data = {"username":"123", "password": "21321"}

        response = current_app.test_client().post(
            url_for('user.register_user'),
            json=data
        )
        json_data = json.loads(response.data)
        self.assertEqual(json_data['message'], "invalid arguments: error: username")
        self.assertEqual(response.status_code, 400)

        """
        TODO: 使用正确的信息进行注册，检查返回值为成功
        TODO: 使用正确注册信息进行登录，检查返回值为成功
        """
        data = {"username":"user12345", "password":"Boinzz_12345", "nickname":"fish", "url":"https://www.boinzz.com", "mobile":"+65.651234562102", "magic_number":"13"}

        response = current_app.test_client().post(
            url_for('user.register_user'),
            json = data
        )
        json_data = json.loads(response.data)
        self.assertEqual(json_data['message'], "ok")
        self.assertEqual(response.status_code, 200)
        
        response = current_app.test_client().patch(
            url_for("user.login"),
            json = data
        )
        json_data = json.loads(response.data)
        self.assertEqual(json_data["username"], data["username"])
        self.assertEqual(json_data["nickname"], data["nickname"])
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """
        TODO: 未登录直接登出
        """
        response = current_app.test_client().patch(
            url_for("user.warperlogout")
        )

        json_data = json.loads(response.data)
        self.assertEqual(json_data['message'],'User must be authorized.')
        self.assertEqual(response.status_code, 401)
        
if __name__ == '__main__':
    unittest.main()
