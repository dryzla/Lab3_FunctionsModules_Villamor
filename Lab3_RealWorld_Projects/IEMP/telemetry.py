def generate_telemetry(last_name, seed, artist):
    artist_value = sum(ord(c) for c in artist if c.isalpha())
    base = len(last_name) * seed

    for i in range(8):
        value = base + ((i * seed + artist_value) % 41) - 20
        yield value