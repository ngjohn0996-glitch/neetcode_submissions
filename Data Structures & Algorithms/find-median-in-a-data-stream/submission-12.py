class MedianFinder:

    def __init__(self):
        #1)smaller_value_maxheap & larger_value_minheap
        self.smaller_heap = []
        self.larger_heap = []
        
    def addNum(self, num: int) -> None:
        #2)always insert into smaller_value_maxheap 
        heapq.heappush(self.smaller_heap, -1*num)

        #2.1)ensure max at smaller_value_maxheap < min at larger_value_minheap
        if (self.smaller_heap and self.larger_heap and
        -1*self.smaller_heap[0] > self.larger_heap[0]):
            maximum = -1*heapq.heappop(self.smaller_heap)
            heapq.heappush(self.larger_heap, maximum)

        #2.2)ensure heap_size diffrence is 0 / 1
        if len(self.smaller_heap) > len(self.larger_heap)+1:
            maximum = -1*heapq.heappop(self.smaller_heap)
            heapq.heappush(self.larger_heap, maximum)
        if len(self.larger_heap) > len(self.smaller_heap)+1:
            minimum = heapq.heappop(self.larger_heap) 
            heapq.heappush(self.smaller_heap, -1*minimum)


    def findMedian(self) -> float:
        #3)find median
        if len(self.smaller_heap) == len(self.larger_heap):
            return (-1*self.smaller_heap[0] + self.larger_heap[0]) / 2
        elif len(self.smaller_heap) > len(self.larger_heap):
            return -1*self.smaller_heap[0]     
        elif len(self.larger_heap) > len(self.smaller_heap):
            return self.larger_heap[0]   
        
    