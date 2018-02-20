from django.test import TestCase
from .models import Resume, Experience, Education

# Create your tests here.
class ResumeTestCases(TestCase):
    Resume = None;
    Experience = None;
    Education = None;

    def setUp(self):
        """
        This runs at the beginning of every single test
        """
        self.Resume=Resume.objects.create(
                                            first_name='Andry',
                                            last_name='Bintoro'
                                         )
        self.Experience=Experience.objects.create(
                                                    parent_resume=self.Resume,
                                                    title='Response Engineer',
                                                    location='Greenpages, Inc',
                                                    start_date='2015-10-12',
                                                    end_date='2017-03-07'
                                                 )
        self.Education=Education.objects.create(
                                parent_resume=self.Resume,
                                institution_name='University of New Hampshire',
                                degree='Master of Science',
                                major='Information Technology',
                                gpa='3.8',
                                )

    def test_get_last_name_first_name(self):
        my_resume = Resume.objects.first()
        self.assertEqual(my_resume.get_last_name_first_name(), 'Bintoro Andry')

    def test_get_full_name(self):
        my_resume = Resume.objects.first()
        self.assertEqual(my_resume.get_full_name(), 'Andry Bintoro')

    def test_get_experience(self):
        my_resume = Resume.objects.first()
        actual = list(my_resume.get_experience())
        expected = list(my_resume.experience_set.all())
        self.assertEqual(actual, expected)

    def test_get_education(self):
        my_resume = Resume.objects.first()
        actual = list(my_resume.get_education())
        expected = list(my_resume.education_set.all())
        self.assertEqual(actual, expected)
