from django.test import SimpleTestCase, Client

from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """Unit tests for home page."""

    def setUp(self):
        self.client = Client()

    def test_render_page_200(self):
        """Test the page is rendered with HTTP 200 response."""
        url = reverse('home:index')
        res = self.client.get(url)

        self.assertContains(res, 'Sample')
