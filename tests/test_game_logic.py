from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_logic_utils_no_longer_stubs():
    # Bug: all functions in logic_utils.py raised NotImplementedError before refactoring.
    # This test verifies all four functions are fully implemented and callable.
    assert parse_guess("5") == (True, 5, None)
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert update_score(0, "Win", 1) == 80
    outcome, _ = check_guess(5, 5)
    assert outcome == "Win"

def test_integer_secret_comparison_not_string():
    # Bug: secret was cast to str on even-numbered attempts.
    # String comparison breaks for multi-digit numbers —
    # e.g. check_guess(9, "10") returns "Too High" because "9" > "10" lexicographically,
    # even though 9 < 10. Secret must always be an int.
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low", (
        "check_guess(9, 10) should be 'Too Low', but string comparison "
        "of '9' > '10' incorrectly returns 'Too High'"
    )
