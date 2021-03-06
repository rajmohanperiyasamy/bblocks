# Generated by Django 2.2 on 2020-02-09 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bblocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belonging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(upload_to='bblocks/static/images/cars'),
        ),
        migrations.CreateModel(
            name='Borrowed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('returned', models.DateTimeField(blank=True, null=True)),
                ('to_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bblocks.Friend')),
                ('what', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bblocks.Belonging')),
            ],
        ),
    ]
