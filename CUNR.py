'''    
We can apply here the same properties found in the solved exercise INOD, which I summarize below.
Using one theorem (already applied with the Rosalind exercise TREE) that any tree with N nodes will have N-1 Edges,plus two 
more observations related to the trees, we can state the following:
        Let's call:
            E = total number of edges of the tree
            L = number of leaves
            IN = number of internal nodes
            N = total number of nodes
        we can write 3 equations:
            1) 2E = L + 3*IN (the number of leaves edges + 3 times the number of internal nodes (because each has 3 edges) 
                              will give twice the number of total edges, because with the sum we are counting twice the edges )
            2) N = L + IN (the total number of nodes is equal to the leaves plus the internal nodes)
            3) E = N-1 (this is the theorem stating that the number of edges in a tree is equal to the number of nodes minus 1)
    Resolving this system for E as a function of L we will have this equation: 
        
        (1) E=2L-3
        
If we consider that:
    - A split occurs cutting an edge.
    - 2 distinct trees have different splits
Than, if we add one leave to an edge, the cut of that edge (right before the new node created) will generate a split 
that will be different form a similar cut to any of the other edges.
This means that adding a leave to any edge of a tree with m egdes will generate m distinct trees.
Let's consider a recursive way, starting form 3 leaves.
- 3 Leaves: we have only 1 possible tree (3 leaves all connected to a node)
- 4 leaves: a tree with 4 leaves can be constructed adding 1 additional leave to any of the edges of the 3 leaves tree.
            since a tree with 3 leaves has 3 edges, we can construct 3 trees with 4 leaves.
- 5 leaves: each of the 4 leaves trees has 5 edges, so we can construct 5 trees for each of the possible 4 leaves tree,
            which gives a total of 5 edges x 3 trees = 15 trees.
If we consider b(n) be the number of distinct trees with n leaves, in general we can say that a tree with n leaves can 
be contructed from a tree with n-1 leaves and b(n) = b(n-1)*(number of edges of a n-1 leaves tree) -> 
-> b(n)=b(n-1)*(2*(n-1)-3) ; as per equation in (1).
'''
# Definition of a recursive function that calculate b(n) modulo 1.000.000
def b_n(n):
    if n==3:
        return 1
    else:
        return (2*n-5)*b_n(n-1)%1000000
#####################################################
n=5
result=b_n(n)
print(result)
