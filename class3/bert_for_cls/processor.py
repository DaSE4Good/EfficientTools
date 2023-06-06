from datasets.load import load_dataset
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='binary')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }


def build_process_function(tokenizer):
    def func(examples):
        # Tokenize the texts
        args = (examples["sentence"], )
        result = tokenizer(*args, padding="max_length", max_length=128, truncation=True)
        return result
    return func

def load_data(tokenizer):
    # 获取dataset
    raw_datasets = load_dataset("sst2")
    print(raw_datasets)
    print(raw_datasets["train"])
    # train_data = raw_datasets["train"]
    # labels = raw_datasets["train"].features["label"].names
    tokenize_func = build_process_function(tokenizer)
    tokenized_datasets = raw_datasets.map(
        tokenize_func,
        batched=True,
        load_from_cache_file=False,
        desc="Running tokenizer on dataset",
        # cache_file_names={k: f"{cache_dir}/cache_{self.data_args.task_name}_{self.data_name}_{str(k)}.arrow" for k in raw_datasets},
        # remove_columns=remove_columns
    )
    return tokenized_datasets
