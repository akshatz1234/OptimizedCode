import commonUtility
import re 
def genex(tokenized_text):
    """
    In: OCR output Tokenized
    out: Gender
    """
    for i in tokenized_text:
        male = re.search("(^MA.E$|^Ma.e$)", i)
        female = re.search("(^FEMA.E$|^Fema.e$)", i)
        if male is not None:
            return "Male"
        if female is not None:
            return "Female"
        
        
def main_ex(output):
    tokenized_text = commonUtility.word_tokenize(output)
    classified_text = commonUtility.st.tag(tokenized_text)
    data = {}
    data['name'] = commonUtility.nameex(classified_text)
    data['dob'] = commonUtility.dateex(output)
    data['age'] = commonUtility.age(data['dob'])
    data['docType'] = "Aadhar_Card"
    data['gender'] = genex(tokenized_text)
    data['bloodGroup'] = ""
    data['address'] = ""
    return commonUtility.jsonify(data)