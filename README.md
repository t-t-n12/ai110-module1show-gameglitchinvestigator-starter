# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose: A Streamlit-based number guessing game where the player picks a difficulty (Easy/Normal/Hard) and tries to guess a secret number within a limited number of attempts, using "Too High"/"Too Low" hints.

- [x] Detail which bugs you found: 
(1) Hints were reversed — guessing higher than the secret said "Go HIGHER!" instead of "Go LOWER!". 
(2) Attempts counter was off-by-one — it initialized at 1 instead of 0, so "Attempts left" was always one short. 
(3) A related bug caused score to behave inconsistently on "Too High" outcomes depending on whether the attempt number was even or odd.

- [x] Explain what fixes you applied:
I refactored the core logic (get_range_for_difficulty, parse_guess, check_guess, update_score) out of app.py into logic_utils.py. I fixed the reversed hint direction in check_guess so guessing higher correctly returns "Go LOWER!". I fixed the attempts off-by-one bug by initializing st.session_state.attempts to 0 instead of 1. I verified both fixes with pytest (6/6 tests passing) and by manually testing the live app.

## Demo Walkthrough
1. Game starts in Hard difficulty. Secret number is chosen between 1 and 50. "Attempts left: 5" is shown.
2. User enters a guess of 10 → Game returns "Too High — Go LOWER!"
3. User enters a guess of 8 → Game returns "Too Low — Go HIGHER!"
4. Score updates after each guess (decreases since neither guess was a win).
5. "Attempts left" decreases by 1 after each guess (now shows 3 remaining).
6. User enters a guess of 9, which matches the secret number → Game returns "🎉 Correct!" and displays balloons.
7. Final score is shown, and the game status changes to "won" — further guesses are blocked until "New Game" is clicked.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results
```
============================= test session starts ==============================
platform darwin -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/nguyentuetam/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 6 items

tests/test_game_logic.py ......                                          [100%]

============================== 6 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
