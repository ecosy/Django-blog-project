# Generated by Django 3.0.3 on 2020-03-04 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('subscription_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('contents', models.CharField(max_length=3000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('contents', models.CharField(max_length=3000)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
    ]
