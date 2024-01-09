# A New Benchmark for Automatic Essay Scoring in Portuguese

This repository contains all the code used in the experiments provided in `A New Benchmark for Automatic Essay Scoring in Portuguese`, which was presented at [PROPOR 2024](https://propor2024.citius.gal/).

## Dataset

The dataset used in this project is the AES ENEM Dataset, which can be accessed at:

- [AES ENEM Dataset on Hugging Face](https://huggingface.co/datasets/kamel-usp/aes_enem_dataset)

### Loading the Dataset

The dataset can be loaded using the following commands:

1. For loading the `sourceAWithGraders` slice of the dataset:
- `dataset = load_dataset("kamel-usp/aes_enem_dataset", "sourceAWithGraders", cache_dir="/tmp/aes_enem")`


2. For loading the `sourceB` slice of the dataset:
- `dataset = load_dataset("kamel-usp/aes_enem_dataset", "sourceB", cache_dir="/tmp/aes_enem")`


3. For loading the `sourceAOnly` slice of the dataset:
- `dataset = load_dataset("kamel-usp/aes_enem_dataset", "sourceAOnly", cache_dir="/tmp/aes_enem")`


## Notebooks

We have three Jupyter notebooks available for different purposes:

1. **Train Models Experiment (`train_models_experiment.ipynb`):**
- Used for training models on `sourceA` data.

2. **SourceB MLM Pretraining (`sourceB_mlm_pretraining.ipynb`):**
- Used for training `sourceB` data without a classification head, using MLM (Masked Language Modeling) loss.

3. **SourceB Classification-Head Pretraining (`sourceB_classification-head_pretraining.ipynb`):**
- Used for fine-tuning all `sourceB` data for each concept available using Ordinal Regression.

### Models

All models trained using these notebooks are available on Hugging Face under the models tab:

- [Models on Hugging Face](https://huggingface.co/kamel-usp)

The notebooks vary constant parameters such as `REFERENCE_CONCEPT`, `OBJECTIVE`, and `variant`. These parameters are used to train new concepts and specify the objective (classification, regression, or ordinal regression) and the BERT model variant (base or large).

## Usage

If you want to use the trained models, you can load them by:
```
TOKENIZER_NAME = "TOKENIZER_NAME = f"neuralmind/bert-{VARIANT}-portuguese-cased"
MODEL_NAME = "kamel-usp/aes_enem_models-sourceA-{OBJECTIVE}-from-{FINETUNED-MODEL}-{VARIANT}-C{REFERENCE_CONCEPT}"

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, 
        cache_dir="/tmp/", 
        num_labels=6,
    )
```

If you use regression, `num_labels` must be `1`. All model variants are available on [Hugging Face](https://huggingface.co/kamel-usp) 

## Contact

Please feel free to contact authors through the email shown in the paper.

## Citation

If you use this dataset or any of the associated resources in your research, please cite the following:

```
TODO
```