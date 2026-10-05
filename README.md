

# SchemeScout AI

## OCR-Powered Government Scheme Eligibility Assistant

SchemeScout AI is a Python-based web application that uses Optical Character Recognition (OCR) to extract information from government documents and identify potentially eligible government schemes.

The application allows users to upload a document, extracts relevant details such as income, age, gender, district, and community, and evaluates the information against predefined scheme eligibility criteria.

The system is designed as a guidance tool and does not provide an official government eligibility decision.

---

## Features

* Upload government certificates and documents in JPG, JPEG, or PNG format
* Extract text from uploaded documents using Tesseract OCR
* Mask sensitive information such as Aadhaar and PAN numbers
* Automatically extract important user details
* Allow users to verify and edit extracted information
* Evaluate eligibility using rule-based conditions
* Categorize schemes into:

  * Eligible
  * Needs More Information
  * Not Eligible
* Display the reason for each eligibility result
* Store scheme information in a structured JSON database
* Support Tamil OCR using Tesseract language data

---

## Project Workflow

```text
Upload Government Document
            |
            v
        OCR Processing
            |
            v
      Text Extraction
            |
            v
     Sensitive Data Masking
            |
            v
       Field Extraction
            |
            v
     User Verification
            |
            v
    Eligibility Evaluation
            |
            v
 Eligible / Needs Information / Not Eligible
```

---

## Technology Stack

| Technology          | Purpose                             |
| ------------------- | ----------------------------------- |
| Python              | Application development             |
| Streamlit           | Web application interface           |
| Tesseract OCR       | Text recognition from images        |
| Pytesseract         | Python interface for Tesseract      |
| Pillow              | Image processing                    |
| Regular Expressions | Field and sensitive-data extraction |
| JSON                | Scheme data storage                 |

---

## Project Structure

```text
SchemeScout-AI/
│
├── app.py
├── ocr.py
├── redact.py
├── extractor.py
├── engine.py
├── schemes.json
├── requirements.txt
└── README.md
```

---

## Module Description

### app.py

Handles the Streamlit interface, document upload, extracted-field verification, and display of eligibility results.

### ocr.py

Processes the uploaded image and extracts text using Tesseract OCR.

### redact.py

Identifies sensitive information using regular expressions and masks information such as Aadhaar and PAN numbers.

### extractor.py

Extracts structured information from OCR text, including:

* Annual income
* Age
* Gender
* District
* Community

### engine.py

Contains the rule-based eligibility engine. It compares the user's information against the conditions defined for each government scheme.

### schemes.json

Stores scheme information and eligibility requirements in JSON format.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SchemeScout-AI.git
cd SchemeScout-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Tesseract OCR Setup

Install Tesseract OCR on your system.

For Windows, the default installation path is:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

The project can be configured to use Tamil and English OCR:

```python
pytesseract.image_to_string(image, lang="eng+tam")
```

Make sure the required Tamil language data is installed with Tesseract.

---

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in the browser at:

```text
http://localhost:8501
```

---

## Eligibility Logic

The eligibility engine evaluates different criteria such as:

```text
Income
Age
Gender
District
Community
```

For each scheme, the system produces one of three results:

### Eligible

The available user information satisfies the required conditions.

### Needs More Information

One or more required fields are missing and additional information is required.

### Not Eligible

The user's information does not satisfy one or more scheme requirements.

---

## Privacy and Security

Privacy is an important part of the application.

* Aadhaar numbers are masked after OCR processing.
* PAN numbers are masked before further processing.
* Sensitive identification information is not stored by the application.
* Users can verify extracted information before eligibility evaluation.
* Sample or dummy documents should be used for demonstrations.

---

## Example

A document may contain:

```text
Annual Income: 150000
Gender: Female
District: Chennai
Community: BC
```

After extraction, the application creates a structured profile:

```text
Income: 150000
Gender: Female
District: Chennai
Community: BC
```

The eligibility engine then compares these values against the requirements stored in `schemes.json`.

---

## Future Enhancements

* LLM-based structured information extraction
* AI-generated explanations for eligibility results
* Tamil and English natural-language responses
* Improved OCR using EasyOCR or PaddleOCR
* Image preprocessing using OpenCV
* Support for additional document formats
* Expanded database of verified government schemes
* Scheme source links and last-verified dates
* Improved document layout detection
* Cloud deployment

---

## Disclaimer

SchemeScout AI is a project developed for educational and demonstration purposes.

The eligibility results provided by the application are only guidance based on the information and rules available in the system. They should not be considered an official government eligibility determination.

Users should verify scheme requirements with the relevant government department or official scheme portal before applying.

---

## Author

**Varalakshmi Karthick Kumar**

B.Sc Computer Science with AI

