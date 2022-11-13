# insert api token generated from panel USER account API ( Important: not application API token )
barer_token = 'ptlc_hntWGDPiKyrTmMSHqF9ByQkr6qsbV9IDx6UTIHmHRip'


# the last part of url is server identifier
# make sure to follow the format when adding servers. Esp , the comma at the end. The last server doesn't require comma , <== important
panel_urls = [
                'https://gcpanel.ghostcap.com/api/client/servers/e8785ebc/',
                'https://gcpanel.ghostcap.com/api/client/servers/646e0c79/'
                
    ]

# Time before server restart in seconds
timer_before_start_stop = [60,30,10,5]

# pause intervals between each in-game announcement "say SERVER RESTARTING IN xx SECONDS"
sleep_intervals = [30,20,5,5]