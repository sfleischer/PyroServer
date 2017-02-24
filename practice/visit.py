from person import Person
import sys
import Pyro4

if sys.version_info < (3, 0):
    input = raw_input

# uri = input("Enter the uri of the warehouse: ").strip()
# use the above if there is no Name Server (manual entry)
# there are many configurations of the server ie. PYRO (normal simple
# server) PYRONAME (a normal server with a Name Server)
warehouse = Pyro4.Proxy("PYRONAME:example.warehouse")

# the excepthook is useful for tracing exceptions in the Pyro object
sys.excepthook = Pyro4.util.excepthook

# Pyro will forward warehouse calls to the remote warehouse
janet = Person("Janet")
henry = Person("Henry")
janet.visit(warehouse)
henry.visit(warehouse)
