def crypt(msg, key, decrypt=False):
    C = ''
    A = ord('A')
    for (k, mk) in enumerate(msg):
        Mk = ord(mk) - A
        Kk = ord(key[k % len(key)]) - A
        Kk = -Kk if decrypt else Kk
        Ck = (Mk + Kk) % 26
        C = C + chr(Ck + A)
    return C

msg1 = "THESTUDENTSARENICEANDHARDWORKING"
key1 = "ORARETHEY"
cyp1 = crypt(msg1,key1)
decyp1 = crypt(cyp1, key1 ,True)

assert cyp1 == 'HYEJXNKILHJAIIGPGCOEDYEKKAMFBIEK'
assert decyp1 == msg1

import ngram_score as ns
fitness = ns.ngram_score()

def int_arr_to_str(arr):
    return ''.join(chr(c) for c in arr)

def get_score(cyp, key_char_arr):
    key = int_arr_to_str(key_char_arr)
    decypt = crypt(cyp, key, True)
    return fitness.score(decypt)

def autobreak_with_len(cyp, key_len):
    max_score = -10000
    max_score_key_char_arr = []

    # try AAA... to ZZZ...
    for base_char in range(ord('A'), ord('Z')+1):
        key_char_arr = [ base_char for i in range(key_len) ]
        autobreak_round(cyp, key_char_arr)
        score = get_score(cyp, key_char_arr)
        if score > max_score:
            max_score = score
            max_score_key_char_arr = key_char_arr
    
    # redo with max_score_key_char_arr
    # print(int_arr_to_str(max_score_key_char_arr), max_score)
    for a in range(5):
        new_key_char_arr = autobreak_round(cyp, max_score_key_char_arr)
        if max_score_key_char_arr == new_key_char_arr:
            key = int_arr_to_str(new_key_char_arr)
            #print(crypt(cyp, key, True), get_score(cyp, new_key_char_arr))
            return {
                'key': key,
                'message': crypt(cyp, key, True),
                'score': get_score(cyp, new_key_char_arr)
            }
        max_score_key_char_arr = new_key_char_arr


def autobreak_round(cyp, key_char_arr):
    for i in range(len(key_char_arr)):
        local_max_score = -10000
        local_max_c = 0
        # bruteforce 1 charater
        # and check for the local max score
        for j in range(ord('A'), ord('Z')+1):
            key_char_arr[i] = j
            score = get_score(cyp, key_char_arr)
            if score > local_max_score:
                local_max_score = score
                local_max_c = key_char_arr[i]
        key_char_arr[i] = local_max_c
    return key_char_arr

def autobreak(cyp):
    max_score = -10000
    max_res = None
    for i in range(1, 10):
        res = autobreak_with_len(cyp, i)
        if max_score < res.get('score'):
            max_res = res
    print(max_res.get('message'), max_res.get('key'), max_res.get('score'))

autobreak('HYEJXNKILHJAIIGPGCOEDYEKKAMFBIEK')
autobreak('MVUDHIVKSMREKSGMMEKOZXSVZVNMTATSLZTOITYGIROLZWMGFRIMIQCLXECSIXLASULCR')
autobreak('GVVMFEMMCTKYQBPZBDPYHJYYZIYSOHZRMNIOXMIQPYGBPMLUKVWZRFHAIWECJC')
autobreak('LXATDEMAFLIDVVFZKZHPBWARJEWXMAHSMZATGWPCJIDIWFSSVTMNAUTVJCYFDVVL')
autobreak('LXATDEMAFLIDVVFZKZHPBWARJEZEHWQTIINWRMNUWEXMTTPMQZXHQDLIPKZSYMDHREVVXCZPX')
autobreak('XCZJLWVGIKEYQRBVTQNSPAFMWJEICSIHXNVRPLDIAKENVHFTAMTNGIGIDPWMPRCYUDIBKWHKWTEWEXUCIGOCQAVS')
