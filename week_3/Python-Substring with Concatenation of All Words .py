"""
Problem Statement:
Given a string s and a list of words words where all words are of the same length, find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Requirements:
You can return the answer in any order.
A substring of s to form from words must contain all words exactly once, and there can be no additional characters in the substring not part of the words.
Example:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively. The output order does not matter, returning [9,0] is fine too.
"""

from collections import defaultdict
def findSubstring(s, words):
    hash_map = defaultdict(int)
    word_length = len(words[0])
    result = []
    for word in words:
        hash_map[word] +=1
    
    for i in range(word_length):
        left = i
        right = i
        count = 0
        count_map = defaultdict(int)
        while right+word_length<= len(s):
            word = s[right:right + word_length]
            right += word_length
            if word in hash_map:
                
                count_map[word] += 1
                if count_map[word]<=hash_map[word]:
                    count+=1
                
                while count_map[word]> hash_map[word]:
                    left_word = s[left:left+word_length]
                    count_map[left_word]-=1
                    
                    if count_map[left_word] < hash_map[left_word]:
                        print(count_map[left_word])
                        count-=1
                    left+=word_length

                if count == len(words):
                    result.append(left)

            else:
                count_map.clear()
                count = 0
                left = right
    return result
if __name__ == "__main__":

    # Example usage
    s = "barfoofoothfoobarman"
    words = ["foo","bar"]
    print(findSubstring(s, words))