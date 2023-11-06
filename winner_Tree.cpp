class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
       int n=arr.size();
       int cur=arr[0];
       int win=0;
       for(int i=1;i<n;i++)
       {
           if(arr[i]>cur)
           {
               cur=arr[i];
               win=0;
           }
           if(++win>=k) break;
       } 
       return cur;
    }
};
