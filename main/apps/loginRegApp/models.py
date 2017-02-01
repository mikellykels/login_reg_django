from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, **kwargs):
        errors = []

        if len(kwargs['email']) < 1:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(kwargs['email']):
            errors.append("Invalid Email")

        if len(kwargs['first_name']) < 2 or len(kwargs['last_name']) < 2:
            errors.append("Please include a first and/or last name longer than two characters.")

        if len(kwargs['password']) < 1:
            errors.append("Must enter a password")
        if len(kwargs['password']) < 8:
            errors.append("Password must be more than 8 characters")
        if kwargs['password'] != kwargs['confirm_pw']:
            errors.append("Password does not match")
        else:
            pw_hash = bcrypt.hashpw(kwargs['password'].encode(), bcrypt.gensalt())

        if len(errors) is not 0:
            return (False, errors)

        else:
            user = User.UserManager.create(first_name=kwargs['first_name'], last_name=kwargs['last_name'], email=kwargs['email'], pw_hash=pw_hash )
            user.save()
            return (True, user)

    def validateLogin(self, request):
        try:
            user = User.UserManager.get(email=request.POST['email'])
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode()):
                return (True, user)

        except ObjectDoesNotExist:
            pass
        return (False, ["Email/password don't match."])

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pw_hash = models.CharField(max_length=255)

    UserManager = UserManager()
