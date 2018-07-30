
import random

class Groupper(object):
    def __init__(self, names):
        self.names = names

    def random_group(self, group_count):
        group = []
        for j in range(len(self.names)):
            i = random.randint(0, len(self.names) - 1)
            names = self.names.pop(i)
            group.append(names)
        print(group[0:3])
        print(group[3:6])
        print(group[6:9])
        print(group[9:13])

if __name__ == '__main__':
    groupper = Groupper(
        ['김철수', '이명희', '천영희', '박석현', '홍길동', '장길산', '전지현', '김수현', '지현우', '휘성', '쥐디', '강백호', '서태웅'])
    groupper.random_group(4)
    # print(random.randint(0, 1))

    # print(random.randint(0, 1))
    # print(random.randint(0, 1))
    # print(random.randint(0, 1))
