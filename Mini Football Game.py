import random
import time

class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def score_goal(self):
        self.score += 1

def simulate_match(team1, team2, duration=120, goal_interval=20):
    """Simulate a football match between two teams."""
    for second in range(0, duration + 1, goal_interval):
        time.sleep(1)  # Simulate the passing of time (optional)
        if random.random() < 0.5:  # 50% chance to score every 20 seconds
            scoring_team = random.choice([team1, team2])
            scoring_team.score_goal()
            print(f"Second {second}: {scoring_team.name} scored! (Score: {team1.name} {team1.score} - {team2.name} {team2.score})")

    print(f"\nFinal Score: {team1.name} {team1.score} - {team2.name} {team2.score}")
    if team1.score > team2.score:
        print(f"{team1.name} wins!")
    elif team2.score > team1.score:
        print(f"{team2.name} wins!")
    else:
        print("It's a draw!")

def main():
    print("Welcome to the Football Match Simulation!")
    
    team1_name = input("Enter the name of Team 1: ")
    team2_name = input("Enter the name of Team 2: ")

    team1 = Team(team1_name)
    team2 = Team(team2_name)

    simulate_match(team1, team2)

if __name__ == "__main__":
    main()