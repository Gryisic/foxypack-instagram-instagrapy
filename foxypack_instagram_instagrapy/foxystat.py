import asyncio
from datetime import datetime

from instagrapi import Client
from typing_extensions import override

from foxy_entities import EntitiesController
from foxypack import (
    FoxyStat,
    InternalCollectionException,
    AnswersAnalysis,
)

from foxypack_instagram_instagrapy.answers import (
    InstagramEnum,
    InstagramUserAnswersStatistics,
    InstagramMediaAnswersStatistics,
)
from foxypack_instagram_instagrapy.entities import InstagramAccount
from foxypack_instagram_instagrapy.utils import as_instagram_analysis


class FoxyInstagramStat(FoxyStat):

    def __init__(self, entities_controller: EntitiesController | None = None):
        self._entities_controller = entities_controller

    def _get_account(self) -> InstagramAccount:
        if self._entities_controller is None:
            raise InternalCollectionException
        return self._entities_controller.get_entity(InstagramAccount)

    async def _get_client(self) -> Client:
        account = self._get_account()
        client = Client()

        try:
            client.load_settings(account.session_file)
        except FileNotFoundError:
            client.login(account.login, account.password)
            client.dump_settings(account.session_file)

        if self._entities_controller is not None:
            self._entities_controller.add_entity(account)

        return client

    async def _get_statistics_async_internal(
        self, analysis: AnswersAnalysis
    ):
        if analysis.social_platform != "instagram":
            raise InternalCollectionException

        analysis = as_instagram_analysis(analysis)
        client = await self._get_client()

        if analysis.type_content == InstagramEnum.page.value:
            user_id = client.user_id_from_username(analysis.code)
            user = client.user_info(user_id)

            return InstagramUserAnswersStatistics(
                title=user.full_name,
                user_id=user.pk,
                username=user.username,
                full_name=user.full_name,
                media_count=user.media_count,
                follower_count=user.follower_count,
                following_count=user.following_count,
                system_id=user.pk,
                creation_date=datetime.now().date(),
                analysis_status=analysis,
            )

        media_id = client.media_pk_from_url(analysis.url)
        media = client.media_info(media_id)

        return InstagramMediaAnswersStatistics(
            title=media.caption_text[:50] if media.caption_text else "Instagram media",
            media_id=media.pk,
            instagram_id=media.id,
            view_count=media.view_count,
            video_duration=media.video_duration,
            like_count=media.like_count,
            play_count=media.play_count,
            caption_text=media.caption_text,
            comment_count=media.comment_count,
            publish_date=media.taken_at.date(),
            system_id=media.pk,
            analysis_status=analysis,
        )

    @override
    def get_statistics(self, analysis: AnswersAnalysis):
        return asyncio.run(self._get_statistics_async_internal(analysis))

    @override
    async def get_statistics_async(self, analysis: AnswersAnalysis):
        return await self._get_statistics_async_internal(analysis)
