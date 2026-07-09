# 🔐 Password Generator

A simple Python program that generates strong random passwords using letters, numbers, and special characters.

## 📌 Features

- Generates secure random passwords
- Includes:
  - Uppercase letters (`A-Z`)
  - Lowercase letters (`a-z`)
  - Numbers (`0-9`)
  - Special characters (`!@#$%^&*`, etc.)
- User chooses the password length
- Ensures a minimum password length of 8 characters
- Handles invalid input gracefully

## 🛠️ Technologies Used

- Python 3
- Built-in modules:
  - `random`
  - `string`

## 📂 Project Structure

```
password-generator/
│
├── password_generator.py
└── README.md
```

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/password-generator.git
```

2. Navigate to the project folder.

```bash
cd password-generator
```

3. Run the program.

```bash
python password_generator.py
```

## 💻 Example

```
Enter password length: 12

Generated Password:
g@7Y!mP2#Lq$
```

## 📖 How It Works

1. The user enters the desired password length.
2. The program checks that the length is at least **8**.
3. It randomly selects characters from:
   - Letters
   - Digits
   - Punctuation
4. The selected characters are combined into a secure password.
5. The generated password is displayed.

## 🚀 Future Improvements

- Copy password directly to clipboard
- Save passwords to a file
- Generate multiple passwords at once
- Let users choose whether to include:
  - Numbers
  - Symbols
  - Uppercase letters
- Password strength indicator
- Graphical User Interface (GUI)
