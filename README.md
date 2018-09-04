# Form-Builder

> Tested using Windows x64, and Google Chrome.
## Build Setup

### 1. Install latest python 3 version from [here](https://www.python.org/downloads/)
###   (Note: Make sure to tick V in the installaion checkbox "Add python 3.7 to PATH")

### 2. Install MongoDB Community Server from [here](https://www.mongodb.com/download-center?jmp=nav#community) (under Community Server tab)
###   - Add mongodb's bin folder to your PATH variables (if it doesn't exist)
###     You can use this [guide](https://dangphongvanthanh.wordpress.com/2017/06/12/add-mongos-bin-folder-to-the-path-environment-variable/)

### 3. Install nodeJS from [here](https://nodejs.org/en/download)

### 4. Clone the repository to your machine using git (or download as zip)

### 5. Open the /Run folder and execute the files in the following order (make sure you wait until each operation is completed) (Note: The leave the batch files from steps b, c, d open after completion):
###   a.  Run "Install modules.bat" (installing Python modules and Node_modules)
###   b.  Run "Run mongod.bat" (Creates C:\data\db directory for mongoDB and runs mongod)
###   c.  Run "Run Server.bat"
###   d.  Run "Run Client.bat"
###   e.  Run "Open Webpage.bat"

## 6. **Profit!**