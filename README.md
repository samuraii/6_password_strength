# Password Strength Calculator

The script allows you to evaluate the strength of your password. Strong password is required to keep you personal information safe (at least from bruteforce attacks).

Your password is scored from 0 to 10. In order to get maximum score your password should meet following requirements.

1) Be at least 8 characters long (**this is required!**)
2) Use upper case and lower case letters
3) Use numbers at least twice separated by letters or special characters
4) Use special characters like **!@#$%^&\*())** at least twice
5) Use unique character sequences at least 3 times (unique character sequences are those which not present in **blacklist.txt**)

**Note**: _You should pass your own **blacklist.txt** file as a parametr to script, otherwise the check will not be performed. You can obtain a blacklist from: https://github.com/danielmiessler/SecLists/tree/master/Passwords, it's regular updated. The more common words words you will use in your list, the more secure your password will be._


## Password scores examples:

```bash
"password" -> 0
"12345678" -> 1
"Password" -> 2
"Password1" -> 3
"1Password1" -> 4
"1Password1\*&" -> 6
"Pa3wo*rd8ds&nms" -> 10
```

## How to use script

Run script and pass it path to **blacklist.txt** as parametr:

```bash
python password_strength.py <path_to_blacklist>
```

Output:

```bash
Enter password (minimum len: 8):
Your password score is 10
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
