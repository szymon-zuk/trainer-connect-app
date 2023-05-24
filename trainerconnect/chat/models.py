from django.db import models


class Message(models.Model):
    """Model that represents a single message in a thread"""
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:30]
    
class Thread(models.Model):
    """A thread between 2 people - a trainer and his trainee"""
    name = models.CharField(max_length=64)
    trainer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='szymon')
    trainee_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.thread_name