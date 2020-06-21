from math import floor
from operator import truediv, mul, add, sub


def judge_point_24(cards):
    """
    cards = [4, 1, 8, 7]
    operators = [truediv, mul, add, sub]

    expr = [4, truediv, 1, add, 8, sub, 7]
    - In an expr
        -> Will have 4 cards (can't have less)
        -> Will have 3 operators (can't have less)
            -> No unary operators
            -> No joining of cards
    - Can use the same operator over and over again
    - Can use the same cards over and over again
    """
    operations = ['/', '*', '+', '-']
    # operations = [truediv, mul, add, sub]
    n = len(cards)
    expr_limit = 7

    def backtrack(expr):
        if len(expr) >= expr_limit:
            return

        for i in range(n):
            for j in range(n):
                if i != j:
                    for op in operations:
                        new_expr = [*expr, cards[i], op, cards[j]]
                        backtrack(new_expr)

    backtrack([])


if __name__ == '__main__':
    cards = [4, 1, 8, 7]
    result = judge_point_24(cards)
    print(f'result {result}')
