mkdir -p ~/.streamlit/
echo  "
[theme]
base='dark'
primaryColor='#021066'
secondaryBackgroundColor='#05389e'
font='timenewsromans'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
"  > ~/.streamlit/config.toml
