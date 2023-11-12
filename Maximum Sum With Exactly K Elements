class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        int s=0;
        int n=nums.size();
        sort(nums.begin(),nums.end());
        for(int i=0;i<k;i++)
        {
            int c;
            c=nums[n-1];
            s+=c;
            nums[n-1]=c+1;
        }
        return s;
    }
};
