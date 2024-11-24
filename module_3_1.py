calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(string):
    global calls
    count_calls()
    string = (len(string), string.upper(), string.lower() )
    return string
def is_contains (string, list_):
    global calls
    count_calls()
    for i in range(0, len(list_)):
        list_[i] = list_[i].lower()
    if string.lower() in list_:
        print(True)
    else:
        print(False)
    return string, list_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)