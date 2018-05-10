from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

class HomePageTest(TestCase):
    def test_use_home_template(self):
        self.assertTemplateUsed(
            self.client.get('/'),
            'home.html'
        )
