mkdir -p ~/.streamlit/
​
echo "\
[general]\n\
email = \"daniel.giampapa@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
​
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
