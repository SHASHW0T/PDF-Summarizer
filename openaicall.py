from PyPDF2 import PdfFileReader
import openai

# Set your OpenAI API key
openai.api_key = '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'

def extract_pdf_info_and_summarize(pdf_file):
    # Extract text from the PDF
    pdf_text = extract_pdf_info(pdf_file)

    # Summarize the extracted text 
    summary = summarize_text(pdf_text)

    return summary


def extract_pdf_info(pdf_file):
    pdf = PdfFileReader(pdf_file)
    number_of_pages = pdf.getNumPages()

    text = ""
    for i in range(number_of_pages):
        text += pdf.getPage(i).extractText() + "\n"

    return text 

def summarize_text(text):
    # Use GPT-3.5 to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Summarize the following text:\n" + text,
        max_tokens=150  # You can adjust this parameter for desired summary length
    )
    summary = response.choices[0].text.strip()

    return summary

# Example usage:
pdf_file_path = r"C:\Users\Satya Tiwari\OneDrive\Desktop\CSE2002_DATA-STRUCTURES-AND-ALGORITHMS_LTP_2.0_2_CSE2002_DATA-STRUCTURES-AND-ALGORITHMS_LTP_2.0_1_CSE2002-Data Structures and Algorithm.pdf"
summary = extract_pdf_info_and_summarize(pdf_file_path)
print("Summary of the PDF content:")
print(summary)
