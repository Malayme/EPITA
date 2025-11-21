package cours3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<String> noms = new ArrayList<>();
        noms.add("Felix");
        noms.add("Joseph");
        noms.add("Bob");

        //recupere iterateur sur la liste
        Iterator<String> it = noms.iterator();

        // Parcours avec hasNext et next
        while(it.hasNext()){  //vrai si élément suivant existe
            String nom = it.next();
            System.out.println(nom);
        }

        ChatRecord chat = new ChatRecord("Bengal", "Romain");

        System.out.println(chat.espece());
        System.out.println(chat.prenom());

        System.out.println(sommes(1, 2, 3, 4, 5));
        System.out.println(sommes());

    }
    static int sommes(int... vals){
        return Arrays.stream(vals).sum();
    }
}