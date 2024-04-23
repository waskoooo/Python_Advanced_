text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")


# occurrences = {}
#
# for symbol in input():
#     occurrences[symbol] = occurrences.get(symbol, 0) + 1
#
# for symbol, time in sorted(occurrences.items()):
#     print(f"{symbol}: {time} time/s")
