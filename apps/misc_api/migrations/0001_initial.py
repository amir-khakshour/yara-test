# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.misc_api.utils
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPurchaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateTimeField(max_length=255)),
                ('purchase', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(2)], default=None)),
                ('purchase_id', models.IntegerField()),
                ('name', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(2)], default=None)),
                ('phone_number', models.CharField(max_length=20, validators=[apps.misc_api.utils.PhoneValidator, django.core.validators.MinLengthValidator(10)], default=None)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
