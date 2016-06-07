# port-lookup
A small tool to lookup the services associated with the TCP/UDP port numbers

port.csv file from [www.bekkoame.ne.jp](http://www.bekkoame.ne.jp/~s_ita/port/port.csv)

# Features

- type in "ssh" to find the ports related to the query "ssh"
- Or type in "22" to find the services related to "22"

It can be executed by itself, or run it followed by the query
`python3 port.py ssh` or `python3 port.py` and enter the query in prompt.


# TODO

- [ ] Maybe remove the class structure for records again. Since it's only running once, no need to create objects for all rows. It was designed that way at first because I want it to run continuously until user chooses to quit.
- [ ] Make a sort so that the port number come up asending
- [ ] Make it portable so it can be run system wide
