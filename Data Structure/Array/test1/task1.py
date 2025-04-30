# Вход:
# words = ["abab", "baba", "ab"]
# k = 2

# Выход:
# "ab"



from collections import defaultdict

def most_frequent_substring(words, k):
    freq_map = defaultdict(int)

    # Проходим по каждому слову
    for word in words:
        n = len(word)
        # Генерируем все подстроки длиной от 1 до k
        for length in range(1, k + 1):
            for i in range(n - length + 1):
                substr = word[i:i + length]
                freq_map[substr] += 1

    # Ищем максимальную частоту
    max_freq = max(freq_map.values())

    # Фильтруем подстроки по максимальной частоте
    candidates = [substr for substr, freq in freq_map.items() if freq == max_freq]

    # Возвращаем лексикографически минимальную
    return min(candidates)

words = ["abab", "baba", "ab"]
k = 2

result = most_frequent_substring(words, k)
print(result)  # Вывод: "a"
