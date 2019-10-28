# Generated by Django 2.2.4 on 2019-08-19 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_auto_20190710_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='category+', to='wiki.Article'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='member_articles',
            field=models.ManyToManyField(blank=True, related_name='_articlecategory_member_articles_+', related_query_name='categories+', to='wiki.Article'),
        ),
        migrations.AlterField(
            model_name='categoryrelation',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type+', to='contenttypes.ContentType', verbose_name='content type'),
        ),
    ]
