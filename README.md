# Pysilon Tracker  

Pysilon Tracker is a Python-based script designed to monitor the **tria.ge** platform for new Pysilon samples. When a new sample is detected, the script notifies the user with:  

- **Desktop Notifications**: Includes the sample's name and a clickable link to download.  
- **Sound Alerts**: Plays a notification sound stored in the `sound` folder.  

## Features  
- **Automatic Monitoring**: Checks the target URL every 60 seconds for updates.  
- **Custom Notification Sound**: Add your preferred sound file to the `sound` folder (default placeholder included).  
- **Easy-to-Use**: Lightweight and straightforward script for tracking Pysilon samples.  

## Requirements  
- Python 3.11 or later  
- Libraries: `requests`, `beautifulsoup4`, `plyer`, `playsound`  

Install the required dependencies:  
```bash
pip install -r requirements.txt
```  

## How to Use  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/pysilon-tracker.git  
   cd pysilon-tracker  
   ```  
2. Run the script:  
   ```bash
   python pysilon_tracker.py  
   ```  
3. Add a custom notification sound by replacing the placeholder file in the `sound` folder.  

## Notes  
- Ensure a stable internet connection for accurate monitoring.  
- Edit the URL in the script if the target page changes its structure or query parameters.  

---
