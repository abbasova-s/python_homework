# Write your code here.

#Task 1: Hello
def hello():
    return "Hello!"

print(hello())


#Task 2: Greet with a Formatted String
def greet(name):
    return(f"Hello, {name}!")
print(greet("Alex"))


#Task 3: Calculator
def calc(a, b, operation = "multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
        return("You can't multiply those values!")
print(calc(3,5,"add"))        
print(calc(3,5,"subtract"))
print(calc(3,5,"multiply"))
print(calc(3,0,"divide"))
print(calc(3,5,"modulo"))
print(calc(3,"pepsi","int_divide"))
print(calc(3,5,"power"))
print(calc(3,5))


#Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return(float(value))
            case "int":
                return(int(value))
            case "str":
                return(str(value))
    except ValueError:
        return(f"You can't convert {value} into a {type}.")
print(data_type_conversion(3.14, "integer"))
print(data_type_conversion(50, "float"))
print(data_type_conversion(67, "string"))
print(data_type_conversion("nonsense", "float"))


#Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return ("Invalid data was provided.")
    
print(grade(50, 40, 70,90))
print(grade(50, "balloon", 70,90))
print(grade(0, 30, 20,10))

#Task 6: Use a For Loop with a Range
def repeat (string, count):
    new_string = ""
    for i in range (count):
        new_string += string
    return new_string   
        
print(repeat("You're awesome!", 10))
print(repeat("You're awesome!", 0))


#Task 7: Student Scores, Using **kwargs
def student_scores(rating, **kwargs):
    match rating:
        case "best":
            highest_key = ""
            highest_value = 0
            for key, value in kwargs.items():
                if value > highest_value:
                     highest_value = value
                     highest_key = key
                else: 
                    continue
            return highest_key
        case "mean":
            total = sum(kwargs.values())
            count = len(kwargs)
            return total / count
        
print(student_scores("best", Misha = 50, Kamila= 100, Alex = 80))
print(student_scores("mean", Misha = 50, Kamila= 100, Alex = 80))


#Task 8: Titleize, with String and List Operations
def titleize(string):
    new_words = []
    words = string.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    for i, word in enumerate(words):
        if i == 0:
            first_word = word.capitalize()
            new_words.append(first_word)
        elif i == len(words) - 1:
            last_word = word.capitalize()
            new_words.append(last_word)
        elif word in little_words:
            new_words.append(word)
        else:
            other_word = word.capitalize()
            new_words.append(other_word)
    return " ".join(new_words)

print(titleize("game of thrones"))

        
#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    new_string = ""
    for letter in secret:
        if letter in guess:
            new_string += letter
        else:
            new_string += "_"
    return new_string

print(hangman("alphabet", "ab"))


#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(string):
    new_words = []
    words = string.split()
    vowels = ["a", "e", "i", "o", "u"]
    for word in words:
        if word [0] in vowels:
            converted_word = word + "ay"
        elif word.startswith("qu"):
            converted_word = word[2:] + word[:2] + "ay"
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    converted_word = word[i:] + word[:i] + "ay"
                    break
        new_words.append(converted_word)
    return " ".join(new_words)

print(pig_latin("how are you doing"))    