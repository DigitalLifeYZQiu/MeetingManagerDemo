# Generated by Django 3.2 on 2021-07-21 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=20)),
                ('meet_name', models.CharField(max_length=20)),
                ('card_time', models.CharField(max_length=20)),
                ('card_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Card',
            },
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=20)),
                ('allow_num', models.PositiveIntegerField(verbose_name='允许人数')),
                ('statu', models.BooleanField()),
                ('meet_name', models.CharField(max_length=20)),
                ('operation', models.CharField(max_length=20)),
                ('president', models.CharField(max_length=20)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('sub_name', models.CharField(max_length=20)),
                ('meet_kind', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Conference',
            },
        ),
        migrations.CreateModel(
            name='Manage_rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=20)),
                ('room_statu', models.BooleanField()),
                ('allow_num', models.PositiveIntegerField(verbose_name='允许人数')),
                ('open_starttime', models.DateTimeField(null=True)),
                ('open_endtime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'Manage_rooms',
            },
        ),
        migrations.CreateModel(
            name='My_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=20)),
                ('allow_num', models.PositiveIntegerField(verbose_name='允许人数')),
                ('statu', models.BooleanField()),
                ('meet_name', models.CharField(max_length=20)),
                ('operation', models.CharField(max_length=20)),
                ('president', models.CharField(max_length=20)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('sub_name', models.CharField(max_length=20)),
                ('meet_kind', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'My_list',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('repassword', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]