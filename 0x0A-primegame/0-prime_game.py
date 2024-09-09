#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""

def isWinner(x, nums):
    # Helper function to generate a list of prime numbers up to max_n using Sieve of Eratosthenes
    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False
        return is_prime

    max_n = max(nums)  # The maximum value of n in any round
    is_prime = sieve(max_n)  # Precompute primes up to the largest n in nums

    maria_wins = 0
    ben_wins = 0

    # For each round, simulate the game
    for n in nums:
        if n == 1:
            # If n is 1, Ben wins automatically (no prime numbers)
            ben_wins += 1
            continue

        primes_count = 0  # Count of primes available
        for i in range(1, n + 1):
            if is_prime[i]:
                primes_count += 1

        # If the count of prime picks is odd, Maria wins, otherwise Ben wins
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
