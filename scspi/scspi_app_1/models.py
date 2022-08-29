from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date


# Create your models here.




class CustomUser(AbstractUser):
    user_type_choice = ((1,'Admin'),(2,'CoAdmin'),(3,'TechSupport'),(4,'ThirdPartyUsers'),(5,'ApiUsers'),(6,'MainAdmin'))
    user_type = models.CharField(max_length=30, default=6, choices=user_type_choice)




class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, default='', on_delete=models.PROTECT)
    permission_level = models.CharField(max_length=10, default='')
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class CoAdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, default='', on_delete=models.PROTECT)
    permission_level = models.CharField(max_length=10, default='')
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class TechSupportUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, default='', on_delete=models.PROTECT)
    permission_level = models.CharField(max_length=10, default='')
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class ThirdPartyUsersUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, default='', on_delete=models.PROTECT)
    permission_level = models.CharField(max_length=10, default='')
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class ApiUsersUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, default='', on_delete=models.PROTECT)
    permission_level = models.CharField(max_length=10, default='')
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class MainAdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, default='', on_delete=models.PROTECT)
    permission_level = models.CharField(max_length=10, default='')
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class EmailAuthToken(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(CustomUser, default='', on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


def question_image_location(self, filename, **kwargs):
    return f'question/image/{str(self.user.id)}/{date.today()}-{filename}'


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    question = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to=question_image_location, blank=True)
    tags = models.CharField(max_length=255, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


def answer_image_location(self, filename, **kwargs):
    return f'answer/image/{str(self.user.id)}/{date.today()}-{filename}'



class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, default='', on_delete=models.PROTECT)
    answer = models.TextField()
    image = models.ImageField(upload_to=answer_image_location, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=50, blank=False)
    tag_description = models.CharField(max_length=255, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()





@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    # sourcery skip: instance-method-first-arg-name
    if not created:
        return
    if instance.user_type==1:
        AdminUser.objects.create(admin=instance)
    if instance.user_type==2:
        CoAdminUser.objects.create(admin=instance)
    if instance.user_type==3:
        TechSupportUser.objects.create(admin=instance)
    if instance.user_type==4:
        ThirdPartyUsersUser.objects.create(admin=instance)
    if instance.user_type==5:
        ApiUsersUser.objects.create(admin=instance)
    if instance.user_type==6:
        MainAdminUser.objects.create(admin=instance)
       


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.adminuser.save()
    if instance.user_type==2:
        instance.coadminuser.save()
    if instance.user_type==3:
        instance.techsupportuser.save()
    if instance.user_type==4:
        instance.thirdpartyusersuser.save()
    if instance.user_type==5:
        instance.apiusersuser.save()
    if instance.user_type==6:
        instance.mainadminuser.save()
    












































