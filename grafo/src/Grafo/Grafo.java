package Grafo;

import java.util.ArrayList;

public class Grafo<E> {

    ArrayList<Nodo<E>> nodos = new ArrayList<>();

    public Nodo<E> addNodo(E value) {
        Nodo<E> nodo = new Nodo<>(value);
        nodos.add(nodo);
        return nodo;
    }

    public void addArista(E origen, E destino, int peso) {
        Nodo<E> nodoOrigen = getNodo(origen);
        Nodo<E> nodoDestino = getNodo(destino);
        Arista<E> arista = new Arista(nodoOrigen, nodoDestino, peso);
        nodoOrigen.addArista(arista);
    }

    public Nodo<E> getNodo(E value) {
        for (Nodo<E> nodo : nodos) {
            if (nodo.getValue().equals(value)) {
                return nodo;
            }
        }
        return null;
    }

    public void kruskal() {
        ArrayList<Arista<E>> aristas = new ArrayList<>();
        for (Nodo<E> nodo : nodos) {
            for (Arista<E> arista : nodo.getAristas()) {
                aristas.add(arista);
            }
        }
        aristas.sort((a1, a2) -> a1.getPeso() - a2.getPeso());
        int peso = 0;

        ArrayList<Nodo<E>> nodos_arbol = new ArrayList<>();
        for (Arista<E> arista : aristas) {
                if(!nodos_arbol.contains(arista.getAntecesor()) || !nodos_arbol.contains(arista.getSucesor())) {
                    nodos_arbol.add(arista.getAntecesor());
                    nodos_arbol.add(arista.getSucesor());
                    peso += arista.getPeso();
                    System.out.println("arista: " + arista.getAntecesor().getValue() + " - "
                        + arista.getSucesor().getValue() + " peso: " + arista.getPeso());
                }
                
                // nodos_arbol.add(arista.getAntecesor());
                // peso += arista.getPeso();
                // System.out.println(nodos_arbol.size());
        }

        System.out.println(peso);
    }

    public void prim() {
        ArrayList<Arista<E>> aristas = new ArrayList<>();
        for (Nodo<E> nodo : nodos) {
            for (Arista<E> arista : nodo.getAristas()) {
                aristas.add(arista);
            }
        }
        aristas.sort((a1, a2) -> a1.getPeso() - a2.getPeso());
        int peso = 0;
        int i = 0;
        int j = 0;
        while (i < nodos.size() - 1) {
            while (j < aristas.size()) {
                if (!(aristas.get(j).getSucesor().getValue()).equals(nodos.get(i).getValue())) {
                    peso += aristas.get(j).getPeso();
                    aristas.remove(j);
                    j = 0;
                    break;
                }
                j++;
            }
            i++;
        }
        System.out.println(peso);
    }
}
