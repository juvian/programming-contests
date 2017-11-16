#include <iostream>
#include <vector>
using namespace std;


struct Eertree {
	struct Node {
		int length;
		Node* suffix;
		vector<Node*> next;
		Node (int capacity, int length) {
			next = vector<Node*>(capacity, NULL);
			this->length = length;
		}
	};
	
	vector<Node*> nodes;
	vector<int> str;
	int alephbetSize;
	Node* last;
	
	Eertree (int capacity, int alephbetSize) {
	    this->alephbetSize = alephbetSize;
	    str.push_back(alephbetSize);
	    
	    Node* a = makeNode(0);
	    Node* b = makeNode(-1);
	    
	    a->suffix = b;
	    b->suffix = a;
	    
	    last = a;
	}	
	
	Node* makeNode (int length) {
	    Node* n = new Node(alephbetSize, length);	
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
			
		}
		last = last->next[letter];
	}
	
	Node* getSuffix(Node* n) {
		while(str[str.size() - n->length - 2] != str[str.size() - 1]) n = n->suffix;
		return n;
	}	
};