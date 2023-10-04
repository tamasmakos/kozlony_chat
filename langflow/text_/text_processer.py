from transformers import AutoTokenizer
from datasets import load_dataset

tokenizer = AutoTokenizer.from_pretrained("SZTAKI-HLT/hubert-base-cc")

# Loading text file 
dataset = load_dataset("text", data_files="/Users/tamasmakos/dev/langflow/text_/pdfs/Output/pdf_text.txt")

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Saving tokenized dataset
tokenized_datasets.save_to_disk("/Users/tamasmakos/dev/langflow/text_/pdfs/Output/tokenized_text.txt")