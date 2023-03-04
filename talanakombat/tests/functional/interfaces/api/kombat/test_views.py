from django.urls import resolve
from parameterized import parameterized
from rest_framework_api_key.models import APIKey
from talanakombat.interfaces.api.kombat import views
from talanakombat.tests.functional.interfaces.api.kombat import constants
from test_plus import APITestCase


class KombatMethodPostTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.url = self.reverse(name="kombat_api:kombat")
        self.headers = {"format": "json"}

    def test_kombat_api_view_resolves_correctly(self):
        found = resolve(self.url)
        self.assertTrue(found.func.__name__, views.Kombat.__name__)

    @parameterized.expand(
        [
            (constants.CASE1, "¡Arnold gana la pelea"),
            (constants.CASE2, "¡Tony gana la pelea"),
            (constants.CASE3, "¡Arnold gana la pelea"),
        ]
    )
    def test_post_kombat_api_view_return_ok(self, case: dict, response_expected: str):
        response = self.post(self.url, data=case, extra=self.headers)

        self.assert_http_200_ok(response)
        self.assertContains(response, response_expected)

    def test_post_kombat_api_view_return_with_fields_incorrect(self):
        data = {
            "player1222": {
                "movimientos": ["D", "DSD", "S", "DSD", "SD"],
                "golpes": ["K", "P", "K", "K", "P"],
            },
            "player2": {
                "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
                "golpes": ["K", "", "K", "P", "P"],
            },
        }

        response = self.post(self.url, data=data, extra=self.headers)

        self.assert_http_400_bad_request(response)
