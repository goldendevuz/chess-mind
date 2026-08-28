from dataclasses import dataclass


@dataclass
class RatingProfile:
    user_id: str
    rating: float = 1500.0
    rd: float = 350.0
    vol: float = 0.06

