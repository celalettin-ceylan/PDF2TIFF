# PDF2TIFF APP
This basic app convert all pdf pages to tiff file format. This app wrote Python v3.12.4, so you could not able to run on Windows 7 and older version. 

## Installation for Windows

You can apply following steps for installation:
- Clone github repo
- Create a virtual enviroment on Windows CMD and install requirements. You can use VSCode terminal but you should select powershell. 
```bash
$ python.exe -m venv venv
$ .\venv\Scripts\activate.bat
$ pip install -r .\requirements.txt
```
- Compile again for windows by run following command
```bash
pyinstaller.exe --onefiles --noconsole --icon=.\tiff.ico .\main.py
```

- Now you can run application directy. This app named **main.exe** is created under **dist** folder. You can change file name. I shared you a file named sample.pdf in root directory. You can use for testing.

- For opening converted tiff file you should use **windows photo viewer**. Other applications show only one picture or one page. 

