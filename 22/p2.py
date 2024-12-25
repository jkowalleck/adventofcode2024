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


secrets = map(int, open('kow.txt').read().split('\n'))
secret2k = []
for secret in secrets:
  rsecret = mrand(secret)
  for _ in range(2000-1):
    next(rsecret)
  secret2k.append(next(rsecret))

res = sum(secret2k)
print('res', res)

