```powershell
# 步驟 1：建立名為 .venv 的虛擬環境
py -3.12 -m venv .venv

# 步驟 2：啟動虛擬環境
.\.venv\Scripts\activate.bat

# 步驟 3：更新套件管理工具 pip
python.exe -m pip install --upgrade pip

# 步驟 4：將目前的工作目錄切換到 00_Environment_Setup 資料夾
cd 00_Environment_Setup

# 步驟 5：批次安裝 requirements.txt 清單中的所有套件
pip install -r requirements.txt

# 步驟 6：將虛擬環境註冊為 Jupyter Kernel
python -m ipykernel install --user --name=.venv --display-name="WebScraping(venv)"
```

> ✅ 安裝完成後，確認虛擬環境已啟動（命令提示字元前方會出現 `(.venv)` 字樣），  
> 再使用 VS Code 或 Jupyter Lab 開啟後續的 `.ipynb` 筆記本。