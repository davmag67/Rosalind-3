# Let's define a class Tree in which each node is defined by the two children (on left and right)
# the very basic tree will be a node like (a,b) in which a and b are leaves
# Every internal node of the tree will have the same format (left,right) in which left and right might be
# another internal node with a left and right children and so on, until we reach the leaves.
class Tree:
    def __init__(self,left,right):
        self.left=left
        self.right=right    
    def __str__(self):
        return f'({self.left},{self.right})'
#######################################################
# Import the dataset in a list, assuming the taxa names are all in the first line of the txt file
with open('EUBT_file.txt') as input:
        s=next(input)
        taxa_list=s.split()
#################################################
# Define a function that add a new leaf to an edge of the tree.
# We can consider an edge being related to an internal node. Each node will have a left and a right edge
# This function add a leaf to each edge of a given tree and return all of them in a list
# Important note: the tree we are considering here has a root, so the list will return a number of trees that corresponds
# to the unrooted tree of n+1 instead of n.
def add_leaf(tree,leaf):
    tree_list=[]
    tree_list.append(Tree(leaf,tree))
    if isinstance(tree,Tree):
      for i in add_leaf(tree.left,leaf):
          tree_list.append(Tree(i,tree.right))
      for j in add_leaf(tree.right,leaf):
              tree_list.append(Tree(tree.left,j))
    return tree_list    
###########################################################################
# With this function we take the list of taxa we got as input data and build the trees recursively and 
# put all of them in a list
def trees_list(taxa_list):
    all_trees=[]
    if len(taxa_list)==1:
        all_trees.append(taxa_list[0])
    else:
        for i in trees_list(taxa_list[1:]):
            for j in add_leaf(i, taxa_list[0]):
                all_trees.append(j)
    return all_trees
########################################################################
# To build the list of all unrooted trees we choose the first item of the input taxa list as
# final leaf to add to the rooted trees applied to the remaining n-1 items of the taxa list
unrooted_trees_list=[]
for i in trees_list(taxa_list[1:]):
    t='('+str(i)+')'+taxa_list[0]+';'
    unrooted_trees_list.append(t)
for i in unrooted_trees_list:
    print(i)



