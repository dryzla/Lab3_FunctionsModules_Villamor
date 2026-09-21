## Recursive Fault Trace [RFT]

LAST_NAME = "Villamor"
STUDENT_ID = "TUPM-26-3469"
SEED_NUM = int(STUDENT_ID[-1])
FAVORITE_ARTIST = "Steve Lacy"

def generate_fault_code(last_name, seed, artist):
    surname_value = sum(ord(c) for c in last_name)
    artist_value = sum(ord(c) for c in artist if c.isalpha())

    return (surname_value + seed * 100 + artist_value) % 9000 + 1000

def trace_fault(code, trace=None, calls=0):
    if trace is None:
        trace = []

    trace.append(code)
    calls += 1

    # Base condition
    if code <= 100:
        return trace, calls

    return trace_fault(code // 2, trace, calls)

fault_code = generate_fault_code(
    LAST_NAME, SEED_NUM, FAVORITE_ARTIST
)

trace, recursive_calls = trace_fault(fault_code)

print("Generated Fault Data:", fault_code)
print("Recursive Trace:", trace)
print("Number of Recursive Calls:", recursive_calls)
print("Final Result:", trace[-1])