package cours3;

public record ChatRecord(String espece, String prenom) {

    public ChatRecord {
        if (prenom.equals("Felix"))
            throw new IllegalArgumentException("Non pas ce prenom");

    }

}
