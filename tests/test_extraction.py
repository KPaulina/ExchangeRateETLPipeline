import requests


def test_api_is_giving_200_status_code():
    ENDPOINT = 'https://open.er-api.com/v6/latest/PLN'
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


