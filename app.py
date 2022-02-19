import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename)

datos = cargar_datos("VehiculosImputed.csv")
#@st.cache
#def plot_heatmap(df, x, y):
#    data_heatmap = (
#        df.reset_index()[[x, y, "index"]]
#        .groupby([x, y])
#        .count()
#        .reset_index()
#        .pivot(x, y, "index")
#        .fillna(0)
#    )
#    fig = px.imshow(
#        data_heatmap,
#        color_continuous_scale="Blues",
#        aspect="auto",
#        title=f"Heatmap {x} vs {y}",
#    )
#    fig.update_traces(
#       hovertemplate="<b><i>"
#      + y
#     + "</i></b>: %{y} <br><b><i>"
#    + x
#   + "</i></b>: %{x} <br><b><i>Conteo interacción variables</i></b>: %{z}<extra></extra>"
#)
#return fig


#satisfaction level quedo como cilindraje
#average_montly_hours quedo como potencia

# Sidebar
st.sidebar.markdown("# Selectores de datos para estimador de precio")
st.sidebar.markdown("---")
Cilindraje = st.sidebar.slider(
    label="Cilindraje", min_value=0, max_value=15950, value=8000
)
Potencia = st.sidebar.slider(
    label="Potencia", min_value=0, max_value=662, value=300
)
Clase = st.sidebar.selectbox(
    label="Clase", options=["BUS / BUSETA / MICROBUS", "CAMION", "CARROTANQUE", "CHASIS",
       "FURGON", "REMOLCADOR", "VOLQUETA", "CAMPERO", "AUTOMOVIL",
       "REMOLQUE", "MOTOCICLETA", "PICKUP SENCILLA", "CAMIONETA PASAJ",
       "FURGONETA", "MOTOCARRO", "PICKUP DOBLE CAB", "CAMIONETA REPAR",
       "ISOCARRO", "UNIMOG"]
)
Marca = st.sidebar.selectbox(
    label = "Marca", options=["ALEKO", "AMERICAN MOTOR", "AUTECO", "AROCARPATI", "ASIA", "AUDI",
       "AUTOCAR", "BMW", "DINA", "BUICK", "CAGIVA", "CADILLAC", "CORCEL",
       "CHEVROLET", "CHRYSLER", "CITROEN", "DACIA", "DAEWOO", "DAIHATSU",
       "DERBI", "DODGE", "DUCATI", "FIAT", "FREIGHTLINER", "FORD",
       "MOTO GUZZI", "HYUNDAI", "HARLEY DAVIDSON", "HONDA", "IFA",
       "INTERNATIONAL", "HINO", "ISUZU", "JAWA", "JAGUAR", "JEEP",
       "KAMAZ", "KENWORTH", "KAWASAKI", "KIA", "KRAZ", "LADA", "MARMON",
       "LANCIA", "HYOSUNG", "LAND ROVER", "MORINI", "MACK", "MAZDA",
       "MERCEDES BENZ", "MINI", "MERCURY", "MG", "MITSUBISHI", "NISSAN",
       "PEGASO", "OLTCIT", "PEUGEOT", "PAZ", "PIAGGIO", "BEIJING",
       "PONTIAC", "PORSCHE", "RENAULT", "SCANIA", "SEAT", "SSANGYONG",
       "SISU", "SKODA", "SUBARU", "SUZUKI", "TAVRIA", "TOYOTA", "UAZ",
       "VOLKSWAGEN", "VOLGA", "VOLVO", "WESTERN STAR", "YUGO", "YAMAHA",
       "TATA", "KYMCO", "IVECO", "AGRALE", "CHANA", "CHERY", "HAFEI",
       "RENNO", "SAICWULING", "CHANGHE", "BYD", "HALEI", "JAC", "TITANIA",
       "ZHONGXING", "AMPLE", "GLOW", "VERUCCI", "JIALING", "GERLAP",
       "DAYANG", "JINCHENG", "GEELY", "INFINITI", "JINGLONG", "UTILITY",
       "KEEWAY", "KYOTO", "FIRENZE", "SERVICHASIS", "HONLEI", "OPEL",
       "TRAILER SANDER", "TECNIPESADOS", "KAZUKI", "UNITED MOTORS",
       "PIONEER", "TALLER OVEL", "TRACTEC", "AYCO", "XINKAI",
       "DFSK/DFM/DFZL", "YINGANG", "SIGMA", "TECNICAR", "APRILIA",
       "RAFAEL ESCOBAR", "SHINERAY", "TODO TRAIL", "QINGQI",
       "GOLDEN DRAGON", "USW MOTORS", "STELL TRAILERS", "XIANFENG",
       "TRAYCOL", "JMC", "AKT", "MANETRA", "JINFENG", "BRP CAN AM",
       "GREAT WALL MOTOR", "INDUCAM JC", "HEIL", "WABASH NATIONAL",
       "FALCON", "PETERBILT", "MAXMOTOR", "KTM", "GOMOTOR", "CANACOL",
       "GERMAR GMG", "BORGO", "TALLERES MILTON", "SUKIDA", "ZAHAV",
       "ESTEMCO", "NITRO", "ITANREM", "SERVI VOLCOS", "CMC",
       "TRAILERS DE SANTANDER", "DUST", "FOTON", "CEDAL", "VENTO",
       "XINGYUE", "ROMARCO", "FAMERS", "INTRAILER", "FEGAM",
       "TRAILERS TULUA", "MECANICOS UNIDOS", "IMECOL", "RHINO",
       "GREAT DANE", "TONGKO", "TRAYVOCOL", "HIDROAMERICA", "METAL INOX",
       "YAKIMA", "WANXIN", "SERVITRACK", "IMEVA", "GAZ", "MORENO",
       "INDUSTRIAS BERMEO", "CONSTRUTRAILER", "INCALLES COLOMBIA",
       "GUERCAR", "EAGLE TRUCK", "TRAILERS DE ANTIOQUIA", "BISON TRUCK",
       "KAYAK", "INCA FRUEHAUF", "PRISMA", "PANAMERICANA", "ZOTYE",
       "EL TRAILERO", "ORLTRAILER", "INOX MEC", "METALCONT", "HUMMER",
       "AUPACO", "INCOLTRAILERS", "IMCOLTRANS", "LIFAN", "TECNOTRAILERS",
       "INDUROC", "APONCAR", "TALLERES CESPEDES", "HIGER",
       "CARROCERIAS MODERNA", "MD BIKES", "TALLER T F S", "SAAB", "SANYA",
       "EL SOL", "TIANMA", "MTK", "AMC", "WCR", "ZQ MOTORS", "ALCAR",
       "ACB", "SUKYAMA", "FAW AMI", "CHANGFENG", "SKYGO", "FERRELAMINAS",
       "INDUGWEST", "ANDITRAILERS", "INDUREMOLQUES", "TRAILERS SUPERIOR",
       "EQUITRAILER", "BAYONA TRAILER", "FULL TRAILER", "GUZI", "STEYR",
       "SHUANGHUAN", "HONGXING", "MUDAN", "CARROCERIAS JAGUER",
       "TECNITANQUES", "TODOTRAILERS", "ZONGSHEN", "DITE", "RANDON",
       "INDUVOLCOS", "TX MOTORS", "OXITANQUES", "TALLERES CEPEDA",
       "MULTITRAILERS", "EUROSTAR D`LONG", "EAGLE CARGO", "SER REMOLQUES",
       "INSAR", "TRAILERS DE LA SABANA", "TRAILERS HERCULES",
       "SERVITRAILER", "REPATRAILERSVAN", "SAN MARCOS", "CAPRI", "TVS",
       "COLTRAILER", "EL CHINO BERNA", "LOHR", "TECNITRACS", "POLARIS",
       "CILINDRAULICOS", "METALLICA", "UFO", "MACTRAILERS", "DORSEY",
       "GONOW", "ONEIDA", "RODRIREMOLQUES", "ATM", "VOLCOS UFF", "FMI",
       "APOLO", "CONSTRUTANQUES", "BAW", "VYR CARVAJAL", "CONALCAR",
       "GREMCAR", "TRAILERS & TRAILERS", "INDUCAPI", "TECNISANDER",
       "JINBEI", "CONTAPA", "GESMET", "EL ABARCO", "SOYAT",
       "TECNITRAILER", "ZHONGNENG", "SATURN", "TEMPEST", "TECNITRAILERS",
       "TALLERES PACHON", "LA QUINTA RUEDA", "GAS GAS", "PASSAGGIO",
       "UKM", "SACHS", "YUTONG", "SG INGENIERIA", "NON PLUS ULTRA",
       "VESPA", "EUROPAMOTOS", "SYM", "CYAN", "ACURA", "LEXUS", "AG",
       "SINOTRUK", "FONTAINE", "FRANCOCOL", "BRONTO", "SMC", "HUSQVARNA",
       "TMD", "LANDWIND", "PROCEIN", "ROVER", "MASERATI", "ALFA ROMEO",
       "YAKEY", "FERRARI", "ROYAL ENFIELD","AMERICAN TRAYLER", "GMC",
       "YAXING", "SCION", "AVA", "TRIUMPH", "T-KING", "HAIMA", "ZNA",
       "HUANGHAI", "MAHINDRA", "HAOJIANG", "LINCOLN", "HUALIN",
       "ARCTIC CAT", "DADI", "BENELLI", "CARMEX", "MOTO ABC",
       "BRILLIANCE", "LML", "JOYLONG", "CIMC", "MAXUS", "INCOLTANQUES",
       "DFAC", "SMART", "MV AGUSTA", "BAIC", "LMX", "CHANGAN", "DONGBEN",
       "YUEJIN-NAVECO", "HERO", "VICTORY", "VAISAND", "FUSO", "DAF",
       "STÄRKER", "SCOMADI", "HAOJUE", "DS"])
