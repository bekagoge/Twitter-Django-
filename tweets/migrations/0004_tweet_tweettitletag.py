# Generated by Django 4.0.2 on 2022-04-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_alter_tweet_tweetauthor_alter_tweet_tweettext_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweetTitleTag',
            field=models.CharField(blank=True, default='Twitter!', max_length=255, null=True),
        ),
    ]