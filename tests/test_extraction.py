import requests

ENDPOINT = 'https://open.er-api.com/v6/latest/PLN'


def test_api_is_giving_200_status_code():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


