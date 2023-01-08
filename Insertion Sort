#include <vector>

#include <iostream>

using namespace std;
//head

void insertionSort(vector <int>  ar) {

    int to_be_sorted = *( ar.end() - 1);
    int i ;
    for (i = ar.size(); i > 1; --i) {
        if(to_be_sorted < ar[i-2]) {
            ar[i-1] = ar[i-2];
            for (int j = 0; j < ar.size(); ++j) {
                cout << ar[j] << " ";
            }
            cout << endl;
        }
        else {
            break;
        }
    }
        ar[i-1] = to_be_sorted;
            for (int j = 0; j < ar.size(); ++j) {
                cout << ar[j] << " ";
            }
            cout << endl;
}


/* Tail */
int main() {
   vector <int>  _ar;
   int _ar_size;
cin >> _ar_size;
for(int _ar_i=0; _ar_i<_ar_size; _ar_i++) {
   int _ar_tmp;
   cin >> _ar_tmp;
   _ar.push_back(_ar_tmp); 
}

insertionSort(_ar);
   
   return 0;
}
