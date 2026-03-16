# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
-  PROBLEM 1 --> When I press on "New game" after finishing one, it generates a random number but does not clear the memory of the previous game from it. 
Case 1 : If the new game is started amid the previous ongoing game, the score is not affected even though the number of attempts are. 
Case 2: If the game ends, in both the scenerio of winning and losing, the "submit guess" button does not take to a new instance.

- PROBLEM 2 --> The hints shown by the game are completely wrong. When input a lower number than the correct one, it suggests going even further lower and vice versa for higher numbers. 

- PROBLEM 3 --> Easy mode got fewer attempts than normal mode, making the easy mode even harder. 

- PROBLEM 4 --> the "auto rerun" option after clicking the three dots has no effect on the game. 

- PROBLEM 5 --> It always showed "choose between 1 and 100" even if the numbers differed according to the       difficulty level
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For this project, I used Claude and Co-pilot. Most of the issues it fixed was based on the FIXME lines I wrote beforehand to guide it throughout what to fix. This also prevented the agent from overdoing things I would not have wanted to change. 

One example of an AI suggestion that was correct and was not something I thought about was about the even-numberes attempt that convers the secrect to a string and makes it impossible to win on even attempts. After verifying this error by playing the games on multiple even number attempts, I let the AI fix it. 

One example of an AI suggestion that was incorrect was that it could not give me the correct gihub command for pytesst but I did this tallying the commands in google gemini search 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested the update in the Streamlit app in my browser and tested the game to see if the update worked without any errors. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I tested it in the brower manually by playing the guessign game and the update worked and ran smoothly. 
- Did AI help you design or understand any tests? How?
I did not know about pytest before this. Google gemini helped to clarify the test with specific examples. Using claude, I was able to implement it as well.


## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Stremlit "reruns" re-executes the whole line of code everytime something is changes. In this case, the session state saves the data between those refreshes. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I had rarely used FIXMEs before and that made it hard to keep track of the errors. In this project, the fixme was very helpful and I will be using them a lot in future projects.
  
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time, I would like to ask AI in detail about every function being implemented to know more about how AI maps out problem solving.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  From this project, I realised that AI could both completely resolve or mess up the code the developer has been working on. Rewatching every implementation carefully so that the final code does not crash is also very important in AI-assisted projects. 
