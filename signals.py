def static_signal(traffic):
    return sum(traffic.values()) * 30

def smart_signal(traffic, waiting):
    scores = {}  

    for lane in traffic:
        scores[lane] = (0.7 * traffic[lane]) + (0.3 * waiting[lane])

    best_lane = max(scores, key=scores.get)

    return sum(scores.values()), best_lane
