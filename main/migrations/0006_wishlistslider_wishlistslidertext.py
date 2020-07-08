# Generated by Django 3.0.2 on 2020-07-06 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_kidsdreamtext'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishListSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='wishlist/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishListSliderText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_list_slider_text', models.CharField(max_length=500)),
                ('wish_list_slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.WishListSlider')),
            ],
        ),
    ]
