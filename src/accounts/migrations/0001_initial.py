# Generated by Django 3.2.6 on 2021-09-08 10:15

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=80, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=80, null=True, verbose_name='نام خانوادگي ')),
                ('username', models.CharField(max_length=60, unique=True, verbose_name='نام كاربري')),
                ('password', models.CharField(max_length=20, verbose_name='پسورد')),
                ('password_rep', models.CharField(max_length=20, verbose_name='تكرار پسورد')),
                ('device', models.CharField(blank=True, max_length=200, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'كاربر',
                'verbose_name_plural': 'كاربران',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'verbose_name': ' كاربر سايت',
                'verbose_name_plural': 'كاربران  سايت ',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Owner_site',
            fields=[
            ],
            options={
                'verbose_name': ' مالك سايت',
                'verbose_name_plural': 'مالكان سايت ',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
            ],
            options={
                'verbose_name': ' كارمند',
                'verbose_name_plural': 'كارمندان ',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200, verbose_name='شهر ')),
                ('street', models.CharField(max_length=200, verbose_name=' خيابان')),
                ('postal_code', models.CharField(max_length=16, verbose_name='كدپستي')),
                ('address_line1', models.CharField(max_length=100, verbose_name='ادرس اول')),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True, verbose_name='ادرس دوم')),
                ('status', models.BooleanField(default=False, verbose_name='وضعيت ')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها ',
            },
        ),
    ]
