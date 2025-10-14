import re
import urllib.parse
import uuid
from enum import Enum
from dataclasses import dataclass

from foxypack.entitys.balancers import BaseEntityBalancer
from foxypack.entitys.pool import EntityPool
from pydantic import Field

from foxypack import (
    FoxyStat,
    FoxyAnalysis,
    Entity,
    Storage,
    AnswersAnalysis,
    AnswersStatistics,
)


class InstagramEnum(Enum):
    reel = "reel"
    reels = "reels"
    post = "post"
    page = "page"


@Storage.register_type
@dataclass(kw_only=True)
class InstagramAccount(Entity):
    login: str | None = None
    password: str | None = None
    path_session_file: str | None = None


class InstagramAnswersAnalysis(AnswersAnalysis):
    answer_id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    code: str


class FoxyInstagramAnalysis(FoxyAnalysis):
    @staticmethod
    def get_code(link):
        match = re.search(r"/(p|reel|reels)/([^/?]+)", link)
        if match:
            return match.group(2)

        page_match = re.search(r"instagram\.com/([^/?]+)", link)
        return page_match.group(1) if page_match else None

    @staticmethod
    def clean_link(link):
        parsed_url = urllib.parse.urlparse(link)
        clean_link = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        return clean_link

    @staticmethod
    def get_type_content(url: str) -> str | None:
        parsed_url = urllib.parse.urlparse(url)
        print(parsed_url)
        print(parsed_url.path.split("/"))
        match parsed_url.path.strip("/").split("/"):
            case ["reel" | "reels", *rest]:
                return InstagramEnum.reel.value
            case ["p", *rest]:
                return InstagramEnum.post.value
            case [username, *rest] if username:
                return InstagramEnum.page.value
            case _:
                return None

    def get_analysis(self, url: str) -> AnswersAnalysis | None:
        type_content = self.get_type_content(url)
        if type_content is None:
            return None
        return InstagramAnswersAnalysis(
            url=self.clean_link(url),
            social_platform="instagram",
            type_content=type_content,
            code=self.get_code(url),
        )


class FoxyInstagramStat(FoxyStat):
    def __init__(
        self,
        entity_pool: EntityPool | None = None,
        entity_balancer: BaseEntityBalancer | None = None,
    ):
        self.entity_pool = entity_pool
        self.entity_balancer = entity_balancer

    def get_stat(
        self, answers_analysis: InstagramAnswersAnalysis
    ) -> AnswersStatistics | None:
        pass

    async def get_stat_async(
        self, answers_analysis: InstagramAnswersAnalysis
    ) -> AnswersStatistics | None:
        pass
