

with open('output.txt', 'r') as file:
    data = file.read().split('\n')
RFP= [
  8,40,16,48,24,56,32,64,
  7, 39,15,47,23,55,31,63,
  6,38,14,46,22,54,30,62,
  5,37,13,45, 21,53,29,61,
  4,36,12,44,20,52,28,60,
  3, 35, 11,43,19,51,27,59,
  2, 34, 10, 42,18, 50,26,58,
  1,33,9,41, 17, 49, 25,57,
]

mapping = {'f' : "0000",
 'h' : "0010",
 'g' : "0001",
 'i' : "0011",
 'j' : "0100",
 'k' : "0101",
 'l' : "0110",
 'm' : "0111",
 'n' : "1000",
 'o' : "1001",
 'p' : "1010",
 'q' : "1011",
 'r' : "1100",
 't' : "1110",
 's' : "1101",
 'u' : "1111"
 }
INV_P = [
	9, 17, 23, 31,
	13, 28, 2, 18,
	24, 16, 30, 6,
	26, 20, 10, 1,
	8, 14, 25, 3,
	4, 29, 11, 19,
	32, 12, 22, 7,
	5, 27, 15, 21,
]

E= [
  32, 1, 2, 3, 4, 5,
  4, 5,6, 7, 8, 9,
  8, 9, 10, 11, 12, 13,
  12, 13, 14, 15, 16, 17, 
  16, 17, 18, 19, 20, 21, 
  20, 21, 22, 23, 24, 25, 
  24, 25, 26, 27, 28, 29,
  28, 29, 30, 31, 32, 1
  ]

# outtput = open("sample.txt", "a")

# outtput.write(str(a[0]))

IFP_array=[]
IFP = open("IFP.txt", "a")

output_xor=[]
output_xor_file = open("output_xor.txt","a")

SBOX_output_xor=[]
SBOX_output_xor_file = open("SBOX_output_xor.txt","a")

Expanded_R5 = []
Expanded_R5_file = open("Expanded_R5.txt","a")

Expanded_R5_xor = []
Expanded_R5_xor_file = open("Expanded_R5_xor.txt","a")

def permutation(permutation_arr,input_arr,length):
    temp=""
    for j in range(length):
          temp = temp+input_arr[permutation_arr[j]-1]
    return temp

# x=permutation([2,1],"ab",2)
# print(x)

for i in range(200000):
        tmp=""
        for j in range(16):
           tmp=tmp+mapping[data[i][j]]
        IFP_array.append(permutation(RFP,tmp,64))
        IFP.write(IFP_array[i]+"\n")
        Expanded_R5.append(permutation(E,IFP_array[i][0:32],48))
        Expanded_R5_file.write(Expanded_R5[i]+"\n")
for i in range(100000):
     tmp=""
     tmp1=""
     for j in range(64):
          tmp=tmp+str(ord(IFP_array[2*i][j])^ord((IFP_array[2*i+1][j])))
     output_xor.append(tmp)
     output_xor_file.write(output_xor[i]+"\n")
     SBOX_output_xor.append(permutation(INV_P,tmp[32:64],32))
     SBOX_output_xor_file.write(SBOX_output_xor[i]+"\n")
     for j in range(48):
          tmp1=tmp1+str(ord(Expanded_R5[2*i][j])^ord((Expanded_R5[2*i+1][j])))
     Expanded_R5_xor.append(tmp1)
     Expanded_R5_xor_file.write(Expanded_R5_xor[i]+"\n")


IFP.close()
output_xor_file.close()
SBOX_output_xor_file.close()
Expanded_R5_file.close()
Expanded_R5_xor_file.close()