// 151/A: Soft Drinking
#include<iostream>
using namespace std;

int main(){
    int n, k, l, c, d, p, nl, np;
    cin>> n>> k >>l >>c >>d >>p >>nl >>np;

    int liters= k* l/ nl, totalSlice= c* d;
    p/= np;

    cout<< min(liters, min( p, totalSlice))/ n;

    return 0;
}