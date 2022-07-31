
class ST:
    '''
    Segement Tree Implementation: 
    Use Edit # to edit ST as per your need

    '''
    class STNode:
        # EDTI 1 : default value of _sum
        # 1. for SUM : 0
        # 2. for MIN : float('inf')
        # 2. for MAX : -float('inf')
        def __init__(self, _sum=float('inf'), left=None, right=None) -> None:
            # EDIT 2 : default behaviour
            # 1. For SUM
                # self.sum = _sum
                # self.left = left
                # self.right = right
                # if left != None:
                #     self.sum += left.sum
                # if right != None:
                #     self.sum += right.sum
            # 2. for MIN
            self.sum = _sum
            self.left = left
            self.right = right
            if left:
                self.sum = min(self.sum, left.sum)
            if right:
                self.sum = min(self.sum, right.sum)
    
    def __init__(self, nums):
        self.arr = nums
        self.STN = self.__build(0, len(arr)-1)

    def __build(self, tl, tr) -> STNode:
        if (tl == tr):
            return self.STNode(_sum=self.arr[tl])
        else:
            tm = (tl + tr) // 2
            return self.STNode(left=self.__build(tl, tm), right= self.__build(tm+1, tr))

    def __update(self, node, tl, tr, index, val) -> STNode:
        if tl == tr:
            self.arr[tl] = val
            return self.STNode(_sum=val)
        else:
            tm = (tl + tr) // 2
            if index <= tm:
                return self.STNode(left=self.__update(node.left, tl, tm, index, val), right=node.right)
            else:
                return self.STNode(left=node.left, right=self.__update(node.right, tm+1, tr, index, val))

    def __query(self, node, tl, tr, ql, qr)-> int:
        if qr<ql:
            # EDIT 3 : default behaviour when invalid query
            # 1. for SUM
                # return float('inf')
            # 2. for MIN
            return float('inf')

        if ql == tl and qr == tr:
            return node.sum
        tm = (tl + tr) // 2

        # EDIT 4 : Default return value, changes with the question
        # for SUM
            # return (query(node.left, tl, tm, ql, min(qr, tm)) + query(node.right, tm+1, tr, max(tm+1, ql), qr) )
        # for MIN
        return min(self.__query(node.left, tl, tm, ql, min(qr, tm)), self.__query(node.right, tm+1, tr, max(tm+1, ql), qr) )



    def update(self, index, val) -> None:
        self.STN = self.__update(self.STN, 0, len(self.arr), index, val)

    def query(self, left, right):
        return self.__query(self.STN, 0, len(self.arr), left, right)

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5, 6]

    st = ST(arr)
    
    print(st.query(0, len(arr)-1))
    st.update(5, -1251)
    print(st.query(0, len(arr)-1))
