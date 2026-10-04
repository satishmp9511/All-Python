# File Name: lecture2.py

# 1. Strings define karna
str1 = "Hello"
str2 = "World"

# 2. String Concatenation (Do strings ko jodna)
final_str = str1 + " " + str2
print(final_str)  # Output: Hello World

# 3. String Length (len function)
print("Length of str1:", len(str1))
print("Length of final_str:", len(final_str))

# File Name: lecture2.py

# 1. Indexing (Characters ko position se access karna)
str = "Apna_College"
print(str[0])   # Output: 'A'
print(str[5])   # Output: 'C'

# Note: str[0] = 'B' allowed nahi hai kyunki Strings immutable hoti hain.

# 2. Slicing (Positive Indexing)
str2 = "ApnaCollege"
print(str2[1:4])  # Output: "pna" (ending index 4 include nahi hota)
print(str2[:4])   # Output: "Apna" (Same as str2[0:4])
print(str2[1:])   # Output: "pnaCollege" (Same as str2[1:len(str2)])

# 3. Slicing (Negative Indexing)
str3 = "Apple"
print(str3[-3:-1]) # Output: "pl"

# File Name: lecture2.py

str = "i am a coder."

# 1. endsWith: Check karta hai ki string kisi specific word par khatam ho rahi hai ya nahi
print(str.endswith("er."))  # Output: True

# 2. capitalize: First character ko Capital kar deta hai
print(str.capitalize())     # Output: I am a coder.

# 3. replace: Purane word/letter ko naye word/letter se badal deta hai
print(str.replace("coder", "python developer"))  # Output: i am a python developer.

# 4. find: Kisi word/character ka pehla index position batata hai
print(str.find("coder"))    # Output: 7

# 5. count: Kisi word/character ka total occurrence count karta hai
print(str.count("a"))       # Output: 2
