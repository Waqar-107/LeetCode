class Solution:
    def solve(self, head, sz):
        if head == None:
            return None

        if sz == 1:
            return head

        half = sz // 2
        uno = head
        dos = None

        cnt = 0
        while head:
            cnt += 1

            if cnt == half:
                temp = head
                dos = head.next
                temp.next = None
                break

            head = head.next

        uno = self.solve(uno, cnt)
        dos = self.solve(dos, sz - cnt)

        # now merge
        ret = None
        ans = None
        while uno or dos:
            if uno and dos:
                if uno.val < dos.val:
                    if ret:
                        ret.next = uno
                        ret = ret.next
                    else:
                        ret = uno
                        ans = uno

                    uno = uno.next
                    ret.next = None
                else:
                    if ret:
                        ret.next = dos
                        ret = ret.next
                    else:
                        ret = dos
                        ans = dos
                    dos = dos.next
                    ret.next = None

            elif uno:
                if ret:
                    ret.next = uno
                    ret = ret.next
                else:
                    ans = uno
                    ret = uno
                uno = uno.next
                ret.next = None

            elif dos:
                if ret:
                    ret.next = dos
                    ret = ret.next
                else:
                    ans = dos
                    ret = dos
                dos = dos.next
                ret.next = None
                
        return ans

    def sortList(self, head: ListNode) -> ListNode:
        cnt = 0

        temp = head
        while head:
            cnt += 1
            head = head.next

        return self.solve(temp, cnt)
    