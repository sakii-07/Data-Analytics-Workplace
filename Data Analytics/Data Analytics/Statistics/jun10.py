# Binomial distribution

from scipy.stats import binom
p = 0.6
k = 6
n = 10
print(binom.pmf(k,n,p)) # 0.2508226559999998

p = 0.8
k = 7
n = 10
print(binom.pmf(k,n,p)) # 0.20132659199999978

# poission probability distribution
from scipy.stats import poisson
lam = 50
k = 10
print(poisson.pmf(k, lam)) # 5.190544459331622e-12