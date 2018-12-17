# Generated by Django 2.1.2 on 2018-11-26 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seniordesign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(default='example@nyu.edu', max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('memberSince', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('university', models.CharField(max_length=30)),
                ('profilePic', models.ImageField(default='/home/SeniorDesign/NeedPath', upload_to='')),
                ('year_in_school', models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior')], default='Freshman', max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seniordesign.CustomUser')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
