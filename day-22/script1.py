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


def play_game(cards):
    while cards["Player 1"] and cards["Player 2"]:
        a, b = [x.pop(0) for x in cards.values()]
        if a > b:
            cards["Player 1"] += [a, b]  
        else:
            cards["Player 2"] += [b, a]
    for final_set in [x for x in cards.values()]:
        if len(final_set) > 0:
            result = 0
            final_set.reverse()
            for i, v in enumerate(final_set):
                result += (i + 1) * v
    return result


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    cards = get_player_cards(lines)
    print(cards)
    result = play_game(cards)
    print(result)


if __name__ == "__main__":
    main()