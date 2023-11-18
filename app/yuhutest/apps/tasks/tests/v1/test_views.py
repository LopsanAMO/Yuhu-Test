from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from yuhutest.apps.tesks.models import Task
from yuhutest.apps.tasks.tests.factories import TaskFactory


class TestTaskListTestCase(TestCase):
    """
    Tests /tasks list operations.
    """

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('tasks_list')
        self.user = User.objects.create_user(
            username="foo2", email="user@foo.com", password="pass"
        )
        self.url_login = reverse("login")
        self.login_data = {"username": "foo2", "password": "pass"}
        login_resp = self.client.post(self.url_login, self.login_data, format="json")
        token = login_resp.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)
        self.task_data = TaskFactory.build(user=self.user)

    def test_get_request_to_tasks_list_succeeds(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('title'), self.task_data.title)



class TestTaskListTestCaso(TestCase):
    """
    Tests /tasks post operations.
    """

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('tasks')
        self.user = User.objects.create_user(
            username="foo2", email="user@foo.com", password="pass"
        )
        self.url_login = reverse("login")
        self.login_data = {"username": "foo2", "password": "pass"}
        login_resp = self.client.post(self.url_login, self.login_data, format="json")
        token = login_resp.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)
        self.task_data = TaskFactory.build(user=self.user)

    def test_get_request_to_tasks_succeeds(self):
        response = self.client.get(self.url, {'id': self.task_data.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('title'), self.task_data.title)

    def test_get_request_with_invalid_data_fails(self):
        response = self.client.get(self.url, {'id': 0})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_request_with_no_data_fails(self):
        response = self.client.get(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_request_with_no_credentials_fails(self):
        self.client.credentials()
        response = self.client.get(self.url, {'id': self.task_data.id})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        task = Task.objects.get(pk=response.data.get('id'))
        self.assertEqual(task.title, self.task_data.get('title'))
        self.assertEqual(task.description, self.task_data.get('description'))
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.due_date, self.task_data.get('due_date'))

    def test_post_request_with_no_credentials_fails(self):
        self.client.credentials()
        response = self.client.post(self.url, self.task_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_request_with_valid_data_succeeds(self):
        task = TaskFactory(user=self.user)
        task_data = TaskFactory.build(user=self.user)
        response = self.client.put(self.url, task_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task = Task.objects.get(pk=response.data.get('id'))
        self.assertEqual(task.title, task_data.get('title'))
        self.assertEqual(task.description, task_data.get('description'))
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.due_date, task_data.get('due_date'))

    def test_put_request_with_invalid_data_fails(self):
        response = self.client.put(self.url, {'id': 0})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_request_with_no_credentials_fails(self):
        self.client.credentials()
        response = self.client.put(self.url, self.task_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_request_with_valid_data_succeeds(self):
        task = TaskFactory(user=self.user)
        response = self.client.delete(self.url, {'id': task.id})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        task = Task.objects.filter(pk=task.id).first()
        self.assertIsNone(task)

    def test_delete_request_with_invalid_data_fails(self):
        response = self.client.delete(self.url, {'id': 0})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_request_with_no_credentials_fails(self):
        self.client.credentials()
        response = self.client.delete(self.url, {'id': 0})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
