# RLCard Tutorial
This is an official tutorial for [RLCard: A Toolkit for Reinforcement Learning in Card Games](https://github.com/datamllab/rlcard). We provide step-by-step instructions and running examples with Jupyter Notebook for both **Python** and **R**. The Python tutorial is available in Colab, where you run your experiments in the cloud without installation.
*   Official Website: [http://www.rlcard.org](http://www.rlcard.org)
*   Paper: [https://arxiv.org/abs/1910.04376](https://arxiv.org/abs/1910.04376)
*   Resources: [Awesome-Game-AI](https://github.com/datamllab/awesome-game-ai)

## For Python
### Installation (Skip if using Colab)
Make sure that you have **Python 3.5+** and **pip** installed. Run the following command:
```
pip3 install -r requirements.txt
```

### Tutorials
*   [Having Fun with Pretrained Leduc Model](https://github.com/datamllab/rlcard-tutorial/blob/master/Python-rlcard-tutorial/leduc_holdem_pretrained.ipynb)
*   [Training DQN on Blackjack](https://colab.research.google.com/github/mia1996/r-rlcard_test/blob/master/Blackjack_dqn.ipynb)
*   [Running multiple processes](https://colab.research.google.com/github/mia1996/r-rlcard_test/blob/master/Blackjack_mutiple_process.ipynb)
*   [Leduc Hold'em as single-agent environment](https://colab.research.google.com/github/mia1996/r-rlcard_test/blob/master/Leduc_single_agent.ipynb)
*   [Training CFR on Leduc Hold'em](https://colab.research.google.com/github/mia1996/r-rlcard_test/blob/master/leduc_holdem_cfr.ipynb)

### Tutorials in Colab
*   [Having Fun with Pretrained Leduc Model](https://github.com/datamllab/rlcard-tutorial/blob/master/Python-rlcard-tutorial/leduc_holdem_pretrained.ipynb)
*   [Training DQN on Blackjack](https://colab.research.google.com/github/mia1996/r-rlcard_test/blob/master/Blackjack_dqn.ipynb)
*   [Running multiple processes](https://colab.research.google.com/github/mia1996/r-rlcard_test/blob/master/Blackjack_mutiple_process.ipynb)
*   [Leduc Hold'em as single-agent environment](https://colab.research.google.com/github/mia1996/r-rlcard_test/blob/master/Leduc_single_agent.ipynb)
*   [Training CFR on Leduc Hold'em](https://colab.research.google.com/github/mia1996/r-rlcard_test/blob/master/leduc_holdem_cfr.ipynb)

## For R
This tutorial uses [reticulate](https://rstudio.github.io/reticulate/) to call RLCard with R interfaces. Please make sure that you have **Python 3.5+** and **pip** installed.

*   [Training DQN on Blackjack](https://github.com/datamllab/rlcard-tutorial/blob/master/R-rlcard-tutorial/Deep-Q_learning_blackjack/Deep-Q_Learning_Blackjack.ipynb)
*   [Training CFR on Leduc Hold'em](https://github.com/datamllab/rlcard-tutorial/blob/master/R-rlcard-tutorial/CFR_leduc_holdem/CFR_leduc_hold'em.ipynb)
*   [Leduc Hold'em as single-agent environment](https://github.com/datamllab/rlcard-tutorial/blob/master/R-rlcard-tutorial/Random_agent_blackjack/Random_agent_blackjack.ipynb)
*   [Texas Hold'em nolimit](https://github.com/datamllab/rlcard-tutorial/blob/master/R-rlcard-tutorial/Texas_holdem_nolimit/r-rlcard_no-limit_Texas_Holdem.ipynb)
*   [Running Random agent on Blackjack](https://github.com/datamllab/rlcard-tutorial/blob/master/R-rlcard-tutorial/Random_agent_blackjack/Random_agent_blackjack.ipynb)

## Contributing
Contribution to this project is greatly appreciated! Please create an issue/pull request for feedbacks or more tutorials.

## Cite this work
If you find this repo useful, you may cite:
```bibtex
@article{zha2019rlcard,
  title={RLCard: A Toolkit for Reinforcement Learning in Card Games},
  author={Zha, Daochen and Lai, Kwei-Herng and Cao, Yuanpu and Huang, Songyi and Wei, Ruzhe and Guo, Junyu and Hu, Xia},
  journal={arXiv preprint arXiv:1910.04376},
  year={2019}
}
```

## Acknowledgements
The R tutorial is mainly based on the code provided by [@systats](https://github.com/systats). See [here](https://github.com/datamllab/rlcard/issues/96).
