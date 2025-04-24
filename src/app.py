#!/usr/bin/python
#
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import mysql.connector

from flask import Flask

app = Flask(__name__)

# MySQL 資料庫連線設定
DB_HOST = os.getenv('DB_HOST', '<YOUR_SQL_IP>')  # 從環境變數中獲取資料庫服務名稱
DB_NAME = os.getenv('DB_NAME', 'exampledb')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'rootpassword')

def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return connection

    
@app.route('/')
def hello_world():
    # 連接資料庫並查詢當前時間
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SYSDATE();")  # 查詢當前時間
    result = cursor.fetchone()  # 獲取查詢結果
    current_time = result[0] if result else 'No time found'
    cursor.close()
    conn.close()
    
    return f"Hello World v1.0! Current Time: {current_time}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)