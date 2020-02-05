# Generated by Django 2.2.9 on 2020-02-05 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('Skilled', 'Skilled'), ('Unskilled', 'Unskilled')], max_length=10)),
                ('Descripton', models.CharField(max_length=500)),
                ('Assigned', models.BooleanField()),
                ('ApplyBy', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=200)),
                ('Username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryTags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfinder.Category')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfinder.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfinder.Category')),
                ('Job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfinder.Job')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='Characteristics',
            field=models.ManyToManyField(through='jobfinder.JobCategory', to='jobfinder.Category'),
        ),
        migrations.AddField(
            model_name='job',
            name='Poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfinder.Profile'),
        ),
        migrations.AddField(
            model_name='category',
            name='Characteristics',
            field=models.ManyToManyField(through='jobfinder.SkillSet', to='jobfinder.Profile'),
        ),
    ]