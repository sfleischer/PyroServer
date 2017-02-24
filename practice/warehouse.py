from __future__ import print_function
import Pyro4
import person


@Pyro4.expose  # Pyro can access this class remotely
class Warehouse(object):
    def __init__(self):
        self.contents = ["chair", "bike", "flashlight", "laptop", "couch"]

    def list_contents(self):
        return self.contents

    def take(self, name, item):
        self.contents.remove(item)
        print("{0} took the {1}.".format(name, item))

    def store(self, name, item):
        self.contents.append(item)
        print("{0} stored the {1}.".format(name, item))


def main():
    Pyro4.Daemon.serveSimple(
        {
            # other computers can access this daemon
            Warehouse: "example.warehouse"
        },
        ns=True)

    # ns stands for Name Server and is used to register the objects in
    # ns=False means that there is no Name Server and you have to manually copy and paste the server uri to the proxy constructor
    # ns=True means that there is no need to copy and paste. The proxy will
    # try to recognize where the server is.
    # before running the daemon it is crucial to start the name server
    # Start the name server with the following command
    # python -m Pyro4.naming
    # to view objects registered on the name server type the following command
    # python -m Pyro4.nsc list


if __name__ == "__main__":
    main()

    # when the daemon starts it will print something like
    #  uri = PYRO:example.warehouse@localhost:61019
    # the user needs a proxy to connect to the standalone warehouse
