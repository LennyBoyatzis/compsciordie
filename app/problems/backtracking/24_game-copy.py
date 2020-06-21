from math import floor
from operator import truediv, mul, add, sub


def judge_point_24(cards):
    print(f'what are the cards {cards}')

    if not cards:
        return False

    n = len(cards)

    if n == 1:
        print(f'cards[0] {cards[0]}')
        return cards[0] == 24

    for i in range(n):
        for j in range(n):
            if i != j:
                card_one, card_two = cards[i], cards[j]
                rest = [cards[k] for k in range(n) if k != i and k != j]

                for op in (truediv, mul, add, sub):
                    if (op is add or op is mul) and j > i:
                        continue

                    if op is not truediv or cards[j]:
                        rest.append(op(card_one, card_two))

                        if judge_point_24(rest):
                            return True

                        rest.pop()
    return True


def judge_point(cards):



if __name__ == '__main__':
    cards = [4, 1, 8, 7]
    result = judge_point_24(cards)
    print(f'result {result}')
