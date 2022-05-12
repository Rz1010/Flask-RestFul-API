from unittest import TestCase, main
from service import app

class TestPhoto(TestCase):
    def test_process_photo(self):
        self.app = app.test_client()
        str = "{'1': ['X1', '122', 'Y1', '28', 'X2', '238', 'Y2', '198']}"
        with open('static/test_photo.png', 'b') as test_file:
            response = self.app.post('/photo', data=test_file)
        self.assertEqual(str, str(response))
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    main()
