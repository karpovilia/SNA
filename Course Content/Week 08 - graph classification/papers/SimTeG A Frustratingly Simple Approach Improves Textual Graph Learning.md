| [arxiv](https://arxiv.org/abs/2308.02565) | [openreview](https://openreview.net/forum?id=EFGwiZ2pAW)|  ICLR 2024 reject (!) | [huggingface](https://huggingface.co/datasets/vermouthdky/SimTeG) |

Советуют сравнить с [[GraphFormers GNN-nested Transformers for Representation Learning on Textual Graph]]

В данной работе мы рассматриваем [Textual graph](Textual%20graph) (TGs) - graphs whose nodes correspond to text (sentences or documents), which are widely prevalent. The representation learning of TGs involves two stages:
- unsupervised feature extraction
- supervised graph representation learning

Получение топовых результатов на бенчмарках во многом основывается на traditional feature engineering.

Большое распространение LLM позволяет обучаться на TG одновременно используя оба источника данных или обучась независимо через извлечение признаков.

Предлагается сделать [[Parameter Efficient Fine-tuning]] ([PEFT](Parameter%20Efficient%20Fine-tuning.md)) on a pre-trained LM on the downstream task, such as node classification.

При обучении языковой модели используется [LoRA](LORA%20LOW-RANK%20ADAPTATION%20OF%20LARGE%20LANGUAGE%20MODELS)

![[Pasted image 20240612235551.png]]