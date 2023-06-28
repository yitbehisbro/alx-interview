#!/usr/bin/python3
"""0x0A. Prime Game"""


def isWinner(x, nums):
    """ Return: name of the player that won the most rounds """
    if nums not instanceof(list):
        return None
    if not nums or x < 1:
        return None
    if not x:
        return None

    def is_prime(n):
        """Checks if prime """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """Gets the value of number which is prime """
        primes = []
        for i in range(2, n+1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        """Lets playing game"""
        primes = get_primes(n)
        turn = 0
        while primes:
            prime = primes.pop(0)
            primes = [x for x in primes if x % prime != 0]
            turn += 1
        return turn % 2 == 0

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Ben"
    elif ben_wins > maria_wins:
        return "Maria"
    else:
        return None
