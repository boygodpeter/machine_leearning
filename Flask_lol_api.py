from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# 讀取隊伍與英雄資料
tm_path = r"D:\機器學習\專題\project_demo\team_member_for_UI.xlsx"
champ_path = r"D:\機器學習\專題\project_demo\champions.xlsx"

tm_df = pd.read_excel(tm_path)
champ_df = pd.read_excel(champ_path)

# 轉換隊伍資料為 {隊伍名稱: {位置: 選手名, ...}} 格式
def get_team_data():
    teams = {}
    for _, row in tm_df.iterrows():
        team_name = row['team']
        position = row['position']
        player = row['player']
        if team_name not in teams:
            teams[team_name] = {}
        teams[team_name][position] = player
    return teams


def get_champions_data():
    positions = ['TOP', 'JUNGLE', 'MID', 'AD', 'SUPPORT']
    champions = {pos: champ_df[pos].dropna().tolist() for pos in positions}
    return champions

@app.route("/teams", methods=["GET"])
def teams():
    return jsonify(get_team_data())

@app.route("/champions", methods=["GET"])
def champions():
    return jsonify(get_champions_data())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
