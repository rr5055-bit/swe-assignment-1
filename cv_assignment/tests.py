# Tests for the CV views
from django.test import SimpleTestCase

from .loader import load_cv


class CvViewTests(SimpleTestCase):
    def test_home_renders_all_sections(self):
        html = self.client.get("/").content.decode()
        self.assertIn("Rohan Aditya Ram", html)
        for name in load_cv()["sections"]:
            self.assertIn(f'id="{name}"', html)

    def test_footer_uses_context_processor(self):
        self.assertContains(self.client.get("/"), "&copy;")

    def test_section_partial_only(self):
        response = self.client.get("/section/projects/")
        self.assertContains(response, 'id="projects"')
        self.assertNotContains(response, "<html")

    def test_unknown_section_is_404(self):
        self.assertEqual(self.client.get("/section/nope/").status_code, 404)

    def test_links_render_only_when_present(self):
        html = self.client.get("/").content.decode()
        self.assertIn("mailto:rr5055@nyu.edu", html)
        self.assertNotIn('href="None"', html)
