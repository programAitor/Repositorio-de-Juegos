```python
#!/usr/bin/env python3

def start_game():
    print("\n### The Hero's Journey: A Text Adventure\n")
    print("**Starting Scenario:**")
    print("You are a young adventurer named Elara, living in a small village on the edge of the Whispering Forest. One day, a messenger arrives with alarming news: a dark beast has begun to terrorize nearby villages, and the village leader asks brave young people to join an expedition to stop it. You are at a crossroads, what will you do?\n")

    # First decision point
    print("**Decision 1: Answer the call or Stay in the village**\n")
    choice1 = input("Choose (1 to Join the expedition, 2 to Stay in the village): ")

    if choice1 == '1':
        print("\n**Option 1.1: Join the expedition**")
        print("You join the group of adventurers. After days of travel, you arrive at a fork in the forest. One path seems safer and known, the other is dark and less traveled, but could be a shortcut.\n")

        # Second decision for Option 1.1
        print("**Decision 1.1.1: Take the safe path or Take the shortcut**\n")
        choice2_1 = input("Choose (1 to Take the safe path, 2 to Take the shortcut): ")

        if choice2_1 == '1':
            print("\n**Outcome: The Patient Hero**")
            print("After a longer but uneventful journey, the expedition finally reaches the beast's lair. With a coordinated attack, they manage to defeat it, although several are wounded. Elara is hailed as a hero, and the village lives in peace. You learned that patience is sometimes the best weapon.\n")
        elif choice2_1 == '2':
            print("\n**Outcome: The Brave Sacrifice**")
            print("The shortcut leads you directly into an ambush of minor creatures, guardians of the beast. In the battle, Elara sacrifices herself to allow the rest of the expedition to escape and warn the village. The beast remains free, but the village is warned. Your bravery will be remembered, but at an immense cost.\n")
        else:
            print("Invalid choice. The expedition gets lost in the forest, and the beast continues to wreak havoc.\n")

    elif choice1 == '2':
        print("\n**Option 1.2: Stay in the village**")
        print("You decide to stay to protect your family and friends in the village. Time passes, and news from the expedition grows darker. The village prepares for the worst.\n")

        # Second decision for Option 1.2
        print("**Decision 1.2.1: Defend the village or Flee the village**\n")
        choice2_2 = input("Choose (1 to Defend the village, 2 to Flee the village): ")

        if choice2_2 == '1':
            print("\n**Outcome: The Fortress of Home**")
            print("The beast attacks the village. Despite their few forces, the inhabitants fight bravely, led by Elara. They manage to repel the beast, but the village is devastated. Elara becomes the leader of the reconstruction, demonstrating that true strength lies in unity and defending one's own.\n")
        elif choice2_2 == '2':
            print("\n**Outcome: The Lonely Exile**")
            print("The beast approaches, and panic takes over the village. You decide to flee with some others, leaving your home behind. You spend the rest of your days as a nomad, pursued by remorse and loneliness. You never again find a place to call home.\n")
        else:
            print("Invalid choice. The village falls prey to the beast while Elara hesitates about what to do.\n")

    else:
        print("Invalid choice. Elara remains undecided, and the fate of the village hangs in the balance.\n")


if __name__ == "__main__":
    start_game()
```
