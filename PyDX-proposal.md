## Title

There's Hope for Chatbots

## Description

Intermediate python developers will learn how to build a chatbot engine that identifies bullying in chatrooms. Studies show that most social networks -- Twitter, Facebook, Twitch, Slack -- unintentionally make us less kind.[1] But there's `Hope`. At Hopester we've built an open source chatbot engine with an open API called `Hope`. We'll show you how to add `Hope` to your chat channels or build your own.

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

### Technical References

[1]: http://www.dplabucy.com/uploads/2/5/9/0/25908118/fanti_demetriou_hawa_2012.pdf
[2]: http://www.aclweb.org/anthology/P11-2102
[3]: http://jezebel.com/gamergate-trolls-arent-ethics-crusaders-theyre-a-hate-1644984010
[4]: http://ahnjune.com/wp-content/uploads/2011/11/0Final-Ahn2011JASIST.pdf
[5]: http://github.com/totalgood/twip

## Bio

After 12 years as an aerospace engineer, and living my childhood dream of sailing around for 4 years, Hobson eventually found what he was looking for in Portland's Open Source community. The inclusiveness of Portland combined with the openness of early MOOCs made it possible for him to retrain himself as a Machine Learning developer. He's been repaying that debt to "openness" ever since. Hobson recently cofounded TotalGood with Chick Wells to make that payback official. Total Good supports nonprofits with data science, hopefully adding to the common good.


## Prior Speaking Experience

Hobson started his career as a high school science teacher. During his aerospace career he gave academic talks regularly and taught 2 semesters a year of robotics engineering to other engineers. In Portland and in the python community hobson contributes to several open source projects (PyBrain, gensim, pyexiv, pug, twip, etc), taught college-level python machine learning classes (Hack University), mentors up and coming data scientists at Total Good and Sliderule, and has given a [lightning talk](https://www.youtube.com/watch?v=yws4n-0-Yj8&list=PLOa5qP-zwt209jXYXou8ZOWJpHq1jf4cb&index=1) and a [tutorial session](https://www.youtube.com/watch?v=oSSnDeOXTZQ&list=PLOa5qP-zwt209jXYXou8ZOWJpHq1jf4cb&index=2) at PyCon.

# Other Links

http://hopester.com
http://hobsonlane.com
http://totalgood.com
http://github.com/totalgood/
https://www.linkedin.com/in/hobsonlane