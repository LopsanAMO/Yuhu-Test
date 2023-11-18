import uuid
import celery
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from yuhutest.apps.users.models import User


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)

    @property
    def email(self):
        return self.user.email


@receiver(post_save, sender=Task)
def create_task(sender, instance=None, created=False, **kwargs):
    celery.current_app.send_task('yuhutest.apps.tasks.tasks.task_email_notification', (
    instance.email, instance.title, instance.due_date, instance.description, "created" if created else "updated",
    settings.EMAIL_HOST_USER))
