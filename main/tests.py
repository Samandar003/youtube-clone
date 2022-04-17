from django.test import TestCase, Client
from .models import *
from .serializers import *
# Create your tests here.

class UserSerializerTest(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(name='John', username='John', 
        email='john@gmail.com', phone=978456245, country='America', 
        city='Los Angels', age=40, avatar="https://images.com/my_photo_04")

    def test_is_valid(self):
        data = {
        'name':'Olex',
        'username':'Olex',
        'email':'olex@gmail.com',
        'phone':9784561235,
        'country':'Uk',
        'city':'manchester',
        'age':51,
        'avatar':"https://images.com/my_photo_07"
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid(raise_exception=True))

class UserViewsetTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user1 = User.objects.create(name='John', username='John', 
        email='john@gmail.com', phone=978456245, country='America', 
        city='Los Angels', age=40, avatar="https://images.com/my_photo_04")
    
    def test_get_users(self):
        response = self.client.get('/users/')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data[0]['name'], 'John')
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
    # def add_users(self):
    #     self.new_user = User.objects.create(name='Bayden', username='Bayden', 
    #     email='bayden@gmail.com', phone=914561221, country='America', 
    #     city='Las Vegas', age=48, avatar="https://images.com/my_photo_06")

    def test_user_search(self):
        response = self.client.get('/users/?search=john')
        data = response.data 
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data),1)
        self.assertEquals(data[0]['username'], 'John')
        self.assertEquals(data[0]['email'], 'john@gmail.com')
    
class CommentTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user1 = User.objects.create(name='Bayden', username='Bayden', 
        email='bayden@gmail.com', phone=914561221, country='America', 
        city='Las Vegas', age=48, avatar="https://images.com/my_photo_06")
        self.playlist1 = Playlist.objects.create(user=self.user1, playlist_name='Motivation',
        playlist_text='There are 2 types of motive'
        )
        self.video1 = Video.objects.create(video_name='Stop wasting time',
        video_text='It tells you about spending time efficiently',
        video_views=1, video_user=self.user1, video_playlist=self.playlist1, 
        video='https://myvideos.com/video23nfkd.mp4'
        )

        self.comment1 = Comment.objects.create(user=self.user1, video=self.video1,
        comment_text='Yulduz usmonova pardani aytgan ekan')

    def test_valid(self):
        data = {
            'user':self.user1.id, 
            'video':self.video1.id,
            'comment_text':'Yulduz usmonova pardani aytgan ekan'
        }
        serializer = CommentSerializer(data=data)
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_get_comments(self):
        response = self.client.get('/comments/')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data),1)
        self.assertEquals(data[0]['video'],1)
    def test_search_comments(self):
        response = self.client.get('/comments/?search=Stop wasting time')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data),1)
        self.assertEquals(data[0]['user'], self.user1.id)



