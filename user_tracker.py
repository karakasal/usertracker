user_list = {101: "John", 102: "Jane"}
user_nums = list(user_list.keys())
user_names = list(user_list.values())
report_monthly = []
confirm = ["y", "n"]

holidays = [{6, 7, 13, 14, 20, 21, 27, 28}, {3, 4, 10, 11, 17, 18, 24, 25}, {6, 7, 13, 14, 20, 21, 27, 28}, {3, 4, 10, 11, 17, 18, 24, 25}
            , {6, 7, 13, 14, 20, 21, 27, 28}, {3, 4, 10, 11, 17, 18, 24, 25}, {6, 7, 13, 14, 20, 21, 27, 28}, {3, 4, 10, 11, 17, 18, 24, 25}
            , {6, 7, 13, 14, 20, 21, 27, 28}, {3, 4, 10, 11, 17, 18, 24, 25}, {6, 7, 13, 14, 20, 21, 27, 28}, {3, 4, 10, 11, 17, 18, 24, 25} ]
month_length = [32,29,32,29,32,29,32,29,32,29,32,29]

for m in range(1,13):
    month_days = set(range(1, month_length[m-1])).difference(set(holidays[m-1]))
    for d in month_days:
        print(f"{d}/{m}/2024")
        new_user_question = input("New user? Y/N ") 
        while new_user_question.lower() not in confirm:
            new_user_question = input("Only Y or N! ")
        if new_user_question.lower() == "y":
            new_user_num = input("New user number? ")
            while not new_user_num.isdigit():
                new_user_num = input("Only numbers! ")
            while int(new_user_num) in user_nums:
                new_user_num = input("Number exist! ")
                while not new_user_num.isdigit():
                    new_user_num = input("Only numbers! ")
            new_user_name = input("New user name? ")
            while not new_user_name.isalpha():
                new_user_name = input("Only letters! ")
            user_list.update({int(new_user_num) : new_user_name.capitalize()})
        elif new_user_question.lower() == "n":
            pass
        print(f"\n{user_list}")
        user_nums = list(user_list.keys())
        user_names = list(user_list.values())
        report_daily = []
        absent_question = input("Any absent user? Y/N ")
        while absent_question.lower() not in confirm:
            absent_question = input("Only Y or N! ")
        if absent_question.lower() == "y":
            absent_num = input("Absent user number? ")
            for _ in user_nums:
                while not absent_num.isdigit():
                    absent_num = input("Only numbers! ")
                if int(absent_num) in user_nums and int(absent_num) not in report_daily:
                    report_daily.append(int(absent_num))
                    absent_question_other = input(f"Except {user_list[int(absent_num)]} any absent user? Y/N ")
                    while absent_question_other.lower() not in confirm:
                        absent_question_other = input(f"Only Y or N! ")
                    if absent_question_other.lower() == "y":
                        absent_num = input("Absent user number? ")
                        continue
                    elif absent_question_other.lower() == "n":
                        print("\nAbsents;")
                        for num in range(len(report_daily)):
                            print(f"- {user_list[report_daily[num]]}")
                        break
                elif int(absent_num) in user_nums and int(absent_num) in report_daily:
                    absent_num = input("User exist! Absent user number? ")
                    continue
                elif int(absent_num) not in user_nums:
                    absent_num = input("User not exist! Absent user number? ")
                    continue
        elif absent_question.lower() == "n":
            pass
        with open("report.txt", "a") as file:
            file_list = []
            for i in range(len(report_daily)):
                file_list.append(f"{report_daily[i]}: {user_list[report_daily[i]]}")
            file.writelines(f"{d}/{m}/2024 {file_list}\n")
        report_monthly.append(report_daily)
        print("")
    print(report_monthly)
    report_monthly.clear()
print("2025!")