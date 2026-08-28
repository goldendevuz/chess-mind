from .entities import RatingProfile


class Glicko2Calculator:
    def update(self, profile: RatingProfile, score: float) -> RatingProfile:
        delta = (score - 0.5) * 32
        return RatingProfile(
            user_id=profile.user_id,
            rating=max(100.0, profile.rating + delta),
            rd=max(30.0, profile.rd * 0.95),
            vol=profile.vol,
        )

