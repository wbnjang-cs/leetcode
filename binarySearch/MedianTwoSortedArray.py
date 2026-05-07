def findMedianSortedArrays(nums1, nums2):
    A = nums1
    B = nums2

    totalLen = len(nums1) + len(nums2)
    halfLen = totalLen // 2

    if len(B) < len(A):
        A, B = B, A

    l = 0
    r = len(A) - 1

    while True:
        mA = l + (r - l) // 2
        mB = halfLen - mA - 2

        ALeft = A[mA] if mA >= 0 else float("-infinity") 
        ARight = A[mA + 1] if (mA + 1) < len(A) else float("infinity")

        BLeft = B[mB] if mB >= 0 else float("-infinity")
        BRight = B[mB + 1] if (mB + 1) < len(B) else float("infinity")

        if ALeft <= BRight and BLeft <= ARight:
            #is odd
            if totalLen % 2:
                return min(BRight, ARight)
            else:
                return (max(BLeft, ALeft) + min(ARight, BRight)) / 2
        elif ALeft > BRight:
            r = mA - 1
        else:
            l = mA + 1


        
        

