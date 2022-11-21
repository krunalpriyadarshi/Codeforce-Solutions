#include<iostream>
using namespace std;

void findWinner(int x){
    (x%2)==0?
        cout<<"Malvika":
        cout<<"Akshat";
}

int main(){
    int n, m;
    cin>> n>> m;
    (n>m)?
        findWinner(m):
        findWinner(n);
    return 0;
}