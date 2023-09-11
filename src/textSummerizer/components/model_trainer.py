import os
from textSummerizer.entity.config_entity import ModelTrainerConfig
from transformers import AdamWeightDecay
from transformers import DataCollatorForSeq2Seq
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):        
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_t5_small = TFAutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_t5_small, return_tensors='tf')
        
        #loading data 
        dataset_samsum_tf = load_from_disk(self.config.data_path)

        train_dataset = dataset_samsum_tf["train"].to_tf_dataset(
             batch_size= self.config.batch_size,
             columns=["input_ids", "attention_mask", "labels"],
             shuffle=True,
            collate_fn=seq2seq_data_collator,
            )
        
        validation_dataset = dataset_samsum_tf["validation"].to_tf_dataset(
             batch_size= self.config.batch_size,
             columns=["input_ids", "attention_mask", "labels"],
             shuffle=False,
             collate_fn=seq2seq_data_collator
             )      


        optimizer = AdamWeightDecay(learning_rate= self.config.learning_rate, 
                                    weight_decay_rate= self.config.weight_decay_rate
                                    )
        model_t5_small.compile(optimizer= optimizer)

        model_t5_small.fit(
            train_dataset,
            validation_data=validation_dataset,
            epochs= self.config.num_train_epochs)

        ## Save model
        model_t5_small.save_pretrained(os.path.join(self.config.root_dir,"t5-small-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))