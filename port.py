#!/usr/bin/env python3
import csv, os

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

    def run(self, port=None):
        """ The startup function to handle query """
        csvfile = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "port.csv"
        data = [] # For raw data
        self.database = [] # A list of record objects

        with open(csvfile) as db:
            for row in csv.reader(db):
                data.append(row)

        # Create record objects
        for row in data:
            self.database.append(Record(row))

        if port == None:
            port = input("Enter port number : ")
        if port != "":
            try:
                result = self.query(int(port))
            except ValueError:
                print("[-] Input is not number!")
            else:
                if len(result) > 0:
                    print("\n")
                    print("{} Records found".format(len(result)))
                    self.print_result(result)
                    print("\n")
                else:
                    print("\nNo result found for {}\n".format(port))

    def query(self, port):
        """
        Responsible for querying the database
        :param port: An integer representing the port number to query
        """
        matched = [] # A list to capture matched objects
        for row in self.database:
            # Check if row.portrange is list
            if isinstance(row.portrange, list):
                if port in row.portrange:
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
            print("| {:{}} | ({:^{}}) | {}".format(row.name, 7 if leftspace == 0 else leftspace, row.proto, 7, row.description))


class Record:
    """ A record object to handle each row of record """
    def __init__(self, row):
        """ :param row: A 'list' of row """
        self.name = "" if row[3] == "#" else row[3]
        self.proto = row[2]
        self.portrange = int(row[0]) if row[0] == row[1] else [port for port in range(int(row[0]), int(row[1])+1)]
        # 2 possibilities for portrange, 1. just a single int, 2. a range of int in list format
        self.description = row[4]
        self.type = row[5]

    def __str__(self):
        return "{} ({}) : {} | {}".format(self.name, self.proto, self.portrange, self.description)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1: 
        print("Port lookup tool")
        lookup().run()
    else:
        lookup().run(int(sys.argv[1]))
