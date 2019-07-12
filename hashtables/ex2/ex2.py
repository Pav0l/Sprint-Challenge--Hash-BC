#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    current_ticket = None

    # for every ticket in tickets
    # add it to the hash table key = source, value = destination
    for i in range(length):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)
        # when you find ticket with current location (NONE)
        if tickets[i].source == "NONE":
            # add it to variable `current_ticket`
            current_ticket = tickets[i].destination
            # and make it the first destination of the route
            route[0] = current_ticket

    # then loop over the tickets again
    for i in range(1, length):
        # find the next destination
        dest = hash_table_retrieve(ht, current_ticket)
        # add it to the route array
        route[i] = dest
        # and make it current_ticket
        current_ticket = dest

    return route
