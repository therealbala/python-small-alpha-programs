st='The quick brown fox jumps over a lazy dog'
s={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'} 
for i in s:
    if i in st.lower():
        t=' pangram '
    else:
        t=' not a pangram'
        break
print(t)
