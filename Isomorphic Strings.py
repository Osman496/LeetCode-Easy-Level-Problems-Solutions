# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true



# The class `Solution` contains a method `isIsomorphic` that checks if two strings `s` and `t` are
# isomorphic by mapping characters from one string to the other.
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        #Dict to store mappings
        s_to_t = {}
        t_to_s = {}

        # The line `for char_s, char_t in zip(s,t):` is iterating over the characters of strings `s`
        # and `t` simultaneously. The `zip()` function combines the characters of both strings into
        # pairs, so in each iteration, `char_s` will represent a character from string `s` and
        # `char_t` will represent the corresponding character from string `t`. This allows for
        # comparing and mapping characters from both strings at the same time.

        for char_s, char_t in zip(s,t):
            #check if there is miss matching in mapping

        # This part of the code is checking if there is a mismatch in the mapping between characters in
        # strings `s` and `t`.
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False
            

        # This part of the code is checking if there is a mismatch in the mapping between characters in
        # strings `s` and `t`.
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False


        # The lines `s_to_t[char_s] = char_t` and `t_to_s[char_t] = char_s` are creating mappings between
        # characters in strings `s` and `t`.
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        # The `return True` statement in the `isIsomorphic` method of the `Solution` class is used to
        # indicate that the strings `s` and `t` are isomorphic, meaning that the characters in string
        # `s` can be replaced to get string `t` while preserving the order of characters and ensuring
        # that no two characters map to the same character. If the method reaches this point without
        # encountering any mismatches in the character mappings, it returns `True` to signify that the
        # strings are indeed isomorphic.
        return True


#Another way of achieving the same
def isIso(s,t):
    return len(s) == len(t) and len(set(s)) == len(set(t))

print(isIso("foo", "boo")) # False
