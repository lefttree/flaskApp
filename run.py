#!flask/bin/python
import os, sys
""" start the server """

#sys.path.append(os.path.dirname(__file__))

# import app variable from our app package
from app import app
app.run(debug=True)
