from math import isqrt
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

def colour_trio(colors):
    from math import log
    if len(colors) == 1:
        return colors

    color_dict = {'rr':'r', 'bb':'b', 'yy': 'y', 'br':'y',
                 'rb': 'y', 'by': 'r', 'yb': 'r', 'ry': 'b', 'yr': 'b'}

    if len(colors) == 3**int(log(len(colors)-1,3))+1:
        return color_dict.get(colors[0]+ colors[-1])

    while len(colors) > 1:
        new_string = ''
        for i in range(len(colors) - 1):
           new_string += color_dict[colors[i]+colors[i+1]]
        colors = new_string
        if len(colors) == 3**int(log(len(colors) - 1, 3)) + 1:
            return color_dict.get(colors[0] + colors[-1])

    return colors

def is_left_handed(pips):
    return tuple(pips) in {(1, 2, 3), (2, 3, 1), (3, 1, 2), (1, 4, 2), (4, 2, 1), (2, 1, 4), (1, 3, 5), (3, 5, 1), (5, 1, 3), (6, 3, 2),
     (3, 2, 6), (2, 6, 3), (1, 5, 4), (5, 4, 1), (4, 1, 5), (6, 2, 4), (2, 4, 6), (4, 6, 2), (6, 5, 3), (5, 3, 6),
     (3, 6, 5), (6, 4, 5), (4, 5, 6), (5, 6, 4)}


def words_with_given_shape(words, shape):
    n = len(shape) + 1
    result = []
    for word in words:
        if len(word) != n:
            continue
        for i in range(len(word) -1):
            if(word[i] > word[i+1]) and shape[i] != -1:
                break
            if(word[i] < word[i+1]) and shape[i] != 1:
                break
            if(word[i] == word[i+1]) and shape[i] != 0:
                break
        else:
            result.append(word)

    return result

def topswops(cards):
    cards = list(cards)
    count = 0
    while cards[0] != 1:
        count += 1
        swap = cards[0:cards[0]][::-1]
        swap += cards[cards[0]:]
        cards = swap

    return count

def word_positions(sentence, word):
    words = sentence.split()
    return [i for i,v in enumerate(words) if v == word]

def extract_increasing(digits):
    result = []
    current = 0
    prev = -1
    for d in digits:
        current = 10 * current + int(d)
        if current > prev:
            result.append(current)
            prev = current
            current = 0
    return result

def knight_jump(knight, start, end):
    diffs = sorted(abs(s - e) for s, e in zip(start, end))
    return diffs == sorted(knight)


def can_balance(items):
    for mid in range(len(items)):
        left = sum((mid - i) * items[i] for i in range(mid))
        right = sum((i - mid) * items[i] for i in range(mid + 1, len(items)))
        if left == right:
            return mid
    return -1


def seven_zero(n):
    d = 1
    while True:
        for k in range(d if n % 2 and n % 5 else 1, d + 1):
            num = int('7' * k + '0' * (d - k))
            if num % n == 0:
                return num
        d += 1

def tukeys_ninthers(items):
    while len(items) > 1:
        items = [sorted(items[i:i+3])[1] for i in range(0, len(items), 3)]
    return items[0]

def words_with_letters(words, letters):
    def is_sub(word):
        it = iter(word)
        return all(c in it for c in letters)
    return [word for word in words if is_sub(word)]


def approval_voting(ballots):
    votes = {i: 0 for i in range(len(ballots[0]))}

    for ballot in ballots:
        for i, vote in enumerate(ballot):
            if vote == 'Y':
                votes[i] = votes.get(i, 0) + 1

    result = 0
    max_vote = 0
    for k, v in votes.items():
        if v > max_vote:
            max_vote = v
            result = k
    return result

def expand_intervals(intervals):
    result = []
    if len(intervals) == 0:
        return result
    for v in intervals.split(','):
        if '-' in v:
           i = v.index('-')
           start = int(v[:i])
           end = int(v[i+1:]) + 1
           result+= [k for k in range( start, end)]
        else:
            result.append(int(v))
    return result

