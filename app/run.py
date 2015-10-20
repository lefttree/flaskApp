#!flask/bin/python
""" start the server """

# import app variable from our app package
from app import app
app.run(debug=True)
