import wikipedia
import json

thing_read = open('thing.json', "r")
things = json.load(thing_read)

place_read = open('place.json', "r")
places = json.load(place_read)

people_read = open('people.json', "r")
peoples = json.load(people_read)

while(True):
    
    article = raw_input("Name of article\n")

    isWhat = raw_input("People, place, or thing?\n")


    summary = wikipedia.summary(article, sentences=6)

    if isWhat.lower() == "people":
        people_updates = peoples.update({article.lower() : summary.lower()})
        people_key_write = open(isWhat + '.json', "w")
        json.dump(peoples, people_key_write)
        people_key_write.close()        
    if isWhat.lower() == "place":
        place_updates = places.update({article.lower() : summary.lower()})
        place_key_write = open(isWhat + '.json', "w")
        json.dump(places, place_key_write)
        place_key_write.close()        
        
    if isWhat.lower() == "thing":
        thing_updates = things.update({article.lower() : summary.lower()})
        thing_key_write = open(isWhat + '.json', "w")
        json.dump(things, thing_key_write)
        thing_key_write.close()



