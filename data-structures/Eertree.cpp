#include <iostream>
#include <vector>
#include <map>
#include <assert.h>     /* assert */

using namespace std;


struct Node {
    int length;
    Node* suffix;
    map<int, Node*> next;
    int index; // only needed if recovering string is needed
    Node (int length) {
        this->length = length;
    }
};

struct Eertree {	
	vector<Node*> nodes;
	vector<int> str;
	int alephbetSize;
	Node* last;
	
	Eertree () {
	    str.push_back(-1);
	    
	    Node* a = makeNode(0);
	    Node* b = makeNode(-1);
	    
	    a->suffix = b;
	    b->suffix = a;
	    
	    last = a;
	}	
	
	Node* makeNode (int length) {
	    Node* n = new Node(length);	
	    nodes.push_back(n);
	    return n;
	}
	
	void add(int letter) {
		str.push_back(letter);
		last = getSuffix(last);
		if (last->next[letter] == NULL) {
			Node* n = getSuffix(last->suffix)->next[letter];
			last->next[letter] = makeNode(last->length + 2);
			last->next[letter]->suffix = n == NULL ? nodes[0] : n;
            last->next[letter]->index = str.size() - 1; // only needed if recovering string is needed
		}

		last = last->next[letter];
	}
	
	Node* getSuffix(Node* n) {
		while(str[str.size() - n->length - 2] != str[str.size() - 1]) n = n->suffix;
		return n;
	}

    ~Eertree () {
		for (int i = 0; i < nodes.size(); i++) delete nodes[i];
	}
};