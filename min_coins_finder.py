import time


def find_coins_greedy(coins_arr, necessary_sum):
    coins_arr.sort(reverse=True)
    current_sum = 0
    solution = {}

    for coin in coins_arr:
        while current_sum + coin <= necessary_sum:
            current_sum += coin
            solution[coin] = solution.get(coin, 0) + 1

        if current_sum == necessary_sum:
            break

    return solution


def find_min_coins(coins_arr, necessary_sum):
    dp = {}
    coins_arr.sort(reverse=True)

    for amount in range(1, necessary_sum + 1):
        remaining_amount = amount
        dp.setdefault(amount, {})

        for coin in coins_arr:
            if coin <= remaining_amount:
                coin_count = remaining_amount // coin
                dp[amount][coin] = coin_count
                remaining_amount -= coin_count * coin

    return dp[necessary_sum]


def compare_algorithms(coins_arr, necessary_sum):
    start_time = time.time()
    greedy_result = find_coins_greedy(coins_arr, necessary_sum)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(coins_arr, necessary_sum)
    dp_time = time.time() - start_time

    print("Greedy Solution:", greedy_result)
    print(f"Greedy Time: {greedy_time:.10f} seconds")
    print("DP Solution:", dp_result)
    print(f"DP Time: {dp_time:.10f} seconds")


coins_arr = [50, 25, 10, 5, 2, 1]
necessary_sum = 150700
compare_algorithms(coins_arr, necessary_sum)
