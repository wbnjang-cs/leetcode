class TimeMap(object):

    def __init__(self):
        self.map = {}
        
        

    def set(self, key, value, timestamp):
        if key not in self.map:
            self.map[key] = []
        
        self.map[key].append((timestamp, value))
        

    def get(self, key, timestamp): 
        if key not in self.map:
            return ""
        arr = self.map[key]
        i = 0
        j = len(arr) - 1
        
        if arr[0][0] > timestamp:
            return ""
        if arr[-1][0] < timestamp:
            return arr[-1][1]
        
        while i <= j:
            m = i + (j - i) // 2
            
            currTime = arr[m][0]
            
            if currTime == timestamp:
                return arr[m][1]
            elif currTime > timestamp:
                j = m - 1
            else:
                i = m + 1
        
        #IMPORTANT************************
        #when a binary search ends without finding answer, 
        #i is to the right of where answer would be 
        # and j is to the left of where it would be 
        return arr[j][1]
        #IMPORTANT************************