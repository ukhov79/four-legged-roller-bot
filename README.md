# four-legged-roller-bot
Four-legged roller bot is a project of small quadroped robot with 4 rollers on legs.

Use DietPi OS from here: https://dietpi.com/

nano /etc/systemd/system/robot-script.service
chmod 664 /etc/systemd/system/robot-script.service

/etc/systemd/system/robot-script.service:

[Unit]
Description=Robot script
After=network.target
[Service]
Type=notify
User=root
Restart=on-failure
RestartSec=60s
ExecStart=/root/copy.sh
ExecReload=/root/copy.sh
[Install]
WantedBy=multi-user.target

/root/copy.sh:

#!/bin/bash
P_D='/root'
cd "$P_D"
rm -rf four-legged-roller-bot
git clone https://github.com/ukhov79/four-legged-roller-bot
cd four-legged-roller-bot
python3 start.py <ip_adress>

systemctl enable robot-script.service
