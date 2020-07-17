############
#Resource
#https://medium.com/@ashiqgiga07/rule-based-matching-with-spacy-295b76ca2b68
############
import spacy
from spacy.pipeline import EntityRuler # import EntityRuler 


#convert the input sentence into the document object
#print the entity types of each entity in the sentence

nlp = spacy.blank('en')
doc = nlp("The First Estate included the clergy (church-d2+ leaders), the Second Estate included the nobles, and the Third Estate included the commoners. The Third Estate paid most of the taxes, while the nobility lived lives of luxury and got all the high-ranking jobs.")
print([(ent.text, ent.label_) for ent in doc.ents])


#instantiate an object of EntityRuler class
#define the pattern
ruler = EntityRuler(nlp)
patterns = [{"label": "NOUN", "pattern": "church"}, 
             {"label": "ORG",              
             "pattern": [{"lower": "the"}, 
             {"lower": {"IN": ["first", "second", "third"]}},                          
             {"ORTH": "Estate"}]}]

# add the pattern to the matcher object
# add the matcher object as a new pipe to the model
ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

# convert the input sentence into the document object using the newly added 'nlp'
# print the entities in the sentenced after adding the EntityRuler matcher
doc = nlp("The First Estate included the clergy (church leaders), the Second Estate included the nobles, and the Third Estate included the commoners. The Third Estate paid most of the taxes, while the nobility lived lives of luxury and got all the high-ranking jobs.")
print([(ent.text, ent.label_) for ent in doc.ents])
