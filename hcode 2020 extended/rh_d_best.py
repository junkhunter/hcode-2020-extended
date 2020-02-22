import math

nb_b, nb_lib, days_limit = list(map(int, input().rstrip().split()))

s = list(map(int, input().rstrip().split()))

libs = []
book_possesor = {}
min_index = 0
for x in range(nb_lib):
    cur_l = {}
    cur_l['index'] = len(libs)
    for k, i in zip(['b', 'sd', 'bpd'], list(map(int, input().rstrip().split()))):
        cur_l[k] = i
    cur_l['score'] = {}
    cur_l['books'] = {}
    for book in sorted(list(map(int, input().rstrip().split())), key=lambda x : s[x])[::-1]:
        cur_l['books'][book] = s[book]
        book_possesor[book] = book_possesor.get(book, []) + [cur_l]
    cur_l['id'] = x
    cur_l['sqsd'] = cur_l['sd'] * cur_l['sd']
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

abs = lambda x : -x if x < 0 else x

def get_score_bd(lib, dl=-1):
    if dl == -1:
        dl = days_limit
    if dl not in lib['score']:
        # lib['books'] = [i for i in lib['books'] if i not in placed_lib]
        # print('eval lib {}:'.format(lib['id']))
        # return lib['sd']
        size = minimum(lib['bpd'] * (dl - lib['sd']), len(lib['books']))
        # print('minimum({}, {})'.format(lib['bpd'] * (dl - lib['sd']), len(lib['books'])))
        if size > 0:
            lib['score'][dl] = sum([s[i] for i in list(lib['books'].keys())[:size]]) / ((lib['sd']))
            return lib['score'][dl]
            # return sum([s[i] for i in list(lib['books'].keys())[:size]]) / (lib['sd'] + abs(len(lib['books']) - size))
        return 0
    return lib['score'][dl]

placed_lib = []
save_days_limit = days_limit
libs = sorted(libs, key=get_score_bd, reverse=True)
while days_limit > 0 and libs != []:
    lib = libs.pop(0)
    if lib['sd'] >= days_limit or lib['books'] == []:
        del lib
        continue
    size = minimum(lib['bpd'] * (days_limit - lib['sd']), len(lib['books']))
    if size <= 0:
        del lib
        continue
    lib['potentiel'] = size - len(lib['books'])
    lib['book_placed'] = list(lib['books'].keys())[:size]
    placed_lib.append(lib)
    for book in lib['book_placed']:
        for x in book_possesor[book]:
            del x['books'][book]
    days_limit -= lib['sd']
    libs = sorted(libs, key=get_score_bd, reverse=True)


# for lib in placed_lib:
#     lib['score'] = sum([s[i] for i in lib['book_placed']])

for x in range(len(placed_lib)):
    swapped = False
    days_limit = save_days_limit - placed_lib[0]['sd']
    for i in range(1, len(placed_lib) - x):
        next_dl = days_limit - placed_lib[i]['sd']
        dl_swap = next_dl + placed_lib[i-1]['sd']

        lst_bp = list(placed_lib[i-1]['book_placed'])
        new_book1 = lst_bp[:len(lst_bp) + minimum(0, placed_lib[i]['potentiel'] - placed_lib[i]['sd'] * placed_lib[i-1]['bpd'])]
        new_book2 = placed_lib[i]['book_placed'] + list(placed_lib[i]['books'].keys())[placed_lib[i-1]['sd'] * placed_lib[i]['bpd']:]
        
        score1 = sum([s[i] for i in new_book1])
        score2 = sum([s[i] for i in new_book2])
        
        save_books = placed_lib[i-1]['books']
        placed_lib[i-1]['books'] = {**{x : s[x] for x in placed_lib[i-1]['book_placed']}, **placed_lib[i-1]['books']}
        diff1 = score1 - get_score_bd(placed_lib[i-1], days_limit + placed_lib[i-1]['sd'])
        # placed_lib[i-1]['score'][days_limit + placed_lib[i-1]['sd']]
        placed_lib[i-1]['books'] = save_books
        save_books = placed_lib[i]['books']
        placed_lib[i]['books'] = {**{x : s[x] for x in placed_lib[i]['book_placed']}, **placed_lib[i]['books']}
        diff2 = score2 - get_score_bd(placed_lib[i], days_limit)
        placed_lib[i]['books'] = save_books
        # print('p_l[i][sd] * p_l[i-1][bpd]', placed_lib[i]['sd'] * placed_lib[i-1]['bpd'], 
        #     '\np_l[i-1][score]',  placed_lib[i-1]['score'][days_limit + placed_lib[i-1]['sd']], 
        #     'score1', score1, 
        #     '\nplaced_lib[i][score][days_limit]', placed_lib[i]['score'][days_limit], 'score2', score2)
        # get_score_bd(placed_lib)[i-1], dl_swap)
        if abs(diff2) > abs(diff1):
            placed_lib[i-1]['books'] = {z : s[z] for z in [x for x in new_book1 if x not in placed_lib[i-1]['books']] + list(placed_lib[i-1]['books'].keys())}
            placed_lib[i-1]['book_placed'] = new_book1
            placed_lib[i-1]['score'][days_limit] = score1
            placed_lib[i]['books'] = {z : s[z] for z in [x for x in placed_lib[i]['books'] if x in new_book2]}
            placed_lib[i]['book_placed'] = new_book2
            placed_lib[i]['score'][days_limit + placed_lib[i]['sd']] = score1
            placed_lib[i], placed_lib[i-1] = placed_lib[i-1], placed_lib[i]
            # print('diff1', diff1, 'diff2', diff2)
            swapped = True
        days_limit = next_dl
    if swapped == False:
        break

print('score : ', sum([s[i] for l in placed_lib for i in l['book_placed']]))
# print(len(placed_lib))
# for lib in placed_lib:
#     print('{} {}'.format(lib['id'], len(lib['book_placed'])))
#     print(' '.join(list(map(str, lib['book_placed']))))
