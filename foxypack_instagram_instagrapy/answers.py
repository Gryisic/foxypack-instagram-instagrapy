from enum import Enum
from foxypack.foxypack_abc.answers import (
    AnswersAnalysis,
    AnswersSocialContent,
    AnswersSocialContainer,
)


class InstagramEnum(Enum):
    reel = "reel"
    post = "post"
    page = "page"


class InstagramAnswersAnalysis(AnswersAnalysis):
    code: str


class InstagramUserAnswersStatistics(AnswersSocialContainer):
    user_id: int
    username: str
    full_name: str
    media_count: int
    follower_count: int
    following_count: int


class InstagramMediaAnswersStatistics(AnswersSocialContent):
    media_id: int
    instagram_id: str
    view_count: int
    video_duration: float
    like_count: int
    play_count: int
    caption_text: str
    comment_count: int
