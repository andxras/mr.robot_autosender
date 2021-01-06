# Autoleak

Based on Mr. Robot's episode 6 from season 1 "eps1.5_br4ve-trave1er.asf"

[![Elliot Plans To Break Vera Out Of Jail | Mr. Robot](https://heavy.com/wp-content/uploads/2017/12/vera-season-1-pic-2.jpg?quality=100&strip=all)](https://www.youtube.com/watch?v=21-5b_UJdJI)


### Overview

This is a recreational script that verifies there was contact with a user every 24 hours and sends an email simulating a data leak if there was no contact.


### Setup
-----------

Please ensure you have Python >=3.x and Pip in your machine and on your path.
Also modify values to your needs in `cfg.py` and emails/password in the `settings.ini` file

Make sure you enable less secure apps access at: https://myaccount.google.com/lesssecureapps

```
pip install -r requirements.txt
python run.py
```

You now have 24 hours before the email is being sent. Go to http://localhost:5000/ping in order to cancel "Data Leakage".
