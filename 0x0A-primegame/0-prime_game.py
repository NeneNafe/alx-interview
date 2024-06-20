#!/usr/bin/python3
""" a Prime game module """


def isWinner(x, nums):
    """ a function to find a winner between two players """
    # Return None when invalid option has been picked
    if not nums or x < 1:
        return None
    max_num = max(nums)

    # Initialize a list to determine prime status of
    # numbers up to max_num
    is_prime = [True for _ in range(max(max_num + 1, 2))]

    # Implement the Sieve of Eratosthenes
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[i]:
            continue

        # Mark multiples of i as non-prime
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False

    # Mark 0 and 1 as non-prime explicitly
    is_prime[0] = is_prime[1] = False

    # y will count the number of primes up to each index
    y = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            y += 1
        # Store the count of primes up to index i in is_prime[i]
        is_prime[i] = y

    player_1 = 0
    for p in nums:
        # Maria wins if the count of primes up to p is odd
        player_1 += is_prime[p] % 2 == 1

    # Determine the overall winner
    if player_1 * 2 == len(nums):
        # If Maria and Ben win the same number of rounds, it's a tie
        return None

    if player_1 * 2 > len(nums):
        return "Maria"  # Maria wins more rounds than Ben

    return "Ben"  # Ben wins more rounds than Maria
