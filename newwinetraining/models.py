from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __repr__(self):
        return f'<{self.__class__.__name__} pk={self.pk}>'