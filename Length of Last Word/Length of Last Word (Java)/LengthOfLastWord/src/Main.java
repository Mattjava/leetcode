import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a sentence: ");
        String sentence = input.nextLine();

        int lastWordLength = Solution.lengthOfLastWord(sentence);

        System.out.println("The last word is about " + lastWordLength + " characters long");

    }
}