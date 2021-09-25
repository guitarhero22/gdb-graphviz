#include <iostream>
#include <list>
#include <vector>
#include <fstream>

using namespace std;

class Graph;
class Node;

class Graph{
    public:
        vector<Node> nodes;
};

class Node{
    public:
        Node(){}
        Node(int i): data(i) {}
        void addChild(Node * child){
            children.push_back(child);
        };
        list<Node*> children;
        int data;
};

int main(){

    int n;
    int a, b;

    Graph graph = Graph();
    vector<Node> &nodes = graph.nodes;

    cin >> n;
    nodes.resize(n);
    for(int i=0; i<n; ++i) nodes[i] = Node(i);
    
    for(int i=0; i<n; ++i){
        cin >> a >> b;
        nodes[a].addChild(&nodes[b]);
    }

    ofstream output("output.dot");

    output << "graph {\n";
    for(auto node : graph.nodes){
        output << node.data << "\n";

        for(auto child : node.children){
           output << node.data << " -- " << child -> data << "\n";
        }

    }
    output << "}";
    output.close();
}