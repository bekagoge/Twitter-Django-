# Generated by Django 4.0.2 on 2022-04-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_tweettitletag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweetDate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweetTitleTag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
