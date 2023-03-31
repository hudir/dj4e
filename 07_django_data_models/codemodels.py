from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

# python3 manage.py makemigrations
# python3 manage.py migrate
u = User(name='kristen', email='hudir@123.com')
u.save()
print(u.id)

from django.db import connection
print(connection.queries)

User.objects.values()
User.objects.filter(email="hudir@123.com").values()

User.objects.filter(email="hudir@123.com").delete()
User.objects.values()

User.objects.filter(email="hudir@123.com").updata(name="chuck")
User.objects.values()

User.objects.values().order_by('email')
User.objects.values().order_by('-name')

