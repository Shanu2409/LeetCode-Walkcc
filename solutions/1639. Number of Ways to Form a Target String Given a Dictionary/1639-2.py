class Solution:
  def numWays(self, words: List[str], target: str) -> int:
    kMod = 1_000_000_007
    wordLength = len(words[0])
    # dp[i][j] := # of ways to form first i characters of target using j first characters in each word
    dp = [[0] * (wordLength + 1) for _ in range(len(target) + 1)]
    # counts[j] := count map for words[i][j] where 0 <= i < len(words)
    counts = [collections.Counter() for _ in range(wordLength)]

    for i in range(wordLength):
      for word in words:
        counts[i][word[i]] += 1

    dp[0][0] = 1

    for i in range(len(target) + 1):
      for j in range(wordLength):
        if i < len(target):
          # Pick the character target[i] from word[j].
          dp[i + 1][j + 1] = dp[i][j] * counts[j][target[i]]
          dp[i + 1][j + 1] %= kMod
        # Skip word[j].
        dp[i][j + 1] += dp[i][j]
        dp[i][j + 1] %= kMod

    return dp[len(target)][wordLength]
