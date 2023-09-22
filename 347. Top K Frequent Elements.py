class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        output  = []
        for num in nums:
          if num in hashmap:
            hashmap[num] += 1
          else:
            hashmap[num] = 1
        freqmap = dict()
        for key in hashmap:
          if hashmap[key] in freqmap:
            freqmap[hashmap[key]].add(key)
          else:
            freqmap[hashmap[key]] = {key}
        print(freqmap)
        while k > 0:
          max_key = max(freqmap)
          k -= len(freqmap[max_key]) 
          for val in freqmap[max_key]:
            output.append(val)
          del freqmap[max_key]
        return output
