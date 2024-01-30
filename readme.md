# About
A shitty little program I made to track where shots take place on screen in OS

Move your mouse to the location of the shot, and press a key corresponding to the player who shot it.  First selection will be the scorer, the rest will be assists.  Note that adding assisters will rotate via FIFO system, so the second assister will become the first, and the first assister will be dropped.  The only way to modify the scorer is to use the backspace key

Default settings are 1,2,3 for team 1 shots/passes,  q,w,e for team 2 with the order being Forward 1, Forward 2 and goalie.  Order doesn't matter for forwards but goalie must be in that last spot.

Holding shift while clicking will register that the strike was a coreflip.  Backspace will delete the last assist.  If there are no assists it will replace the scorer.  F keys set the strike type.  Press enter to register the shot/goal

# Keys
- F1: Set strike type to "Strike"
- F2: Set strike type to "Primary"
- F3: Set strike type to "Secondary"
- F4: Set strike type to "Special"
- F5: Set strike type to "Passive"
- Enter: Enter the goal as constructed (or return focus when done with a checkbox, will not register the goal)
- 1,2,3: set the player on team 1
- q,w,e: set the player on team 2
- backspace: Delete the last player entry (second assister if exists, otherwise first assister if it exists, otherwise the scorer)

#Todo:
  - Redcore key binding
  - Stagger toggle or keybinding
  - track mouse on assists?
