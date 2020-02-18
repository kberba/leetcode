# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # declare a dictionary
        dictionary = dict()

        # iterate through the list of words
        for word in words:

            string = ""

            # iterate through each character
            for char in word:

                # add each morse code to the string
                string += morse_code[ord(char) - 97]

            # if the string not already in the dictionary
            if string not in dictionary:

                # add it to the dictionary
                dictionary[string] = string

        # find the length of the dictionary
        num = len(dictionary)

        return num



        
