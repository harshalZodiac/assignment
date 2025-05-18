
def validate_response(response, response_code):
    assert response.status_code == response_code