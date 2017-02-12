vnstati -s -i eth0 -o /opt/netflix-proxy/wwwroot/static/summary.png
vnstati -h -i eth0 -o /opt/netflix-proxy/wwwroot/static/hourly.png
vnstati -d -i eth0 -o /opt/netflix-proxy/wwwroot/static/daily.png
vnstati -t -i eth0 -o /opt/netflix-proxy/wwwroot/static/top10.png
vnstati -m -i eth0 -o /opt/netflix-proxy/wwwroot/static/monthly.png
