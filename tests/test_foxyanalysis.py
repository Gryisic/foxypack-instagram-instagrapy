import pytest

from foxypack_instagram_instagrapy import FoxyInstagramAnalysis


@pytest.mark.analysis
def test_instagram_reel_link():
    analyzer = FoxyInstagramAnalysis()

    analysis = analyzer.get_analysis(
        "https://www.instagram.com/reel/C0abcdEFGhI/"
    )
    analysis_two = analyzer.get_analysis(
        "https://www.instagram.com/reel/C0abcdEFGhI/"
    )

    assert analysis.answer_id != analysis_two.answer_id
    assert analysis.url == "https://www.instagram.com/reel/C0abcdEFGhI/"
    assert analysis.social_platform == "instagram"
    assert analysis.type_content == "reel"
    assert analysis.code == "C0abcdEFGhI"

@pytest.mark.analysis
def test_instagram_post_link():
    analyzer = FoxyInstagramAnalysis()

    analysis = analyzer.get_analysis(
        "https://www.instagram.com/p/C0abcdEFGhI/"
    )

    assert analysis.social_platform == "instagram"
    assert analysis.type_content == "reel"  # post → media
    assert analysis.code == "C0abcdEFGhI"

@pytest.mark.analysis
def test_instagram_profile_link():
    analyzer = FoxyInstagramAnalysis()

    analysis = analyzer.get_analysis("https://www.instagram.com/instagram")
    analysis_two = analyzer.get_analysis("https://www.instagram.com/instagram")

    assert analysis.answer_id != analysis_two.answer_id
    assert analysis.url == "https://www.instagram.com/instagram"
    assert analysis.social_platform == "instagram"
    assert analysis.type_content == "page"
    assert analysis.code == "instagram"
