import re
from decimal import Decimal

from input import inp

blocks = inp('kow')

pat_button = re.compile(r'^Button .: X\+(\d+), Y\+(\d+)$')
pat_prize = re.compile(r'^Prize: X=(\d+), Y=(\d+)$')

offset = 10000000000000

res = 0

for block in blocks:
    block = block.split('\n')
    ax, ay = map(Decimal, pat_button.match(block[0]).groups())
    bx, by = map(Decimal, pat_button.match(block[1]).groups())
    px, py = map(Decimal, pat_prize.match(block[2]).groups())
    px, py = offset + px, offset + py
    """original equations:
    px = ax * an + bx * bn
    py = ay * an + by * bn
    """
    bn = (px - (ax * py / ay)) / (bx - (ax * by / ay))
    an = (py - (by * bn)) / ay
    if an < 0 or bn < 0:
        continue
    an, bn = round(an), round(bn)
    if not (
            px == (ax * an) + (bx * bn)
            and py == (ay * an) + (by * bn)
    ):
        continue
    res += (3 * an) + bn

print('res', res)
