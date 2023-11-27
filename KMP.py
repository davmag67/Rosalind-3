from Bio import SeqIO
# Import record from fasta file and put it in a string variable s
seq_record=SeqIO.parse("KMP_FASTA_file.txt", "fasta")
seq_list=[]
for i in seq_record:
    seq_list.append(i.seq)
s=''
for i in range(len(seq_list[0])):
    s=s+seq_list[0][i]
if len(s)>1000:
    raise Exception('the max lenght of the string must be 1000')
# Definition of a function that compare 2 strings (of equal lenght) and return their length if equal each other
def comp_str(s1,s2):
    if s1==s2:
        return len(s1)
    else:
        return None
# Definition of a function that given a string s and a number k will return the element P(k) of the failure array
def p(s,k):
    j=1
    while True:
        s1=s[j:k+1]
        s2=s[0:k-j+1]
        if comp_str(s1,s2)==None:
            if j==k:
                return 0
                break
            else:
                j+=1
        else:
            return comp_str(s1,s2)
            break
# Iteration along the entire string and put the result in an array
fail_arr=[]
for k in range(len(s)):
    fail_arr.append(p(s,k))
print(fail_arr)
    


                