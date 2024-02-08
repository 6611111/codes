class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int s=0,c=0;
        for(int i=0;i<nums.size();i++)
        {
            s+=nums[i];
            if(s==0)
            {
                c+=1;
            }
        }
        if(c!=0)
        {
            return c;
        }
        return 0;
    }
};
