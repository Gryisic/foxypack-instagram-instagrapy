from foxy_entities import EntitiesController

from foxypack_instagram_instagrapy import (
    FoxyInstagramAnalysis,
    FoxyInstagramStat,
)


def test_account_entity(test_account):
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
    assert stat_one.caption_text == stat_two.caption_text
    assert stat_one.analysis_status == stat_two.analysis_status
