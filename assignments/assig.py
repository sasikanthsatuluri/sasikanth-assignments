'''def func(name):
    start = name[0]
    end = name[-1]
    print(end+name[1:-1]+start)
func("sasikanth")'''             # swapping first and last characters of a string

'''name = input("enter the name:")
result = ""
for i in range(len(name)):
    if i%2==0:
        result = result+name[i]
print('the result is :',result)''' # remove odd index values of a string

'''def func(name):
    count=0
    for i in name:
        count=count+1
    print("the count is:",count)
func("sasikanth")'''   # finding length of a string

'''class String:
    def __init__(self):
        self.nam = input('enter the string:')
    def func(self):
        result =self.nam[0:4]
        print(result)
s = String()
s.func()'''          # slicing the string

'''list = ["cat","ox","tiger","elephant"]
print("The original list : " + str(list))
result = max(list, key= len)
print("Maximum length string is : " + result,len(result))''' # length of longest string in list given


'''def count_word(string,word):
    print (string.count(word))
sentence = "sasikanth is from bhimavaram and he likes vishakapatnam after bhimavaram"
count_word(sentence,"bhimavaram")'''              # counting of word in given string using function

'''sentence = input('enter your string :')
word = input('enter the word:')
for i in sentence.split():
    if i == word:
        pass
print('required count is:',sentence.count(word))''' # counting of word in given string using for loop

'''string = input('enter :')
print('required :', string.upper())
print('required :', string.lower())'''

'''string= input('the sentence is:')
print('the original string is :'+str(string))
result =''
for i in range(len(string)):
    if i%2:
        result = result+string[i].upper()
    else:
        result = result+string[i].lower()
print('the resultant string is :'+str(result))''' # string in upper & lower case

'''string = input('enter the sentence :')
print('the last character of string is :',string.split()[-1])''' # printing last part of string

'''def sentence(string):
    for i in string.split():
        if i[:4]:
            pass
    print(i)
char = input('enter the string:')
sentence(char)'''    # printing last part of string using for loop

'''text= input('enter something :')
print('after conversion :{}'.format(text.upper()))''' #converting a given string into all upper case


'''stringg = 'my name is sasikanth\n'
stringg2 = 'iam so aggressive'
print(stringg.rstrip())
print(stringg2)'''

'''x = float(input('enter the value :'))
print("\nOriginal Number: ", x)
print("Formatted Number with sign:{:.2f}".format(x)) '''

'''y = -12.9999
print("Original Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y))'''

'''string = input('enter something')
word = input('enter the word you want:')
print(string.startswith(word))'''

'''string = input('enter something')
word = input('enter the word you want:')
search = string.startswith(word)
if search:
    print('yes its there')
else:
    print('match not found')'''

'''def count(string,word):
    for i in string.split():
        if i ==word:
            pass
    print(string.count(word))

string = input('enter something :')
char = input('enter the character:')

count(string,char)'''  #counting repeated character in a string


'''def convert(string):
    p = list(string.split())
    return p

st = input('enter the string:')
print(convert(st))'''         #  converting a string into a list

'''string = input('enter something:')
dictionary = {'.':',',',':'.'}
char =string.maketrans(dictionary)
final = string.translate(char)
print(final)'''  # swapping  dots and commas in given string

'''class String:
    def __init__(self):
        self.char = input('enter the string :')
    def swap(self):
        dictionary = {'.':',',',':'.'}
        ch = self.char.maketrans(dictionary)
        final = self.char.translate(ch)
        print(final)
character = String()
character.swap()''' # swapping dots & commas in string by class method

'''string= input('enter something :')
for index,char in enumerate (string):
    print("Current character", char, "position at", index)''' #printing the index of character in string

'''class String:
    def __init__(self):
        self.stri = input('enter something :')
    def alpha(self):
        for index, char in enumerate(self.stri):
            print("Current character", char, "position at", index)

i = String()
i.alpha()'''  # printing the index of character in string using class method


'''string = input('enter something :')
vowels_set = 'aeiouAEIOU'
final=[word for word in string if word in vowels_set]
print('the words available are:', final)
print('presence is:',len(final))''' # to count & display the number of vowels in given string

'''class String:
    def __init__(self):
        self.start = input('enter something :')
    def count(self,vowels_set):
        final = [word for word in self.start if word in vowels_set]
        print('the words available are:', final)
        print('presence is:', len(final))
ch = String()
ch.count('aeiouAEIOU')''' #to count & display the number of vowels in given string using class

'''def remove(string):
    return string.replace(" ", "")
character = ' s as  i kan th '
print(remove(character))'''  # removing spaces from a given string

'''class String:
    def __init__(self):
        self.name = input('enter something string :')
    def remove(self):
        print(self.name.replace(' ',''))

character = String()
character.remove()''' # removing spaces from a given string in class

'''def capital(string):
    string = string.title()
    result =""
    for word in string.split():
        result += word[:-1] + word[-1].upper() + " "
    return result
print(capital('sasikanth lives in bimavaram'))''' #capitalizing first & last letters of each word of a given string

'''class String:
    def __init__(self):
        self.loc = input('enter the sentence :')
    def caps(self):
        new = self.loc.title()
        result =""
        for word in new.split():
            result += word[:-1] + word[-1].upper() + " "
        print(result)
char = String()
char.caps()'''  # above program using class method











