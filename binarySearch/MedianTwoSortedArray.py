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


def findMedianSortedArraysRe(nums1, nums2):
    arr1 = nums1
    arr2 = nums2

    if len(arr2) < len(arr1):
        arr1, arr2 = arr2, arr1 

    totalLen = len(arr1) + len(arr2)
    halfLen = totalLen // 2

    i = 0
    j = len(arr1) - 1

    while True:

        m1 = i + (j - i) // 2
        m2 = halfLen - m1 - 2

        left1 = arr1[m1] if m1 >= 0 else float("-infinity")
        right1 = arr1[m1 + 1] if (m1 + 1) < len(arr1) else float("infinity")

        left2 = arr2[m2] if m2 >= 0 else float("-infinity")
        right2 = arr2[m2 + 1] if (m2 + 1) >= 0 else float("infinity")

        if left1 <= right2 and left2 <= right1:
            if totalLen % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return min(right1, right2)
        
        elif left1 > right2:
            j = m1 - 1
        
        else:
            i = m1 + 1


        
        

