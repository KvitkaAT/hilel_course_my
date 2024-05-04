user_input = int(input("Введіть число: "))
if 8640000 > user_input >= 0:
    days, d_remainder = divmod(user_input, 86400)  # returns number of days & remainder of seconds
    if days == 0:
        days_output = "0 днів"
    elif days % 10 == 1 and days != 11 or days == 1:  # output for 1, 21, 31, 41.. days excl. 11
        days_output = f"{days} день"
    elif days % 10 in {2, 3, 4} and days not in {12, 13, 14}:  # output for days 2-4, 22-24, 32-34.. excl.12-14
        days_output = f"{days} дні"
    else:
        days_output = f"{days} днів"
    hours, h_remainder = divmod(d_remainder, 3600)  # returns the number of hours & remainder of seconds
    hours_output = f"{hours}".zfill(2)  # formatted hours string filled with zeroes up to length 2
    minutes, seconds = divmod(h_remainder, 60)  # returs number of minutes & remainder is seconds
    minutes_output = f"{minutes}".zfill(2)  # formatted minutes string filled with zeroes up to length 2
    seconds_output = f"{seconds}".zfill(2)  # formatted seconds string filled with zeroes up to length 2
    print(f"{days_output}, {hours_output}:{minutes_output}:{seconds_output}")  # formatted output
else:
    print("Число має бути >= 0 та < 8640000. Спробуйте ще раз.")  # wrong input user messages
