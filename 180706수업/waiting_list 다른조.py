# TODO : implement WatingList.


class WaitingList(object):
    def __init__(self):
        self.waitinglist = []

    def add_customer(self, name):
        self.waitinglist.append(name)
        return self.waitinglist

    def print_current_list(self):
        print (self.waitinglist)

    def pop_customer(self):
        name = self.waitinglist[0]
        del self.waitinglist[0]
        return name
