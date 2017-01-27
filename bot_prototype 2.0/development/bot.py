import json
import re
import random
import datetime
global pyttsx
import pyttsx
from termcolor import colored
import sympy
import time
import sys
from num2words import num2words
import js2py

engine = pyttsx.init()

def write_file():
    is_interest = raw_input("Is it a bot interest?\n")

    keyvalue = raw_input("Is it a dynamic or specific answer?\n")

    if is_interest.lower() == "yes":
        topic = raw_input("Please type in the interest:\n")
        topic_desc = raw_input("What is the bot's opinion on this interest?\n")
        newTopicDesc = bot_interests.update({topic.lower() : topic_desc.lower()})
        bot_interest_write = open("bot_interest.json", "w")
        json.dump(bot_interests, bot_interest_write)
        
    elif keyvalue.lower() == "yes" and is_interest.lower() == 'no':
        filename_key = raw_input("What is the name of the file to write to?\n" +
                                 "Remember, you can look in project folder for names.\n")
        key_value = raw_input("What is the name of the dynamic or specific answer?\n"  +
                              "Remember, this is usually the name of a person, place or thing.\n")
        key_desc = raw_input("And what is the description for the name?\n")

        if filename_key.lower() == "people":
            people_updates = peoples.update({key_value.lower() : key_desc.lower()})
            filename_key_write = open(filename_key + '.json', "w")
            json.dump(peoples, filename_key_write)
            
        if filename_key.lower() == "place":
            place_updates = places.update({key_value.lower() : key_desc.lower()})
            filename_key_write = open(filename_key + '.json', "w")
            json.dump(places, filename_key_write)
            
        if filename_key.lower() == "bot_question":
            bot_question_updates = bot_questions.update({key_value.lower() : key_desc.lower()})
            filename_key_write = open(filename_key + '.json', "w")
            json.dump(bot_questions, filename_key_write)
            
        if filename_key.lower() == "thing":
            thing_updates = things.update({key_value.lower() : key_desc.lower()})
            filename_key_write = open(filename_key + '.json', "w")
            json.dump(things, filename_key_write)
            
        if filename_key.lower() == "greeting":
            greeting_updates = greetings.update({key_value.lower() : key_desc.lower()})
            filename_key_write = open(filename_key + '.json', "w")
            json.dump(greetings, filename_key_write)
            
        else:
            print("")    
    else:                      
        category = raw_input('If you did not choose either of the above answers,\n'
                             + 'you are able to add a keyword for a generalized response.\n'
                             + 'Please enter a category (The file name followed by an "s")\n')
        category_add = raw_input('Please enter the keyword or keyword phrase: \n')
        
        if category == "bot_states":
            category = bot_states['keywords'].append(category_add.lower())
            category = bot_states
        elif category == "greetings":
            category = greetings['keywords'].append(category_add.lower())
            category = greetings
        elif category == "questions":
            category = questions['keywords'].append(category_add.lower())
            category = questions
        elif category == "fluffs":
            category = fluffs['keywords'].append(category_add.lower())
            category = fluffs
        file_name = raw_input('Now, please enter the file name of the category (no "s")\n')
        filename_read = open(file_name + '.json', "r")
        filename_write = open(file_name + '.json', "w")
        json.dump(category, filename_write)


greeting_read  = open('greeting.json', "r")
greetings = json.load(greeting_read)

bot_state_read = open('bot_state.json', "r")
bot_states = json.load(bot_state_read)

bot_interest_read = open('bot_interest.json', "r")
bot_interests = json.load(bot_interest_read)

question_read = open('question.json', "r")
questions = json.load(question_read)

people_read = open('dynamic_specific/people.json', "r")
peoples = json.load(people_read)

place_read = open('dynamic_specific/place.json', "r")
places = json.load(place_read)

fluff_read = open('fluff.json', "r")
fluffs = json.load(fluff_read)

bot_question_read = open('bot_question.json', "r")
bot_questions = json.load(bot_question_read)

thing_read = open('dynamic_specific/thing.json', "r")
things = json.load(thing_read)


