---
Field:
    - 机器翻译
,    - 自然语言处理

License:
    - CC0 公共领域共享

Ext:
    - .zip
---

## 任务：

（1）基于序列到序列（Seq2Seq）学习框架，设计并训练一个中英文机器翻译模型，完成中译英和英译中翻译任务。具体模型选择可以参考如 LSTM，GRU，Transformer 等，但不做限制；
 （2）实验数据集为 WMT18 新闻评论数据集 News Commentary v13，整个语料库分训练集（约 252,700 条）、验证集和测试集（分别约 2,000 条）三部分，每部分包含中英文平行语料两个文件，全部语料已预分词处理；
（3）根据指定的评价指标和测试集数据评价模型性能。

## 评价指标：

（1）BLEU1/2/3：BLEU（Bilingual Evaluation Understudy）计算同时出现在系统译文和参考译文中的 n 元词重叠程度，实验要求计算 n=1/2/3。
（2）Perplexity：Perplexity 是衡量语言模型生成句子能力的评价指标

### 数据来源：
https://www.statmt.org/wmt18/translation-task.html

## **引用格式**
```
@misc{translate8686,
    title = { 中英文翻译数据集 },
    author = { 趙先森 },
    howpublished = { \url{https://www.heywhale.com/mw/dataset/60c41b7a19d601001898b34a} },
    year = { 2021 },
}
```