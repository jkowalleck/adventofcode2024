import re

from input import inp

have, _, *wants = inp('kow')

have_opt = set(have.split(', '))
for h in tuple(have_opt):
    have_opt.remove(h)
    pat = re.compile(f'^(?:{"|".join(have_opt)})+$')
    if pat.match(h) is None:
        have_opt.add(h)

pat = re.compile(f'^(:?{"|".join(sorted(have_opt))})+$')

print('have_opt:', len(have_opt), sorted(have_opt))
print('pat:', pat)

cnt = 0
for w, want in enumerate(wants):
    print(w)
    if pat.match(want) is not None:
        cnt += 1
print('cnt:', cnt)
