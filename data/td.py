# Exact trace distance between orthogonally-twirled t-copy states (delta=0 and delta=1)
# and the t-copy Haar state, from the closed forms of the thesis (Cor. on rho_O(d,t,0); Eq. for delta=1).
from math import lgamma, exp, log, sqrt
def ldf(n):  # log(n!!)
    if n <= 0: return 0.0
    if n % 2 == 0: return (n//2)*log(2) + lgamma(n//2 + 1)
    return lgamma(n + 1) - ldf(n - 1)
def td0(d, t):
    return (1 - t*(t-1)/((d+t-1)*(d+t-2))) * (1 - exp(lgamma(d+t) - ldf(d-1) - ldf(d+2*t-2)))
def td1(d, t):
    return t*(t-1)/((d+t-1)*(d+t-2))
d = 2**16
tmax = (5 + sqrt(9 + 8*d*log(d/2)))/2
assert abs(td0(d, 1)) < 1e-12 and abs(td1(d, 1)) < 1e-12   # one copy: both are I/d
assert abs(td0(d, 2) - 1/d) / (1/d) < 1e-2                  # t(t-1)/(2d) regime
ts = sorted({int(round(10**(k/50))) for k in range(16, 151)} )
with open("td.txt", "w") as f:
    for t in ts:
        if t < tmax: f.write(f"{t}\t{td0(d,t):.10g}\t{td1(d,t):.10g}\n")
print(len(ts), tmax)
