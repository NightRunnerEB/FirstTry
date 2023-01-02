import os

# "Dummy" allows all users to login regardless of password
c.JupyterHub.authenticator_class = "dummy"

c.DummyAuthenticator.password = "admin"
