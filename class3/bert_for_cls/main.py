import torch
import torch.nn as nn
from datasets.load import load_dataset
from transformers import TrainingArguments
from transformers.models.bert.modeling_bert import BertForSequenceClassification
from transformers.models.bert.tokenization_bert import BertTokenizer
from transformers.trainer import Trainer
from data_collator import DataCollator

from processor import load_data, compute_metrics

if __name__ == "__main__":
    # 获得配置
    training_args = TrainingArguments(
        output_dir='./classification_results',          # output directory
        num_train_epochs=5,              # total number of training epochs
        per_device_train_batch_size=8,  # batch size per device during training
        per_device_eval_batch_size=16,   # batch size for evaluation
        warmup_steps=200,                # number of warmup steps for learning rate scheduler
        weight_decay=0.01,               # strength of weight decay
        logging_dir='./classification_logs',            # directory for storing logs
        evaluation_strategy='steps',      # "no": No evaluation is done during training.
        logging_steps=100,
    )
    # 获得模型
    model = BertForSequenceClassification.from_pretrained("bert-base-cased")
    # 获得分词器
    tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
    # 获得数据
    tokenized_datasets = load_data(tokenizer)
    train_dataset = tokenized_datasets["train"]
    eval_dataset = tokenized_datasets["validation"]

    data_collator = DataCollator(tokenizer=tokenizer, max_length=128)

    # 获得训练器
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        compute_metrics=compute_metrics,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()
