letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word):
    total = 0
    for letter in word:
        total += letter_to_points.get(letter.upper(), 0)
    return total

print(score_word("EARTH"))
print(score_word("zap"))


player_to_words = {
    "player1": ["wordNerd", "Lexi", "Con", "Prof", "Reader"],
    "BLUE": ["EARTH", "ERASER", "ZAP"],
    "TENNIS": ["EYES", "BELLY", "COMA"],
    "EXIT": ["MACHINE", "HUSKY", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)


def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]

def update_point_totals():
    for player, words in player_to_words.items():
        player_to_points[player] = sum(score_word(word) for word in words)

play_word("player1", "MAGIC")
update_point_totals()
print(player_to_points)
