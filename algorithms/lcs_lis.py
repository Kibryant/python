def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def longest_increasing_subsequence(word):
    n = len(word)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if word[i] > word[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == "__main__":
    s1 = "abcde"
    s2 = "ace"
    print(longest_common_subsequence(s1, s2))  # 3

    s1 = "abc"
    s2 = "abc"
    print(longest_common_subsequence(s1, s2))  # 3

    s1 = "abc"
    s2 = "def"
    print(longest_common_subsequence(s1, s2))  # 0

    s1 = "hieroglyphlogy"
    s2 = "michaelangelo"
    print(longest_common_subsequence(s1, s2))  # 5

    word = "carbohydrate"
    print(f"abort = {longest_increasing_subsequence(word)}")  # 5
