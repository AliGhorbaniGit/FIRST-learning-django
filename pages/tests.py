
from django.test import TestCase
from django.contrib.auth.models import User
from .models import PageDetail
from django.shortcuts import reverse
from show.models import Show
from personal.models import ViewPersonal


class PagesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='user')  # we use tha self.user to other method in class could use than user by keyword 'self.user'
        self.pages1 = PageDetail.objects.create(
            title='sss',
            text='ala',
            # author=self.user,
        )
        self.pages2 = ViewPersonal.objects.create(
            author = self.user,
            text = 'fffffffadaaaaa',
            status = ViewPersonal.STATUS_CHOICES[1][0] , # or i can write status ='drf'
        )

    def test_str_equal_by(self):
        exam = self.pages1
        self.assertEqual(str(exam), exam.title)

    def test_model_title_equal_to_name(self):
        self.assertEqual(self.pages1.title, 'sss')
        self.assertEqual(self.pages1.text, 'ala')

    def test_pages_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_pages_by_url_name(self):
        response2 = self.client.get(reverse('show_list'))
        self.assertEqual(response2.status_code, 200)

    def test_exist_data_in_pages(self):
        response3 = self.client.get(reverse('show_list'))
        self.assertContains(response3, self.pages1.title)  # or  self.assertContains(response3 , 'ala')

    def test_page_detail_id_by_url_name(self):
        var = self.client.get(f'/{self.pages1.id}/')
        self.assertEqual(var.status_code, 200)

    def test_page_detail_view_by_url_name(self):
        vari = self.client.get(reverse('show_all_comment', args=[self.pages1.text.id]))  # cause the show_all_comment give a entrant so  its need to give it args=[self.pages1.id
        self.assertEqual(vari.status_code, 200)

    def test_pages1_detail_is_in_ditail_page(self):
        # response4 = self.client.get('/1')  # we guess that the id of our post is 1 but this is just a guess, so it's
        # better to use another way  instead  of that :
        response4 = self.client.get(f'/{self.pages1.id}/') # and its better to use than reverse('show_all_comment',args=[self.pages1.id])
        # instead of f'/{self.pages1.id}/' cause its more confident
        self.assertContains(response4, self.pages1.text)
       # self.assertContains(response4, self.pages1.title)  # this will be fail because i show only text in  id page  😁

    def test_status_404_if_id_does_not_exist(self):
        vari = self.client.get(reverse('show_all_comment', args=[99991])) # use a id that think doesn't exist
        self.assertEqual(vari.status_code, 404) # its will be fail because in show -> veiws i said if the id dose not exist
        # return data with none and go to page that is blank

    def test_publish_or_draft(self):
        var = self.client.get('show_list')
        self.assertContains(var, self.pages1.title)
        self._assert_contains(var, self.pages2.title)

    def test_post_create(self):
        response = self.client.post(reverse('add'),{
            'text': 'ahhhay', 'title': 'by by'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PageDetail.objects.last().title, 'by by')
        self.assertEqual(PageDetail.objects.last().text, 'ahhhay')

    def test_post_update(self):

        response = self.client.post(reverse('add',args=[self.pages2.id]),{
            'text':'sali','title':'aali'}) # i wanna give id to addres so im most put in args[]
        self.assertEqual(response.status_code,302)
        self.assertEqual(PageDetail.objects.last().title, 'aali')
        self.assertEqual(PageDetail.objects.last().text, 'sali')

    def test_post_delete(self):
        response = self.client.post(reverse('delete',args=[self.pages1]),{'title':'ssss','title':'dddd'})
        self.assertEqual(response.status_code,302)


