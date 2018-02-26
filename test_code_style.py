import unittest
import pycodestyle
import os


class TestCodeFormat(unittest.TestCase):

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        path_f = []
        for d, dirs, files in os.walk('./src'):
            for f in files:
                if f.split('.')[1] == 'py' \
                        and not f.split('.')[0][0].isdigit() \
                        and f.split('.')[0] != 'base_settings' \
                        and f.split('.')[0] != 'production_settings' \
                        and f.split('.')[0] != 'local_settings':
                    path = os.path.join(d, f)
                    st = pycodestyle.Checker(filename=path, show_source=True)
                    print(st.check_all())
                    path_f.append(path)
        result = style.check_files(path_f)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (warnings).")


if __name__ == "__main__":
    unittest.main()
