DEFAULT_PLAYER_BALANCE: int = 100
DEFAULT_PLAYERS = (
    ('Alice', DEFAULT_PLAYER_BALANCE),
    ('Boris', DEFAULT_PLAYER_BALANCE),
    ('Chen', DEFAULT_PLAYER_BALANCE),
)

DEFAULT_GEESE = (
    ('Blizzard', 8, 'war'),
    ('Echo', 5, 'honk'),
    ('Nimbus', 6, 'war'),
    ('Spark', 7, 'honk'),
)

MIN_BET: int = 5
MAX_BET: int = 30
WIN_MULTIPLIER: float = 1.5
WAR_GOOSE_MIN_DAMAGE: int = 10
WAR_GOOSE_MAX_DAMAGE: int = 25
HONK_IMPACT: int = 3
STEAL_MIN: int = 5
STEAL_MAX: int = 15
BONUS_MIN: int = 10
BONUS_MAX: int = 25
MERGE_HYPE_BONUS: int = 5
CHIP_BASE_VALUE: int = 10
