# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self, vertex_lst, max_len, str_len):
        self.grh = {}
        self.max_len = max_len
        self.str_len = str_len
        self.add_vertex(vertex_lst)

    def add_vertex(self, vertex_lst):
        for item in set(vertex_lst):
            print(item)
            self.grh[item] = []
        for index, key in enumerate(vertex_lst):
            self.grh[key].append(index + 1)

    def get_picture_count(self):
        value = 0
        for item in self.grh.keys():
            value += self.get_group_list(item)
        return value

    def get_group_list(self, key):
        print("key", key)
        p_list = self.grh[key]
        o_list = []
        for x in range(len(p_list)):
            if not p_list[x] % self.str_len == 0 and x != len(p_list) - 1:
                if p_list[x] + 1 == p_list[x + 1]:
                    if not any(p_list[x] in item for item in o_list):
                        o_list.append([p_list[x], p_list[x + 1]])
                    print(o_list)
            if p_list[x] + self.str_len in p_list:
                if any(p_list[x] in item for item in o_list):
                    for item in o_list:
                        if p_list[x] in item:
                            item.append(p_list[x] + self.str_len)
            else:
                if not any(p_list[x] in item for item in o_list):
                    o_list.append([p_list[x]])
        print(o_list)
        return len(o_list)

    def print_vertex(self):
        return self.grh


class NProcess:
    def __init__(self, input_lst):
        self.source = input_lst
        self.max_len = self.get_max_len(input_lst)
        self.str_len = self.get_str_len(input_lst)
        self.final_lst = self.get_vertex_list(input_lst)
        one = Node(self.final_lst, self.max_len, self.str_len)
        print(one.print_vertex())
        value = one.get_picture_count()
        print("Picture Count", value)

    def get_vertex_list(self, input_lst):
        new_lst = []
        for item in input_lst:
            print(item)
            lst = list(str(item))
            new_lst.append(lst)
        org_lst = []
        for item in new_lst:
            org_lst += item
        return org_lst

    def get_max_len(self, input_lst):
        if len(input_lst) == 0:
            return 0
        return len(input_lst) * len(input_lst[0])

    def get_str_len(self, input_lst):
        if len(input_lst) == 0:
            return 0
        return len(input_lst[0])


lst = ["aabba", "aabbc", "abbca"]
one = NProcess(lst)
