from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero_v2.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange - Fase 1 - Organizar (Arrange)

    response = client.get('/')  # Act - Fase 2 - Agir (Act)

    assert response.status_code == HTTPStatus.OK  # Assert - Fase 3 - Afirmar (Assert)
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert