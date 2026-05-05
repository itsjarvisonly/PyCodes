def check_answer(user_input, correct_answer):
    """
    Checks if the user's answer matches the correct answer.
    Returns 1 for correct, 0 for incorrect.
    """
    # .upper() ensures that 'a' and 'A' are treated the same
    if user_input.upper() == correct_answer:
        print("Correct! ✅\n")
        return 1
    else:
        print("Wrong! ❌ The correct answer was", correct_answer, "\n")
        return 0

def run_quiz():
    """
    Main function to run the quiz application.
    """
    print("--- Python Mini Project Quiz ---")
    print("Type the letter of your answer and press Enter.\n")
    
    # Data structure: A simple list of lists.
    # Format: [ "Question text", "Options separated by \n", "Answer" ]
    quiz_data = [
        [
            "1. How can you create a string variable in Python?",
            "A. Enclosing characters in square brackets, like [Hello]\nB. Enclosing characters in quotes, like \"Hello\"\nC. Enclosing characters in parentheses, like (Hello)\nD. Enclosing characters in curly braces, like {Hello}",
            "B"
        ],
        [
            "2. What is the purpose of the `in` operator in Python?",
            "A. To add an element to a sequence.\nB. To remove an element from a sequence.\nC. To check for the presence of an element in a sequence.\nD. To count the number of elements in a sequence.",
            "C"
        ],
        [
            "3. What does the `ord()` function do in Python?",
            "A. Checks if a character is present in a string.\nB. Combines two characters into a string.\nC. Converts a character to its integer representation.\nD. Converts an integer to a character.",
            "C"
        ],
        [
            "4. What is the primary purpose of the slice operation in Python?",
            "A. To reverse the order of sequences.\nB. To delete elements from sequences.\nC. To extract portions of sequences.\nD. To define new sequences.",
            "C"
        ],
        [
            "5. If you have the string `word = \"Python\"`, what would `word[-1]` output?",
            "A. y\nB. n\nC. P\nD. o",
            "B"
        ],
        [
            "6. Which Python module provides functions for managing files and directories?",
            "A. random\nB. math\nC. os\nD. sys",
            "C"
        ],
        [
            "7. What is the output of the following code?\nf = open(\"test.txt\", \"w\")\nf.write(\"ABC\")\nprint(f.read())",
            "A. ABC\nB. Empty\nC. Error\nD. None",
            "C"
        ],
        [
            "8. Which method is used to remove an empty directory in Python?",
            "A. os.delete_dir()\nB. os.rmdir()\nC. os.remove_folder()\nD. os.clear_dir()",
            "B"
        ],
        [
            "9. To open a file c:\\scores.txt for writing, we use ________",
            "A. outfile = open(\"c:\scores.txt\", \"w\")\nB. outfile = open(\"c:\\\\scores.txt\", \"w\")\nC. outfile = open(file = \"c:\scores.txt\", \"w\")\nD. outfile = open(file = \"c:\\\\scores.txt\", \"w\")",
            "B"
        ],
        [
            "10. What is the output of the following code?\nf = open(\"test.txt\", \"w\")\nf.write(\"hello\")\nf.close()\n\nf = open(\"test.txt\", \"r\")\ndata = f.read()\nprint(data.upper())",
            "A. hello\nB. HELLO\nC. Error\nD. None",
            "B"
        ]
    ]
    
    score = 0
    
    # Loop through our list of questions
    for item in quiz_data:
        question_text = item[0]
        options_text = item[1]
        correct_answer = item[2]
        
        # Display to the user
        print(question_text)
        print(options_text)
        
        # Take input
        user_choice = input("Enter your choice (A/B/C/D): ")
        
        # Call our check_answer function and add the result to the score
        score += check_answer(user_choice, correct_answer)

    # Final result
    print("==============================")
    print("Quiz Over! Your final score is:", score, "out of", len(quiz_data))

# Start the program
run_quiz()