def collapse_intervals(items):
    result = []
    if len(items) == 0:
     return ''

    start = items[0]
    prev = items[0]

    def emit(a, b):
        result.append(str(a) if a == b else f'{a}-{b}')
    for item in items[1:]:
        if item == prev + 1:
            prev = item
        else:
            emit(start, prev)
            start = prev = item
    emit(start, prev)
    return ','.join(result)


def give_change(amount, coins):
    result = []
    for coin in coins:
        while coin <= amount:
            result.append(coin)
            amount -= coin
    return result


def safe_squares_rooks(n, rooks):
    occupied_rows = {r for r, c in rooks}
    occupied_cols = {c for r, c in rooks}
    safe_rows = n - len(occupied_rows)
    safe_cols = n - len(occupied_cols)
    return safe_rows * safe_cols


def group_and_skip(n, out, ins):
    result = []
    while n > 0:
        result.append(n % out)
        n = (n // out) * ins
    return result

def collect_numbers(perm):
      n = len(perm)
      inv = [0] * n
      for j, x in enumerate(perm):
          inv[x] = j

      rounds = 1
      for i in range(1, n):
          if inv[i] < inv[i - 1]:
              rounds += 1
      return rounds


def verify_betweenness(perm, constraints):
    pos = [0] * len(perm)
    for i, v in enumerate(perm):
        pos[v] = i
    return all((pos[a] - pos[b]) * (pos[c] - pos[b]) < 0
               for a, b, c in constraints)

def three_summers(items, goal):
      n = len(items)
      for i in range(n - 2):
          need = goal - items[i]
          lo, hi = i + 1, n - 1
          while lo < hi:
              s = items[lo] + items[hi]
              if s == need:
                  return True
              elif s < need:
                  lo += 1
              else:
                  hi -= 1
      return False


def sum_of_two_squares(n):
    lo, hi = 1, isqrt(n)
    while lo <= hi:
        s = lo * lo + hi * hi
        if s == n:
            return hi, lo
        elif s < n:
            lo += 1
        else:
            hi -= 1
    return None


def count_carries(a, b):
    carry = 0
    count = 0
    while a > 0 or b > 0:
        carry = (a % 10 + b % 10 + carry) // 10
        count += carry
        a //= 10
        b //= 10
    return count


def candy_share(candies):
    n = len(candies)
    rounds = 0
    while any(c >= 2 for c in candies):
        new = list(candies)
        for i in range(n):
            if candies[i] >= 2:  # decision uses the round-start state
                new[i] -= 2
                new[(i - 1) % n] += 1
                new[(i + 1) % n] += 1
        candies = new
        rounds += 1
    return rounds


def duplicate_digit_bonus(n):
    s = str(n)
    score = 0
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        k = j - i
        if k > 1:
            block = 10 ** (k - 2)
            if j == len(s):
                block *= 2
            score += block
        i = j
    return score


def ordinal_transform(seed, i):
    seq = list(seed)
    while len(seq) <= i:
        counts = {}
        transform = []
        for x in seq:
            counts[x] = counts.get(x, 0) + 1
            transform.append(counts[x])
        seq = seq + transform
    return seq[i]

def squares_intersect(s1, s2):
      x1, y1, r1 = s1
      x2, y2, r2 = s2
      if x1 + r1 < x2 or x2 + r2 < x1:
          return False
      if y1 + r1 < y2 or y2 + r2 < y1:
          return False
      return True


def remove_after_kth(items, k=1):
    counts = {}
    result = []
    for x in items:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] <= k:
            result.append(x)
    return result


def count_corners(points):
    pset = set(points)
    cols = {}
    for (x, y) in points:
        cols.setdefault(x, []).append(y)

    count = 0
    for (x, y) in points:
        for y2 in cols[x]:
            h = y2 - y
            if h > 0 and (x + h, y) in pset:
                count += 1
    return count


def first_preceded_by_smaller(items, k=1):
    for i, x in enumerate(items):
        if sum(1 for y in items[:i] if y < x) >= k:
            return x
    return None


