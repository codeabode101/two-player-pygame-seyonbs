🎮 5-Day Python: Simple Navigation Challenge
Practice moving your character around a screen and interacting with objects!
---
### Day 1: Move Your Square Up and Down
1. Create `move_game.py` and set up a basic Pygame window (e.g., 600x400).
2. Create a red square `character_rect = pygame.Rect(250, 150, 50, 50)` and a `speed` variable.
3. Inside your game loop, add code to move the square up using `pygame.K_UP` and down using `pygame.K_DOWN` (like in class).
4. Add simple boundary checks so the square doesn't go off the top or bottom of the screen:
   - If `character_rect.y < 0`, set `character_rect.y = 0`.
   - If `character_rect.y > screen_height - character_rect.height`, set `character_rect.y = screen_height - character_rect.height`.
5. Run your game and make sure your red square moves up and down and stops at the edges.
---
### Day 2: Go Left and Right Too!
1. Continue using your `move_game.py` from Day 1.
2. Add code to move your red square left using `pygame.K_LEFT` and right using `pygame.K_RIGHT`.
3. Add simple boundary checks so the square doesn't go off the left or right sides of the screen:
   - If `character_rect.x < 0`, set `character_rect.x = 0`.
   - If `character_rect.x > screen_width - character_rect.width`, set `character_rect.x = screen_width - character_rect.width`.
4. Run your game. Your square should now move in all four directions and stay on screen.
---
### Day 3: A Friend Joins the Game
1. In `move_game.py`, create a *second* blue square `player2_rect` (e.g., at `(50, 50, 50, 50)`).
2. Give this second square its own movement controls using `pygame.K_w` (up), `pygame.K_s` (down), `pygame.K_a` (left), and `pygame.K_d` (right).
3. Add the same boundary checks for `player2_rect` as you did for `character_rect` on Day 1 and Day 2.
4. (After core) Change the color of your first character to green.
5. Run your game. Now two squares should move independently with different keys and stay on screen.
---
### Day 4: Reach the Safe Zone
1. Keep your two moving characters.
2. Create a small, light gray `safe_zone_rect` (e.g., `pygame.Rect(500, 150, 80, 80)`) and draw it on the screen.
3. If `character_rect` (your first square) moves into the `safe_zone_rect` area, print a message like "Player 1 is safe!" to your console.
   (Hint: Check if `character_rect.centerx` is between `safe_zone_rect.left` and `safe_zone_rect.right`, AND if `character_rect.centery` is between `safe_zone_rect.top` and `safe_zone_rect.bottom`).
4. (After core) Change the `safe_zone_rect` color to bright green *while* Player 1 is inside it. Change it back to light gray when Player 1 leaves.
---
### Day 5: Your Own Small Change
1. Continue with your `move_game.py`.
2. (Open) Add one small feature to make your game more fun or different. You could:
   - Make the characters move faster or slower if you press the `SPACE` key.
   - Add a different color background to the game.
   - Change the size of one of the characters (e.g., make it wider).
   - Add a simple "Reset" button (e.g., `R` key) that moves both characters back to their starting positions.
3. Show off your unique addition!
