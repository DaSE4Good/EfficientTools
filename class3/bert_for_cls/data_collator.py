import torch
from dataclasses import dataclass
from typing import Optional
from transformers import PreTrainedTokenizerBase


@dataclass
class DataCollator:
    tokenizer: PreTrainedTokenizerBase
    max_length: Optional[int] = 128

    def __call__(self, features):
        # Tokenize
        # is_train = features[0]["is_train"] > 0
        batch = []
        for f in features:
            # print("f=", f)
            batch.append(
                {
                    "input_ids": f["input_ids"],
                    "token_type_ids": f["token_type_ids"],
                    "attention_mask": f["attention_mask"]
                })

        batch = self.tokenizer.pad(
            batch,
            padding="max_length",
            max_length=self.max_length,
            return_tensors="pt") 
        # add labels
        batch["labels"] = torch.Tensor([f["label"] for f in features]).long()

        return batch
