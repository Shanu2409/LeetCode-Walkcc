class Solution:
  def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    curr = head
    prev = None  # prev.next == curr

    while curr:
      # Set the m-th node as `prev`.
      for _ in range(m):
        if not curr:
          break
        prev = curr
        curr = curr.next
      # Set the (m + n + 1)-th node as `curr`.
      for _ in range(n):
        if not curr:
          break
        curr = curr.next
      # Delete nodes [m + 1..n - 1].
      prev.next = curr

    return head
