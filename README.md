# Pysilon Tracker  

Pysilon Tracker is a Python-based script designed to monitor the **tria.ge** platform for new Pysilon samples. When a new sample is detected, the script notifies the user with:  

- **Desktop Notifications**: Includes the sample's name and a clickable link to download.  
- **Sound Alerts**: Plays a notification sound stored in the `sound` folder.  

## Features  
- **Automatic Monitoring**: Checks the target URL every 60 seconds for updates.  
- **Custom Notification Sound**: Add your preferred sound file to the `sound` folder (default placeholder included).  
- **Easy-to-Use**: Lightweight and straightforward script for tracking Pysilon samples.  

## What to Do with a Pysilon  
Once you have downloaded a Pysilon file:  
1. Go to [Uncover it](https://www.uncoverit.org).  
2. Upload the Pysilon file to decompile it.  
3. Extract the Discord bot token from the file.  
4. Use the token with my [Nuker Tool](https://github.com/XDLIN57/PYNUKE) to perform further actions.

## Requirements  
- Python 3.11 or later  
- Libraries: ```requests, beautifulsoup4, plyer, playsound```

Install the required dependencies:  
```bash
pip install -r requirements.txt
 ```

## How to Use  
1. Clone the repository:  
   ```bash
   git clone https://github.com/XDLIN57/Pysilon-Checker.git  
   cd pysilon-checker  
   ```  
2. Run the script:  
   ```bash
   python PYSILONCHECKER.py  
   ```  
3. Add a custom notification sound by replacing the placeholder file in the `sound` folder. 
