package Grafo;

import java.util.ArrayList;

public class Nodo<T> {
    private T value;
    private ArrayList<Arista<T>> aristas = new ArrayList<>();

    public Nodo(T value) {
        this.value = value;
    }

    public void addArista(Arista<T> arista) {
        aristas.add(arista);
    }

    public void setAristas(ArrayList<Arista<T>> aristas) {
        this.aristas = aristas;
    }

    public void setValue(T value) {
        this.value = value;
    }

    public ArrayList<Arista<T>> getAristas() {
        return aristas;
    }

    public T getValue() {
        return value;
    }

}
