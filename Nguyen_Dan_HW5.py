"""
Dan Nguyen
Algorithms 3104 HW 5
10/12/2915

A chain of words is a list of words where the i-th word is the (i - 1) st word with
one extra character and some reordering of letters. For example, AN, TAN, RANT,
TRAIN, RETINA, NASTIER is a chain of length 6. Write a python program that
reads a wordlist filename via command line and finds the longest chain in the wordlist
file. A sample wordlist file is provided at moodle via a separate link. Print out three
example chains you can find in this file that have the maximum length (there will be
a TON... just give three chains).

Hint: In order to do this, first build a DAG. The DAG will consist of a node for each
word (you might want to collapse words into a single node when it makes sense to),
and an edge from word x to word y if y can follow x in a chain. Then run DFS from
each source node in the DAG and keep track of the maximum depth you reach.

https://networkx.github.io/documentation/latest/tutorial/tutorial.html#nodes

"""

import networkx as nx



def main():
    List = open("testlist.txt").readlines()             # Open text file
    #print wordList
    
    List = sorted(List)                                 # Sort the list alphabetically 
        
    for i in range(0, len(List)):                       # The List kept on making it so there was a \n after each string
        List[i] = List[i].rstrip()                      # Take the \n off

    #print 'test string\n'.rstrip()                       Testing the stripping of "\n" 
    
    print List
    alphaList = []
    
    for i in range (0, len(List)):
        alphaList.append("".join(sorted(List[i])))      # Sorted each word in the list, but by character: CAT -> ACT
        
    print alphaList
    
    G = nx.Graph()
    
    for i in range(0 , len(alphaList)):
        G.add_node(i , word = alphaList[i])
        
    print G.node[0]['word']
    
    if (len(G.node[3]['word']) == (len(G.node[2]['word'])+1)):
        print "length of dog is 1 less than dogs"
        
    for i in range(0, G.number_of_nodes()-1):
        
        if ( ( (len(G.node[i]['word'])+1)  == len(G.node[i+1]['word']) ) and (G.node[i]['word'] in G.node[i+1]['word'])):
            print G.node[i]['word'], G.node[i+1]['word']
            G.add_edge( i, (i+1) )
        
    # print G.neighbors(3)
    
    
    print "TEST 2 DOUBLE LOOP!"
    for i in range(0, G.number_of_nodes()-1):
        
        for u in range(0, G.number_of_nodes()-1):
            
            if ( ( (len(G.node[i]['word'])+1)  == len(G.node[u+1]['word']) ) and (G.node[i]['word'] in G.node[u+1]['word'])):
                print G.node[i]['word'], G.node[u+1]['word']
                G.add_edge( i, (u+1) )
                i = i+1
   
    
    #for i in range(0, G.number_of_edges):
                
    
    
   
    
    
    
    
    
    
    
    
    

    
if __name__ == "__main__":
    main()