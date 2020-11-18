def smash(stones):
    if not stones: return 0

    
    # concerting to max_heap
    heap_stones = [-stone for stone in stones]

    # heapify 
    heapify(heap_stones) # O(n)



    while len(heap_stones) > 1:

        stone1 = heappop(heap_stones)
        stone2 = heappop(heap_stones)

        #print(stone1,stone2)

        push_stone = -1 * abs(stone1 - stone2)

        heappush(heap_stones,push_stone)
    if heap_stones: return heap_stones[0] * -1

    return 0


# using max heap (Rare)

def smash(stones):
        maxheap = []
        for i in range(len(stones)):
            maxheap.append(stones[i])
        heapq._heapify_max(maxheap)

        while len(maxheap) > 1:
            last = heapq._heappop_max(maxheap)
            last2 = heapq._heappop_max(maxheap)
            if last != last2:
                heapq.heappush(maxheap,last - last2)
                heapq._heapify_max(maxheap)
        if len(maxheap) == 1:
            return heapq._heappop_max(maxheap)
        return 0
