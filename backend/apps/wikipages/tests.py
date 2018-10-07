from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.wikipages.models import WikiPage


class WikiPageModelTestCase(TestCase):
    def setUp(self):
        WikiPage.objects.create(title="WikiPage 1", text="really good content")
        WikiPage.objects.create(title="WikiPage 2", text="one more good article")

    def test_wikipage_is_updated(self):
        wp1 = WikiPage.objects.get(title="WikiPage 1")
        wp2 = WikiPage.objects.get(title="WikiPage 2")
        # Avoid using time.sleep, change created_at for 1 sec
        now = timezone.now() - timedelta(seconds=1)
        wp2.created_at = now
        wp2.text = 'changed text'
        wp2.save()
        self.assertEqual(wp1.is_updated, False)
        self.assertEqual(wp2.is_updated, True)

    def test_wikipage_name_is_title(self):
        wp1 = WikiPage.objects.get(title="WikiPage 1")
        wp2 = WikiPage.objects.get(title="WikiPage 2")
        expected_object_name1 = wp1.title
        expected_object_name2 = wp2.title
        self.assertEqual(expected_object_name1, str(wp1))
        self.assertEqual(expected_object_name2, str(wp2))


class WikiPageAPITestCase(APITestCase):

    def test_can_create_wikipage(self):
        wiki_data = {"title": "WikiPage", "text": "really good content"}
        response = self.client.post(reverse('wikipage-list'), wiki_data)
        wp = WikiPage.objects.get(title="WikiPage")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(wp.title, "WikiPage")

    def test_can_read_wikipage_list(self):
        WikiPage.objects.create(title="WikiPage", text="really good content")
        response = self.client.get(reverse('wikipage-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_can_read_wikipage_detail(self):
        WikiPage.objects.create(title="WikiPage", text="really good content")
        wp = WikiPage.objects.get(title="WikiPage")
        response = self.client.get(reverse('wikipage-detail', args=[wp.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "WikiPage")
        self.assertEqual(response.data["text"], "really good content")
        self.assertEqual(response.data["is_updated"], False)

    def test_can_update_wikipage_detail(self):
        WikiPage.objects.create(title="WikiPage", text="really good content")
        wp = WikiPage.objects.get(title="WikiPage")
        new_wiki_data = {"title": "New WikiPage", "text": "New really good content"}
        response = self.client.put(reverse('wikipage-detail', args=[wp.id]), new_wiki_data)
        updated_wp = WikiPage.objects.get(id=wp.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_wp.title, "New WikiPage")
        self.assertEqual(updated_wp.text, "New really good content")