request_data = [
   {
       "Cilindraje": Cilindraje ,
       "Potencia": Potencia,
       "Clase": Clase,
       "Marca":Marca
   }
]

#url_api='http://127.0.0.1:8000/predict'
#url_api = "http://0.0.0.0:8000/predict"
#data = str(request_data).replace("'", '"')
#prediccion = requests.post(url=url_api, data=data).text
st.sidebar.markdown("---")
opciones1 = list(datos.columns)
eje_x_heatmap1 = st.sidebar.selectbox(label="Heatmap X", options=opciones1)
opciones2 = opciones1.copy()
opciones2.pop(opciones1.index(eje_x_heatmap1))
eje_y_heatmap1 = st.sidebar.selectbox(label="Heatmap Y", options=opciones2)

# Main Body
st.header("Web app para el Diplomado de Python: Ejemplo Employee Turnover")
st.markdown("---")
#col1, col2 = st.columns(2)
#col1.metric(
#    value=f'{100*pd.read_json(prediccion)["employee_left_proba"][0]} % ',
#    label="Predicción probabilidad renuncia",
#)
#col2.write("Esto quedaría en la columna de la derecha")
#st.markdown("---")

# Display an interactive table
st.write(datos)
#scatter_1 = plot_heatmap(df=datos, x=eje_x_heatmap1, y=eje_y_heatmap1)

#col1, col2 = st.columns(2)

#col1.plotly_chart(scatter_1, use_container_width=True)
#

st.plotly_chart(
#    fig  =  px . bar ( datos_canada ,  x = 'año' ,  y = 'pop' ) 
    px.bar(
        datos.groupby(["Importado", "Clase"])
        .count()
        .reset_index()
        .sort_values(by="valor_modelo", ascending=False),
        color_discrete_sequence=["gray"],
        x ="Clase",
        y ="valor_modelo"
#        ,facet_col="left",
    ),
    use_container_width=True, 
)
def comparadorPrecios (valor: int):
    df = pd.DataFrame()
    df = datos[(datos['valor_modelo'] <= valor)]
    return df
st.markdown("---")
st.markdown("# ¿Tiene algun presupuesto?")
referencia_precio = st.number_input("¡Busque vehiculos por su presupuesto!")
if st.button("Aceptar"):
    st.dataframe(comparadorPrecios(referencia_precio))
    st.success("Valores encontrados")
st.markdown("---")

