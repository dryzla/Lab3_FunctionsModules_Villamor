## Equipment Diagnostic System [EDS]

LAST_NAME = "Villamor"
STUDENT_ID = "TUPM-26-3469"
SEED_NUM = int(STUDENT_ID[-1])
FAVORITE_ARTIST = "Steve Lacy"

def generate_readings(last_name, seed, artist):
    artist_value = sum(ord(c) for c in artist if c.isalpha())
    base = len(last_name) * seed + (artist_value % 20)

    return [
        base + ((i * seed + artist_value) % 15) - 7
        for i in range(1, 6)
    ]

def validate_readings(readings):
    return [50 <= value <= 100 for value in readings]

def diagnose(readings):
    average = sum(readings) / len(readings)

    if average >= 75:
        condition = "NORMAL"
    elif average > 60:
        condition = "WARNING"
    else:
        condition = "CRITICAL"

    return average, condition

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_execution
def diagnostic_report():
    readings = generate_readings(
        LAST_NAME, SEED_NUM, FAVORITE_ARTIST
    )

    validation = validate_readings(readings)

    if not all(validation):
        raise ValueError("Invalid equipment reading detected.")

    average, condition = diagnose(readings)

    print("Generated Equipment Data:", readings)
    print("Validation Results:", validation)
    print("Diagnostic Results:")
    print("Average:", average)
    print("Condition:", condition)

diagnostic_report()