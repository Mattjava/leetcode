class Solution {
    public static int lengthOfLastWord(String s) {
        int count = 0;
        int wordCount = 0;
        if(s.length() == 1)
        {
            return 1;
        }
        for(int i = s.length()-1; i > -1; i--)
        {
            if(Character.isLetter(s.charAt(i)) && wordCount == 0)
            {
                count++;
                if(i != 0 && !Character.isLetter(s.charAt(i-1)))
                {
                    wordCount++;
                }
            }
        }
        return count;
    }

}