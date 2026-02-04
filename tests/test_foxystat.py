from foxy_entities import EntitiesController

from foxypack_instagram_instagrapy import (
    FoxyInstagramAnalysis,
    FoxyInstagramStat,
)


def test_get_statistics_media(test_account):
    controller = EntitiesController()
    controller.add_entity(test_account)

    instagram_stat = FoxyInstagramStat(entities_controller=controller)
    instagram_stat_two = FoxyInstagramStat(entities_controller=controller)

    analysis = FoxyInstagramAnalysis().get_analysis(
        "https://www.instagram.com/reels/DQcTCktDNQh/"
    )

    stat_one = instagram_stat.get_statistics(analysis)
    stat_two = instagram_stat_two.get_statistics(analysis)

    assert stat_one.answer_id != stat_two.answer_id
    assert stat_one.media_id == stat_two.media_id
    assert stat_one.like_count == stat_two.like_count
    assert stat_one.analysis_status == stat_two.analysis_status

def test_get_statistics_profile(test_account):
    controller = EntitiesController()
    controller.add_entity(test_account)

    instagram_stat = FoxyInstagramStat(entities_controller=controller)
    instagram_stat_two = FoxyInstagramStat(entities_controller=controller)

    analysis = FoxyInstagramAnalysis().get_analysis(
        "https://www.instagram.com/instagram"
    )

    stat_one = instagram_stat.get_statistics(analysis)
    stat_two = instagram_stat_two.get_statistics(analysis)

    assert stat_one.answer_id != stat_two.answer_id
    assert stat_one.user_id == stat_two.user_id
    assert stat_one.username == stat_two.username
    assert stat_one.analysis_status == stat_two.analysis_status
