class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}  # Store karega character : uska last seen index
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # Agar character pehle dikha hai aur sliding window ke andar hai
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1  # Window ke left pointer ko jump karayein
            
            char_map[char] = right  # Character ka naya index update karein
            
            # Window ki current length calculate aur max update karein
            current_len = right - left + 1
            if current_len > max_length:
                max_length = current_len
                
        return max_length
