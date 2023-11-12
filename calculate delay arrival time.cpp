class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        int s;
        s=arrivalTime+delayedTime;
        if(s<24)
        {
          return s;
        }
        else if(s==24)
        {
           return 0;
        }
        else{
          return (s-24);
        }
    }
};
