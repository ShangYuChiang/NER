import spacy
from spacy import displacy
from pathlib import Path
import en_core_web_sm

#label format
colors = {"GENE": "linear-gradient(90deg, #aa9cfc, #fc9ce7)","SPECIES":"linear-gradient(90deg, #e7fc9c, #9cfce7)"}
options = { "colors": colors}

#load text and do visulization
sent = 'Identification of the chitinase genes from the diamondback moth, Plutella xylostella. UNASSIGNED: Chitinases have an indispensable function in chitin metabolism and are well characterized in numerous insect species. Although the diamondback moth (DBM) Plutella xylostella, which has a high reproductive potential, short generation time, and characteristic adaptation to adverse environments, has become one of the most serious pests of cruciferous plants worldwide, the information on the chitinases of the moth is presently limited. In the present study, using degenerated polymerase chain reaction (PCR) and rapid amplification of cDNA ends-PCR strategies, four chitinase genes of P. xylostella were cloned, and an exhaustive search was conducted for chitinase-like sequences from the P. xylostella genome and transcriptomic database. Based on the domain analysis of the deduced amino acid sequences and the phylogenetic analysis of the catalytic domain sequences, we identified 15 chitinase genes from P. xylostella. Two of the gut-specific chitinases did not cluster with any of the known phylogenetic groups of chitinases and might be in a new group of the chitinase family. Moreover, in our study, group VIII chitinase was not identified. The structures, classifications and expression patterns of the chitinases of P. xylostella were further delineated, and with this information, further investigations on the functions of chitinase genes in DBM could be facilitated.'
nlp = spacy.load("Gene_194")
doc = nlp(sent)
show = displacy.render(doc, style="ent",options= options,jupyter=False)

#save as "test.html"
file_name = 'demo' + ".html"
output_path = Path("./" + file_name)
output_path.open("w", encoding="utf-8").write(show)
print("Successfully visulized")
