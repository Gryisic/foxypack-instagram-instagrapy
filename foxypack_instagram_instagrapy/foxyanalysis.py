import re
import urllib.parse
from typing_extensions import override

from foxypack import FoxyAnalysis, DenialAnalyticsException
from foxypack_instagram_instagrapy.answers import (
    InstagramAnswersAnalysis,
    InstagramEnum,
)


class FoxyInstagramAnalysis(FoxyAnalysis):

    @staticmethod
    def get_code(link: str) -> str:
        match = re.search(r"/(p|reel|reels)/([^/?]+)", link)
        if match:
            return match.group(2)

        page_match = re.search(r"instagram\.com/([^/?]+)/?$", link)
        if page_match:
            return page_match.group(1)

        return ""

    @staticmethod
    def clean_link(link: str) -> str:
        parsed = urllib.parse.urlparse(link)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    @staticmethod
    def get_type_content(link: str) -> str | None:
        if re.search(r"/(p|reel|reels)/", link):
            return InstagramEnum.reel.value
        if re.match(r"https?://(www\.)?instagram\.com/[^/?]+/?$", link):
            return InstagramEnum.page.value
        return None

    @override
    def get_analysis(self, url: str) -> InstagramAnswersAnalysis:
        type_content = self.get_type_content(url)
        if type_content is None:
            raise DenialAnalyticsException(url)

        return InstagramAnswersAnalysis(
            url=self.clean_link(url),
            social_platform="instagram",
            type_content=type_content,
            code=self.get_code(url),
        )
