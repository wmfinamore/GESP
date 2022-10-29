from django.contrib.auth.models import AbstractUser
# from django.db import models
from apps.core.models import Auditoria


# Atributos customizados devem ser adicionados aqui
class CustomUser(AbstractUser, Auditoria):
    pass
