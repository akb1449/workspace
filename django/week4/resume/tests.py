from django.test import TestCase
from .models import Resume

# Create your tests here.
class ResumeTestCases(TestCase):

    def setup(self):
        """
        This runs at the beginning of every single test
        """
        my_resume = Resume(first_name='Andry', last_name='Bintoro')
        my_resume.save()

    def test_get_last_name_first_name(self):
        r = Resume.objects.first()
        self.assertEqual(r.get_last_name_first_name(), 'Bintoro Andry')

    def test_get_full_name(self):
        r = Resume.objects.first().get_full_name()
        self.assertEqual(r.get_full_name(), 'Andry Bintoro')

    def test_get_experience(self):
        r = Resume.objects.first()
        self.assertIsNotNone(r.get_experience(self.resume))

    def test_get_education(self):
        r = Resume.objects.first()
        self.assertIsNotNone(r.get_education(self.resume))

if __name__ == '__main__':
    unittest.main()
