answers = ['y', 'yes', 'n', 'no']
choice = ['verb', 'v', 'noun', 'n']
thirdly = ['r', 'n', 'x', 'l', 't']

aspects = ['gender', 'number', 'case', 'declension']
gens = ['feminine', 'masculine', 'neuter']
nums = ['singular', 'plural']
decl = ['first', 'second', 'third', 'fourth', 'fifth'] 
cases = ['nominative', 'genitive', 'accusative', 'dative', 'ablative', 'vocative']
gender = ""
number = ""
declension = ""
case = ""
decs = {'first': '1', 'second': '2', 'third': '3', 'fourth': '4', 'fifth': '5'}
noms = {'feminine1': 'a', 'masculine2': 'us', 'neuter2': 'um', 'masculine3': 'is', 'feminine3': 'is', 'neuter3': 'is', 'masculine4': 'us', 'feminine4': 'us', 'neuter4': 'ū', 'masculine5': 'ēs', 'feminine5': 'ēs'}

aspects2 = ['person', 'number', 'tense', 'voice', 'mood', 'conjugation']
persons = ['first', 'second', 'third']
tenses = ['present', 'imperfect', 'future', 'perfect', 'pluperfect', 'future perfect']
voices = ['active', 'passive', 'deponent']
moods = ['indicative', 'imperative', 'subjunctive']
conjugations = ['first', 'second', 'third', 'third/fourth', 'fourth']
person = ""
tense = ""
voice = ""
mood = ""
conjugation = ""
conjs = {'first': 'āre', 'second': 'ēre', 'third': 'ere', 'fourth': 'īre', 'third/fourth': 'ere'}



def aspect(word):
    global gender
    global number
    global declension
    global case
    word = word.lower()
    
    if word == 'gender':
        gender = input("Please input the gender of the noun (feminine/masculine/neuter): ")
        gender = gender.lower()
        while gender not in gens:
            gender = input("Not a valid answer. Please select one of the following: feminine/masculine/neuter: ")
            gender = gender.lower()
    elif word == 'number':
        number = input("Is the noun plural or singular?: ")
        number = number.lower()
        while number not in nums:
            number = input("Not a valid answer. Please select either singular or plural: ")
            number = number.lower()
    elif word == 'declension':
        declension = input("Please select a declension (first/second/third/fourth/fifth): ")
        declension = declension.lower()
        while declension not in decl:
            declension = input("Not a valid answer. Please select one of the following: first/second/third/fourth/fifth: ")
            declension = declension.lower()
    elif word == 'case':
        case = input("Please select a case (nominative/genitive/accusative/dative/ablative/vocative): ")
        case = case.lower()
        while case not in cases:
            case = input("Not a valid answer. Please select one of the following: nominative/genitive/accusative/dative/ablative/vocative: ")
            case = case.lower()

def aspect2(word):
    global person
    global tense
    global voice
    global mood
    global conjugation
    global number
    word = word.lower()
    
    if word == 'person':
        person = input("Please input the person of the noun (first/second/third): ")
        person = person.lower()
        while person not in persons:
            person = input("Not a valid answer. Please select one of the following: feminine/masculine/neuter: ")
            person = person.lower()
    elif word == 'number':
        number = input("Is the verb plural or singular?: ")
        number = number.lower()
        while number not in nums:
            number = input("Not a valid answer. Please select either singular or plural: ")
            number = number.lower()
    elif word == 'tense':
        tense = input("Please select a tense (present/future/imperfect/perfect/pluperfect/future perfect): ")
        tense = tense.lower()
        while tense not in tenses:
            tense = input("Not a valid answer. Please select one of the following: present/future/imperfect/perfect/pluperfect/future perfect: ")
            tense = declension.lower()
    elif word == 'voice':
        voice = input("Please select a voice (active/passive/deponent): ")
        voice = voice.lower()
        while voice not in voices:
            voice = input("Not a valid answer. Please select one of the following: active/passive/deponent: ")
            voice = voice.lower()
    elif word == 'mood':
        mood = input("Please select a mood (indicative/imperative/subjunctive): ")
        mood = mood.lower()
        while mood not in moods:
            mood = input("Not a valid answer. Please select one of the following: indicative/imperative/subjunctive: ")
            mood = mood.lower()
    elif word == 'conjugation':
        conjugation = input('Please input the conjugation of the verb (first/second/third/third "-io"/fourth: ')
        conjugation = conjugation.lower()
        while conjugation not in conjugations:
            conjugation = input('Not a valid answer. Please select one of the following: first/second/third/third "-io"/fourth: ')
            conjugation = conjugation.lower()
            
        
def quest(ans1):
    ans1 = ans1.lower()
    while ans1 not in answers:
        print(ans1, "is not a valid answer.")
        ans1 = input("Please answer with Y, YES, N, or NO: ")
    if ans1 == 'n' or ans1 == 'no':
        pass
    while ans1 == 'y' or ans1 == 'yes':
        ans2 = input("Please enter which an aspect of the noun: gender/declension/number/case (Please select only one at a time): ")
        ans2 = ans2.lower()
        while ans2 not in aspects:
            ans2 = input("Not a valid answer. Please select one from the following list: gender/declension/number/case: ")
            ans2 = ans2.lower()
        aspect(ans2)
        if gender != "" and number != "" and case != "" and declension != "":
            break
        else:
            ans1 = input("Do you know any other aspects of your noun (gender/declension/number/case)? Y/YES/N/NO ")
            ans1 = ans1.lower()
            while ans1 not in answers:
                print(ans1, "is not a valid answer.")
                ans1 = input("Please answer with Y, YES, N, or NO: ")
                ans1 = ans1.lower()

