package Grafo;

public class Arista<T> {
    private Nodo<T> antecesor;
    private Nodo<T> sucesor;
    private int peso;

    public Arista(Nodo<T> antecesor, Nodo<T> sucesor, int peso) {
        this.antecesor = antecesor;
        this.sucesor = sucesor;
        this.peso = peso;
    }

    public void setPeso(int peso) {
        this.peso = peso;
    }

    public void setSucesor(Nodo<T> sucesor) {
        this.sucesor = sucesor;
    }
    public void setAntecesor(Nodo<T> antecesor) {
        this.antecesor = antecesor;
    }

    public int getPeso() {
        return peso;
    }

    public Nodo<T> getSucesor() {
        return sucesor;
    }
    public Nodo<T> getAntecesor() {
        return antecesor;
    }

}
