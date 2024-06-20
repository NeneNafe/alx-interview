#!/usr/bin/python3
""" a Prim game function """


def isWinner(x, nums):
    """ a function to find a winner between two players """
    # Determine the maximum number in nums
    max_num = max(nums)

    # Fine all prime numbers
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] is True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1

    primes = [i for i in range(max_num + 1) if is_prime[i]]

    def play_game(n):
        remaining_primes = [p for p in primes if p <= n]
        move_count = 0

        while remaining_primes:
            current_prime = remaining_primes.pop(0)
            remaining_primes = [p for p in remaining_primes
                                if p % current_prime != 0]
            move_count += 1

        return move_count

    # Count the wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = play_game(n)
        if moves % 2 == 1:  # Maria wins if the number of moves is odd
            maria_wins += 1
        else:  # Ben wins if the number of moves is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
