import spacy
import contextualSpellCheck

print("text")
# remove the tagger, parser and ner components since they are not required for spell checking
nlp = spacy.load("en_core_web_sm", disable=['tagger', 'ner', 'parser'])
contextualSpellCheck.add_to_pipe(nlp)

def spellcheck(text):
    doc = nlp(text)

    return doc._.outcome_spellCheck

if __name__ == "__main__":
    text = "I am a student of IIIT Hyderabad. I am studing here from last 3 years."
    print(text)
    outcome = spellcheck(text)

    print(outcome)