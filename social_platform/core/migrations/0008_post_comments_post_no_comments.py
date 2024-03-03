# Generated by Django 4.2.6 on 2024-02-13 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_postcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='core.postcomment'),
        ),
        migrations.AddField(
            model_name='post',
            name='no_comments',
            field=models.IntegerField(default=0),
        ),
    ]