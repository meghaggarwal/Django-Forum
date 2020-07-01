from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, board_topics, new_topic
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
# Create your tests here.

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Python', description='Python is the new job')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_home_url_resolve_home_views(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topic_page(self):
        url = reverse('board_topics', kwargs={'pk':1})
        self.assertContains(self.response, 'href="{}"'.format(url))


class BoardTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Python', description='Python is the new job!!')
        url = reverse('board_topics' , kwargs={'pk':1})
        self.response = self.client.get(url)

    def test_board_topics_view_success_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_board_topics_not_found_status_code(self):
        url = reverse('board_topics' , kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)
    
    def test_board_topics_contains_navigation_link(self):
        new_topic_url = reverse('new_topic' , kwargs={'pk':1})
        home_page_url = reverse('home')
        self.assertContains(self.response, 'href="{}"'.format(new_topic_url))
        self.assertContains(self.response, 'href="{}"'.format(home_page_url))
        

class NewTopicTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django is the coolest frame")
        self.user = User.objects.create(username='xyz', email='xyz@company.com', password='123')
        url = reverse('new_topic', kwargs={'pk':1})
        self.response = self.client.get(url)

    def test_new_topic_view_success_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk':100})
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 404)

    def test_new_topics_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func , new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        board_topic_url = reverse('board_topics', kwargs={'pk':1})
        self.assertContains(self.response, 'href="{}"'.format(board_topic_url))

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)

    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'pk':1})
        data =  {
            'subject': 'testing',
            'message': 'testing via test.py'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())


    def test_new_topic_invalid_post_data(self):
        url = reverse('new_topic', kwargs={'pk':1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
    
    def test_new_topic_empty_post_data(self):
        url = reverse('new_topic', kwargs={'pk':1})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())
        self.assertEquals(response.status_code, 200)







