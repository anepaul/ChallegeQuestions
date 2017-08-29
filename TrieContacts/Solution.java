import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int a0 = 0; a0 < n; a0++){
            String op = in.next();
            String contact = in.next();
        }
    }

    public class Node {
        HashMap<Character, Node> children = new HashMap();
        boolean isWord;
        char value;

        public Node(char val) {
            value = val;
        }
    }

    public class Trie {
        Node root = new Node('*');
        
        public void addWord(String word) {
            Node node = root;
            char arr[] = word.toCharArray();
            for (int i = 0; i < arr.length; i++) {
                if (!node.children.containsKey(arr[i])) {
                    Node child = new Node(arr[i]);
                    node.children.put(arr[i], child);
                }
                node = node.children.get(arr[i]);
                if (i == arr.length -1) {
                    node.isWord = true;
                }
            }
        }

        public int findWords(String word) {
            Node node = root;
            char arr[] = word.toCharArray();
            for (char c : arr) {
                if (node.children.containsKey(c)) {
                    node = node.children.get(c);
                } else {
                    return 0;
                }
            }
            return 
        }

        public static int trieSize(Node node) {
            int size = 0;
            if (node.isWord) {
                size ++;
            }
            if (node.children.size() == 0) {
                return size;
            } else {
                for(Node n : node.children.values()) {
                    size += Trie.trieSize(n);
                }
                return size;
            }
        }
    }
}