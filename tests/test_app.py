from app import app


def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"


def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["healthy"] is True


def test_version():
    client = app.test_client()
    resp = client.get("/version")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["version"] == "0.1.0"
