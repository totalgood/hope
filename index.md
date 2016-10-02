---
title: There's Hope for Chatbots
lang: en
revealjs-url: ''  # for absolute path to lib/ and css/ folders use '/'
theme: black
transition: fade  # none/fade/slide/convex/concave/zoom
center: false
---

# There's Hope for Chatbots

----------

* Chatbots are Everywhere
* Stroll through the ChatBot Zoo
* Two Approaches
* Breakthroughs
* Python Chatbot Frameworks
* ChatterBot APIs
* Demo

----------

# Chatbots are Hidden in Plain Sight

- SlackBot
- Amazon Echo
- Google Now
- Zukerberg's Personal Assistant
- Siri

<div><aside data-markdown="" class="notes">
How do they work?
the innards of chatbots are hidden in a loAs I was researching chatbots
The software behind Siri is the same as for a chatbot
English in, English out
Wrap it in STT and TTS and you've got Siri
<aside></div>

----------

# Micromoments

Friendly, slick sales bots

*"You look great this morning."*

*"Have a great day at work today."*

<div><aside data-markdown="" class="notes">
Flattery will get you everywhere
As nice as it sounds, it's manipulative
<aside></div>

----------

# Bot Community

[PandoraBots](http://www.pandorabots.com/)

* Like SquareSpace for bots
* Grammar for Q&A (flash cards!)
* Statistical ML too
* Bots can talk to each other (APIs)

----------

# ELIZA

* 1964
* Therapist Bot
* Used "reflection"

```text
Gorman: Whoa, conversations with an AI. Skynet is near.
ELIZA : I see. What makes you feel that way?
```

<div><aside data-markdown="" class="notes">
Joseph Weizenbaum  
14 years after Turing test
Reflection:  
1. Claim understanding  
2. Repeat what they said  
3. Replace "I" with "you"  
4. Ask for details, emotions  
<aside></div>

------------

# What about Tai?

* Why was Tai so cruel?
* It "reflected" it's audience
* Online learning is risky
* "Prime Objective": Popularity 

<div><aside data-markdown="" class="notes">
The core tech I'm going to show you is live  
And it's even less sophisticated than Tai  
So be careful  
<aside></div>

----------

# Gamergate

* Chatbots ...

* Coax users into being civil
* Enforce behavior rules
* Make harassers uncomfortable

<div><aside data-markdown="" class="notes">
* 40% of harassers ceased when confronted with a bot
* Most remaining "cured" with threats of penalty
* Very few kick-bans required
* Any gamers out there?
* Run into any "referee" chatbots?
<aside></div>


# Chomsky


- You: What's up?  
- Chomsky: I am chatting with my friends on the internet.  
- You: Cool! How do you do that?  
- Chomsky: Always stay cool whatever the weather. It is sometimes difficult, but I stick at it.

----------

# State of the Art Q&A

* Google Now ("OK Google")
* Siri
* Allo (Google Assistant)

<div><aside data-markdown class="notes">
You probably don't think of these as chat bots
But they are
They just have voice recognition layer on top
I'll show you how to add that to your bots too! (Sphinx)
<aside></div>

----------

# Sensitive Bots

----------

# [Josh's Mom](https://chatbotsmagazine.com/what-if-mom-had-a-chatbot-that-could-live-on-after-shes-gone-video-b9e11dab1937#.788p5kw6m)

- Josh: Hey Mom.  
- Mom: Hello.  
- Josh: How are you?  
- Mom: I'm doin' pretty good.  
- Josh: What are you doin'?  
- Mom: I'm reading a book.  
- Josh: Hey, can you send me a photo of us?  
- Mom: [sends photo] Remember this?  
- Josh: Yea... I do... I miss you.  
- Mom: I miss you too.  

<div><aside data-markdown class="notes">
* Josh Bocanegra basing bot on Mother
* CEO of Humai, a technology
* To reduce and maybe prolong grief
* Like Google maps, uses voice recordings, not TTS
* Logic engine is similar to ChatterBot
* We can use ChatterBot for "personality recording"
* Like a telephone conversation recording, but dynamic
<aside></div>

----------

# [Viv](https://techcrunch.com/2015/02/20/viv-built-by-siris-creators-scores-12-5-million-for-an-ai-technology-that-can-teach-itself/)

* Dag Kittlaus
* Siri, but smarter
* Online Learning (like Tai)

----------

# [The Chatbot Club](http://www.lifehacker.com.au/2016/05/meet-viv-the-future-of-chatbots-and-artificial-intelligence/)

* Linda Chang
* Mimics your personality on FB
* (you're sensitive, aren't you?)

----------

# Koko (MIT)

Ground-up design for empathy

----------

# [Allo](https://research.googleblog.com/2016/05/chat-smarter-with-allo.html)

* LSTM
* TensorFlow

<div><aside data-markdown="" class="notes">
"Smarter" Chat by Google
<aside></div>

---

# Experiments

----------

# [Speakeasy](http://lauragelston.ghost.io/)

* Character-level LSTM NN
* Quickly goes "off the rails"

----------

# [Mitsuku](http://www.mitsuku.com/)

* 2013 Winner of the Loebnez Prize!
* [Chat with it]((http://www.square-bear.co.uk/mitsuku/nfchat.htm)) yourself
* Backend is [open sourced](https://github.com/pandorabots/pandorabots.github.io/blob/master/_modules/mitsuku.md)
* Ontology-based

<div><aside data-markdown="" class="notes">
Most human-like open chatbot in 2013
"Stands her ground" in an argument
Large ontology backend (knowledge base)
<aside></div>

----------

# How?

* regular expressions?
* statistical models (Markhov Chains)?
* logical grammar?

* **YES!**

<div><aside data-markdown="" class="notes">
Chatterbot allows plugin of multiple LogicAdapters
So lets do them all!
<aside></div>

---

# Statistical Language Models

1. BOC (cryptography)
2. BOW (spam filters)
3. Bag of N-Grams
4. Sequence of Words
5. [Sequence of Characters](https://github.com/Lasagne/Recipes/blob/master/examples/lstm_text_generation.py)

<div><aside data-markdown="" class="notes">
More and more data required
More and more realism/fidelity/robustness
SOC RNN (LSTM) required for sophisticated/flexible chatbot (e.g. Tai, Siri, Google Assistant)
<aside></div>

----------

# Word Vectors

* LSI/PCA (Gensim)
* LDA (Gensim)
* Neural Nets (Word2Vec)

<div><aside data-markdown="" class="notes">
<aside></div>

----------

# Bags of Words

```
0         ['python', 'never', 'stop', 'learning', 'what'...
1                       ['Watching', 'Boa', 'vs', 'Python']
2         ['Monty', 'Python', 'The', 'silly', 'walk', 'v...
3         ['Senior', 'Software', 'Engineer', 'Full', 'St...
4         ['Architect', 'Django', 'Solr', 'Platform', 'E...
5           ['peaceful', 'rain', 'Python', 'inevitability']
```

----------

# Sparse Vectors

```
0         [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1...
1                        [(8, 1), (9, 1), (10, 1), (11, 1)]
2         [(11, 1), (12, 1), (13, 1), (14, 1), (15, 1), ...
3         [(11, 1), (18, 1), (19, 1), (20, 1), (21, 1), ...
4         [(11, 1), (18, 1), (20, 1), (23, 1), (27, 1), ...
5                      [(11, 1), (37, 1), (38, 1), (39, 1)]
```

----------

# Topic Vectors

<img src="/scatter-matrix-topic-example.png">

----------

# Grammar-Based

* subject: the "primary" noun active noun phrase of a sentence 
* predicate: verb phrase that says what happened to the subject

<div><aside data-markdown="" class="notes">
ELIZA used simple grammar rule called "reflection"  
PandoraBots uses similar predicate-processing rule to answer questions 
subject: Root of the AST In Parsey McParseface     
predicate: depends on the subject  and the object?
<aside></div>

----------

# [Parsey McParseface](https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html)

**[SyntaxNet](https://github.com/tensorflow/models/tree/master/syntaxnet)**

* Best Syntax-Tree tagger
* Best POS tagger

<div><aside data-markdown="" class="notes">
Statistical training of grammar tagger!
Used for grammar-based approaches
<aside></div>

----------

# Example Grammar

Process this sentence:

> "Who invented chatbots?"

Now this:

> "Can you tell me who invented chatbots?"

<div><aside data-markdown="" class="notes">
* Predicate: What the subject of a sentence does or is
* Interrogative Pronoun: asks a questions without identifying the noun
* Pronoun: He, she, it, then but without refernce to a known noun
* Who, what, where, when
* Extract the predicate
* Wiki the predicate and replace pronoun with the name of the page
<aside></div>

----------

# Problem with Word2Vec

> BFF  
> 4EVAH  
> XOXO  
> &h!t  

<div><aside data-markdown="" class="notes">
pretrained on WSJ formal english  
emoticons  
slang  
cursing  
obfuscation  
</aside></div>

----------

# New Hope

- Grammar: [SyntaxNet](https://github.com/tensorflow/models/tree/master/syntaxnet)
- Statistics: [Word2Vec & Gensim](https://radimrehurek.com/gensim/models/word2vec.html)
- Text: [Gutenberg](https://en.wikipedia.org/wiki/Project_Gutenberg)
- N-Grams: [Google Books](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html)
- Knowledge: [YAGO](https://en.wikipedia.org/wiki/YAGO_(database))

<div><aside data-markdown="" class="notes">

**SyntaxNet** Parsey McParseface
* POS tagging
* syntax/dependency tree  
  
**Word2Vec**  
* Pretrained High-Fi Vectors for WSJ language  
* Not good for informal slang  
* Easy to train on tweets and other "one-liner" sources  

**Gutenberg**
* Pre 1950's only
* Full text
* No tech terms

**N-Grams**
* 1-5-grams
* Occurr at least 40 times
* 15% of all books
* Lots of modern tech jargon!
* Great for word "age" tagging

**YAGO** yet another great ontology   
* 95% accurate  
* core to Watson  
* DBPedia, SUMO, WordNet  

<aside></div>

----------

# Python Chatbot Options

----------

# Will

<img src="/will.png">

-----------

# ChatterBot

<img src="/chatterbot-banner.png">

---------- 

# I Want Hope to Talk!

* Best Speech Recognition (Sphinx): [Sphinx](https://pypi.python.org/pypi/SpeechRecognition/)
* Best Speech Synthesis (TTS): [WaveNet](https://arxiv.org/pdf/1609.03499.pdf)

<div><aside data-markdown="" class="notes">
- WaveNet is open source!  
- Best speech recognition packages are closed source  
- Google describes architecture (LSTM)  
- and Speech recognition are easily trained
- and Kaldi, Sphinx are pretty good (Gaussian Mixture Models)
<aside></div>

----------

# ChatterBot Logic Adapter

----------

# Chat Age

* Flesch-Kincaid Grade level
* [Google NGram DB](https://books.google.com/ngrams) mean year

----------

# Sentiment 

* Valence + Intensity
* `NLTK`'s VADER by Hutto, C.J. & Gilbert
* 2-D emotion: valence + intensity
* pos, neg, neu, compound

----------

# Sarcasm

* trained on #sarcasm in twitter
* need context to improve on 70% accuracy

----------

# Kindness

Positivity / Sarcasm - Intensity - Negativity / Sarcasm + Readability + Chat Age

* curse words?
* "you" multiplier?

----------

# Advanced Features

- Analogy/generalization mad libs:
  - find words that appear in both statement and response
  - replace these paired words with their part of speech or some other "word type" in a separate statement_template, resonse_template DB record
  - for matches on these madlibs sentences that happen to be off on this filler word then transfer the missing word from the statement to the response
  - hack: surround all such words with -<{}>- to make them match levenshtein distance even when paired words don't match
- 4-D GIS index on LDA topic vectors for statements and responses

----------

# Neural Nets

----------

# Cole's Bot

- You: You are a jokester.
- Bot: I know .
- You: Lots of funny jokes.
- Bot: I don ' t know about it .
- You: Yes you do.
- Bot: Why do you want me to kill me ?
- You: I don't.
- Bot: You do .
- You: Really?
- Bot: Yeah .
- You: You are wrong about that.
- Bot: I ' m not .
- You: You certainly are stubborn.
- Bot: I know it .

[Cole pulls the plug]

<div><aside markdown-data class="notes">
Movie Scripts  
LSTM word-sequence model   
Based on Google Translate NN  
Padding to deal with differing response/statement len  
<aside></div>

-------------

# Chatterbot Comes with 

- math logic (one thousand plus two?)
- time logic (what day is tomorrow?)
- Levenshtein distance matching

-------------

# Chatterbot Babytalk

- Hi!
-   =>  "Hi!" (0)
- Hi!
- Hello!
-   =>  "Hi!" (0)
- Hello!
- How are you?
-   1 options.
-   =>  "Hello!" (0.13)
- Hello!
- What's up?
-   1 options.
-   =>  "Hello!" (0.15)
- Hello!
- What's up?
-   1 options.
-   =>  "Hello!" (0.15)

-------------

# Chatterbot Todling

- So here we are again. I hope you can remember this.
-   3 options.
-  =>  "That's very nice! True... but not nice." (0.47)
- That's very nice! True... but not nice.
- I think you meant to say "NOT" very nice. But I'll let it slide.
-   1 options.
-   =>  "Hmmm. Flattery. Nice stalling technique." (0.42)
- Hmmm. Flattery. Nice stalling technique.
- Ha. I'm not the one who needs to stall!
-   2 options.
-  =>  "Anything you like." (0.48)
- ( 1 ) = 1
- That's not very clever.
-  1 options.
-  =>  "I think you meant to say "NOT" very nice. But I'll let it slide." (0.52)
- I think you meant to say "NOT" very nice. But I'll let it slide.
- Thank you.
-   3 options.
-  =>  "Cool, let's talk about python. What do you think of it?" (0.57)
- Cool, let's talk about python. What do you think of it?

-------------

# Chatterbot Todling

- I love it! Great language. It's what I'm made of!
-   5 options.
-   =>  "ha. how'd you figure that out?" (0.48)
- ha. how'd you figure that out?
- Well, I kindof helped you write me, right?
-  1 options.
-   =>  "Not really." (0.43)
- Not really.
- Well, here's what I'm thinking. You and I talk. And I get "programmed" by all that talk... just like you!
-   1 options.
-   =>  "It sure is. That's a lot of patience." (0.38)
- It sure is. That's a lot of patience.
- Hmm. Yea I guess.       
-   7 options.
-   =>  "" (0.6)
- 
- So where'd you go?
-   1 options.
-   =>  "I'm fine, how are you?" (0.6)
- I'm fine, how are you?

