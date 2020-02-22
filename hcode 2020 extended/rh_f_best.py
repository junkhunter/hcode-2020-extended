import math

nb_b, nb_lib, days_limit = list(map(int, input().rstrip().split()))

s = list(map(int, input().rstrip().split()))

one_element = len(list(dict.fromkeys(s))) == 1

libs = []
book_possesor = {}
min_index = 0
for x in range(nb_lib):
    cur_l = {}
    cur_l['index'] = len(libs)
    for k, i in zip(['b', 'sd', 'bpd'], list(map(int, input().rstrip().split()))):
        cur_l[k] = i
    cur_l['books'] = {}
    for book in sorted(list(map(int, input().rstrip().split())), key=lambda x : s[x])[::-1]:
        cur_l['books'][book] = s[book]
        book_possesor[book] = book_possesor.get(book, []) + [cur_l]
    cur_l['id'] = x
    if cur_l['sd'] < days_limit:
        libs.append(cur_l)

# print('b : {}  l : {}  d : {}\ns : {}\n'.format(nb_b,nb_lib,days_limit,s))

# for n_l,i in enumerate(libs):
#     print('lib {} : {}\n'.format(n_l, i))
# exit()

def minimum(x, y):
    return x if x < y else y

def maximum(x, y):
    return x if x > y else y

average = sum(s) // len(s)
weight_l = average - min(s) + (max(s) - average)
# if average == max:
#     weight_l = 100
# else:
#     weight_l = 2

def get_score_bd(lib):
    # lib['books'] = [i for i in lib['books'] if i not in placed_lib]
    # print('eval lib {}:'.format(lib['id']))
    # return lib['sd']
    size = minimum(lib['bpd'] * (days_limit - lib['sd']), len(lib['books']))
    if one_element:
        return -lib['sd']
    # print('minimum({}, {})'.format(lib['bpd'] * (days_limit - lib['sd']), len(lib['books'])))
    if size > 0: #                                                                                         5106784
        return sum([s[i] for i in list(lib['books'].keys())[:size]]) / maximum((lib['sd'] * lib['sd']) + (lib['bpd'] * (days_limit - lib['sd']) - len(lib['books'])), 0.0000000000001)
    return 0

# def f_cmp(l1, l2):
#     if l1['sd'] > l2['sd']:
#         return 1
#     elif l1['sd'] == l2['sd']:
#         return len(l1['books']) - len(l2['books'])
#     return -1

placed_lib = []
save_days_limit = days_limit
libs = sorted(libs, key=lambda x : get_score_bd(x), reverse=True)
while days_limit > 0 and libs != []:
    lib = libs.pop(0)
    if lib['sd'] >= days_limit or lib['books'] == []:
        continue
    # if one_element:
    size = minimum(lib['bpd'] * (days_limit - lib['sd']), len(lib['books']))
    if size <= 0:
        continue
    lib['book_placed'] = list(lib['books'].keys())[:size]
    placed_lib.append(lib)
    for book in lib['book_placed']:
        for x in book_possesor[book]:
            del x['books'][book]
    libs = sorted(libs, key=lambda x : get_score_bd(x), reverse=True)
    days_limit -= lib['sd']

# placed_lib = sorted(placed_lib, key=lambda x : x['sd'])
print('one ', one_element, '\nscore : ', sum([s[i] for l in placed_lib for i in l['book_placed']]))
# print('score : ', sum([s[i] for l in placed_lib for i in l['book_placed']]))
print(len(placed_lib))
for lib in placed_lib:
    print('{} {}'.format(lib['id'], len(lib['book_placed'])))
    print(' '.join(list(map(str, lib['book_placed']))))
