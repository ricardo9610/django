# Generated by Django 4.1.3 on 2022-11-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('nivel', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField(verbose_name='fecha de modificacion')),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
