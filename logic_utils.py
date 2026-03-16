def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal": # FIXME: logic breaks here, should have a smaller range than "Hard", FIX : the range for normal was decreaed here, AI set it to 1 to 50, I apporved
        return 1, 50
    if difficulty == "Hard":  # FIXME: logic breaks here, should have a larger range than "Normal", FIX : the range for hard was increased here, AI set it to 1 to 100, I apporved
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!" #FIXME: logic breks here, should be "GO LOWER", FIX: the "HIGHER" was changed to "LOWER"
        else:
            return "Too Low", "📈 Go HIGHER!" #FIXME: logic breks here, should be "GO HIGHER", FIX: the "LOWER" was changed to "HIGHER"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!" #FIXME: logic breks here, should be "GO LOWER", FIX: the "HIGHER" was changed to "LOWER"
        return "Too Low", "📈 Go HIGHER!" #FIXME: logic breks here, should be "GO HIGHER", FIX: the "LOWER" was changed to "HIGHER"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
