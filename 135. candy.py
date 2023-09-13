class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        left_list = [1]
        right_list = [1]
        temp = 1
        candy_count = 0
        prev_left_num = ratings[0]
        prev_right_num = ratings[len(ratings)-1]
        for num in range(1, len(ratings)):
            if ratings[num] > prev_left_num:
                temp += 1
            else:
                temp = 1
            prev_left_num = ratings[num]
            left_list.append(temp)
        temp = 1
        for num in range(len(ratings) - 2, -1, -1):
            if ratings[num] > prev_right_num:
                temp += 1
            else:
                temp = 1
            prev_right_num = ratings[num]
            right_list.append(temp)
        for i in range(len(left_list)):
            x = len(left_list) - 1 - i
            candy_count += max(left_list[i], right_list[x])
        return candy_count
