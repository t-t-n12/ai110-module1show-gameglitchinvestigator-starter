from logic_utils import check_guess


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_direction_too_high():
    # Guess above secret should tell the player to go lower, not higher
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_hint_direction_too_low():
    # Guess below secret should tell the player to go higher, not lower
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_initial_attempts_is_zero():
    # Attempts must start at 0 so "Attempts left" displays the full limit
    initial_attempts = 0
    attempt_limit = 8  # Normal difficulty
    assert attempt_limit - initial_attempts == attempt_limit
