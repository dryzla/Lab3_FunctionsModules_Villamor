from telemetry import generate_telemetry
from diagnostics import validate, process_data, find_abnormal

LAST_NAME = "Villamor"
STUDENT_ID = "TUPM-26-3469"
SEED_NUM = int(STUDENT_ID[-1])
FAVORITE_ARTIST = "Steve Lacy"


def monitor(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}")
        return result

    return wrapper


@monitor
def run_monitoring():

    telemetry = generate_telemetry(
        LAST_NAME,
        SEED_NUM,
        FAVORITE_ARTIST
    )

    valid_data = []
    invalid_data = []

    for value in telemetry:
        try:
            if validate(value):
                valid_data.append(value)
            else:
                invalid_data.append(value)
        except ValueError as error:
            print("Error:", error)

    processed = process_data(valid_data)
    abnormal = find_abnormal(valid_data)

    print("\nStudent-Specific Inputs:")
    print("LAST_NAME:", LAST_NAME)
    print("SEED_NUM:", SEED_NUM)
    print("FAVORITE_ARTIST:", FAVORITE_ARTIST)

    print("\nGenerated Telemetry Data:")
    print(valid_data)

    print("\nValid/Invalid Results:")
    print("Valid:", len(valid_data))
    print("Invalid:", len(invalid_data))

    print("\nProcessed Results:")
    print(processed)

    print("\nRecursive Analysis:")
    print(abnormal)

    print("\nFinal Diagnostic Summary:")
    if abnormal:
        print("ABNORMAL CONDITION DETECTED")
    else:
        print("SYSTEM NORMAL")


run_monitoring()