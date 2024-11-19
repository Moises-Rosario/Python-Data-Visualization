def eligibility(gpa):
    if gpa > 2.9:
        return name + ", you are currently eligible to get the scholarship."
    else:
        return name + ", only people with a GPA of 3.0 and above are eligible for the scholarship."

def handle_request():
    request = input("Which would you like help with? 'scholarship', 'contact', or 'catalog': ").lower()

    # Handle different requests
    if "scholarship" in request:
        try:
            gpa = float(input("What is your current GPA? "))
            print(eligibility(gpa))
            if gpa > 2.9:
                print("In order to opt for this privilege, please contact the admission department.")
        except ValueError:
            print("Please enter a valid GPA.")
    elif "contact" in request:
        print("You can contact AD at AdmissionD@myscholar.edu")
    elif "catalog" in request:
        print("We offer a variety of courses: Computer Science, Pre-Nursing, Business Administration.")
    else:
        print("I'm sorry, this chatbot is currently under development and can provide information on scholarship, contact, and catalog.")

def main():
    global name
    name = input("Welcome to the University of Rut's Chatbot. What's your name? ").capitalize()

    if "Donald" in name:
        print("I'm sorry, " + name + ", you are not permitted in the University.")
        exit()
    else:
        print("Welcome " + name + "!")
    
    # Interaction loop to handle multiple rounds of user input
    while True:
        handle_request()
        request = input("Is there anything else you'd like help with? (y/n) ").lower()
        
        if request == 'n':
            print("Thank you for using this chatbot!")
            break  # Exit the loop and end the program
        elif request != 'y':
            print("Please enter a valid response: 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()

   