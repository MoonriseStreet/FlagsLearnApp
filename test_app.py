from app import app


def test_1_home():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_2_quiz():
    tester = app.test_client()

    response = tester.get('/')
    assert response.status_code == 200

    for i in range(10):
        response = tester.get('/country_quiz')
        assert response.status_code == 200
        response = tester.post('/country_quiz')
        assert response.status_code == 200
        response = tester.post('/next_country_question')
        assert response.status_code == 302

    for i in range(10):
        response = tester.get('/flag_quiz')
        assert response.status_code == 200
        response = tester.post('/flag_quiz')
        assert response.status_code == 200
        response = tester.post('/next_flag_question')
        assert response.status_code == 302


def test_3_random_country():
    tester = app.test_client()

    response = tester.get('/')
    assert response.status_code == 200
    response = tester.get('/random_country')
    assert response.status_code == 200
    response = tester.get('/')
    assert response.status_code == 200


def test_4_settings():
    tester = app.test_client()

    response = tester.get('/')
    assert response.status_code == 200
    response = tester.get('/settings')
    assert response.status_code == 200
    response = tester.post('/settings')
    assert response.status_code == 200
    response = tester.get('/')
    assert response.status_code == 200
