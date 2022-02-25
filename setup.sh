mkdir -p ~/.streamlit/
echo  "
[theme]
base='dark'
primaryColor='#484a54'
secondaryBackgroundColor='#58587a'
font='timenewsromans'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
"  > ~/.streamlit/config.toml
