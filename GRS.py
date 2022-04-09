import numpy as np
from numpy.linalg import inv

def GRS(alpha, resids, mu):
    T, N = resids.shape
    L = mu.shape[1]
    mu_mean = np.nanmean(mu, axis=0)
    cov_resids = np.matmul(resids.T, resids) / (T-L-1)
    cov_fac = np.matmul(np.array(mu - np.nanmean(mu, axis=0)).T, np.array(mu - np.nanmean(mu, axis=0))) / T-1
    GRS = (T / N) * ((T - N - L) / (T - L - 1)) * ((np.matmul(np.matmul(alpha.T, inv(cov_resids)), alpha)) / (1 + (np.matmul(np.matmul(mu_mean.T, inv(cov_fac)), mu_mean))))
    pVal = 1-f.cdf(GRS, N, T - N - L)
    return GRS, pVal
