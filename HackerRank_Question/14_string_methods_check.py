if __name__ == '__main__':
    s = input()
  
    # 1. Any alphanumeric character? (a-z, A-Z, 0-9)
    print(any(c.isalnum() for c in s))
    
    # 2. Any alphabetical character? (a-z, A-Z)
    print(any(c.isalpha() for c in s))
    
    # 3. Any digit? (0-9)
    print(any(c.isdigit() for c in s))
    
    # 4. Any lowercase character? (a-z)
    print(any(c.islower() for c in s))
    
    # 5. Any uppercase character? (A-Z)
    print(any(c.isupper() for c in s))
