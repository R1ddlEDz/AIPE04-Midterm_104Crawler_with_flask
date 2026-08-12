## .venv虛擬環境建立 (python3.12)
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
#
## 104爬蟲Python使用方法 (Crawler.py)
```
find_jobs(keyword="",area="",ro=0,jobexp=1)
在keyword裡輸入要查詢的關鍵字

在area裡輸入要搜尋的地區 如果要搜尋多個區域以,來分隔
台北市=6001001000 新北市=6001002000 桃園市=6001005000 新竹縣市=6001006000 台中市=6001008000 高雄市=6001016000

ro 0全部職缺 1正職 2兼職

jobexp 1= 一年以下 3= 1-3年 5= 3-5年 10= 5-10年 99= 10年以上

上面的參數都可以不打 默認為搜尋工作經驗一年以下，並且正兼職都會列出
```

## 網頁使用方法 (app.py)
```
安裝.venv虛擬環境後(或安裝python3.12) 使用終端機前往該檔案所處資料夾 使用 python app.py 來開啟網頁
網頁網址為: http://127.0.0.1:5000/
```