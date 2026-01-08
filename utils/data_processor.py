def process_data(prices):
    if not prices:
        return 0, 0
    avg = sum(prices) / len(prices)
    change = (prices[-1] - prices[0]) / prices[0] * 100 if prices[0] != 0 else 0
    return avg, change