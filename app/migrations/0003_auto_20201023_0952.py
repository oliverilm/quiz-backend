# Generated by Django 3.1.2 on 2020-10-23 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201022_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswerinsession',
            name='question_answered',
        ),
        migrations.AddField(
            model_name='questionanswerinsession',
            name='answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.answeroption'),
            preserve_default=False,
        ),
    ]
