from django.test import TestCase
import subprocess


class TestAll(TestCase):

    def test_1(self):
        with open("library_management/utils.py", "w"):
            pass

        with open("library_management/utils_sample1.py") as f:
            with open("library_management/utils.py", "w") as f1:
                for line in f:
                    f1.write(line)
        check = True
        try:
            subprocess.check_output("python3 manage.py test library_management", shell=True)
            check = False
        except:
            pass

        self.assertTrue(check, msg='\nفیکسچر شما، در حالتی که هیچ کتابی با مشخصات خواسته شده یافت نشود؛ به درستی عمل نمی‌کند.')

    def test_2(self):
        with open("library_management/utils.py", "w"):
            pass

        with open("library_management/utils_sample2.py") as f:
            with open("library_management/utils.py", "w") as f1:
                for line in f:
                    f1.write(line)
        check = True
        try:
            subprocess.check_output("python3 manage.py test library_management", shell=True)
            check = False
        except:
            pass

        self.assertTrue(check, '\nفیکسچر شما، حالت‌های مختلف مسئله را در نظر نمی‌گیرد.')