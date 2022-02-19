mkdir -p ~ /.streamlit/
echo  "
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
"  > %userprofile%/.streamlit/config.toml
