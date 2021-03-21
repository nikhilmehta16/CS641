#include<iostream>
#include<fstream>
#include<string>
using namespace std;




int main(){

string a;
string b;
string c[16];
    ofstream XOR("output_xor.txt",ios::app);
    ifstream RFP("sample1.txt");

    while(RFP >> a >>b )
    
    // c[0] = a[0];
    // XOR << c[0] << "\t"<<b[0]<< "\n";

    for(int i=0;i<4;i++){
        c[i] = (int(a[i])^int(b[i]));

    }
    XOR<< c[0] << "\n";

    return 0;
}
