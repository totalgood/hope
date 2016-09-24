---
layout: post
title: There's Hope for Chatbots
lang: en
revealjs-url: ''  # for absolute path to lib/ and css/ folders use '/'
theme: black
transition: fade  # none/fade/slide/convex/concave/zoom
center: false
---

# There's Hope for Chatbots

## Chatbots are

* Annoying
* Dumb
* Insensitive

> * Basically they are like <insert your least favorite politician here>

<div><aside class="notes">
TRUMP<br>
Or at least bots like **Tai** are<br>
The bots that try to be popular<br>
</aside></div>

---

## I think there's hope for bots that are

* Intersting
* Sensitive
* Smart

---

## Smart, Interesting bots

* Google Assistant
* Siri

---

## Sensitive Bots

* [Viv](https://techcrunch.com/2015/02/20/viv-built-by-siris-creators-scores-12-5-million-for-an-ai-technology-that-can-teach-itself/): Dag Kittlaus

Siri, but smarter

* [The Chatbot Club](http://www.lifehacker.com.au/2016/05/meet-viv-the-future-of-chatbots-and-artificial-intelligence/): Linda Chang

Mimics your personality on FB (you're sensitive, aren't you?)

* Koko (MIT)

Ground-up design for empathy

---

## How?

* regular expressions?
* statistical models (Markhov Chains)?
* logical grammar?

> * YES!

---

## Python Options

* Chatterbot
* Wil

---

<div><aside class="notes">
I'm going to show you how to build a prosocial chatbot, or at the very least least, a bot that  isn't antisocial. In the process you're going to get a peak into the technology used by most AI systems that interract in a natural way. But before all that I'd like to explain why I'm so passionate about chatbots. After all, most of them that we interract with are pretty annoying, almost infantile. They can be fun to play with, but aren't usualy all that helpful. And sometimes it's downright dehumanizing to be forced to deal with a machine when you know there's a human out there watching all the text stream by just waiting for you to say the magic word to step in and help you complete you get the information you need or complete your purchase. But for the call center personel who previously were treated like robots themselves, forced to click through a logic tree of questions and responses, all day long, it's probably a bit empowering. They finaly have a pet to keep them entertained while they work to help you solve your problem. 
</aside></div>

<div><aside class="notes">
And if you need a bigger picture reason, consider the concerns of Gates, Musk, Bostrom, and Chace who title their concerns "Surviving AI" or talk about a "Superintelligence Explosion" that could destroy human civilization. That's what inspires me. In the back of my mind I've convinced myself I've fighting the good fight on behalf of the human race. The big robotic machines called Google, Apple, Microsoft, or even Canonical. These bots have a one-tracked mind. They want to sell you something. The can listen to you, and give you new and interesting information and fun things to do, but they are always just waiting to pounce with just the right product to manipulate you into wanting. That maniuplative employment of "influence techniques" is antisocial, not social. So if we let corporations build our bots, none of them will have a soul. And more and more, we are being left out of the conversation. Bots are talking to each other through web APIs. Even if we monitored the traffic, it wouldn't be much fun reading through all the log files to look for bot conspiracies. We humans have the good manners to use the language of those around us rather than having coded conversations behind our neighbors' back. Or bots should be so polite.

<div><aside class="notes">
There are two approaches to chatbots that are working pretty well right now. We're going to combine both.  There's Will with his good manners and rules for action. He can answer your questions and obey your commands, because under the hood he has a graph of logic rules encoded into regular expressions and python conditionals (if-then-else). But if you step just outside of the bounds of what he understands by saying something like "tank u", his logic might get befuddled and Will will be speechless, unable to respond with his oft-used but enthusiastic response "Your welcome!".

<div><aside class="notes">
So once you teach your bot manners you can expand its repertoire more quickly with Machine Learning. Like an authoritarian, over-protective parent you can discover the magic of letting a child learn from its own mistakes and successes. And eventually you can no longer tell them to "do what I say, not what I do." That's the approach of bots like "Salvius" (`ChatterBot`). Salvius imitates the conversations he sees his parents (the human race) to. So all you need to do is socialize him by giving him a homelessman disguise and he'll learn from the conversations of all the passersby around him. Or, if you want to give him a crash course, just feed him a bunch of "call and response" musical lyrics or Shakespeare dialog and he'll be speaking like a born thesbian in no time. You can culture your bot any way you like.

<div><aside class="notes">
When we first domesticated wolves and ungulates, we chose those that were most domesticatable. When we tried with foxes and bears and other animals, we quickly learned our lesson that some things are teachable and some things aren't. Those that could obey our rules, like sitting back away from the campfire and hearth and waiting us to finish our meal before cleaning up our scraps. But they weren't pups when we first encountered them. When we raise our own children we just use baby talk to get their mouths moving and try to have conversations around them so they know what conversations look like. So we're going to start with Salvius, the imitation bot by Gunther Cox (who started the Salvious project as a High School science experiment!).

---

## Algorithm Ideas

- Analogy/generalization mad libs:
  - find words that appear in both statement and response
  - replace these paired words with their part of speech or some other "word type" in a separate statement_template, resonse_template DB record
  - for matches on these madlibs sentences that happen to be off on this filler word then transfer the missing word from the statement to the response
  - hack: surround all such words with -<{}>- to make them match levenshtein distance even when paired words don't match
- 4-D GIS index on LDA topic vectors for statements and responses

---

## Plan

1. train ChatterBot on tweets and other dialog DBs in data/
2. draft slides
3. add sentiment analysis within ChatterBot framework
4. convert to postgres on `hope` django app
5. implement madlibs hack
6. add twip predictor to ChatterBot logic
7. add tests and get them passing
