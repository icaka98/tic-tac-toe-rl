<h1 align='center'>
  Tic-Tac-Toe Reinforcement Learning
  <a href="https://github.com/sindresorhus/awesome"><img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Markdownify" width='120'>
  </a>
</h1>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Setup](#setup)
    * [Windows](#windows)
    * [MacOS](#macos)
* [Instructions](#instructions)
    * [Running a model training](#running-a-model-training)
    * [Running a simulation](#running-a-simulation)
    * [Playing a game](#playing-a-game)
    * [Pre-trained model policy](pre-trained-model-policy)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

This project is built with the intention of training a Reinforcement Learning bot to play Tic-Tac-Toe. The bot is able to play against itself and learn an optimal policy. The policy is then preserved and loaded when a human wants to play against the bot.

## Setup

### Windows
```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### MacOS
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Instructions


### Running a model training
The default training uses Q-Learning (Reinforcement Learning) to teach the bot the game of Tic-Tac-Toe.
It initializes two fresh models that play agains each other and continuously train.
The default number of training games is `1_000_000`.

You can perform training using the following command:
```
python train.py
```

### Running a simulation
The model simulation brings up the pre-trained model and simulates Tic-Tac-Toe games with a random bot.
The random bot stochastically selects an available free square and plays it.
The goal of this operation is to evaluate the performance of the model.
During experimentation, the best performing bot had 0 losses within `1_000_000` games played.
The default number of games to play in the simulation script is `10_000`.

You can run a simulation using the following command:
```
python simulate.py
```

### Playing a game
You can play a human vs bot game using the following command:
```
python play.py
```

### Pre-trained model policy
The `best_policy_top.json` file contains the optimal policy of the bot that performed best.
This is the policy that the `play` script loads to play Tic-Tac-Toe against the human.
Feel free to modify the code, so you play with a bot that you've trained. 

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact
Hristo Minkov - minkov.h@gmail.com

Codebase Link: [https://github.com/icaka98/tic-tac-toe-rl](https://github.com/icaka98/tic-tac-toe-rl)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: git_images/present.png