from foxypack_instagram_instagrapy.engine import FoxyInstagramAnalysis

data = FoxyInstagramAnalysis().get_analysis(
    "https://www.instagram.com/reels/DOu9aQNjUkO/"
)
print(data)

data = FoxyInstagramAnalysis().get_analysis("https://www.instagram.com/_fr_404/reels/")
print(data)
