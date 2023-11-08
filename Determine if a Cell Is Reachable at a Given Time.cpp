class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        if((sx==fx) && (sy==fy))//
        {
            if(t==1)
            return false;
        }
        int xd=abs(sx-fx);
        int yd=abs(sy-fy);
        if(max(xd,yd)<=t)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
