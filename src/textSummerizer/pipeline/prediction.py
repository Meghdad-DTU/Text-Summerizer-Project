from textSummerizer.config.configuration import configurationManeger
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = configurationManeger().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_t5_small = TFAutoModelForSeq2SeqLM.from_pretrained(self.config.trained_model_path)
        
        get_kwargs = {'length_penalty': 0.8, 'max_length': 128}

        summarizer = pipeline("summarization", 
                              model=model_t5_small, 
                              tokenizer=tokenizer, 
                              framework="tf")

        print('Dialogue: ')
        print(text)

        output = summarizer(text, **get_kwargs)[0]['summary_text']
        print("\Model Summary: ")
        print(output)

        return output