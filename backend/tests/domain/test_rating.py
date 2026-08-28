from app.domain.rating.entities import RatingProfile
from app.domain.rating.services import Glicko2Calculator


def test_glicko_update_moves_rating_up_on_win() -> None:
    profile = RatingProfile(user_id="u1", rating=1500)
    updated = Glicko2Calculator().update(profile, 1.0)
    assert updated.rating > profile.rating

