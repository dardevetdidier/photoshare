# Generated by Django 4.0.1 on 2022-01-11 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='photo',
            name='add_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photos.category'),
        ),
    ]