# Generated by Django 4.2.2 on 2023-06-29 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('transferer_name', models.CharField(max_length=200)),
                ('receiver', models.CharField(max_length=250)),
                ('receiver_acct', models.CharField(max_length=12)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remark', models.CharField(max_length=100, null=True)),
                ('alert_type', models.CharField(max_length=50)),
                ('time_processed', models.DateTimeField(auto_now_add=True)),
                ('transferer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
