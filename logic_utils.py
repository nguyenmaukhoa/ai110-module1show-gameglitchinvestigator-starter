#FIX: Refactored logic into logic_utils.py using agent mode
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # Bug fix: Hard must be harder than Normal, so it needs a LARGER range.
        # Previously this returned (1, 50), making "Hard" easier than "Normal".
        return 1, 500
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    # Bug fix: previously "5.9" was silently truncated to 5 via int(float(raw)).
    # A guessing game expects whole numbers, so reject non-integer input instead.
    try:
        value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a whole number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # Bug fix: removed the off-by-one (attempt_number + 1) that over-penalized.
        # Winning on attempt 1 now awards the full 100 points.
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # Bug fix: a wrong guess must never INCREASE the score. The old code added
    # 5 points for "Too High" on even attempts. Both wrong outcomes now cost 5.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
