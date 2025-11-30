class Solution {
    public int characterReplacement(String s, int k) {
        
        int[] count = new int[26]; // frequency of characters
        int maxFreq = 0;           // max frequency in current window
        int l = 0;
        int res = 0;

        for (int r = 0; r < s.length(); r++) {
            char ch = s.charAt(r);
            count[ch - 'A']++;  

            maxFreq = Math.max(maxFreq, count[ch - 'A']);

            // shrink window if replacements needed > k
            while ((r - l + 1) - maxFreq > k) {
                count[s.charAt(l) - 'A']--;
                l++;
            }

            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}
