# Generated by Django 4.0 on 2021-12-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_tag_article_category_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
