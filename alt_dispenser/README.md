# Setup
1. Do `git clone https://github.com/hkyq/r_requestabot/`
2. Do the following commands:
```
pip3 install wheel
pip3 install requests
pip3 install discord.py
```
3. Create your username:password lists
4. Do `cd r_requestabot`
5. Do `nano main.py`, in the last line add your bots token. If you don't have one, see [this](https://twentysix26.github.io/Red-Docs/red_guide_bot_accounts/). Scroll down to the steps, and paste your token (from step 4) into the quotes
6. Do `crontab -e`, and pick out a time for the alt dispenser to reset from [here](https://crontab.guru/)
7. On a new line in `crontab -e`, paste the time from the crontab site like this:

```5 4 * * * [your username] rm /home/[your username]/r_requestabot/users.txt```

8. Run bot with `python3 main.py`
