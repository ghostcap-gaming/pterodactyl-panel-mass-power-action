import requests
import json
import asyncio
import config as cfg

_token = "Bearer {}".format(cfg.barer_token)

headers = {
    "Authorization": _token,
    "Accept": "application/json",
    "Content-Type": "application/json",
    }

async def power_action(server_url,action):
    
    if action == 'stop':
        payload = {'signal': 'stop'}
        response = requests.post('{}power'.format(server_url), data=json.dumps(payload), headers=headers)
        if response.status_code == 204:
            print("{} has successfully stopped!".format(server_url))

    elif action == 'start':
        payload = {'signal': 'start'}
        response = requests.post('{}power'.format(server_url), data=json.dumps(payload), headers=headers)
        if response.status_code == 204:
            print("{} has successfully started!".format(server_url))

async def cmd_action(server_url,seconds):
    if seconds == 0:
        txt = "say SERVER RESTARTING NOW!!"
    else:
        txt = "say SERVER RESTARTING IN {} SECONDS".format(str(seconds))
    payload = {'command': txt}
    response = requests.post('{}command'.format(server_url), data=json.dumps(payload), headers=headers)

async def initiate_action():
    _count = 0
    for y in cfg.timer_before_start_stop:
        for x in cfg.panel_urls:
            await cmd_action(x,y)
        await asyncio.sleep(cfg.sleep_intervals[_count])
        _count += 1
        if _count > 3:
            await asyncio.sleep(5)
            for x in cfg.panel_urls:
                await cmd_action(x,0)

    for x in cfg.panel_urls:
        await power_action(x,'stop')
    
    await asyncio.sleep(5)

    for x in cfg.panel_urls:
        await power_action(x,'start')

asyncio.run(initiate_action())
