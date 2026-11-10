import random

print("⚔️ AI DUNGEON GENERATOR ⚔️")
print("--------------------------")

player_name = input("Enter your hero name: ")

locations = [
    "Forgotten Castle",
    "Crystal Cave",
    "Dark Forest",
    "Ancient Temple",
    "Volcanic Mountain"
]

quests = [
    "Recover a stolen artifact",
    "Rescue a trapped explorer",
    "Defeat a powerful monster",
    "Find a lost treasure map",
    "Protect a village from attack"
]

enemies = [
    "Shadow Dragon",
    "Goblin King",
    "Ice Troll",
    "Skeleton Warrior",
    "Fire Demon"
]

loot = [
    "Legendary Sword",
    "100 Gold",
    "Magic Staff",
    "Dragon Armor",
    "Rare Gem"
]

events = [
    "A mysterious traveler offers help.",
    "You discover a hidden passage.",
    "A trap activates beneath your feet.",
    "A magical storm appears.",
    "You find an old journal with clues."
]

player_hp = 100
enemy_hp = random.randint(50, 100)

location = random.choice(locations)
quest = random.choice(quests)
enemy = random.choice(enemies)
reward = random.choice(loot)
event = random.choice(events)

print("\n🎮 ADVENTURE GENERATED")
print(f"\n🏰 Location: {location}")
print(f"📜 Quest: {quest}")
print(f"👾 Enemy: {enemy}")
print(f"💰 Reward: {reward}")
print(f"🎲 Event: {event}")

input("\nPress ENTER to battle!")

while player_hp > 0 and enemy_hp > 0:

    attack = random.randint(10, 25)
    enemy_hp -= attack

    print(f"\n⚔️ You hit the {enemy} for {attack} damage!")

    if enemy_hp <= 0:
        break

    enemy_attack = random.randint(5, 15)
    player_hp -= enemy_attack

    print(f"💥 {enemy} hits you for {enemy_attack} damage!")

    print(f"❤️ Your HP: {player_hp}")
    print(f"👾 Enemy HP: {enemy_hp}")

if player_hp > 0:
    print("\n🏆 VICTORY!")
    print(f"You defeated the {enemy}!")
    print(f"You earned: {reward}")
else:
    print("\n💀 GAME OVER")

print(f"\nThanks for playing, {player_name}!")
