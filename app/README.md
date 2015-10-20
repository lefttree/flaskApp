## `__init_.py`

`__init__.py` is used to initialize Python packages, tells the python interpreter
that the directory should be treated like a python package.

### setup package level

It can be empty but it is often used to perform setup for the package.

One common thing to do is to import selected Classes, functions to make them
available at the package level.


### `__all__`


`__all__` is a list containing the names of modules that you want to be imported with `import *` so looking at our above example again if we wanted to import the submodules in subpackage the `__all__` variable in subpackage/__init__.py would be:

`__all__ = ['submodule1', 'submodule2']`

`from subpackage import *` would import submodule1 and submodule2


## My `__init__.py`

```python
from flask import Flask

app = Flask(__name__)
from app import views
```

import views is at last line because `views.py` would import the app variable, it 
avoids the circular import error.
