import pytest
import numpy as np
import math

import newton2

## Important: structure of tests assumes a dictionary with an 'x'
## key as the output. 

def test_basic_function():
    assert np.isclose(newton2.find(2.95, np.cos)['x'], math.pi)

def test_bad_input():8
    with pytest.raises(TypeError):   
        newton2.find(np.cos, 2.95)
    ## Ideally, our function would raise the exception with a useful message.
    with pytest.raises(TypeError, match='`x0` must be numeric'):
        newton2.find(np.cos, 2.95)

