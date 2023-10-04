class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l_ptr = 0;
        int r_ptr = numbers.size() - 1;
        vector<int> myVector(2);
        while (l_ptr < r_ptr){
            if (numbers[l_ptr] + numbers[r_ptr] == target){
                myVector[0] = l_ptr+1;
                myVector[1] = r_ptr+1;
                return myVector;
            }
            if (numbers[l_ptr] + numbers[r_ptr] < target){
                l_ptr++;
                continue;
            }
            else{
                r_ptr--;
                continue;
            }

        }
        return myVector;
    }
};