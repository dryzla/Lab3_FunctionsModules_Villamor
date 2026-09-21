def validate(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Invalid telemetry value.")

    return 50 <= value <= 90


def process_data(data):
    transform = lambda x: round(x * 1.1, 2)
    return list(map(transform, data))


def find_abnormal(data, index=0, trace=None):
    if trace is None:
        trace = []

    if index >= len(data):
        return trace

    if data[index] > 85:
        trace.append((index, data[index]))

    return find_abnormal(data, index + 1, trace)