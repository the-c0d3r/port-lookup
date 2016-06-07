import csv

"""
Can do 2 approaches
1. Only search for the port within the csv, no objects, fast for the first time,
   slower for consequent search
2. Create each object for each row, memory intensive, but faster after consequent search

TODO
1. Write Unittest code
2. Print the official port services first
3. Print it in a table format nicely
"""

class lookup:
    def sort(self, data):
        """
        To sort so that the data with 'i' tag comes first
        'i' refers to the status of the item
        :param data: a list of rows
        :output: sorted list
        """
        return sorted(data, key=lambda t: ord(t.type[0]))

    def run(self):
        """ The startup function to handle query """
        data     = [] # For raw data
        self.database = [] # A list of record objects

        with open("port.csv") as db:
            for row in csv.reader(db):
                data.append(row)

        # Create record objects
        for row in data:
            self.database.append(Record(row))

        while True:
            port = input("Enter port number : ")
            if port != "":
                result = self.query(int(port))
                if len(result) > 0:
                    print("{} Records found".format(len(result)))
                    self.print_result(result)
            else:
                break

    def query(self, port):
        """
        Responsible for querying the database
        :param port: An integer representing the port number to query
        """
        matched = [] # A list to capture matched objects
        for row in self.database:
            # Check if row.portrange is list
            if isinstance(row.portrange, list):
                if port in range(row.portrange[0], row.portrange[1]):
                    matched.append(row)
            else:
                if port == row.portrange:
                    matched.append(row)
        result = self.sort(matched)
        return result

    def print_result(self, data):
        """
        To print the result in a nicely formated table
        :param data: A list of record objects that matches the query
        """
        leftspace = max([len(d.name) for d in data])
        for row in data:
            print("| {:{}} | {}".format(row.name, leftspace, row.description))

class Record:
    """ A record object to handle each row of record """
    def __init__(self, row):
        """ :param row: A 'list' of row """
        # 22,22,"tcp/udp","ssh","SSH Remote Login Protocol","i"
        self.name = "" if row[3] == "#" else row[3]
        self.portrange = int(row[0]) if row[0] == row[1] else [int(row[0]), int(row[1])]
        self.description = row[4]
        self.type = row[5]

    def __str__(self):
        return "{} : {} | {}".format(self.name, self.portrange, self.description)

    def check(self, query):
        """ Returns the port information if it matches, else nothing """
        return self.desc if query == self.port else ""

if __name__ == "__main__":
    print("Port lookup tool")
    lookup().run()
