name: auftanken

on:
  schedule:
    - cron: '00 */12 * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: config
        run: |
          git config --global user.email "<>"
          git config --global user.name "auftanken bot"

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install beautifulsoup4 requests

      - name: Execute Python script
        run: python3 ressources/infos/barkers/auftanken.py > ressources/infos/barkers/auftanken.m3u8

      - name: git add
        run: |
          git add -A
          ls -la 
          
      - name: commit & push
        run: |
          git pull origin master
          git commit -m "auftanken updated"
          git push origin master
