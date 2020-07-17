import re
import re
import spacy
from spacy.lang.en import English
from spacy.pipeline import EntityRuler


ner_model = spacy.load('test_1')
doc1 = ner_model("""14-3-3 epsilon HvCDA2, dFMR1, WSV181, ABCG3, BgILP2, 18S, Spb18S STAT92E, CYP4G123, CYP6B50, eIF4E, 
Bm-hb, Cf-dronc, miR-960, MSTRG.3372, nlu-miR-173, Hox3-like, cecropin-A,miR-13b
MpecCu/Zn-SOD, FMRP, HvJHEH, dFMRP
""")

for token in doc1:
    regex="^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]+.*$"
    text=str(token)
    a = re.findall(regex,text)
    if len(a)!=0:
        print('re=',a)

print("Before add Regex: NER=>",[(ent.text, ent.label_) for ent in doc1.ents])


ruler = EntityRuler(ner_model)
pattern = [{"TEXT": {"REGEX":"^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]+.*$"}}]
ruler.add_patterns([{"label": "Gene", "pattern": pattern}])
ner_model.add_pipe(ruler)
ner_model.to_disk("Re")

#test
nlp2 = spacy.load("Re")
doc2 = nlp2("""14-3-3 epsilon HvCDA2, dFMR1, WSV181, ABCG3, BgILP2, 18S, Spb18S STAT92E, CYP4G123, CYP6B50, eIF4E, 
Bm-hb, Cf-dronc, miR-960, MSTRG.3372, nlu-miR-173, Hox3-like, cecropin-A,miR-13b
MpecCu/Zn-SOD, FMRP, HvJHEH, dFMRP
""")

print("After added Regex: NER=>",[(ent.text, ent.label_) for ent in doc2.ents])






