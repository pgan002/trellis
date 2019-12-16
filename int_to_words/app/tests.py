from django.test import TestCase

from app.en import TEST_CASES_OK, TEST_CASES_ERROR


class TestCalls(TestCase):
    def test_ok(self):
        for n, expected_val in TEST_CASES_OK:
            expected = {'status': 'ok', 'num_in_english': expected_val}
            response = self.client.get(n)
            self.assertEquals(response.status_code, 200, n)
            self.assertEquals(response.body, expected, response.body)

    def test_error(self):
        for n in TEST_CASES_ERROR:
            response = self.client.get(n)
            self.assertEquals(response.status_code, 401, n)
            self.assertContains(response.body, {'status': 'error'})