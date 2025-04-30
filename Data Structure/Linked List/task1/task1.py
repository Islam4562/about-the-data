# Пусть у нас список: 3 -> 2 -> 0 -> -4 -> (указатель назад на 2)
# Это цикл, потому что -4 -> 2


class ListNode:
    """
    Класс узла односвязного списка.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: ListNode) -> bool:
    """
    Определяет, содержит ли связный список цикл.
    Использует алгоритм Флойда: два указателя (медленный и быстрый).
    
    :param head: Начало связного списка.
    :return: True, если есть цикл, иначе False.
    """
    slow = head  # Двигается на 1 шаг
    fast = head  # Двигается на 2 шага

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # Указатели встретились — есть цикл

    return False  # Быстрый указатель достиг конца — цикла нет

if __name__ == "__main__":
    # Пример списка: 3 -> 2 -> 0 -> -4 -> (назад к 2)
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b  # <-- Цикл тут

    print(hasCycle(a))  # Ожидается: True
