from .models import *
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Sum, Q, F

# Create your views here.
def animal(request):
    return render(request,'main/animal.html')
def movie(request):
    return render(request,'main/movie.html')
def game(request):
    return render(request,'main/game.html')
def sport(request):
    return render(request,'main/sport.html')
def food(request):
    return render(request,'main/food.html')
def detail(request):
    return render(request,'main/detail.html')

from .models import TbChannelInfo

def animal(request):
    channels1 = TbChannelInfo.objects.filter(category='ANIMAL').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='ANIMAL').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'channel_names1': [channel.channel_name for channel in channels1],
        'channel_names2': [channel.channel_name for channel in channels2]
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channel_names = TbChannelInfo.objects.filter(category='ANIMAL', channel_id__in=[channel['channel'] for channel in channels]).values_list('channel_name', flat=True)

    context['channel_names3'] = channel_names

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4].values('video_title', 'video_thumbnail', 'video_url')
    context['hot_videos'] = hot_videos

    return render(request, 'main/animal.html', context)

def movie(request):
    channels1 = TbChannelInfo.objects.filter(category='MOVIE').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='MOVIE').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'channel_names1': [channel.channel_name for channel in channels1],
        'channel_names2': [channel.channel_name for channel in channels2]
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channel_names = TbChannelInfo.objects.filter(category='MOVIE', channel_id__in=[channel['channel'] for channel in channels]).values_list('channel_name', flat=True)
    
    context['channel_names3'] = channel_names

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4].values('video_title', 'video_thumbnail', 'video_url')
    context['hot_videos'] = hot_videos

    return render(request, 'main/movie.html', context)
def game(request):
    channels1 = TbChannelInfo.objects.filter(category='GAME').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='GAME').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'channel_names1': [channel.channel_name for channel in channels1],
        'channel_names2': [channel.channel_name for channel in channels2]
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channel_names = TbChannelInfo.objects.filter(category='GAME', channel_id__in=[channel['channel'] for channel in channels]).values_list('channel_name', flat=True)
    
    context['channel_names3'] = channel_names

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4].values('video_title', 'video_thumbnail', 'video_url')
    context['hot_videos'] = hot_videos
    
    return render(request, 'main/game.html', context)
def sport(request):
    channels1 = TbChannelInfo.objects.filter(category='SPORTS').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='SPORTS').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'channel_names1': [channel.channel_name for channel in channels1],
        'channel_names2': [channel.channel_name for channel in channels2]
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channel_names = TbChannelInfo.objects.filter(category='SPORTS', channel_id__in=[channel['channel'] for channel in channels]).values_list('channel_name', flat=True)
    
    context['channel_names3'] = channel_names

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4].values('video_title', 'video_thumbnail', 'video_url')
    context['hot_videos'] = hot_videos
    
    return render(request, 'main/sport.html', context)
def food(request):
    channels1 = TbChannelInfo.objects.filter(category='MUKBANG').order_by('-subscribers_count')[:5]
    channels2 = TbChannelInfo.objects.filter(category='MUKBANG').order_by('-total_view')[:5]

    # 채널 이름을 리스트에 저장하여 템플릿으로 전달
    context = {
        'channel_names1': [channel.channel_name for channel in channels1],
        'channel_names2': [channel.channel_name for channel in channels2]
    }

    channels = TbVideoInfo.objects.values('channel').annotate(total_likes=Sum('like_count')).order_by('-total_likes')
    channel_names = TbChannelInfo.objects.filter(category='MUKBANG', channel_id__in=[channel['channel'] for channel in channels]).values_list('channel_name', flat=True)
    
    context['channel_names3'] = channel_names

    hot = [channel.channel_id for channel in channels1]
    hot_videos = TbVideoInfo.objects.filter(channel__in=hot).order_by('-view_count')[:4].values('video_title', 'video_thumbnail', 'video_url')
    context['hot_videos'] = hot_videos
    
    return render(request, 'main/food.html', context)
