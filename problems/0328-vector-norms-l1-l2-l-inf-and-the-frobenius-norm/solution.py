import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here

    sum = 0 
    max = 0 
    sqr = 0 
    if arr.ndim == 2 :
        for i in arr:
            for j in i :
                sum += abs(j)
                sqr += j** 2 
                if abs(j) > max:
                    max = abs(j)
        sqr = float(pow(sqr,0.5) ) 

    else:
        
        for i in arr:
            sum += abs(i)
            sqr += i ** 2
            if abs(i) > max:
                max = abs(i)

        sqr = float(pow(sqr,0.5))


    if norm_type == 'l1' :
        return  float(sum)

    elif norm_type == 'l2' :
        return sqr

    elif norm_type == 'linf':
        return float(max)

    elif norm_type == 'frobenius':
        if arr.ndim == 1: raise ValueError
        else : return sqr

    else: raise ValueError
    pass
