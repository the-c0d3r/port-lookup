#!/usr/bin/env python3
import csv
import os
import sys


class lookup:
    """ A control class for lookuping query """
    def __init__(self):
        """ init the default class variables """
        self.csvfile = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "port.csv"
        self.database = []

    def sort(self, data):
        """
        To sort the values so that the row with official "i" status
        comes before the unofficial "o" ones
        :param data: a list of rows
        :output: sorted list
        """
        return sorted(data, key=lambda t: ord(t.type[0]))

    def run(self, query=None):
        """ The startup function to handle query """

        with open(self.csvfile) as db:
            for row in csv.reader(db):
                # create Record Object
                self.database.append(Record(row))

        if query == None:
            query = input("Enter (port number) or (service) : ")

        if query.isdigit():
            result = self.query_port(int(query))
            # Means the query is port
            if len(result) > 0:
                print("\n")
                print("{} Records found".format(len(result)))
                self.print_result(result)
                print("\n")
            else:
                print("\nNo result found for [{}]\n".format(query))
        else:
            # Means the query is service
            result = self.query_service(query)
            if len(result) > 0:
                print("\n")
                print("{} Records matched [{}]".format(len(result),query))
                self.print_result(result)
                print("\n")
            else:
                print("\nNo result found for [{}]\n".format(query))

    def query_service(self, query):
        """
        For searching the service in record.name, and/or record.description
        :param query: a string to search for
        """
        matched = []
        for row in self.database:
            if query.lower() in row.name.lower() or query.lower() in row.description.lower():
                matched.append(row)
        return self.sort(matched)

    def query_port(self, port):
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
        portspace = 0
        # Ugly hack to find the max lenght for port field
        # Change it if possible
        for r in data:
            if isinstance(r.portrange, list):
                tmp = len(str(r.portrange[0])) + len(str(r.portrange[-1])) + 1
                if tmp > portspace:
                    portspace = tmp
            else:
                if len(str(r.portrange)) > portspace:
                    portspace = len(str(r.portrange))

        for row in data:
            if isinstance(row.portrange, list):
                ports = str(row.portrange[0]) + "-" + str(row.portrange[-1])
            else:
                ports = row.portrange
            print("| {:{}} | {:<{}} | ({:^{}}) | {}".format(
                row.name if row.name else "",
                7 if leftspace == 0 else leftspace,
                ports, portspace, row.proto, 7, row.description
            ))

class Record:
    """ A record object to handle each row of record """
    def __init__(self, row):
        """ :param row: A 'list' of row """
        self.name = row[3] #"" if row[3] == "#" else row[3]
        self.proto = row[2]
        self.portrange = int(row[0]) if row[0] == row[1] else [port for port in range(int(row[0]), int(row[1])+1)]
        # 2 possibilities for portrange, 1. just a single int, 2. a range of int in list format
        self.description = row[4]
        self.type = row[5]

    def __str__(self):
        return "{} ({}) : {} | {}".format(self.name, self.proto, self.portrange, self.description)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Port lookup tool")
        lookup().run()
    else:
        if len(sys.argv) > 2:
            query = " ".join([i for i in sys.argv if sys.argv.index(i) >= 1])
            print(query)
        else:
            query = sys.argv[1]
        lookup().run(query)
