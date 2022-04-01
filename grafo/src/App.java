import Grafo.Grafo;

public class App {
    public static void main(String[] args) throws Exception {
        Grafo<String> grafo = new Grafo<>();
        grafo.addNodo("a"); 
        grafo.addNodo("d");
        grafo.addNodo("f");
        grafo.addNodo("b");
        grafo.addNodo("c");
        grafo.addNodo("e");
        grafo.addNodo("g");
        grafo.addArista("a", "b", 7);
        grafo.addArista("b", "c", 8);
        grafo.addArista("a", "d", 5);
        grafo.addArista("d", "b", 9);
        grafo.addArista("d", "e", 15);
        grafo.addArista("d", "f", 6);
        grafo.addArista("b", "e", 7);
        grafo.addArista("f", "e", 8);
        grafo.addArista("f", "g", 11);
        grafo.addArista("e", "g", 9);
        grafo.addArista("c", "e", 5);
        

        // grafo.addNodo("1");
        // grafo.addNodo("2");
        // grafo.addNodo("3");
        // grafo.addNodo("4");
        // grafo.addNodo("5");
        // grafo.addNodo("6");

        // grafo.addArista("1", "2", 2);
        // grafo.addArista("1", "3", 3);
        // grafo.addArista("1", "6", 5);
        // grafo.addArista("2", "4", 2);
        // grafo.addArista("3", "4", 1);
        // grafo.addArista("3", "5", 5);
        // grafo.addArista("4", "6", 7);
        // grafo.addArista("5", "6", 2);

        grafo.kruskal();
        grafo.prim();
    }
}
