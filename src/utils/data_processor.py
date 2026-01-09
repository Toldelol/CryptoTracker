def process_data(prices):
    if not prices or len(prices) == 0:
        return 0, 0
    avg = sum(prices) / len(prices)
    first = prices[0]
    last = prices[-1]
    change = ((last - first) / first * 100) if first != 0 else 0
    return avg, change