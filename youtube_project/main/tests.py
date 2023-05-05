from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import TbChannelInfo, TbCommentInfo, TbVideoInfo

#동물 테스트 케이스 (나머지 카테고리들은 동일하므로 하나에서 두 개까지의 카테고리만 테스트 케이스를 만들고 상세 케이스에 대한 테스트 케이스를 만든다)
class AnimalViewTestCase(TestCase):
    def setUp(self):
        # 테스트에 사용될 데이터 생성
        self.channel1 = TbChannelInfo.objects.create(
            channel_id='channel1',
            channel_name='Channel 1',
            category='ANIMAL',
            subscribers_count=100,
            total_view=1000
        )
        self.channel2 = TbChannelInfo.objects.create(
            channel_id='channel2',
            channel_name='Channel 2',
            category='ANIMAL',
            subscribers_count=200,
            total_view=2000
        )
        self.video1 = TbVideoInfo.objects.create(
            video_id='video1',
            video_title='Video 1',
            channel=self.channel1,
            view_count=500,
            like_count=100
        )
        self.video2 = TbVideoInfo.objects.create(
            video_id='video2',
            video_title='Video 2',
            channel=self.channel2,
            view_count=1000,
            like_count=200
        )
    
    def test_animal_view(self):
        # Client 객체를 생성하여 URL 호출 및 반환값 검증
        client = Client()
        url = reverse('animal')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/animal.html')
        
        # 검증할 데이터 설정
        sort_subscribers_channels = response.context['sort_subscribers_channels']
        sort_viewCount_channels = response.context['sort_viewCount_channels']
        sort_like_channels = response.context['sort_like_channels']
        hot_videos = response.context['hot_videos']
        
        # 각 데이터를 검증
        self.assertEqual(len(sort_subscribers_channels), 2)
        self.assertIn(self.channel1, sort_subscribers_channels)
        self.assertIn(self.channel2, sort_subscribers_channels)
        
        self.assertEqual(len(sort_viewCount_channels), 2)
        self.assertIn(self.channel2, sort_viewCount_channels)
        self.assertIn(self.channel1, sort_viewCount_channels)
        
        self.assertEqual(len(sort_like_channels), 2)
        self.assertIn(self.channel1, sort_like_channels)
        self.assertIn(self.channel2, sort_like_channels)
        
        self.assertEqual(len(hot_videos), 1)
        self.assertIn(self.video2, hot_videos)
        
#영화 테스트 케이스         
class MovieViewTestCase(TestCase):
    def setUp(self):
        self.channel1 = TbChannelInfo.objects.create(
            channel_id='channel1',
            channel_name='Channel 1',
            category='MOVIE',
            subscribers_count=100,
            total_view=1000
        )
        self.channel2 = TbChannelInfo.objects.create(
            channel_id='channel2',
            channel_name='Channel 2',
            category='MOVIE',
            subscribers_count=200,
            total_view=2000
        )
        self.video1 = TbVideoInfo.objects.create(
            video_id='video1',
            video_title='Video 1',
            channel=self.channel1,
            view_count=500,
            like_count=100
        )
        self.video2 = TbVideoInfo.objects.create(
            video_id='video2',
            video_title='Video 2',
            channel=self.channel2,
            view_count=1000,
            like_count=200
        )

    def test_movie_view(self):
        client = Client()
        url = reverse('movie')
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/movie.html')

        sort_subscribers_channels = response.context['sort_subscribers_channels']
        sort_viewCount_channels = response.context['sort_viewCount_channels']
        sort_like_channels = response.context['sort_like_channels']
        hot_videos = response.context['hot_videos']

        self.assertEqual(len(sort_subscribers_channels), 2)
        self.assertIn(self.channel1, sort_subscribers_channels)
        self.assertIn(self.channel2, sort_subscribers_channels)

        self.assertEqual(len(sort_viewCount_channels), 2)
        self.assertIn(self.channel2, sort_viewCount_channels)
        self.assertIn(self.channel1, sort_viewCount_channels)

        self.assertEqual(len(sort_like_channels), 2)
        self.assertIn(self.channel1, sort_like_channels)
        self.assertIn(self.channel2, sort_like_channels)

        self.assertEqual(len(hot_videos), 1)
        self.assertIn(self.video2, hot_videos)        
        
class DetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 테스트에 필요한 데이터 생성
        cls.channel1 = TbChannelInfo.objects.create(
            channel_id='UCNzcxCN_Hh_lu5RCSFXKgGQ', #악동김블루(게임유튜버)
            channel_name='악동 김블루',
            category='GAME',
            subscribers_count=1730000,
            total_view=1310079639,
        )
        cls.video1 = TbVideoInfo.objects.create(
            video_id='HRXPbByHWYY',
            video_title='편집자 결혼식에 축의금 천만원 준 김블루',
            view_count=1900002,
            channel=cls.channel1,
        )
        cls.comment1 = TbCommentInfo.objects.create(
            comment_id='UgyT0E88MSRFeu2DiTZ4AaABAg',
            like_count=8167,
            video=cls.video1,
        )

    def test_detail_view_with_valid_channel_id(self):
        # 존재하는 채널 ID를 이용한 테스트
        channel_id = self.channel1.channel_id
        url = reverse('main:detail', args=[channel_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/detail.html')
        self.assertEqual(response.context['channel_info'], self.channel1)
        self.assertIn(self.comment1, response.context['top_comments'])
        self.assertIn(self.video1, response.context['top_videos'])

    def test_detail_view_with_invalid_channel_id(self):
        # 존재하지 않는 채널 ID를 이용한 테스트
        url = reverse('main:detail', args=['invalid_channel_id'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)