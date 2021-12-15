def strStr(self, haystack, needle):
    try:
        return haystack.index(needle, 0, len(haystack))
    except:
        return -1
