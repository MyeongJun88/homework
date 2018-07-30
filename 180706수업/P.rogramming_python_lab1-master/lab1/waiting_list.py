# TODO : implement WatingList.


class WaitingList(object):
    def __init__(self):
        self.waitinglist = []

    def add_customer(self, name):
        self.waitinglist.append(name)

    def print_current_list(self):
        for name in self.waitinglist:
            print(name)

    def pop_customer(self):
        name = self.waitinglist[0]
        del self.waitinglist[0]
        return name
