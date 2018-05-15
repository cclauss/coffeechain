from django.db import models
from django.db.models import fields, ForeignKey, CASCADE


# Create your models here.
class RequestLog(models.Model):
    url = fields.CharField(max_length=128)
    type = fields.CharField(max_length=128)
    action = fields.CharField(max_length=128)
    content = fields.TextField()
    batch = ForeignKey(to="ChainBatch", null=True, blank=True, on_delete=CASCADE)
    created_at = fields.DateTimeField(auto_now_add=True)


class ChainObject(models.Model):
    key = fields.CharField(max_length=128)
    type = fields.CharField(max_length=32)
    address = fields.CharField(max_length=70)
    batch = ForeignKey(to="ChainBatch", null=False, blank=False, on_delete=CASCADE)
    created_at = fields.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('key', 'type')


class ChainBatch(models.Model):
    batch_id = fields.CharField(max_length=128)
    status = fields.CharField()
    updated_at = fields.DateTimeField(auto_now=True)
    created_at = fields.DateTimeField(auto_now_add=True)
