import re 


with open("F:\Ali\Privat File\Additional Traning\Programinig\Python\Project\Language Dectector/file1.txt") as file :
    content = file.read()


def Sentence_detctore(content):
    sentences = re.findall(r"(?ms)^(.*?[.!?])\n", content)
    return sentences
def count_sentences(content):
   sentences = re.findall(r"(?ms)^(.*?[.!?])\n", content)
   countsentences = len(sentences)
   return countsentences

def word_detctore(content):
    words = re.findall(r"\w+" , content)
    return words
def count_words(content):
   words = re.findall(r"\w+", content)
   countwords = len(words)
   return countwords

def alphabet_detctore(content):
    alphabet = list(content)
    return alphabet
def count_characters(content):
    countalphabehte = len(content)
    return countalphabehte


if __name__ == "__main__":

 sentences = Sentence_detctore(content)
 countsentences = count_sentences(content)
 words = word_detctore(content)
 countwords = count_words(content)
 alphabet = alphabet_detctore(content)
 countalphabehte = count_characters(content)


print ("Your Wellcome ")
uinput = input("Choose Your State : \n 1.ALPHABEHT \n 2.WORD \n 3.SENTENCE \n")


if uinput == "1" :
    uchar = input("Enter Your Alphabet: \n")
    spl1 = alphabet
    print ("List of Alphabet : {0} \n".format(alphabet))
    count = 0
    for alphabet in spl1:
      if alphabet == uchar:
        count += 1
    print("Your Alphabet is : " + uchar + "\n Number of Alphabet : {0}".format(count)) 
elif uinput == "2" :
    uwords = input("Enter Your Word: \n")
    spl2 = words
    print ("List of Words : {0}\n".format(words))
    count = 0
    for words in spl2:
      if words == uwords:
        count += 1
    print("Your Word is : " + uwords + "\n Number of Words : {0}".format(count))
elif uinput == "3" :
    usentences = input("Enter Your Sentences: \n")
    spl3 = sentences
    print ("List of Sentences : {0} \n".format(sentences))
    count = 0
    for sentences in spl3:
      if sentences == usentences:
        count += 1
    print("Your Sentence is : " + usentences + "\n Number of Sentence : {0} ".format(count))
else : 
   print("\n oops! your input is invalid  ")   