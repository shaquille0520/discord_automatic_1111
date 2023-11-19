from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from flask import Flask
import discord
from discord.ext import commands
import time
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
app = Flask(__name__)

client = discord.Client(intents=discord.Intents.default())
#options.add_argument('--headless=new')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Create a new WebDriver instance for each message
    with webdriver.Chrome(options=options) as driver:

        if message.content == '1':
            while True:
                try:
                    driver.find_element(By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[1]/div/label/div/div[1]/div/svg").click()
                except:
                    print('somthing went wrong.')
        
        driver.get('http://127.0.0.1:7860/')

        while True:
            try:
                driver.find_element(By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[2]/label/textarea").send_keys(message.content)
                print('Loaded!!!')
                driver.find_element(By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/button[3]").click()
                time.sleep(1)
                prog = driver.find_element(By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div[3]/div[1]/div")
                break
            except:
                print('Loading.')
                time.sleep(0.5)
                os.system('cls')
                print('Loading..')
                time.sleep(0.5)
                os.system('cls')
                print('Loading...')
                time.sleep(0.5)
                os.system('cls')

        while True:
            try:
                await message.channel.send(progtext)
                progtext = prog.text
                print(str(progtext))
                time.sleep(0.5)
                os.system('cls')
                
            except StaleElementReferenceException:
                await message.channel.send(file=discord.File('C:\\Users\\mui\\Downloads\\pc link parser-20231114T022042Z-001\\second\\2023-11-19\\image.png'))
                print("Image Created.")
                break

client.run('MTE3NTIyMDgwMDY2MDQzOTA1MA.Gut0nE.P_3fi1JjdNL1MHzHAVOQgQKi_Iju5NmzDN9G78')
