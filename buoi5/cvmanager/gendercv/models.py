from django.db import models

# Create your models here.
class CV(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    title = models.TextField()
    honorrs = models.TextField()
    email = models.EmailField()
    github = models.URLField()
    phone = models.CharField(max_length=15)
    school = models.CharField(max_length=100)
    specialized = models.CharField(max_length=100)
    gpa = models.CharField(max_length=10)
    code = models.TextField()
    tech = models.TextField()
    image = models.ImageField(upload_to='cv_images/')  # Thêm trường để lưu trữ hình ảnh

    def __str__(self):
        return self.name