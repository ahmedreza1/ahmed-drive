from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator
from django.core.exceptions import PermissionDenied

# The Folders Model.

class Folder(models.Model):
	name = models.CharField(max_length = 250)
	parent = models.ForeignKey('self', on_delete = CASCADE, null = True, blank = True )
	cr_date = models.DateTimeField(auto_now_add = True)
	created_by = models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)
	def __str__(self):
		return "%s" % self.name

# The FileShare Model (This model is used to build upload and download logic)

class Fileshare(models.Model):
	folder = models.ForeignKey(to=Folder, related_name='fildeshare', on_delete=CASCADE, null=True, blank=True)
	fileupload = models.FileField(null = True)
	uploaded_by = models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)
	def __str__(self):
		return "%s" % self.fileupload
