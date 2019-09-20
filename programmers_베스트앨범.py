def get_total(genre_dict, play_dict) :
    tmp_dict = dict()
    for i in genre_dict :
        if genre_dict[i] not in tmp_dict :
            tmp_dict[genre_dict[i]] = play_dict[i]
        else :
            tmp_dict[genre_dict[i]] += play_dict[i]
    return tmp_dict

def make_dict(li) :
    li_dict = dict()
    for elem in li :
       if elem[0] not in li_dict :
           li_dict[elem[0]] = elem[1]
       else :
           li_dict[elem[0]] += elem[1]
    return li_dict

def get_two_song(ordered, genre_dict, play_dict) :
    ans = []
    for i in range(len(ordered)):
        li = []
        tmp = ordered.pop(0)
        genre = tmp[0]
        for key in genre_dict:
            if genre == genre_dict[key]:
                li.append(play_dict[key])
        li = sorted(li, reverse=True)
        ans.append(li[:2])
    return ans

def get_song_values(ans) :
    final = []
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            final.append(ans[i].pop(0))
    return final

def enum_genres(genres) :
    li = []
    for i, genre in enumerate(genres):
        li.append([i, genre])
    return li

def get_ans(final, play_dict) :
    ans = []
    for i in final:
        for key, value in play_dict.items():
            if value == i and key not in ans:
                ans.append(key)
    return ans

def solution(genres, plays):
    li = enum_genres(genres)
    genre_dict = make_dict(li)
    li = []
    for i, play in enumerate(plays):
        li.append([i, play])
    play_dict = make_dict(li)
    tmp_dict = get_total(genre_dict, play_dict)
    ordered = sorted(tmp_dict.items(), key=lambda x : x[1], reverse=True)
    ans = get_two_song(ordered, genre_dict, play_dict)
    final = get_song_values(ans)
    ans = get_ans(final, play_dict)
    return ans
