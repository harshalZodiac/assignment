import json

import pytest

from api_services.api_common import validate_response
from api_services.api_services import *
from utilities.json_utilities import get_payload_json


class TestReqresUsers:


    def test_get_all_user_data(self):
        response = get_user_data()
        validate_response(response, 200)

    @pytest.fixture(scope="class")
    def user_creation_request(self):
        payload = get_payload_json("D:\\PythonProject\\Finacplus\\api_tests\\templates\\create_new_user.json")
        response = create_new_user(json.dumps(payload))

        return response

    def test_create_new_user(self, user_creation_request):
        response = user_creation_request
        validate_response(response, 201)

    def test_update_user_data(self, user_creation_request):
        creation_response = user_creation_request
        user_id = creation_response.json()["id"]
        payload = get_payload_json("D:\\PythonProject\\Finacplus\\api_tests\\templates\\create_new_user.json")
        payload["name"] = 'Shinde'
        response = update_user_data(payload, user_id)
        validate_response(response, 200)
