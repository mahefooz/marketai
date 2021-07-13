# marketai

This program downloads the optionchain data from NSE website and pushes it to Excel file (Index OI.xlsx). The excel file refreshes the data every 5m. Below is the installation procedure.

1. Install Latest Python from python.org.
2. Install pipenv - "pip install pipenv".
3. Download the git folder.
4. Change to downloaded folder and issue command - "pipenv install"/
5. The above command downloads all the dependencies.
6. Whenever you want to view realtime OI data, open terminal (command prompt on windows), change to above folder, and issue these commands - "pipenv shell" and "py manage.py runserver".
7. Then open the excel file and it refreshes automatically.
8. Sometimes you may get "records not found", ignore it. Some other times it will ask to connect, just press connect button and it will refresh.
