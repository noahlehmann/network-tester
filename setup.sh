#!/bin/bash

#write out current crontab
crontab -l > tempcron
echo "@reboot docker-compose -f $(pwd)/docker-compose.yml up -d" >> mycron

crontab tempcron
rm tempcron