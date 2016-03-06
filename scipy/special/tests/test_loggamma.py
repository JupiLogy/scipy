import numpy as np
from scipy.special._testutils import FuncData
from scipy.special import gamma, gammaln, loggamma


def test_identities1():
    # test the identity exp(loggamma(z)) = gamma(z)
    x = np.array([-99.5, -9.5, -0.5, 0.5, 9.5, 99.5])
    y = x.copy()
    x, y = np.meshgrid(x, y)
    z = (x + 1J*y).flatten()
    dataset = np.vstack((z, gamma(z))).T

    def f(z):
        return np.exp(loggamma(z))

    FuncData(f, dataset, 0, 1, rtol=1e-14, atol=1e-14).check()


def test_identities2():
    # test the identity loggamma(z + 1) = log(z) + loggamma(z)
    x = np.array([-99.5, -9.5, -0.5, 0.5, 9.5, 99.5])
    y = x.copy()
    x, y = np.meshgrid(x, y)
    z = (x + 1J*y).flatten()
    dataset = np.vstack((z, np.log(z) + loggamma(z))).T

    def f(z):
        return loggamma(z + 1)

    FuncData(f, dataset, 0, 1, rtol=1e-14, atol=1e-14).check()


def test_realpart():
    # Test that the real parts of loggamma and gammaln agree. It would
    # be nice to test for larger orders, but gammaln(-999.5 + 999.5j)
    # returns nans.
    x = np.array([-99.5, -9.5, -0.5, 0.5, 9.5, 99.5])
    y = x.copy()
    x, y = np.meshgrid(x, y)
    z = (x + 1J*y).flatten()
    dataset = np.vstack((z, gammaln(z).real)).T

    def f(z):
        return loggamma(z).real.astype('complex128')
    
    FuncData(f, dataset, 0, 1, rtol=1e-14, atol=1e-14).check()
