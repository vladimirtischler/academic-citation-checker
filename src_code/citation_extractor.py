import fitz  # PyMuPDF
import re
from transformers import pipeline

def extract_citations(path_to_pdf):
    doc = fitz.open(path_to_pdf)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    # Príklad pre formát [1], [2] atď.
    square_number_citations = re.findall(r'\[\d+\]', full_text)

    # Príklad pre formát (Autor, rok)
    author = re.findall(r'\([A-Z][a-z]+ et al\., \d{4}\)|\([A-Z][a-z]+, \d{4}\)', full_text)

    return list(square_number_citations + author)  # set() odstráni duplikáty

def extract_linked_citations(pdf_path):
    doc = fitz.open(pdf_path)
    found_citations = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        links = page.get_links()

        for link in links:
            if link.get("kind") == fitz.LINK_NAMED:
                rect = link.get("from")  # Coordinates of the link

                citation_text = page.get_text("searchphrase", clip=rect).strip()

                if citation_text:
                    found_citations.append({
                        "text": citation_text,
                        "page": page_num + 1,
                        "target_page": link.get("page") + 1 if "page" in link else None
                    })

    return found_citations

# Použitie:
citations1 = extract_citations("pdf_documents/2024.sdp-1.25.pdf")
citations2 = extract_linked_citations("pdf_documents/2024.sdp-1.25.pdf")
# This is a conceptual example of using a pre-trained NER model
ner_pipeline = pipeline("ner", model="jandek/scibert-base-uncased-scierc", aggregation_strategy="simple")

def extract_scientific_entities(text):
    results = ner_pipeline(text)
    for entity in results:
        print(f"Entity: {entity['word']} | Label: {entity['entity_group']} | Score: {entity['score']:.2f}")

text = "The results in [12] contradict the findings of Smith et al. (2022)."
extract_scientific_entities(text)

# print(citations2)