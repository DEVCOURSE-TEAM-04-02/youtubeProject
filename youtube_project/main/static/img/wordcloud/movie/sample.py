from googleapiclient.discovery import build
import pandas as pd
import operator


class Factory_chellenge_youtube_api:
    def __init__(self):
        self.developer_key = 'AIzaSyDfvhCHcNTn5RB30Ll9oFSjnvjW9x1ncLs'
        self.youtube_api_service_name = "youtube"
        self.youtube_api_version = 'v3'

    def videoID_likes(self):
        youtube = build(self.youtube_api_service_name, self.youtube_api_version, developerKey=self.developer_key)

        search_response = youtube.search().list(
            q='#영화',
            order='viewCount',
            part='snippet',
            maxResults=6
        ).execute()
        # print(search_response)
        # 검색을 위한 videoID 추출
        videoIds = []
        for i in range(0, len(search_response['items'])):
            videoIds.append((search_response['items'][i]['id']['videoId']))

        channel_title_lst = []  # 채널 이름을 담는 리스트
        channel_rating_good = []  # 채널 좋아요 수를 담는 리스트
        dicts = {}  # 채널 이름 + 좋아요 수

        # 영상이름, 조회수 , 좋아요 등 정보 등 추출
        for k in range(0, len(search_response['items'])):
            videoIdslists = youtube.videos().list(
                part='snippet, statistics',
                id=videoIds[k],
            ).execute()

            # Channel title 입력
            channel_title_lst.append(videoIdslists['items'][0]['snippet'].get('channelTitle'))

            # 좋아요 입력
            channel_rating_good.append(videoIdslists['items'][0]['statistics'].get('likeCount'))

        for title_plus_rating in zip(channel_title_lst, channel_rating_good):
            dicts[title_plus_rating[0]] = int(title_plus_rating[1])
        sdicts = sorted(dicts.items(), key=operator.itemgetter(1), reverse=True)

        return sdicts

    def channelID_likes_DataFrame(self, sdicts):
        df = pd.DataFrame(sdicts)
        df.columns = ['Channel_title', 'Video_likes']
        print("######################################")
        print("#                                    #")
        print("#            팩토리챌린지              #")
        print("#             조 회 수                #")
        print("#              TOP6                  #")
        print("#                                    #")
        print("######################################")
        print(df)

        # df.to_csv(r"C:\Users\Student\PycharmProjects\k8s_python\result.csv",
        #           encoding='utf-8-sig')

Factory_chellenge = Factory_chellenge_youtube_api()  # 최초 class 선언
channelID_likes_sum = Factory_chellenge.videoID_likes()  # 좋아요 + 조회수 추출
Factory_chellenge.channelID_likes_DataFrame(channelID_likes_sum)  # 데이터프레임화