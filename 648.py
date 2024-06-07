class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        sen_list = sentence.split(" ")
        dictionary=sorted(dictionary, key=len)
        for ch in dictionary:
            for letter in range(len(sen_list)):
                if sen_list[letter].startswith(ch):
                    sen_list[letter] = ch
        return " ".join(sen_list)


dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
solution = Solution()
result = solution.replaceWords(dictionary, sentence)
print(result)
