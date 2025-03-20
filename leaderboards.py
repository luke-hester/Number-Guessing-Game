import os
import csv

file_name = "leaderboard.csv"
fields = ["Name", "Difficulty", "Guesses"]

def init():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fields)


def add(name, difficulty, guesses):
    with open(file_name, "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([name,difficulty,guesses])

def display():
    rows = []

    with open(file_name, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        fields = next(csv_reader)

        for row in csv_reader:
            rows.append(row)

        # debug prints
        print(f"Total no. of rows: {csv_reader.line_num:d}")
        print("Field names are: " + ", ".join(field for field in fields))

        print("First 5 rows:")
        for row in rows[:5]:
            for col in row:
                print(col,end=" ")
            print()