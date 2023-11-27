from Bio import SeqIO
# Import records from fasta file and put them in a list
seq_record=SeqIO.parse("REVP_FASTA_file.txt", "fasta")
seq_list=[]
for i in seq_record:
    seq_list.append(i.seq)
s=seq_list[0]
if len(s)>1000:
    raise Exception('the max lenght of the string must be 1000')
# Definition of the function that veryfy if a string is reverse palindrome
def rev_pal(s):
    map={'A':'T','T':'A','C':'G','G':'C' }
    s_conv=''
    for i in s:
        s_conv+=map[i]
    s_comp=s_conv[::-1]
    if s==s_comp:
        return True
    else:
        return False
# Definition of a function that given a string and two numbers will return the substring
# from position of first number and lenght of second number
def sub_str(s,i,k):
    s_str=''
    for index in range(i,i+k):
        s_str=s_str+s[index]
    return s_str
# Scanning the string s and populate the output list
output_list=[]
for i in range(len(s)):
    for k in range(4,13):
        if i+k<=len(s):
            if rev_pal(sub_str(s,i,k)):
                output_list.append((i+1,k))
            else:
                pass
        else:
            pass
for i in output_list:
    print(i)
        

