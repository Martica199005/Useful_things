#E-mail address e-mail scraper
import re

#text="A random string."
#text="random string."
#text="A random string. Myname123@website.com . some more random text."
text="A random string. Myname123@website.com . some more random text. YourName888@company.net"

#print(len(text))

#pattern is the regular expression
#pattern=re.compile("A random string.")
# with [] you search one the single letters
#pattern=re.compile("[ABC]")
# use text="random string"
#- is the range
#pattern=re.compile("[a-z]")
#capital letters come after
#pattern=re.compile("[a-zA-Z]")
#with the plus sign I can match multiples ones
#pattern=re.compile("[a-zA-Z]+")
#pattern=re.compile("[a-zA-Z0-9]+")
#pattern=re.compile("[a-zA-Z0-9]+@")
#\ searchs for the symbol after itself
#pattern=re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.")
#search for .com
#pattern=re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
#What does it happen with multiple e-mails?
pattern=re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
#to find both of them we must use findall
#pattern=re.compile("[a-zA-Z0-9\.-\_]+@[a-zA-Z0-9\.-\_]+\.[a-zA-Z]+") if I put Your-Name-8_8_8@company.net






#I'm searching my pattern using text
#the search pattern searchs only for the first match
#result=pattern.search(text)
result=pattern.findall(text)


print(result)