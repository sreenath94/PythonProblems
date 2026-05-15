def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


def is_ascending(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False
    return True


def riffle(items, out=True):
    result = []
    half = len(items) // 2
    first_half = items[:half]
    second_half = items[half:]
    for i in range(half):
        if out:
            result.extend((first_half[i], second_half[i]))
        else:
            result.extend((second_half[i], first_half[i]))

    return result


def only_odd_digits(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return False

        n = n // 10
    return True


def is_cyclops(n):
    digit = str(n)
    return digit.count('0') == 1 and digit[len(digit) // 2] == '0' and len(digit) % 2 == 1


def domino_cycle(tiles):
    for i in range(len(tiles) - 1):
        if tiles[i][1] != tiles[i + 1][0]:
            return False

    return tiles == [] or tiles[0][0] == tiles[-1][1]


def count_dominators(items):
    n = len(items)
    if n == 0:
        return 0
    max_so_far = items[n - 1]
    count = 1
    for i in range(n - 2, -1, -1):
        x = items[i]
        if x > max_so_far:
            max_so_far = x
            count += 1
    return count


def is_chess_960(row):
    king = row.index('K')
    rook1 = row.index('r')
    rook2 = row.index('r', rook1 + 1)
    bishop1 = row.index('b')
    bishop2 = row.index('b', bishop1 + 1)

    return bishop1 % 2 != bishop2 % 2 and ( rook2 > king > rook1)

