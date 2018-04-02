# Password Strength Calculator

The scrip allows you to evaluate the strength of your password. Strong password is required to keep you personal information safe, at least from bruteforce attacks.

Your password is scored from 0 to 10. In order to get maximum score your password should meet following requirements.

1) Be at least 8 characters long (this is required!)
2) Use upper case and lower case letters (+2 points)
3) Use numbers at least twice separated by letters or special characters (78 => +1 point, 7ab8 => +2 points)
4) Use special characters like { !@#$%^&\*()) } at least twice
5) Use unique character sequences at least 3 times (not present in balcklist)

* blacklist file can be extend with words of your choice

Password scores examples:
"password" -> 0
"12345678" -> 1
"Password" -> 2
"Password1" -> 3
"1Password1" -> 4
"1Password1\*&" -> 6
"Pa3wo\*rd8ds\*nms" -> 10

# How to use script

```bash
python password_strength.py
```
Output:
```bash
Enter password (minimum len: 8):
Your password score is 10
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
