from foxy_entities import SocialMediaEntity


class InstagramAccount(SocialMediaEntity):
    login: str | None = None
    password: str | None = None
    session_file: str = "instagram_session.json"
