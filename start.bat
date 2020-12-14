ECHO is on.
if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
pipenv run python bot.py
