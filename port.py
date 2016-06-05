import csv


class lookup:
    """ A control class for lookup function """
    def run():
        """ The startup function to handle query """
        port = input("Enter port number : ")
        self.query(port)
    
class record:
    """ A record object to handle each row of record """
    def __init__(self, row):
        """ :param row: A 'list' of row """
        # 22,22,"tcp/udp","ssh","SSH Remote Login Protocol","i"
        data = row.split(",")
        self.name = "" if data[3] == "#" else data[3]
        self.portrange = data[0] if data[0] == data[1] else [data[0], data[1]]
        self.description = data[4]

    def __str__(self):
        return "{}: {} | {}".format(self.name, self.portrange, self.description)

    def check(self, query):
        """ Returns the port information if it matches, else nothing """
        return self.desc if query == self.port else ""

if __name__ == "__main__":
    lookup().run()
