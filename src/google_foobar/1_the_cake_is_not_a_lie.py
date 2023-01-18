def count(s, p):
    c = s.count(p)
    if c * len(p) < len(s):
        return 1
    return c


def solution(s):
    pattern = None

    for idx in range(1, len(s) + 1):
        sp = s[0:idx]
        sn = s[idx : idx * 2]

        if sp == sn:
            if pattern is None or count(s, sp) >= count(s, pattern):
                pattern = sp

    if pattern is not None:
        return count(s, pattern)

    return 1


print "a: expected=2, actual={}".format(solution("aa"))
print "abc: expected=1, actual={}".format(solution("abc"))
print "abcabc: expected=2, actual={}".format(solution("abcabc"))
print "abcabcabc: expected=3, actual={}".format(solution("abcabcabc"))
print "abcabcabcabc: expected=4, actual={}".format(solution("abcabcabcabc"))
print "abccbaabccba: expected=2, actual={}".format(solution("abccbaabccba"))
print "aaT: expected=1, actual={}".format(solution("aaT"))
print "abcT: expected=1, actual={}".format(solution("abcT"))
print "abcabcT: expected=1, actual={}".format(solution("abcabcT"))
print "abcabcabcT: expected=1, actual={}".format(solution("abcabcabcT"))
print "abcabcabcabcT: expected=1, actual={}".format(solution("abcabcabcabcT"))
print "abccbaabccbaT: expected=1, actual={}".format(solution("abccbaabccbaT"))
print "a: expected=1, actual={}".format(solution("a"))
print "aa: expected=2, actual={}".format(solution("aa"))
print "abcabc: expected=2, actual={}".format(solution("abcabc"))
print "abcabcabc: expected=3, actual={}".format(solution("abcabcabc"))
print "aaT: expected=1, actual={}".format(solution("aaT"))
print "ababT: expected=1, actual={}".format(solution("ababT"))
print "abcabcabcabc: expected=4, actual={}".format(solution("abcabcabcabc"))
print "abccbaabccba: expected=2, actual={}".format(solution("abccbaabccba"))
print "a: expected=1, actual={}".format(solution("a"))
print "aa: expected=2, actual={}".format(solution("aa"))
print "ab: expected=1, actual={}".format(solution("ab"))
print "aaa: expected=3, actual={}".format(solution("aaa"))
print "abb: expected=1, actual={}".format(solution("abb"))
print "abc: expected=1, actual={}".format(solution("abc"))
print "abcab: expected=1, actual={}".format(solution("abcab"))
print "abcabc: expected=2, actual={}".format(solution("abcabc"))
print "abcabcabc: expected=3, actual={}".format(solution("abcabcabc"))
print "abcabcabcabc: expected=4, actual={}".format(solution("abcabcabcabc"))
print "abcccabcccabccc: expected=3, actual={}".format(solution("abcccabcccabccc"))
print "xxxyyyzzzxxxyyyzzz: expected=2, actual={}".format(solution("xxxyyyzzzxxxyyyzzz"))
print "xxyyzzxxyyzz: expected=2, actual={}".format(solution("xxyyzzxxyyzz"))
print "xxyyxxyyxx: expected=1, actual={}".format(solution("xxyyxxyyxx"))
print "xxyyxxyy: expected=2, actual={}".format(solution("xxyyxxyy"))
