# 1. Start with a lightweight version of NGINX
FROM nginx:alpine

# 2. Clear out the default placeholder webpage that comes with NGINX
RUN rm -rf /usr/share/nginx/html/*

# 3. Copy the compiled Ren'Py web game into the NGINX serving folder.
# (The GitHub Action pipeline creates this 'web-build' folder right before this step)
COPY web-build/ /usr/share/nginx/html/

# 4. Open port 80 so the browser can connect to it
EXPOSE 80