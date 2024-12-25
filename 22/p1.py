
def mrand(salt):
  secret = salt
  while True:
    secret = ((secret << 6) ^ secret) & 0xFFFFFF
    secret = ((secret >> 5) ^ secret) & 0xFFFFFF
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

