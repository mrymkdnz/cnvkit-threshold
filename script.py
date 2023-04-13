import math

def calculate_thresholds(target_avg_size):
    thresholds = []
    for cn in range(5):
        threshold = math.log2((cn + 0.5) / 2)
        threshold *= math.sqrt(target_avg_size / 100.0)
        thresholds.append(threshold)
    return thresholds


thresholds = calculate_thresholds(50)
print(thresholds)
