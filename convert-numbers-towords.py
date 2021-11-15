
one_digit_words = {
    '0': ["zero"],
    '1': ["one"],
    '2': ["two", "twen"],
    '3': ["three", "thir"],
    '4': ["four", "for"],
    '5': ["five", "fif"],
    '6': ["six"],
    '7': ["seven"],
    '8': ["eight"],
    '9': ["nine"],
}

two_digit_words = ["ten", "eleven", "twelve"]
hundred = "hundred"
large_sum_words = ["thousand", "million", "billion", "trillion"]

en = input("Enter any number to convert it into words or 'exit' to stop:")
j = int(en)

if len(en) == 1:
    for key, value in one_digit_words.items():
        if en == key:
            print(value)

if len(en) == 2:

    for key, value in one_digit_words.items():
        if key == en[0]:
            m = value[1]
            f = m+"ty"

            for key, value in one_digit_words.items():
                if key == en[1]:
                    m = value[0]
                    print(f+" "+m)
