def isPalindrome(teststr):
    if teststr == teststr[::-1]:
        return True
    return False

run = True
while(run):
    teststr = input("Enter string to test for palindrome or 'exit': ")

    if teststr == 'exit':
        run = False
        break

    teststr = teststr.lower()

    newstr = ''
    for x in newstr:
        if x.isalnum():
            newstr += x
    print("Palindrome test:", isPalindrome(newstr))        