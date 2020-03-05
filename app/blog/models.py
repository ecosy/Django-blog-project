from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )
class User(models.Model):
    user_id = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    subscription_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    contents = models.CharField(max_length=3000)

    def __str__(self):
        return self.user_id

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    contents = models.CharField(max_length=3000)

    def __str__(self):
        return self.post_id
#
# class MyUserManager(BaseUserManager):
#     def create_user(self, user_id, password, name, description=None, subscription=None):
#         if not user_id:
#             raise ValueError('You must have an user id.')
#         user = self.model(
#             user_id=user_id,
#             name=name,
#             description=description,
#             subscription=subscription
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
# class MyUser(AbstractBaseUser):
#     user_id = models.CharField(max_length=10)
#     password = models.CharField(max_length=20)
#     name = models.CharField(max_length=20)
#     description = models.CharField(max_length=300)
#     subscription_time = models.DateTimeField(auto_now=True)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'user_id'
#     REQUIRED_FIELDS = ['user_id', 'password', 'name']
#
#     def __str__(self):
#         return self.user_id
#
#     # def has_perm(self, perm, obj=None):
#     #     "Does the user have a specific permission?"
#     #     return True
#     # def has_module_perms(self, app_label):
#     #     "Does the user have permissions to view the app 'app_label'?"
#     #     return True
#     # @property
#     # def is_staff(self):
#     #     "Is the user a member of staff?"
#     #     return self/