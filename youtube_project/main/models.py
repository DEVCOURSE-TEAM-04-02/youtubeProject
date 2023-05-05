from django.db import models

# Create your models here.
class TbChannelInfo(models.Model):
    category = models.CharField(max_length=255)
    channel_id = models.CharField(primary_key=True, max_length=255)
    channel_name = models.CharField(max_length=255)
    channel_logo = models.TextField(blank=True, null=True)
    subscribers_count = models.BigIntegerField()
    videos_count = models.IntegerField()
    total_view = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'TB_CHANNEL_INFO'


class TbCommentInfo(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=255)
    video = models.ForeignKey('TbVideoInfo', models.DO_NOTHING)
    content = models.TextField()
    like_count = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'TB_COMMENT_INFO'


class TbVideoInfo(models.Model):
    video_id = models.CharField(primary_key=True, max_length=255)
    channel = models.ForeignKey(TbChannelInfo, models.DO_NOTHING)
    video_title = models.CharField(max_length=255)
    video_thumbnail = models.TextField()
    video_url = models.TextField()
    uploaded_date = models.DateTimeField()
    view_count = models.BigIntegerField()
    like_count = models.BigIntegerField()
    comment_count = models.IntegerField()
    hashtag = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'TB_VIDEO_INFO'