# 🔒 Password Generator in Python
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

This project is a simple Python-based password generator that creates strong, customizable passwords for any account. The script guarantees password complexity and saves each password with its account name to a local text file.

## 🚀 Features
  - **Custom Length:** Specify your desired password length (minimum 4 characters).
  - **Guaranteed Security:** Each password includes at least one uppercase letter, one lowercase     letter, one digit, and one symbol.
  - **Randomized Output:** Passwords are shuffled for extra security.
  - **Account Tagging:** Assign each password to an account name (e.g., Gmail, Facebook).
  - **Automatic Saving:** Passwords and their associated accounts are saved to `passwords.txt` for easy reference.

## 🛠️ How to Use

1. **Clone or Download the Script**
   - Save the code as `password_generator.py`.
  
2. **Run the Script**
python password_generator.py
or
python3 password_generator.py

3. **Follow the Prompts**
  - Enter the desired password length (minimum 4).
  - Specify what the password is for (e.g., Facebook, Gmail).

4. **Get Your Password**
  - The generated password will be displayed and saved to a file named `passwords.txt` in the same directory.

## 📋 Example
Enter the length of your password (min 4): 12
What is this password for? (e.g., Facebook, Gmail): github

Sucessfully generated password for Github: 8@tPz2w!qLrD
Password saved to 'passwords.txt'.

## 📂 Output File Structure
Each generated password is stored in `passwords.txt` as:
AccountName: password
Example:
Gmail: x7@Kq9!bLp2T
Facebook: 1!dEw3@GhTzP

## ⚠️ Security Note
  - **Keep your `passwords.txt` file safe!**
  - It contains all your generated passwords in plain text.
  - For extra security, consider encrypting the file or using a dedicated password manager.

## 🧑‍💻 Requirements
- Python 3.x (no external libraries required)

## 🤝 Contributing
Feel free to fork this repository and submit pull requests for improvements or new features!

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

*Made with ❤️ by Syed Afaq Gilani in Python*
*Try it now and beat the odds! 🚀*
