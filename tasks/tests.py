from django.test import TestCase
from .models import Day, Task, Status
from users.models import CustomUser as User

class TaskModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpassword')

        self.task = Task.objects.create(
            title='Test Task',
            user=self.user,
        )
        monday = Day.objects.get(id=2)
        wednesday = Day.objects.get(id=4)
        friday = Day.objects.get(id=6)
        self.task.days_of_week.set([monday, wednesday, friday])

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.user, self.user)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_status_choices(self):
        # Check if the status field only allows certain choices
        allowed_choices = [choice.value for choice in Status]
        self.assertIn(Status.IN_PROGRESS.value, allowed_choices)
