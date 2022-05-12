from unittest import TestCase, main
from service import app

class TestPhoto(TestCase):
    def test_process_photo(self):
        self.app = app.test_client()
        strb = "{'1': ['X1', '122', 'Y1', '28', 'X2', '238', 'Y2', '198']}"
        with open('test_image.png', 'r') as test_file:
            #img=test_file.read()
            response = self.app.post('/photo', "tes")
            print(response)
        test_file.close()
        #self.assertEqual(strb, str(response))
        #self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    main()
