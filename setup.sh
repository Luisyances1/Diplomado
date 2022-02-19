mkdir -p ~ /.streamlit/
echo  "
[tema]
base='oscuro'
colorprimario='#4b64ff'
color de fondo secundario = '# 2c2c2d'
fuente = 'monoespacio'
[servidor]
sin cabeza = cierto
enableCORS=falso
enableXsrfProtection=falso
puerto = $PORT
"  >  ~ /.streamlit/config.tom
