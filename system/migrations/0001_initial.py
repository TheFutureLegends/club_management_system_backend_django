# Generated by Django 3.1.7 on 2021-02-27 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('student_id', models.CharField(max_length=9)),
                ('role', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communication', models.IntegerField()),
                ('timeliness', models.IntegerField()),
                ('quality_of_work', models.IntegerField()),
                ('daily_communication', models.IntegerField()),
                ('helpful_teammate', models.IntegerField()),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='system.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.member')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to='system.Member'),
        ),
    ]