def count_and_say(digits):
    result = []
    i = 0
    n = len(digits)
    while i < n:
        j = i
        while j < n and digits[j] == digits[i]:
            j += 1
        result.append(str(j - i))
        result.append(digits[i])
        i = j
    return ''.join(result)


def safe_squares_bishops(n, bishops):
    diff = set()
    summ = set()
    for (r, c) in bishops:
        diff.add(r - c)
        summ.add(r + c)

    count = 0
    for r in range(n):
        for c in range(n):
            if (r - c) not in diff and (r + c) not in summ:
                count += 1
    return count


def reverse_vowels(text):
    vowels = [c for c in text if c in 'aeiouAEIOU']
    result = []
    j = len(vowels) - 1
    for c in text:
        if c in 'aeiouAEIOU':
            v = vowels[j]
            j -= 1
            result.append(v.upper() if c.isupper() else v.lower())
        else:
            result.append(c)
    return ''.join(result)


def nearest_polygonal_number(n, s):
    def poly(i):
        return ((s - 2) * i * i - (s - 4) * i) // 2

    a, b = 1, 2
    while poly(b) < n:
        b *= 2
    while b - a >= 2:
        mid = (a + b) // 2
        if poly(mid) <= n:
            a = mid
        else:
            b = mid

    lo, hi = poly(a), poly(b)
    return lo if n - lo <= hi - n else hi


def postfix_evaluate(items):
    stack = []
    for item in items:
        if item in ('+', '-', '*', '/'):
            b = stack.pop()
            a = stack.pop()
            if item == '+':
                stack.append(a + b)
            elif item == '-':
                stack.append(a - b)
            elif item == '*':
                stack.append(a * b)
            else:
                stack.append(a // b if b != 0 else 0)
        else:
            stack.append(item)
    return stack[0]


def subtract_square(queries):
    top = max(queries)
    heat = [False] * (top + 1)
    for n in range(1, top + 1):
        k = 1
        while k * k <= n:
            if not heat[n - k * k]:
                heat[n] = True
                break
            k += 1
    return [heat[q] for q in queries]


def reverse_ascending_sublists(items):
    result = []
    i = 0
    n = len(items)
    while i < n:
        j = i + 1
        while j < n and items[j] > items[j - 1]:
            j += 1
        result.extend(items[i:j][::-1])
        i = j
    return result


def autocorrect_word(word, words, df):
    best = None
    best_dist = None
    for w in words:
        if len(w) != len(word):
            continue
        d = sum(df(a, b) for a, b in zip(word, w))
        if best_dist is None or d < best_dist or (d == best_dist and w < best):
            best = w
            best_dist = d
    return best

# Too slow
def unscramble(words, word):
    target = sorted(word)
    n = len(word)
    return [w for w in words
            if len(w) == n
            and w[0] == word[0]
            and w[-1] == word[-1]
            and sorted(w) == target]


def sort_by_digit_count(items):
    def key(x):
        s = str(x)
        return tuple(s.count(d) for d in '9876543210') + (x,)

    return sorted(items, key=key)


def count_divisibles_in_range(start, end, n):
    return end // n - (start - 1) // n


def bridge_hand_shape(hand):
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    return [sum(1 for _, s in hand if s == suit) for suit in suits]


def frequency_sort(items):
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    decorated = sorted((-counts[x], x) for x in items)
    return [x for (_, x) in decorated]


def balanced_ternary(n):
    result = []
    power = 1
    while n != 0:
        rem = n % 3
        if rem == 0:
            n //= 3
        elif rem == 1:
            result.append(power)
            n = (n - 1) // 3
        else:
            result.append(-power)
            n = (n + 1) // 3
        power *= 3
    return result[::-1]


def count_sevens(n):
    count = 0
    p = 1
    while p <= n:
        higher = n // (p * 10)
        current = (n // p) % 10
        lower = n % p
        if current > 7:
            count += (higher + 1) * p
        elif current == 7:
            count += higher * p + lower + 1
        else:
            count += higher * p
        p *= 10
    return count