CamemBERT API will complete your masked french text such as 

* _J'adore le camembert c'est le <mask\> dessert que j'ai gouté aujourd'hui._
* _Le camembert est vraiment <mask\>._

**According to CamemBERT's team on [camembert-model.fr](https://camembert-model.fr/)**

>CamemBERT is a state-of-the-art language model for French based on the [RoBERTa architecture](https://ai.facebook.com/blog/roberta-an-optimized-method-for-pretraining-self-supervised-nlp-systems/) pretrained on the French subcorpus of the newly available multilingual corpus [OSCAR](https://traces1.inria.fr/oscar/).
We evaluate CamemBERT in four different downstream tasks for French: part-of-speech (POS) tagging, dependency parsing, named entity recognition (NER) and natural language inference (NLI); improving the state of the art for most tasks over previous monolingual and multilingual approaches, which confirms the effectiveness of large pretrained language models for French.
CamemBERT was trained and evaluated by [Louis Martin](https://github.com/louismartin), [Benjamin Muller](https://benjamin-mlr.github.io/), [Pedro Javier Ortiz Suárez](https://pjortiz.com/), [Yoann Dupont](https://github.com/YoannDupont), [Laurent Romary](https://cv.archives-ouvertes.fr/laurentromary), [Éric Villemonte de la Clergerie](http://alpage.inria.fr/~clerger/), [Djamé Seddah](http://pauillac.inria.fr/~seddah/) and [Benoît Sagot](http://alpage.inria.fr/~sagot/).



```
@ARTICLE{2019arXiv191103894M,
       author = {{Martin}, Louis and {Muller}, Benjamin and
         {Ortiz Su{\'a}rez}, Pedro Javier and {Dupont}, Yoann and
         {Romary}, Laurent and {Villemonte de la Clergerie}, {\'E}ric and
         {Seddah}, Djam{\'e} and {Sagot}, Beno{\^\i}t},
        title = "{CamemBERT: a Tasty French Language Model}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Computation and Language},
         year = "2019",
        month = "Nov",
          eid = {arXiv:1911.03894},
        pages = {arXiv:1911.03894},
archivePrefix = {arXiv},
       eprint = {1911.03894},
 primaryClass = {cs.CL},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019arXiv191103894M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```
- - -
EXAMPLE
![output](https://i.ibb.co/DD1mRQW/example.png)
- - -
INPUT

```json
{
  "text": "Le camembert est <mask> :)",
  "top_k": 5
}
```
- - -
EXECUTION
```bash
curl -X POST "https://api-market-place.ai.ovh.net/text-camembert/process" -H "accept: application/json" -H "X-OVH-Api-Key: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" -H "Content-Type: application/json" -d '{ "text": "Le camembert est <mask> :)",  "top_k": 5}'
```
- - -

OUTPUT

```json
[
  [
    "Le camembert est délicieux :)",
    0.49091199040412903,
    " délicieux"
  ],
  [
    "Le camembert est excellent :)",
    0.10556956380605698,
    " excellent"
  ],
  [
    "Le camembert est succulent :)",
    0.03453320264816284,
    " succulent"
  ],
  [
    "Le camembert est meilleur :)",
    0.033031098544597626,
    " meilleur"
  ],
  [
    "Le camembert est parfait :)",
    0.03007647767663002,
    " parfait"
  ],
  [
    "Le camembert est bon :)",
    0.02145528607070446,
    " bon"
  ],
  [
    "Le camembert est délicieuse :)",
    0.015332158654928207,
    " délicieuse"
  ],
  [
    "Le camembert est magnifique :)",
    0.012028267607092857,
    " magnifique"
  ],
  [
    "Le camembert est savoureux :)",
    0.009316671639680862,
    " savoureux"
  ],
  [
    "Le camembert est divin :)",
    0.008841886185109615,
    " divin"
  ]
]
```

please refer to swagger documentation for further technical details: [swagger documentation](https://market-place.ai.ovh.net/#!/apis/1e9818cb-d4f7-4028-9818-cbd4f7802840/pages/0061ba6e-2d89-43b1-a1ba-6e2d8943b12b)

* * *
Mascot by [Alix Chagué](https://twitter.com/Alix_Tz) © 2019