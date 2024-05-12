import pytest
from utils.sicp_data_abstraction import SICP

sicp = SICP()


class TestPair:
    def test_pair(self):
        x, y = (1, 2)
        got = sicp.pair(x, y)
        want = "[1, 2]"
        assert str(got) == want


INDEX_ERROR_MSG = "list index out of range"


class TestHeadTail:
    def test_head(self):
        data = [1, 2]
        got = sicp.head(data)
        want = 1
        assert got == want

    def test_head_empty(self):
        data = []
        with pytest.raises(IndexError, match=INDEX_ERROR_MSG):
            sicp.head(data)

    def test_tail(self):
        data = [4, 3]
        got = sicp.tail(data)
        want = 3
        assert got == want

    def test_tail_only_one_element(self):
        data = [4]
        with pytest.raises(IndexError, match=INDEX_ERROR_MSG):
            sicp.tail(data)

    def test_tail_empty(self):
        data = []
        with pytest.raises(IndexError, match=INDEX_ERROR_MSG):
            sicp.tail(data)


class TestIsNone:
    def test_is_none(self):
        item = None
        got = sicp.is_none(item)
        assert got is True

    def test_is_none_empty_list(self):
        item = []
        got = sicp.is_none(item)
        assert got is True

    def test_is_not_none(self):
        item = [None]
        got = sicp.is_none(item)
        assert got is False


class TestCreatelist:
    def test_create_list(self):
        params = (1, 2, 3, 4)
        got = sicp.create_list(*params)
        want = "[1, [2, [3, [4, None]]]]"
        assert str(got) == want

    def test_create_list_none(self):
        params = ()
        got = sicp.create_list(*params)
        assert got is None

    def test_create_list_one_element(self):
        params = (5,)
        got = sicp.create_list(*params)
        want = "[5, None]"
        assert str(got) == want


class TestIsEqual:
    def test_is_equal(self):
        seq_1 = sicp.create_list(1, 2)
        seq_2 = sicp.create_list(1, 2)
        got = sicp.is_equal(seq_1, seq_2)
        assert got is True


class TestPrint:
    def test_print(self, capfd):
        seq = sicp.create_list(1, 2, 3)
        sicp.print(seq)
        captured = capfd.readouterr()
        assert captured.out == "[1, [2, [3, None]]]\n"


class TestListRef:
    def test_list_ref_first(self):
        seq = sicp.create_list(50, 2, 200)
        got = sicp.list_ref(seq, 0)
        want = 50
        assert got == want

    def test_list_ref_last(self):
        seq = sicp.create_list(50, 2, 200)
        got = sicp.list_ref(seq, 2)
        want = 200
        assert got == want

    def test_list_ref_out_of_range(self):
        seq = sicp.create_list(100, 3, 500)
        with pytest.raises(TypeError, match="'NoneType' object is not subscriptable"):
            sicp.list_ref(seq, 4)


class TestLength:
    def test_length(self):
        seq = sicp.create_list(50, 32, 40, 40)
        got = sicp.length(seq)
        want = 4
        assert got == want

    def test_length_zero(self):
        seq = sicp.create_list()
        got = sicp.length(seq)
        want = 0
        assert got == want


class TestAppend:
    def test_append(self):
        # setting up
        seq_1 = sicp.create_list(1, 2)
        seq_2 = sicp.create_list(4, 5)

        # executing
        result = sicp.append(seq_1, seq_2)

        # comparing with previous helper methods
        want = sicp.create_list(1, 2, 4, 5)
        got = sicp.is_equal(result, want)

        assert got is True

    def test_append_seq_1_empty(self):
        seq_1 = sicp.create_list()
        seq_2 = sicp.create_list(4, 5)

        result = sicp.append(seq_1, seq_2)

        want = "[4, [5, None]]"
        assert str(result) == want

    def test_append_seq_2_empty(self):
        seq_1 = sicp.create_list(1, 2)
        seq_2 = sicp.create_list()

        result = sicp.append(seq_1, seq_2)

        want = "[1, [2, None]]"
        assert str(result) == want
