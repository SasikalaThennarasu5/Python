from fitness import workout, diet, progress

def menu():
    while True:
        print("\n🏋️ FITNESS TRACKER MENU")
        print("1. Log Workout")
        print("2. Log Meal")
        print("3. Log Progress")
        print("4. View Latest Progress")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            wtype = input("Workout type: ")
            duration = int(input("Duration (min): "))
            calories = int(input("Calories burned: "))
            workout.log_workout(wtype, duration, calories)

        elif choice == "2":
            meal = input("Meal description: ")
            calories = int(input("Calories intake: "))
            diet.log_meal(meal, calories)

        elif choice == "3":
            weight = float(input("Current weight (kg): "))
            goal = float(input("Goal weight (kg): "))
            progress.log_progress(weight, goal)

        elif choice == "4":
            progress.view_latest_progress()

        elif choice == "5":
            print("👋 Exiting Fitness Tracker.")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
