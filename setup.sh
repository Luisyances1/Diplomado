mkdir -p ~ /.streamlit/
echo  "
[theme]
base='dark'
primaryColor='#4b64ff'
secondaryBackgroundColor= '# 2c2c2d'
font = 'monoespace'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
"  >  ~ /.streamlit/config.tom
