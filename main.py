MAX_WORD_LENGTH = 20


class Solution:

  def makeOrderMap(self, order):
    self.orderMap = {}

    for index, char in enumerate(order):
      self.orderMap[char] = index

  def checkIsCorrectOrder(self, words):
    isAllCorrect = True

    for index in range(MAX_WORD_LENGTH):
      if isAllCorrect == False or len(words) == 1:
        break

      removeWords = []
      currentMaxIndex = -1

      for word in words:
        if index < len(word):
          print(word, index, word[index], self.orderMap[word[index]])
          wordIndex = self.orderMap[word[index]]

          if wordIndex < currentMaxIndex:
            print('1 FALSE')
            isAllCorrect = False

          if wordIndex > currentMaxIndex:
            if currentMaxIndex != -1:
              removeWords.append(word)

            currentMaxIndex = wordIndex

        # if index >= len(word):
        elif currentMaxIndex >= 0:
          print('2 FALSE')

          isAllCorrect = False

      print('removeWords', removeWords, words)
      for word in removeWords:
        words.remove(word)

    return isAllCorrect

  def isAlienSorted(self, words, order):
    self.makeOrderMap(order)
    print(self.orderMap)

    return self.checkIsCorrectOrder(words)


my = Solution()

words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
trueAns = True

# words = ["word", "world", "row"]
# order = "worldabcefghijkmnpqstuvxyz"
# trueAns = False

# words = ["apple", "app"]
# order = "abcdefghijklmnopqrstuvwxyz"
# trueAns = False

ans = my.isAlienSorted(words, order)

print("ans", ans == trueAns)
