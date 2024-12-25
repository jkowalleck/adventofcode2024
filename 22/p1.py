def mix(value, secret):
  return value ^ secret


def prune(secret):
  return secret % 16777216


def mrand(salt):
  secret = salt
  while True:
    # Step 1: Multiply by 64
    secret = ((secret << 6) ^ secret) & 0xFFFFFF

    # Step 2: Divide by 32 and round down to the nearest integer
    secret = ((secret >> 5) ^ secret) & 0xFFFFFF

    # Step 3: Multiply by 2048
    secret = ((secret << 11) ^ secret) & 0xFFFFFF

    yield secret


mrg = mrand(123)
print(next(mrg))
print(next(mrg))
print(next(mrg))
print(next(mrg))
print(next(mrg))
print(next(mrg))
print(next(mrg))
print(next(mrg))
print(next(mrg))
print(next(mrg))
