from __future__ import division
import empower.vbsp.project_modules.unique
import numpy as np 

def intersect1d(ar1, ar2, assume_unique=False):
    """
    Find the intersection of two arrays.
    Return the sorted, unique values that are in both of the input arrays.
    Parameters
    ----------
    ar1, ar2 : array_like
        Input arrays.
    assume_unique : bool
        If True, the input arrays are both assumed to be unique, which
        can speed up the calculation.  Default is False.
    Returns
    -------
    intersect1d : ndarray
        Sorted 1D array of common and unique elements.
    See Also
    --------
    numpy.lib.arraysetops : Module with a number of other functions for
                            performing set operations on arrays.
    Examples
    --------
    >>> np.intersect1d([1, 3, 4, 3], [3, 1, 2, 1])
    array([1, 3])
    To intersect more than two arrays, use functools.reduce:
    >>> from functools import reduce
    >>> reduce(np.intersect1d, ([1, 3, 4, 3], [3, 1, 2, 1], [6, 3, 4, 2]))
    array([3])
    """
    if not assume_unique:
        # Might be faster than unique( intersect1d( ar1, ar2 ) )?
        ar1 = empower.vbsp.project_modules.unique(ar1)
        ar2 = empower.vbsp.project_modules.unique(ar2)
    aux = np.concatenate((ar1, ar2))
    aux.sort()
    return aux[:,[-1]][aux[[1],:] == aux[:,[-1]]]