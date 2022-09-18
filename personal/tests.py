from django.test import TestCase
from django.urls import reverse

from .models import ViewPersonal
from django.contrib.auth.models import User
# Create your tests here.


class PersonalTest(TestCase):

    @classmethod
    def setUpTestData(cls):  # if we use than def setUpTestData(cls): it will create test data for evry test so  if we replace def setUpTestData(cls) with  def setUp(self):  so its create once for all test
        user = User.objects.create(username='ss'),
        cls.post1 = ViewPersonal.objects.create(

            author=user,
            title='post1',
            text='ali',
            status=ViewPersonal.STATUS_CHOICES[1][0],
        )
        cls.post2 = ViewPersonal.objects.create(

            author=user.id,
            text='sasa',
            title='asa',
            status='drf'
        )

    def test_draf(self):
        response = self.client.get(reverse('person_show'))
        self.assertNotContains(response,self.post1.text)