def main():
    global sentH
    sentH = raw_input("Me >>> ")

    def botPrint(string):
        print("Bot is typing."),
        time.sleep(random.choice([0.25, 0.135, 0.55]))
        print("."),
        time.sleep(random.choice([0.25, 0.135, 0.55]))
        print("."),
        time.sleep(random.choice([0.25, 0.135, 0.55]))
        print(".")
        print("Bot >>> " + string)
    
    def one_word_check(sent):
        sent = sent.split(" ")
        if len(sent) == 1:
            return True
        else:
            return False
        
    def question_check(sent):
        if any(x in sent for x in bot_states['keywords']):
            return False
        if any(x in sent.lower() for x in questions['keywords']):
            return True
        else:
            return False
        
    def check_keyword(sent, doPrint, greetCheck):
        cat = [greetings, bot_states, fluffs]
        sent = sent.lower()
        if greetCheck:
            sent = sent.split(" ")
            if any(x in sent for x in greetings['keyword']):
                   if doPrint == True:
                       botPrint(random.choice(greetings['responses']))
                   return True
        if not(question_check(sentH)):
            for i, val in enumerate(cat):
                which = i
                if any(x in sent for x in cat[which]['keywords']):
                    cat = random.choice(cat[which]['responses'])
                    if doPrint == True:
                        botPrint(cat)
                    return True
        else:   
            return False

    def check_dynamic(sent, doPrint, question_check):
        interest_bot_markers = ["do you like", "are you into", "are you interested in"]
        cat1 = [bot_interests, peoples, places, bot_questions, things]
        sent = sent.lower()
        for i, val in enumerate(cat1):
            which = i
            if question_check == True:
                if any(x in sent for x in cat1[which]):
                    if not(any(x in sent for x in interest_bot_markers)):
                        for i in cat1[which]:
                            if i in sent:
                                cat1 = cat1[which][i]
                                if doPrint == True:
                                    botPrint(cat1)
                                return True
            else:
                if any(x in sent for x in cat1[which]):
                    if sent in cat1[which]:
                        for i in cat1[which]:
                            if i in sent:
                                cat1 = cat1[which][i]
                                if doPrint == True:
                                    botPrint(cat1)
                                return True
        else:
            if any(x in sent for x in interest_bot_markers):
                if any(x in sent for x in bot_interests):
                    for i in bot_interests:
                        if i in sent:
                            if doPrint == True:
                                botPrint(bot_interests[i])
                            return True
            return False

        
    def check_calculator(sent, verbose):
        maths = ["+", "=", "/", "*", "(", ")"]
        maths2 = ["plus", "minus", "percent of", "times", "subtract", "add", "divide"]
        maths3 = ["+", "-", "%", "*", "-", "+", "/"]

        if any(x in sent for x in maths) or any(x in sent for x in maths2):
            for x in maths2:
                if x in sent:
                    foundMath = maths2.index(x)
                    sent = re.sub(maths2[foundMath], maths3[foundMath], sent)
            nums = re.sub('[()\55+=*/]', '', sent)
            try:
                nums2 = nums.split()
                nums2Len = len(nums2)
                nums3 = []
                for x in range(nums2Len):
                    try:
                        nums3.append(text2int(nums2[x]))
                    except:
                        continue
                nums3Len = len(nums3)
                nums4 = []
                for x in range(nums3Len):
                    nums4.append(num2words(nums3[x]).replace(" ", "-"))
                for x in nums4:
                    if x in sent:
                        foundWordNum = nums4.index(x)
                        sent = re.sub(nums4[foundWordNum], str(nums3[foundWordNum]), sent)
            except:
                pass
            chopped = re.findall('[0-9()\55+=*/]+', sent)
            print(chopped)
            try:
                chopped = " ".join(chopped)
                sym = sympy.sympify(chopped)
            except:
                if verbose:
                    botPrint("That expression was weird, " +
                          "the wizard that operates my calculator\ndidn't get it. " +
                          "Try again :/")
            else:
                if verbose:
                    botPrint(str(sym))
            return True
    def text2int(textnum, numwords={}):
        if not numwords:
          units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
          ]

          tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

          scales = ["hundred", "thousand", "million", "billion", "trillion"]

          numwords["and"] = (1, 0)
          for idx, word in enumerate(units):    numwords[word] = (1, idx)
          for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
          for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

        textnum = textnum.replace('-', ' ').replace(',', ' ').replace('.', ' ')
        
        current = result = 0
        for word in textnum.split():
            if (word not in numwords):
              raise Exception("Illegal word: " + word)

            scale, increment = numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0

        return result + current

    check_calculator(sentH, True)
    
    question_check(sentH)
    
    check_keyword(sentH, True, one_word_check(sentH))

    check_dynamic(sentH, True, question_check(sentH))

        
    if check_keyword(sentH, False, one_word_check(sentH)) or check_dynamic(sentH, False, question_check(sentH)) or check_calculator(sentH, False):
        main()
            
    else:
        mistyped = raw_input("Darn, I don't understand yet. Lemme refer you to the database writer... Unless you mistyped."
                                 + " Would you like to try again?\n")
                                      
        if mistyped.lower() == "yes":
            main()
                
        else:
            write_file()
            main()
main()
