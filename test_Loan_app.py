import pytest
from Loan_app import app

@pytest.fixture()
def client():
    return app.test_client()


def test_pinger(client):
    response = client.get('/ping')
    assert response.status_code == 200


def test_json_check(client):
    response = client.get('/json')
    assert response.status_code == 200
    assert response.json == {"message": "Hi I am json!"}

def test_prediction(client):
    test_data = {
                "ApplicantIncome" : 1000000,
                "Credit_History" : 1.0,
                "Gender" : "Male",
                "LoanAmount": 120000,
                "Married": "Yes"
            }

    response = client.post('/predict', json=test_data)

    assert response.status_code == 200
    assert response.json == {"loan_approval_status": "Rejected"}