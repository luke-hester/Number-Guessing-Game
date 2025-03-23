import os
import csv

file_name = "leaderboard.csv"
fields = ["Name", "Difficulty", "Guesses"]

if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)

def add(name, difficulty, guesses):
    with open(file_name, "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([name,difficulty,guesses])

def display():
    difficulty_levels = {1: "Easy", 2: "Medium", 3: "Hard"}
    def difficulty_sort(l):
        return int(l[1])

    def guesses_sort(l):
        return int(l[2])

    rows = []

    with open(file_name, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        fields = next(csv_reader)

        for line in csv_reader:
            rows.append(line)

        for i in reversed(range(1, len(difficulty_levels) + 1)):
            entries = []
            print(f"{difficulty_levels[i]} mode:")
            for row in rows:
                if int(row[1]) == i:
                    entries.append(row)

            entries.sort(key=guesses_sort)
            for entry in entries[:5]:
                print(f"Name: {entry[0]} - Guesses: {entry[2]}")