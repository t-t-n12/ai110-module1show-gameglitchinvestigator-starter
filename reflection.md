# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looks like a guessing number game with 3 levels (easy, normal, hard). We have attempts to guess the secret number.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The hints were backwards.
The real items less than 1 to the total attempts displayed on the game (Off-by-one error in attempts count).

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 10 (secret was 9), Hard mode |"Too High" hint shown|"Too Low" hint shown (hints reversed)|none|
|Guess of 8 (secret was 9), Hard mode|"Too Low" hint shown|"Too High" hint shown (hints reversed)|none|
|Played Hard mode, 4 guesses made (10, 8, 90, 90)|Attempts should show 4|Attempts displayed as 5|none|

**AI Help (Step 3):**
I asked the AI ​​to explain why the "Too High/Too Low" hints were reversed.
The AI ​​explained that on even-numbered turns, the code converts the secret number into a string,while the guess remains a number; this causes a data type mismatch (TypeError),forcing the code into a string-vs-string comparison instead of a number-vs-number one,resulting in an incorrect outcome.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code in VS Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested refactoring four functions (get_range_for_difficulty,
parse_guess, check_guess, update_score) out of app.py into logic_utils.py,and fixing the reversed hint logic inside check_guess. I verified this byrunning pytest (6/6 tests passed) and by playing the live game (streamlit run app.py), testing guesses on both odd and even attempts to confirm the hint direction was now correct.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The first time I asked the AI to fix the reversed hint bug, it only swapped the message text ("Go HIGHER!" ↔ "Go LOWER!") without explaining that there was a deeper bug: on even-numbered attempts, the secret gets converted to a string while the guess stays an integer, causing a type-comparison error.If I had only fixed the message wording without understanding the root cause, the outcome itself (Too High/Too Low) could still have been wrong on even attempts. I had to test this myself by playing on an even attempt to confirm the actual outcome was correct, not just the message.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I considered a bug truly fixed only when two things lined up: the automated pytest tests passed, AND I could reproduce the original buggy behavior live in the app and confirm it no longer happened — especially on even-numbered attempts, since that's specifically where the secret-to-string type-flip bug occurred.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran `pytest`, which executed 6 tests and all passed. One key test, test_hint_direction_too_high, checks that guessing higher than the secret returns the outcome "Too High" along with a message containing "LOWER" — this confirmed the hint wording now matches the correct direction. I also manually tested in the live app (`streamlit run app.py`) by guessing on attempt #2 and #4 (even attempts), which is where the type-flip bug used to break the comparison — both showed correct hints, confirming the deeper bug was fixed, not just the message text.

- Did AI help you design or understand any tests? How?
Yes. I asked Claude Code to generate the pytest tests, and it wrote test_hint_direction_too_high/low and test_initial_attempts_is_zero. It also helped me understand why the existing tests were failing before my fix — they were unpacking `outcome, _ = check_guess(...)` but I hadn't realized check_guess returns a tuple, not a plain string, until the AI pointed that out while debugging the test failures.
---

## 4. What did you learn about Streamlit and state?
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit runs again the whole script every time you click something, so normal variables would reset each time. `st.session_state` is a storage box that survives those reruns, so things like score and attempts stay remembered between guesses.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Testing the exact edge case that caused the bug, not just trusting that tests pass.

- What is one thing you would do differently next time you work with AI on a coding task?
Ask the AI to explain the bug's root cause before asking for a fix, not after.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI fixes can look correct (no errors, tests pass) while still missing the real bug, so I need to understand the fix myself before trusting it.