from .models import *
from django.db import connection
from django.conf import settings
from django.shortcuts import render, get_object_or_404
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
from django.db.models import Sum
import io

# Create your views here.

def animal(request):
    channels1 = TbChannelInfo.objects.filter(category='ANIMAL').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='ANIMAL').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'sort_subscribers_channels': channels1,
        'sort_viewCount_channels': channels2
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channels3 = TbChannelInfo.objects.filter(category='ANIMAL', channel_id__in=[channel['channel'] for channel in channels])[:5]

    context['sort_like_channels'] = channels3

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4]
    context['hot_videos'] = hot_videos

    return render(request, 'main/animal.html', context)

def movie(request):
    channels1 = TbChannelInfo.objects.filter(category='MOVIE').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='MOVIE').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'sort_subscribers_channels': channels1,
        'sort_viewCount_channels': channels2
    }
    
    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channels3 = TbChannelInfo.objects.filter(category='MOVIE', channel_id__in=[channel['channel'] for channel in channels])[:5]

    context['sort_like_channels'] = channels3

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4]
    context['hot_videos'] = hot_videos

    return render(request, 'main/movie.html', context)
def game(request):
    channels1 = TbChannelInfo.objects.filter(category='GAME').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='GAME').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'sort_subscribers_channels': channels1,
        'sort_viewCount_channels': channels2
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channels3 = TbChannelInfo.objects.filter(category='GAME', channel_id__in=[channel['channel'] for channel in channels])[:5]

    context['sort_like_channels'] = channels3

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4]
    context['hot_videos'] = hot_videos
    
    return render(request, 'main/game.html', context)

def sport(request):
    channels1 = TbChannelInfo.objects.filter(category='SPORTS').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='SPORTS').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'sort_subscribers_channels': channels1,
        'sort_viewCount_channels': channels2
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channels3 = TbChannelInfo.objects.filter(category='SPORTS', channel_id__in=[channel['channel'] for channel in channels])[:5]

    context['sort_like_channels'] = channels3

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4]
    context['hot_videos'] = hot_videos
    
    return render(request, 'main/sport.html', context)

def food(request):
    channels1 = TbChannelInfo.objects.filter(category='MUKBANG').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='MUKBANG').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'sort_subscribers_channels': channels1,
        'sort_viewCount_channels': channels2
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channels3 = TbChannelInfo.objects.filter(category='MUKBANG', channel_id__in=[channel['channel'] for channel in channels])[:5]

    context['sort_like_channels'] = channels3

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4]
    context['hot_videos'] = hot_videos
    
    return render(request, 'main/food.html', context)

def detail(request, channel_id):
    #채널ID를 통해 가지고 온 채널 정보
    channel_info = get_object_or_404(TbChannelInfo, pk=channel_id)
    #채널ID를 통해 가지고 와 조회한 비디오 중 코멘트 좋아요 수가 높은 것 세 개
    top_comments = TbCommentInfo.objects.filter(video__channel=channel_info).order_by('-like_count')[:3]
    #채널ID를 통해 조회한 비디오 중 조회 수가 높은 것 네 개
    top_videos = TbVideoInfo.objects.filter(channel_id=channel_id).order_by('-view_count')[:4]
    
    #일별 그래프 경로
    graph_day_path = 'img/graph/{}_VIDEO_GRAPH_DATE.png'.format(channel_id)
    #주별 그래프 경로
    graph_week_path = 'img/graph/{}_VIDEO_GRAPH_WEEK.png'.format(channel_id)
    #월별 그래프 경로
    graph_month_path = 'img/graph/{}_VIDEO_GRAPH_MONTH.png'.format(channel_id)
    
    #wordcloud 생성 (각 채널의 영상 키워드)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT video_title
            FROM TB_VIDEO_INFO
            WHERE channel_id = %s
        """, [channel_id])
        query_result1 = cursor.fetchall()
    
    with connection.cursor() as cursor:
        cursor.execute(""" 
            SELECT cmt.content
            FROM TB_VIDEO_INFO as v
            INNER JOIN TB_COMMENT_INFO as cmt ON v.video_id = cmt.video_id
            WHERE v.channel_id = %s
            ORDER BY cmt.LIKE_COUNT DESC
            LIMIT 100
        """, [channel_id])   
        query_result2 = cursor.fetchall()
        
    title_wordcloud_path = get_wordCloud(query_result1, channel_id, "t")
    comment_wordcloud_path =  get_wordCloud(query_result2, channel_id, "c")
    
    context = {'channel_info': channel_info, 'top_comments': top_comments, 'top_videos': top_videos, 'title_wordcloud_path':title_wordcloud_path, 'comment_wordcloud_path':comment_wordcloud_path, 'graph_day_path': graph_day_path, 'graph_week_path': graph_week_path, 'graph_month_path': graph_month_path}
    return render(request, 'main/detail.html', context)

def get_wordCloud(tuples, channel_id, saveMode):
    """
    Make WordCloud
    여러개의 문자열로 이루어진 튜플을 인자로 받는다.
    만들어진 img를 리턴한다.
    """
    # 하나의 문자열로 만들어주는 작업 / 튜플안에서 튜플꺼내기
    longStr = ''.join([text for tuple in tuples for text in tuple])
    # 형태소 분석 및 카운터 - 한글만
    okt = Okt()
    nouns = okt.nouns(longStr)
    counter = Counter(nouns)
    font_path = 'main/static/css/Jua/Jua-Regular.ttf'
    wordcloud = WordCloud(
        font_path = font_path,
        width=800,
        height=600,
        max_words=80,
        prefer_horizontal=1,
        max_font_size=250,
        background_color='white',
    )
    img = wordcloud.generate_from_frequencies(counter)
    # 이미지 저장
    # img_path = os.path.join(settings.BASE_DIR, 'wordcloud', f'{channel_id}_TITLE_WORDCLOUD.png')
    if saveMode == "c":
        img_path = f"main/static/img/wordcloud/{channel_id}_COMMENT_WORDCLOUD.png"
    else:
        img_path = f"main/static/img/wordcloud/{channel_id}_TITLE_WORDCLOUD.png"
        
    # use BytesIO to generate image
    img_bytes = io.BytesIO()
    plt.figure(figsize=(8,6))
    plt.axis('off')
    plt.imshow(img)
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    # write the image to the disk
    with open(img_path, 'wb') as f:
        f.write(img_bytes.read())
    return img_path