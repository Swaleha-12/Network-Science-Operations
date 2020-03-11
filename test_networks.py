import collections
from networks import *
from urllib.request import urlopen

path = 'https://waqarsaleem.github.io/cs201/hw3/'


def fetch_testcases(path):
    TestCase = collections.namedtuple(
        'TestCase', ['file', 'op', 'vtx', 'result'])
    testcases = []
    csv_lines = [line.decode('utf-8').strip()
                 for line in urlopen(path).readlines()[1:]]
    for row in csv_lines:
        if not row:
            continue
        row = [r.strip() for r in row.split(',')]
        case = TestCase(*row)
        testcases.append(case)
    return testcases


cases = fetch_testcases(path+'cases.csv')
# print(cases)


def fetch_content(fname):
    fname += '.txt'
    try:
        return open(fname).read()
    except FileNotFoundError:
        global path
        fstr = urlopen(path+'datasets/'+fname).read().decode('utf-8').strip()
        open(fname, 'w').write(fstr)
        return fstr


def test_degree_centrality_set():
    fname = ''
    for case in cases:
        if case.op == 'C_D':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='sets')
            v = int(case.vtx.strip())
            myresult = round(100 * NetworkOperations.degree_centrality(g, v))
            assert int(case.result) == myresult, \
                'SetGraph failed degree centrality. '\
                f'myresult: {myresult}, testcase: {case}'


def test_degree_centrality_matrix():
    fname = ''
    for case in cases:
        if case.op == 'C_D':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='matrix')
            v = int(case.vtx.strip())
            myresult = round(100 * NetworkOperations.degree_centrality(g, v))
            assert int(case.result) == myresult, \
                'AdjacencyMatrix failed degree centrality. '\
                f'myresult: {myresult}, testcase: {case}'


def test_degree_centrality_list():
    fname = ''
    for case in cases:
        if case.op == 'C_D':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='list')
            v = int(case.vtx.strip())
            myresult = round(100 * NetworkOperations.degree_centrality(g, v))
            assert int(case.result) == myresult, \
                'AdjacencyList failed degree centrality. '\
                f'myresult: {myresult}, testcase: {case}'


def test_clustering_coefficient_set():
    fname = ''
    for case in cases:
        if case.op == 'C_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='sets')
            v = int(case.vtx.strip())
            myresult = round(
                100 * NetworkOperations.clustering_coefficient(g, v))
            assert int(case.result) == myresult, \
                'SetGraph failed clustering coefficient. '\
                f'myresult: {myresult}, testcase: {case}'


def test_clustering_coefficient_matrix():
    fname = ''
    for case in cases:
        if case.op == 'C_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='matrix')
            v = int(case.vtx.strip())
            myresult = round(
                100 * NetworkOperations.clustering_coefficient(g, v))
            assert int(case.result) == myresult, \
                'AdjacencyMatrix failed clustering coefficient. '\
                f'myresult: {myresult}, testcase: {case}'


def test_clustering_coefficient_list():
    fname = ''
    for case in cases:
        if case.op == 'C_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='list')
            v = int(case.vtx.strip())
            myresult = round(
                100 * NetworkOperations.clustering_coefficient(g, v))
            assert int(case.result) == myresult,\
                'AdjacencyList failed clustering coefficient. '\
                f'myresult: {myresult}, testcase: {case}'


def test_average_neighbor_degree_set():
    fname = ''
    for case in cases:
        if case.op == 'K_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='sets')
            v = int(case.vtx.strip())
            myresult = round(NetworkOperations.average_neighbor_degree(g, v))
            assert int(case.result) == myresult, \
                'SetGraph failed average neighbor degree. '\
                f'myresult: {myresult}, testcase: {case}'


def test_average_neighbor_degree_matrix():
    fname = ''
    for case in cases:
        if case.op == 'K_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='matrix')
            v = int(case.vtx.strip())
            myresult = round(NetworkOperations.average_neighbor_degree(g, v))
            assert int(case.result) == myresult, \
                'AdjacencyMatrix failed average neighbor degree. '\
                f'myresult: {myresult}, testcase: {case}'


def test_average_neighbor_degree_list():
    fname = ''
    for case in cases:
        if case.op == 'K_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='list')
            v = int(case.vtx.strip())
            myresult = round(NetworkOperations.average_neighbor_degree(g, v))
            assert int(case.result) == myresult, \
                'AdjacencyList failed average neighbor degree. '\
                f'myresult: {myresult}, testcase: {case}'


def test_similarity_set():
    fname = ''
    for case in cases:
        if case.op == 'J_ij':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='sets')
            v0, v1 = map(lambda v: int(v.strip()), case.vtx.split(':'))
            myresult = round(100 * NetworkOperations.similarity(g, v0, v1))
            assert int(case.result) == myresult,\
                'SetGraph failed similarity. '\
                f'myresult: {myresult}, testcase: {case}'


def test_similarity_matrix():
    fname = ''
    for case in cases:
        if case.op == 'J_ij':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='matrix')
            v0, v1 = map(lambda v: int(v.strip()), case.vtx.split(':'))
            myresult = round(100 * NetworkOperations.similarity(g, v0, v1))
            assert int(case.result) == myresult,\
                'AdjacencyMatrix failed similarity. '\
                f'myresult: {myresult}, testcase: {case}'


def test_similarity_list():
    fname = ''
    for case in cases:
        if case.op == 'J_ij':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='list')
            v0, v1 = map(lambda v: int(v.strip()), case.vtx.split(':'))
            myresult = round(100 * NetworkOperations.similarity(g, v0, v1))
            assert int(case.result) == myresult,\
                'AdjacencyList failed similarity. '\
                f'myresult: {myresult}, testcase: {case}'


def test_popular_distance_set():
    fname = ''
    for case in cases:
        if case.op == 'D_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='sets')
            v = int(case.vtx.strip())
            myresult = round(NetworkOperations.popular_distance(g, v))
            assert int(case.result) == myresult,\
                'SetGraph failed popular distance. '\
                f'myresult: {myresult}, testcase: {case}'


def test_popular_distance_matrix():
    fname = ''
    for case in cases:
        if case.op == 'D_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='matrix')
            v = int(case.vtx.strip())
            myresult = round(NetworkOperations.popular_distance(g, v))
            assert int(case.result) == myresult,\
                'AdjacencyMatrix failed popular distance. '\
                f'myresult: {myresult}, testcase: {case}'


def test_popular_distance_list():
    fname = ''
    for case in cases:
        if case.op == 'D_i':
            if case.file != fname:
                fname = case.file
                g = Graph(fetch_content(fname), imp='list')
            v = int(case.vtx.strip())
            myresult = round(NetworkOperations.popular_distance(g, v))
            assert int(case.result) == myresult,\
                'AdjacencyList failed popular distance. '\
                f'myresult: {myresult}, testcase: {case}'
