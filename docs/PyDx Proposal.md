## Title

There's Hope for Chatbots

## Description

Intermediate python developers will learn how to build a chatbot engine that identifies bullying in chatrooms. Studies show that most social networks -- Twitter, Facebook, Twitch, Slack -- unintentionally make us more cruel and narcissistic.[1] But there's `Hope`. At Hopester we've built an open source chatbot engine with an open API called `Hope`. We'll show you how to add `Hope` to your chat channels or build your own.

## Pitch

Open source python packages for Natural Language Processing can now detect sarcasm and bullying with 70% accuracy, much better than human judges given the same classification task.[2] A variety of python chatbot engines and API wrappers make it possible to build chatbots that can help us all become more sensitive chatters. `Hope` is a chatbot contributing helpful nudges in chat forums and communities to minimize bullying and create a more fun, inclusive world for us all.

This talk will be a condensation and re-purposing of the algorithms and data from a [Pycon 2016 tutorial](https://us.pycon.org/2016/schedule/presentation/1778/) on building a [tweet impact predictor](https://www.youtube.com/watch?v=oSSnDeOXTZQ&list=PLOa5qP-zwt209jXYXou8ZOWJpHq1jf4cb&index=2) 

1. How to build a training set based on tweets
  - twitter API
  - automated tweet "slurping"
  - hashtags like #sarcasm to use as training labels
  - clean up the training set (discard misleading tweets)
2. Training a sentiment analysis engine to identify tweets
  - tokens and N-grams
  - TFIDFs
  - topic vectors
  - scoring tweets
3. Connecting your engine to a chat service
  - twitter API (again)
  - Slack API

## Bio

After 12 years as an aerospace engineer, and living my childhood dream of sailing around for 4 years, Hobson eventually found what he was looking for in Portland's Open Source community. The inclusiveness of Portland combined with the openness of early MOOCs made it possible for him to retrain himself as a Machine Learning developer. He's been repaying that debt to "openness" ever since. Hobson recently cofounded TotalGood with Chick Wells to make that payback official. Total Good support nonprofits with data science, hopefully adding to the commpon good.

[1]: http://www.dplabucy.com/uploads/2/5/9/0/25908118/fanti_demetriou_hawa_2012.pdf
[2]: http://www.aclweb.org/anthology/P11-2102
[3]: http://jezebel.com/gamergate-trolls-arent-ethics-crusaders-theyre-a-hate-1644984010
[4]: http://ahnjune.com/wp-content/uploads/2011/11/0Final-Ahn2011JASIST.pdf