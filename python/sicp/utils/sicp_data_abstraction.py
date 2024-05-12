class SICP:
    def pair(self, x, y):
        return [x, y]

    def head(self, pair):
        return pair[0]

    def tail(self, pair):
        return pair[1]

    def is_none(self, item):
        return item is None or (isinstance(item, list) and len(item) == 0)

    def is_pair(self, items):
        return isinstance(items, list) and len(items) == 2

    def cadr(self, pair):
        return self.head(self.tail(pair))

    def create_list(self, *args):
        if len(args) > 1:
            return self.pair(args[0], self.create_list(*args[1:]))
        elif len(args) == 0:
            return None
        else:
            return self.pair(args[0], None)

    def is_equal(self, seq_1, seq_2):
        return str(seq_1) == str(seq_2)

    def print(self, seq):
        return print(str(seq))

    def list_ref(self, seq, n):
        if n == 0:
            return self.head(seq)
        return self.list_ref(self.tail(seq), n - 1)

    def length(self, seq):
        def length_iter(s, count):
            if self.is_none(s):
                return count
            return length_iter(self.tail(s), count + 1)

        return length_iter(seq, 0)

    def append(self, seq_1, seq_2):
        if self.is_none(seq_1):
            return seq_2
        return self.pair(self.head(seq_1), self.append(self.tail(seq_1), seq_2))
