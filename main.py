import requests
import json
import os
import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow


REGION = "americas"
CONFIG_FILE = "config.json"


# =========================
# API KEY
# =========================

def get_api_key():
    if not os.path.exists("riot_key.txt"):
        print("Falta riot_key.txt con tu API key")
        exit()

    with open("riot_key.txt", "r") as f:
        return f.read().strip()


API_KEY = get_api_key()


# =========================
# API
# =========================

def get_puuid(game_name, tag_line):
    url = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"

    headers = {"X-Riot-Token": API_KEY}

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print("Error obteniendo puuid:", res.status_code, res.text)
        return None

    return res.json()["puuid"]


def get_match_ids(puuid, count=3):
    url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}"

    headers = {"X-Riot-Token": API_KEY}

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print("Error obteniendo matches:", res.status_code, res.text)
        return None

    return res.json()


def get_match(match_id):
    url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    headers = {"X-Riot-Token": API_KEY}

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print("Error obteniendo match:", res.status_code, res.text)
        return None

    return res.json()


# =========================
# PRINT DATA
# =========================

def print_teams(match_data):
    participants = match_data["info"]["participants"]

    team_100 = []
    team_200 = []

    for p in participants:
        name = p["riotIdGameName"]
        tag = p["riotIdTagline"]

        if not name:
            name = p["summonerName"]
            tag = ""

        full_name = f"{name}#{tag}" if tag else name
        champ = p["championName"]
        team = p["teamId"]

        player_info = f"{full_name} - {champ}"

        if team == 100:
            team_100.append(player_info)
        else:
            team_200.append(player_info)

    print("\n=== TEAM 1 (BLUE) ===")
    for player in team_100:
        print(player)

    print("\n=== TEAM 2 (RED) ===")
    for player in team_200:
        print(player)


# =========================
# CONFIG
# =========================

def load_config():
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "riot_id": "",
            "region": "americas"
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=2)

        return default_config

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


# =========================
# TEST (CLI) - NO TOCAR
# =========================

def main_prueba():
    print("=== LoL Match Selector ===\n")

    config = load_config()

    riot_id = config.get("riot_id", "")

    if not riot_id:
        riot_id = input("Ingresá tu Riot ID (nombre#tag): ")

        if "#" not in riot_id:
            print("Formato inválido")
            return

        config["riot_id"] = riot_id
        save_config(config)

    else:
        print(f"Usando Riot ID guardado: {riot_id}")

    game_name, tag_line = riot_id.split("#")

    puuid = get_puuid(game_name, tag_line)
    if not puuid:
        return

    match_ids = get_match_ids(puuid, count=3)
    if not match_ids:
        return

    print("\nÚltimas partidas:\n")
    for i, match_id in enumerate(match_ids, start=1):
        print(f"{i}. {match_id}")

    choice = int(input("\nElegí una partida (1-3): "))
    selected_match = match_ids[choice - 1]

    match_data = get_match(selected_match)

    if match_data:
        print_teams(match_data)


# =========================
# MAIN GUI (LIMPIO)
# =========================

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setFixedSize(1280, 720)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
