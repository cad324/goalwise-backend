from django.test import TestCase
from .models import Task, Status
from django.contrib.auth.models import User

class TaskModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            status='In progress',
            user=self.user,
            days_of_week='monday,wednesday,friday'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertEqual(self.task.status, 'In progress')
        self.assertEqual(self.task.user, self.user)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_status_choices(self):
        # Check if the status field only allows certain choices
        allowed_choices = [choice.value for choice in Status]
        self.assertEqual(self.task.status, Status.IN_PROGRESS.value)
        self.assertIn(Status.IN_PROGRESS.value, allowed_choices)
