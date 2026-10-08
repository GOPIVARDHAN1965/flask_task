class PnLCalculator:
    def process_trade(self, trade_id, instrument_id, buy_sell, price, volume):
        pass

    def process_price_update(self, instrument_id, price):
        pass

    def output_worst_trade(self, instrument_id):
        return ""
if __name__ == "__main__":
    import sys

    calculator = PnLCalculator()
    line = sys.stdin.readline().split()
    n = int(line[0])
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "TRADE":
            tradeId = int(line[1])
            instrumentId = line[2]
            buySell = line[3]
            price = int(line[4])
            volume = int(line[5])
            calculator.process_trade(tradeId, instrumentId, buySell, price, volume)
        elif line[0] == "PRICE":
            instrumentId = line[1]
            price = int(line[2])
            calculator.process_price_update(instrumentId, price)
        elif line[0] == "WORST_TRADE":
            instrumentId = line[1]
            print(calculator.output_worst_trade(instrumentId))
        else:
            raise Exception("Malformed input!")