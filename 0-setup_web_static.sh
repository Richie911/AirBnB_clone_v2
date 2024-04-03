#!/usr/bin/env bash
# Task that sets up the necessary directory structure, creates a test HTML file
# Eestablishes a symbolic link for serving the latest static content, sets permissions
# Updates the Nginx configuration to serve static files correctly on the web servers.

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'

# Create necessary directories if they don't exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file for testing
sudo touch /data/web_static/releases/test/index.html
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link if it doesn't exist
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from /data/web_static/current/
# under the URL path /hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
