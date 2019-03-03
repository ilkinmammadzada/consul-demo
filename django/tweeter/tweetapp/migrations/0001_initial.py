# Generated by Django 2.1.7 on 2019-02-28 17:25

from django.db import migrations, models
import djongo.models.fields
import tweetapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', djongo.models.fields.EmbeddedModelField(model_container=tweetapp.models.Blog, null=True)),
                ('headline', models.CharField(max_length=255)),
            ],
        ),
    ]