# -*- coding: utf-8 -*-
import hashlib
from django.contrib.auth.models import User

class MyBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except Exception:
            print 'no user'
        if password == user.password:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except Exception:
            return None