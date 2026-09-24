class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            #distance to travel = target - p 
            #then divide by speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
            #                      if last <= first: 
                stack.pop() #get rid of first
        return len(stack)
