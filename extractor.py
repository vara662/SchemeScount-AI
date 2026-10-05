import re
from datetime import date

DISTRICTS = ["Chennai", "Chengalpattu", "Kancheepuram", "Tiruvallur", "Vellore",
             "Madurai", "Coimbatore", "Salem", "Tiruchirappalli", "Tirunelveli"]  # add all 38

def extract_fields(text: str) -> dict:
    fields = {"income": None, "age": None, "gender": None,
              "district": None, "community": None}

    m = re.search(r"(?:annual|total)?\s*income[^0-9]{0,30}([\d,]{4,})", text, re.I)
    if m:
        fields["income"] = int(m.group(1).replace(",", ""))

    m = re.search(r"(?:dob|date of birth)[^0-9]{0,10}(\d{2})[/-](\d{2})[/-](\d{4})", text, re.I)
    if m:
        year = int(m.group(3))
        fields["age"] = date.today().year - year

    for g in ["Female", "Male", "Transgender"]:
        if re.search(rf"\b{g}\b", text, re.I):
            fields["gender"] = g
            break

    for d in DISTRICTS:
        if re.search(rf"\b{d}\b", text, re.I):
            fields["district"] = d
            break

    m = re.search(r"\b(MBC|BC|SC|ST|OC)\b", text)
    if m:
        fields["community"] = m.group(1)

    return fields