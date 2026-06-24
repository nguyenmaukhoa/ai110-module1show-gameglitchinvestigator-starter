from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# ---------------------------------------------------------------------------
# check_guess  (note: returns a tuple of (outcome, message))
# ---------------------------------------------------------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# Bug 1: update_score Win was off-by-one and over-penalized.
# Winning on the first attempt should award the full 100 points.
# ---------------------------------------------------------------------------

def test_win_on_first_attempt_awards_full_points():
    # Old buggy formula: 100 - 10 * (1 + 1) = 80. Correct: 100 - 10 * 0 = 100.
    assert update_score(0, "Win", attempt_number=1) == 100

def test_win_points_decay_per_attempt():
    # Each later attempt should be worth 10 fewer points.
    assert update_score(0, "Win", attempt_number=2) == 90
    assert update_score(0, "Win", attempt_number=3) == 80

def test_win_points_never_below_floor():
    # Points are floored at 10 no matter how many attempts were taken.
    assert update_score(0, "Win", attempt_number=50) == 10


# ---------------------------------------------------------------------------
# Bug 2: a wrong guess could INCREASE the score.
# "Too High" on an even attempt used to add 5. Both wrong outcomes must lose 5.
# ---------------------------------------------------------------------------

def test_too_high_never_increases_score():
    # attempt_number=2 is even -> old code returned current_score + 5.
    assert update_score(100, "Too High", attempt_number=2) == 95

def test_too_high_on_odd_attempt_loses_points():
    assert update_score(100, "Too High", attempt_number=3) == 95

def test_too_low_loses_points():
    assert update_score(100, "Too Low", attempt_number=1) == 95


# ---------------------------------------------------------------------------
# Bug 3: "Hard" had a smaller range than "Normal", making it easier.
# Hard must span a strictly wider range than Normal.
# ---------------------------------------------------------------------------

def test_hard_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


# ---------------------------------------------------------------------------
# Bug 4: parse_guess silently truncated decimals ("5.9" -> 5).
# Non-integer input must be rejected, not coerced.
# ---------------------------------------------------------------------------

def test_parse_guess_rejects_decimals():
    ok, value, error = parse_guess("5.9")
    assert ok is False
    assert value is None
    assert error is not None

def test_parse_guess_accepts_integers():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None

def test_parse_guess_rejects_empty_input():
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error is not None
