from dataclasses import dataclass
from enum import Enum, IntEnum


class Suit(str, Enum):
    HEARTS = "H"
    SPADES = "S"
    DIAMONDS = "D"
    CLUBS = "C"


class RankCategory(str, Enum):
    BROADWAY = "Broadway"
    MIDDLE = "Middle"
    LOW = "Low"


class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @property
    def category(self) -> RankCategory:
        if self >= Rank.TEN:
            return RankCategory.BROADWAY
        if self >= Rank.SIX:
            return RankCategory.MIDDLE
        return RankCategory.LOW

    @property
    def symbol(self) -> str:
        return {
            Rank.TEN: "T",
            Rank.JACK: "J",
            Rank.QUEEN: "Q",
            Rank.KING: "K",
            Rank.ACE: "A",
        }.get(self, str(self.value))


@dataclass(frozen=True, slots=True)
class Card:
    rank: Rank
    suit: Suit

    @property
    def category(self) -> RankCategory:
        return self.rank.category

    @property
    def code(self) -> str:
        return f"{self.rank.symbol}{self.suit.value.lower()}"

    def __str__(self) -> str:
        return self.code


@dataclass
class Action:
    type: str
    amount: float
    amount_bb: float

    def to_dict(self):
        return {
            "type": self.type,
            "amount": self.amount,
            "amount_bb": self.amount_bb,
        }
