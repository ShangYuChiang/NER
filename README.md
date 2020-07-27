# Arthropod gene and species Named Entity Recognition

### Project aims to collect a literature corpus as our training and testing data with automated or manual labeled entities, from abstracts in the arthropod sciences. <bt>
### And then, Using SpaCy NLP and computational linguistics algorithms to make inferences and gain insights about data we have


* TeamTat - a collaborative text annotation and web-based annotation [local setup available](https://www.teamtat.org) tool,<br>equipped to manage team annotation projects engagingly and efficiently.

* [Spacy](https://spacy.io/usage/spacy-101#whats-spacy) - a free, open-source library for advanced Natural Language Processing (NLP) in Python.<br>
designed specifically for production use and helps you build applications that process and “understand” large volumes of text. It can be used to build information extraction or natural language understanding systems, or to pre-process text for deep learning.

### Requirment
`Python` `Anaconda` and `Jupyter Notebook`<br>
Python 3.3 or greater is required to install the Jupyter Notebook.
* Anaconda and Jupyter Notebook Install Instructions -[ Windows ](https://mas-dse.github.io/startup/anaconda-windows-install/)
* How to install Python 3.6 and run the Spyder Integrated Development Environment (IDE) or the Jupyter Notebook. [Vedio]( https://www.youtube.com/watch?v=LrMOrMb8-3s)


# 1.Convert data format form BioCxml to spacy
## User guide
The BioCxml format of the TeamTat's annotation
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE collection SYSTEM "BioC.dtd">
<collection>
  <source>PubTator</source>
  <date/>
  <key>BioC.key</key>
  <document>
    <id>3392027</id>
    <infon key="tt_curatable">no</infon>
    <infon key="tt_version">0</infon>
    <infon key="tt_round">0</infon>
    <passage>
      <infon key="type">title</infon>
      <offset>0</offset>
      <text>(title)Primary structure of apolipophorin-III from the migratory locust, Locusta migratoria. Potential amphipathic structures and molecular evolution of an insect apolipoprotein.</text>
      <annotation id="1">
        <infon key="identifier"></infon>
        <infon key="type">Gene</infon>
        <infon key="updated_at">1980-01-01T00:00:00Z</infon>
        <location offset="21" length="17"/>
        <text>apolipophorin-III</text>
      </annotation>
      <annotation id="2">
        <infon key="identifier">7004</infon>
        <infon key="type">Species</infon>
        <infon key="updated_at">1980-01-01T00:00:00Z</infon>
        <location offset="48" length="16"/>
        <text>migratory locust</text>
      </annotation>
    </passage>
  </document>
</collection>

```

The Spacy's entity annotations format
```python
train_data = [
    ('Primary structure of ....',{'entities': [(21,38,'Gene'),(48,64,'Species'),(66,84,'Species'),(225,242,'Gene'),(248,266,'Species'),(423,440,'Gene'),(450,466,'Species'),(468,481,'Species'),(597,610,'Species'),(969,978,'Species'),(1159,1168,'Species'),(1234,1243,'Species')]}),(ex2),(ex3)]
#("Eample text or content"(string), {"entities": [(start_position(int), end_position(int), "label_name"(string))]})
```

## Prerequisite
- Python 3.x { x > 4 }  
check by command  `python --version`  
- Pip (package manager)  
check by command  `pip --version`  
- lxml module  
Install by command `pip install lxml`  
check by command   `pip list` to see whether lxml exists


## Getting started step by step 

- Step1 - Clone the repo to local path
```
cd `Your path`
```
```
git clone https://github.com/ShangYuChiang/NER.git
```

- Step2 - Run BioCxml2spacy.py

```
cd / NER/BioCxml2spacy
```
```
python BioCxml2spacy.py
```
- Step3 - The results are shown in the output file

# 2.

# other
[convert annotation format from BioCxml to Spacy](https://github.com/ShangYuChiang/BioCxml2spacy)
[Convert text file into BioCxml format](https://github.com/ShangYuChiang/txt2BioCxml)


## Reference
XML Tutorial : [w3schools.com](https://docs.python.org/2/library/xml.etree.elementtree.html)  
Spacy : [Training spaCy’s Statistical Models](https://spacy.io/usage/training)  
Github : [BioC-JSON](https://github.com/ncbi-nlp/BioC-JSON)

