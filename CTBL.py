import numpy as np
# Import the file in a list
with open('CTBL_file.txt') as file:
    file_line=(file.readlines())
# Create the variable tree that represents the string of the the Newick format
tree=''
for i in range(len(file_line[0])):
    tree=tree+file_line[0][i]
# Define a function that given a position in the tree will return the node name associated
def node_name(tree,node_pos):
    start=node_pos
    n_name=''
    while tree[start]!='(' and tree[start]!=')' and tree[start]!=',' and tree[start]!=';':
        n_name=n_name+tree[start]
        start+=1
    return n_name
######################################################################################
# Define a function that given a tree will provide a list of tuples representing the positions in the string
# corresponding to the parenthesis coupled each other
def par_group(tree):
    par_stack=[] # Created a stack to track the parenthesis
    par_couples=[]
    for i in range(1,len(tree)-2): # Excluding the extreme parenthesis which refer to the root
        if tree[i]=='(':
            par_stack.append(i)
        else:
            if tree[i]==')':
                par_couples.append((par_stack.pop(),i))
    return par_couples
#################################################################################
# Define a function that takes a tree and a couple of positions (corresponding to coupled parenthesis) and 
# return a list of leaves included in them (which correspond to a character subset)
def subset(tree,couple):
    leaves_list=[]
    start=couple[0]
    end=couple[1]
    i=start+1
    while i<end:
        if tree[i]=='(' or tree[i]==')' or tree[i]==',':
            i+=1
        else:
            if tree[i-1]=='(' or tree[i-1]==',':
                leaves_list.append(node_name(tree,i))
                i+=1
            else:
                i+=1
    return leaves_list
#################################################################################
# Create a sorted list with all leaves using the subset function applied to the extremes of the tree string
taxa_list=subset(tree,(0,len(tree)))
taxa_list=sorted(taxa_list)
if len(taxa_list)>200:
    raise Exception('number of species taxa cannot be higher than 200')
# Create a list of character subsets
par_couple_list=par_group(tree)
subsets_list=[]
for i in par_couple_list:
    subsets_list.append(subset(tree,i))
# Create an empty array
char_tab=np.empty((len(subsets_list),len(taxa_list)),dtype=int)
# Populate the array and print it
for i in range(len(subsets_list)):
    for j in range(len(taxa_list)):
        if taxa_list[j] in subsets_list[i]:
            char_tab[i,j]=1
        else:
            char_tab[i,j]=0
print(char_tab)

        
