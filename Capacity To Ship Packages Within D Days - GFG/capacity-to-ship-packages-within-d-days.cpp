// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    int leastWeightCapacity(int arr[], int N, int D) {
        // code here
        
        // function to check if current weight can deliver in d days
        
        
        // binary search for min weight
        int w1 = *max_element(arr, arr+N);
        int w2 = accumulate(arr, arr + N, 0);
        int w = (w1 + w2)/2;
        
        while(w > w1) {
            if(isValid(arr, N, D, w)) {
                w2 = w;
            }
            else {
                w1 = w;
            }
            
            w = (w1 + w2)/2;
        }
        
        if(isValid(arr, N, D, w)) return w;
        else return w+1;
        
    }
    
  private:
    bool isValid(int arr[], int N, int D, int w) {
        
        int days = 1;
        int sum = 0;
        int i = 0;
        while(i<N) {
            sum += arr[i];
            if(sum <= w){
                i++;
            }
            else {
                sum = 0;
                days++;
            }
        }
        return days <= D;
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N,D;
        cin>>N;
        
        int arr[N];
        for(int i=0; i<N; i++)
            cin>>arr[i];
        cin>>D;

        Solution ob;
        cout << ob.leastWeightCapacity(arr,N,D) << endl;
    }
    return 0;
}  // } Driver Code Ends