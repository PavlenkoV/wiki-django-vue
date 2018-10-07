from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

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
