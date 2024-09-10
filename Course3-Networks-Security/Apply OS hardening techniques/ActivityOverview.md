# Brute Force Attack on YummyRecipesForMe.com

## Overview
In this activity, I investigated a security breach on the website *yummyrecipesforme.com*. A former employee successfully executed a brute force attack to access the admin panel by guessing the default password. Once inside, they embedded malicious JavaScript that redirected users to a fake website hosting malware.

## Investigation
By analyzing network traffic with tcpdump, I identified DNS and HTTP protocols involved in the attack. The DNS resolved *yummyrecipesforme.com* correctly, but a malicious JavaScript prompted a second DNS query, redirecting users to *greatrecipesforme.com*.

## Outcome
I documented the incident and recommended implementing **multi-factor authentication (MFA)**, enforcing **strong password policies**, and enabling **account lockout mechanisms** to prevent future brute force attacks.
