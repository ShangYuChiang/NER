import spacy
from spacy import displacy
from IPython.core.display import display, HTML
from pathlib import Path
#Visulization
ner_model = spacy.load('Gene_194')
colors = {"GENE": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}#,"SPECIES":"linear-gradient(90deg, #e7fc9c, #9cfce7)"
options = {"ent":['GENE'], "colors": colors}

def result (doc,file_name):
    show = displacy.render(doc, style="ent",options= options,jupyter=False)
    file_name = file_name + ".html"
    output_path = Path("./" + file_name)
    output_path.open("w", encoding="utf-8").write(show)
    
while True:
    try:
        text=input('Please type the abstract(q-exit):')
        if text == 'q':
            break
        model = input('The name of model:')
        doc1=ner_model(text)
        result(doc1,'original_labeled')     
        test_model = spacy.load(model)
        doc2=test_model(text)
        result(doc2,'Prediction')
    except:
        print('#####Please try again#####')

