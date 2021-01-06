# Data auto-sender

Based on Mr. Robot's episode 6 from season 1 "eps1.5_br4ve-trave1er.asf"

[![Elliot Plans To Break Vera Out Of Jail | Mr. Robot](https://img.youtube.com/vi/21-5b_UJdJI/0.jpg)](https://www.youtube.com/watch?v=21-5b_UJdJI)


### Overview

This is a script that verifies there was contact with a user every 24 hours and sends an email simulating a data leak if there was no contact.


### Setup
-----------

Please ensure you have Python >=3.x and Pip in your machine and on your path.
Also modify values to your needs in `cfg.py` and emails and password in the `settings.ini` file

Make sure you enable less secure apps access at: https://myaccount.google.com/lesssecureapps

```
pip install -r requirements.txt
python run.py
```