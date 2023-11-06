class Solution {
public:
    int accountBalanceAfterPurchase(int purchaseAmount) {
        int n=100;
        int a=floor((purchaseAmount+5)/10)*10;
        return n-a;
    }
};