def quest2(ans1):
    ans1 = ans1.lower()
    while ans1 not in answers:
        print(ans1, "is not a valid answer.")
        ans1 = input("Please answer with Y, YES, N, or NO: ")
    if ans1 == 'n' or ans1 == 'no':
        pass
    while ans1 == 'y' or ans1 == 'yes':
        ans2 = input("Please enter which an aspect of the verb: person/number/tense/voice/mood/conjugation (Please select only one at a time): ")
        ans2 = ans2.lower()
        while ans2 not in aspects2:
            ans2 = input("Not a valid answer. Please select one from the following list: person/number/tense/voice/mood/conjugation: ")
            ans2 = ans2.lower()    
        aspect2(ans2)
        if person != "" and number != "" and tense != "" and voice != "" and mood != "" and conjugation != "":
            break
        else:
            ans1 = input("Do you know any other aspects of your verb (person/number/tense/voice/mood/conjugation)? Y/YES/N/NO ")
            ans1 = ans1.lower()
            while ans1 not in answers:
                print(ans1, "is not a valid answer.")
                ans1 = input("Please answer with Y, YES, N, or NO: ")
                ans1 = ans1.lower()
                
def noun(word):
    global gender
    global number
    global case
    global declension
    noun = 0 
    data = open("finalgraph.csv", 'r')
    lines = [line.strip() for line in data.readlines()]
    lines = lines[1:]
    lines = [line.split(',') for line in lines]
    quest(input("Do you know the gender, declension, number, or case of your noun? Y/YES/N/NO "))
    print("In the following analyses,  first the dictionary form of the noun will be found")
    print("(that is, its nominative form, with the exception of the third declension that aren't already nominative, where I've instead provided the genitive) and then in order its gender, number, case, and declension group.")
    for line in lines:
        ending = line[4]
        endline = int(len(ending))
        stem = int(len(word)) - endline
        newend = noms[line[0] + decs[line[3]]]
        if gender != "" and line[0] != gender:
            pass
        elif number != "" and line[1] != number:
            pass
        elif case != "" and line[2] != case:
            pass
        elif declension != "" and line[3] != declension:
            pass
        elif word[-1] == ending or word[-2:] == ending or word[-3:] == ending or word[-4:] == ending:
            line[3] = line[3] + ' declension'
            if word[-1] in thirdly:
                newword = word
            else:
                newword = word[:stem] + newend
            print("Dictionary form of the word: ", newword)
            print(", ".join(line[:4]))
        else:
            noun += 1
    if noun == 123:
        print("The given word does not match any standard noun form. It may either be: \n 1. An irregular or indeclinable noun \n 2. Another part of speech (verb, preposition, etc) \n 3. A non-Latin word")
            
          
def verb(word):
    global person
    global tense
    global voice
    global mood
    global conjugation
    global number
    nummy = 0
    datum = open("finalgraphverb.csv", 'r')
    linez = [line.strip() for line in datum.readlines()]
    linez = linez[1:]
    linez = [line.split(',') for line in linez]
    quest2(input("Do you know the person, number, tense, voice, mood, or conjugation of your verb? Y/YES/N/NO "))
    print("In the following analyses,  first the dictionary form of the verb will be found, \n then in order its person, number, tense, voice and conjugation group.")
    for line in linez:
        ending = line[6]
        endline = int(len(ending))
        stem = int(len(word)) - endline
        newend = conjs[line[5]]
        if person != "" and line[0] != person:
            pass
        elif number != "" and line[1] != number:
            pass
        elif tense != "" and line[2] != tense:
            pass
        elif voice != "" and line[3] != voice:
            pass
        elif mood != "" and line[4] != mood:
            pass
        elif conjugation != "" and line [5] != conjugation:
            pass
        elif word[-1] == ending or word[-2:] == ending or word[-3:] == ending or word[-4:] == ending or word[-5:] == ending or word[-6:] == ending or word[-7:] == ending or word[-8:] == ending or word[-9:] == ending:
            if line[5] == 'third/fourth':
                line[5] = 'third "-io"'
            line[5] = line[5] + ' conjugation'
            line[0] = line[0] + ' person'
            print("Dictionary form of the word: ", word[:stem] + newend)
            print(", ".join(line[:6]))
        else:
            nummy += 1
    if nummy == 610:
        print("The given word does not match any standard verb form. It may either be: \n 1. An infinitive or participle \n 2. An irregular verb \n 3. Another part of speech (noun, preposition, etc) \n 4. A non-Latin word")

            
well = input("Do you want to parse a noun or a verb? Enter one of the following: verb/v/noun/n ")
well = well.lower()
while well not in choice:
    well = input("Not a valid answer. Please select one of the following: verb/v/noun/n ")
if well == 'noun' or well == 'n':
    noun(input("Enter your noun: "))
elif well == 'verb' or well == 'v':
    verb(input("Enter your verb: "))
    






    
