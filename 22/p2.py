from collections import deque
from itertools import chain


def mrand(salt):
  secret = salt
  while True:
    secret = ((secret << 6) ^ secret) & 0xFFFFFF
    secret = ((secret >> 5) ^ secret) & 0xFFFFFF
    secret = ((secret << 11) ^ secret) & 0xFFFFFF
    yield secret


secrets = map(int, open('kow.txt').read().split('\n'))
prices_seqs = []
for s, secret in enumerate(secrets):
  print('process secret', s)
  _prices_seqs = {}
  prices_seqs.append(_prices_seqs)

  rsecret = mrand(secret)

  lprice = secret % 10
  prize = next(rsecret) % 10
  price_seq = deque([prize - lprice])
  for _ in range(3):
    lprice = prize
    prize = next(rsecret) % 10
    price_seq.append(prize - lprice)

  for _ in range(2000):
    price_seq_t = tuple(price_seq)
    if price_seq_t not in _prices_seqs:
      _prices_seqs[price_seq_t] = prize
    lprice = prize
    prize = next(rsecret) % 10
    price_seq.append(prize - lprice)
    price_seq.popleft()

print('calc prices_seqs_u')
prices_seqs_u = set(chain.from_iterable(s.keys() for s in prices_seqs))

print('calc prices_seqs_sums')
prices_seqs_sums = {s: sum(ps.get(s, 0) for ps in prices_seqs) for s in prices_seqs_u}

print('calc best_sum')
best_sum = 0
best_k = None
for k, s in prices_seqs_sums.items():
  if s > best_sum:
    best_sum = s
    best_k = k

# 2252

print('best_sum', best_sum)
print('best_k', best_k)
