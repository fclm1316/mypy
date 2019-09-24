from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
import unittest
# Create your tests here.
# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1+1,3)
# @unittest.skip("跳过")
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        #内部函数,用于解析url，并将其映射到相应的视图函数上。
        #检查解析网站根路径“/”时，是否能到到名为home_page的函数
        found = resolve("/")
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        #模拟发送一个http请求
        # request = HttpRequest()
        #将请求丢给视图，等到返回结果
        # response = home_page(request)
        #转码
        # html = response.content.decode('utf-8')
       # # self.assertTrue(html.strip().startswith('<html>'))
       # # self.assertIn('<title>To-Do lists</title>',html)
       # # self.assertTrue(html.strip().endswith('</html>'))
        # expected_html = render_to_string('home.html')
        # self.assertEqual(html,expected_html)
        # 不再手动创建httprequest,也不再直接调用视图函数，而是调用客户端
        response = self.client.get('/')
        html = response.content.decode('utf8')
        # print(html)
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response,'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item',response.content.decode())
