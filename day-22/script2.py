import re


def get_player_cards(lines):
    cards = {}
    for line in lines:
        if re.match("Player", line):
            p = line.strip(":")
            cards[p] = []
        elif re.match("\\d+", line):
            cards[p].append(int(line))
    return cards


def calculate_result(card_list):
    result = 0
    card_list.reverse()
    for i, v in enumerate(card_list):
        result += (i + 1) * v
    return result


def play_game(cards, game=1):
    p = ["Player 1", "Player 2"]
    h1 = []
    h2 = []
    print("Playing game %s" % game)
    i = 0
    while cards[p[0]] and cards[p[1]]:
        i += 1
        print("".join(["-"] * game)+"round %s" % i)
        # check if loop
        if cards[p[0]] in h1 and cards[p[1]] in h2:
            return 0, calculate_result(cards[p[0]])
        else:
            h1.append([x for x in cards[p[0]]])
            h2.append([x for x in cards[p[1]]])
        # each player deals one card
        a, b = [x.pop(0) for x in cards.values()]
        # check if combat
        if len(cards[p[0]]) >= a and len(cards[p[1]]) >= b:
            w, _ = play_game({p[0]: cards[p[0]][:a], p[1]: cards[p[1]][:b]}, game+1)
        else:
            w = 0 if a > b else 1
        if w:
            cards[p[1]] += [b, a]
        else:
            cards[p[0]] += [a, b]
    winner = 0 if len(cards[p[0]]) > 0 else 1
    result = calculate_result(cards[p[winner]])
    return winner, result


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    cards = get_player_cards(lines)
    print(cards)
    winner, result = play_game(cards)
    print(result)


if __name__ == "__main__":
    main()