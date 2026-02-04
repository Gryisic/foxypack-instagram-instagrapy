import os

import pytest
from dotenv import load_dotenv

from foxypack_instagram_instagrapy import InstagramAccount


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session")
def test_account():
    return InstagramAccount(
        login=os.getenv("INSTAGRAM_LOGIN"),
        password=os.getenv("INSTAGRAM_PASSWORD"),
        session_file=os.getenv(
            "INSTAGRAM_SESSION_FILE", "instagram_session.json"
        ),
    )
