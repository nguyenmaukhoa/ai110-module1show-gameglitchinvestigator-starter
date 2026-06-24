# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.
#### #1. Hints are backwards:
  - Input: 13
  - Expected Behavior: Hints: "Go higher", as Secret is 77
  - Actual Behavior: Hints: "Go lower"
  - Console Output / Error: 

#### #2. Attemps are not recorded in history right away in Developer Info:
  - Input: 13 (first attempt)
  - Expected Behavior: 13 is recorded in History
  - Actual Behavior: 13 is not recorded in History until second attempt 
  - Console Output / Error: 

#### #3. Final Score is not the same to score in Developer Info
  - Input: 77
  - Expected Behavior: Final score = 25, Score = 25
  - Actual Behavior: Final score = 25, Score = -10
  - Console Output / Error: 

#### #4. Guess field is not cleared when clicking [New Game]
  - Input: Button [New Game] is clicked
  - Expected Behavior: Guess input field is cleared
  - Actual Behavior: Last game's input still there
  - Console Output / Error: 
  
--- 
## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  - Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - AI explained the difference of the state score in the developer mode and the final score displayed in UI exactly. This causes by the program reading the same variable in different points in time, leading to different value.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - Hints are backwards because the messages are wrong, but AI suggested something different, and irrelevant. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - The bug is fixed when the expected value is the same with the actual value
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - We had a bug related to the page not fully reset when clicking on New Game button. After the bug is fixed, the page is fully reset, and refresh.
- Did AI help you design or understand any tests? How?
  - AI analyzes the cause of the bug, suggest step-by-step fixing guidelines, then ask for premission to fix the code.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
   - Every time you touch anything on the page — click a button, type in a box, move a slider — Streamlit throws away the current page and re-cooks the entire recipe from scratch, top to bottom.

  - That's a "rerun." Your whole script runs again, start to finish, on every single interaction. It's not like a normal web app where only one little piece updates. The whole thing reloads.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - Fixing one bug at a time and re-testing after each. Isolating changes so you know exactly what fixed what.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
   - writing down the input, expected behavior, and actual behavior for every bug before trying to fix it
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI tool is a great way for me to analyze, design, code, and fix bug faster, and more efficient. However, I should be very careful with its answers, I should understand every step in order to code accurately, avoiding trusting AI blindly.
