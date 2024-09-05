import spacy
import json
from spacy.training import Example
import logging

# Configure logging
logging.basicConfig(filename='training.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Load the JSON data
with open('./jsonDataset/dataset1.json', 'r') as f:
    data = json.load(f)

# Convert JSON data to spaCy format
train_data = []
for entry in data:
    text = " ".join(entry["tokens"])
    entities = []
    for i, token in enumerate(entry["tokens"]):
        start = text.find(token)
        end = start + len(token)
        entities.append((start, end, entry["tags"][i]))
    train_data.append((text, {"entities": entities}))

# Load or create a new spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
    logger.info("Loaded pre-trained model 'en_core_web_sm'.")
except:
    nlp = spacy.blank("en")
    logger.info("Created new blank model.")

# Add a new NER component to the pipeline
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
    logger.info("Added 'ner' component to the pipeline.")
else:
    ner = nlp.get_pipe("ner")
    logger.info("'ner' component already exists in the pipeline.")

# Add new labels to the NER component
new_labels = set(tag for _, annotations in train_data for _, _, tag in annotations["entities"])
for label in new_labels:
    ner.add_label(label)
    logger.info(f"Added label '{label}' to the NER component.")

# Define training loop
optimizer = nlp.begin_training()
logger.info("Starting training...")
for epoch in range(10):  # Number of epochs
    losses = {}
    for text, annotations in train_data:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=0.5, losses=losses)  # Adjust dropout if needed
    logger.info(f"Epoch {epoch + 1} - Losses: {losses}")

# Save the trained model
nlp.to_disk("trained_ner_model")
logger.info("Model training complete and saved as 'trained_ner_model'.")

# Test the model (Optional)
def test_model(model_path, text):
    nlp = spacy.load(model_path)
    doc = nlp(text)
    for ent in doc.ents:
        logger.info(f"Entity found: {ent.text} - {ent.label_}")

# Example test (Optional)
test_model("trained_ner_model", "John Doe went to the market.")
