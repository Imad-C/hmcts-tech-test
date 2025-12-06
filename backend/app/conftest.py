import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base
from .main import app, get_db
from .utils import delete_db

# Need to create a db, then delete it once tests have run
@pytest.fixture(scope="session", autouse=True)
def test_db():
    test_db = 'test.db'
    engine = create_engine(f'sqlite:///{test_db}', connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_db

    yield  

    Base.metadata.drop_all(bind=engine)
    delete_db(test_db)