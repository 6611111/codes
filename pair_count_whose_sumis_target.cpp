#include<bits/stdc++.h>
using namespace std;
int countPairs(vector<int>& nums, int target) {
        int n=nums.size();
        int s;
        int c=0;
        for(int i=0;i<n;++i)//-1
        {
            for(int j=i+1;j<n;++j)//1 
            {
            	s=nums[i]+nums[j];
                if(s<target)
                c++;
            }
            s=0;
        }
        return c;
    }
int main()
{
	int n=5;
	vector<int> nums;
	nums.push_back(-1);
	nums.push_back(1);
	nums.push_back(2);
	nums.push_back(3);
	nums.push_back(1);
	int target = 2;
	cout<<countPairs(nums,target);
}
