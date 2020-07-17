import xml.etree.cElementTree as ET
import os

def xml2spacy(tree):
        root = tree.getroot()
        training_data = []
        spacy_text=""
        #print(len(passages)) #result should be 2
        passages = root.find('document').findall('passage') 

        #convert and combine all passage.text(title, abstract) into spacy text format
        spacy_text += (passages[0].find("text").text + " ")
        spacy_text += (passages[1].find("text").text)
        training_data.append(spacy_text)
        training_data.append(annotation2entity(passages))
        training_data = tuple(training_data)
        return training_data

def annotation2entity(passages):
        entities = ", {\"entities\":"
        for passage in passages:  
                passage_annotations = passage.findall('annotation')
                #print(len(passage_annotations))
                
                passage_entities = []
                for ann in passage_annotations:
                        entity_type = ann.find('./infon[@key="type"]').text
                        #print(entity_type)
                        if entity_type == 'Gene':
                                od = ann.find('./location').attrib
                                start = int(od['offset'])
                                end = start + int(od['length'])
                                passage_entities.append((start, end, entity_type))
        spacyd_passage = {"entities": passage_entities}
        return spacyd_passage
                      
if __name__ == "__main__":
        filePath = './Input/'
        allFileList = os.listdir(filePath)
        spacy_data = []
        for file in allFileList:
            filename = filePath+file
            output = file[:-7]+"_out.txt"
            tree = ET.parse(filename)
            xml2spacy(tree)
            spacy_data.append(xml2spacy(tree))
        #print(spacy_data)
        f_out = open('Output.txt', 'w', encoding='utf-8')
        f_out.write(str(spacy_data))
        f_out.close()
