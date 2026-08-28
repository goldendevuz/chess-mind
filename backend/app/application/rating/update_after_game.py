from ...domain.rating.entities import RatingProfile
from ...domain.rating.services import Glicko2Calculator


def update_after_game(profile: RatingProfile, score: float) -> RatingProfile:
    return Glicko2Calculator().update(profile, score)

