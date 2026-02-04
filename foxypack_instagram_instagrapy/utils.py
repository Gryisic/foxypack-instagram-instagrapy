from foxypack import AnswersAnalysis
from foxypack_instagram_instagrapy.answers import InstagramAnswersAnalysis


def as_instagram_analysis(
    analysis: AnswersAnalysis,
) -> InstagramAnswersAnalysis:
    if not isinstance(analysis, InstagramAnswersAnalysis):
        raise TypeError("Analysis is not InstagramAnswersAnalysis")
    return analysis
