import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title = "Web app")

@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename)

datos = cargar_datos("VehiculosImputed.csv")

# Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png")
st.sidebar.markdown("# Selectores de datos para estimador de precio")
st.sidebar.markdown("---")
Bcpp = st.sidebar.slider(
    label = "Bcpp", min_value=1800, max_value=2187500)
Potencia = st.sidebar.slider(
    label="Potencia", min_value=0, max_value=662, value=300
)
Cilindraje = st.sidebar.slider(
    label="Cilindraje", min_value=0, max_value=15950, value=8000
)
PesoCategoria = st.sidebar.slider(
      label= "PesoCategoria", min_value=0, max_value=2, value=1
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
Fechas = st.sidebar.selectbox(                           
    label="Fechas",options=["1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"])

request_data= [
   {
       "Bcpp":Bcpp,
       "Potencia":Potencia,
       "Cilindraje":Cilindraje,
       "PesoCategoria":PesoCategoria,
       "Marca":Marca,
       "Clase":Clase,
       "Fechas":Fechas
   }
]

#url_api="http://0.0.0.0:8000/predict"
#url_api = "https://apidiplomado.herokuapp.com/docs#/default/predict_df_predict_post"
url_api = "https://apidiplomado.herokuapp.com/predict"
data = str(request_data).replace("'", '"')
prediccion = requests.post(url=url_api, data=data).text

st.sidebar.markdown("---")

st.metric(
    value=f'{pd.read_json(prediccion)["precio"][0]}',
    label="Prediccion de precio",
         )
opcionPie = st.sidebar.selectbox(label="Selector de Categorias especiales", 
                                 options =["TipoCaja","Nacionalidad","Combustible","Importado"])


# Main Body
st.header("Web app para el Diplomado de Python")
st.markdown("---")
#col1, col2 = st.columns(2)
#col1.metric(
#    value=f'{pd.read_json(prediccion)["precio"][0]} ',
#    label="Predicción probabilidad renuncia",
#)

st.write(datos)

@st.cache
def graficobarras(datos):
    
    fig = px.bar(
        datos.groupby(["Importado", "Clase"])
        .count()
        .reset_index()
        .sort_values(by="valor_modelo", ascending=False),
        color_discrete_sequence=["gray","black"],
        x ="Clase",
        y ="valor_modelo"
#        ,facet_col="left",
    )
    return fig
varfig = graficobarras(datos)
st.plotly_chart( 
    varfig , 
    use_container_width=True,  
)
def comparadorPrecios (datos,valor: int):
    df = datos[(datos['valor_modelo'] <= valor)]
    return df
st.markdown("---")
st.markdown("# Consultar valor historico")
referencia_precio = st.number_input("Ingrese un valor a buscar")
if st.button("Aceptar"):
    st.dataframe(comparadorPrecios(datos,referencia_precio))
    st.success("Valores encontrados")

st.markdown("---")
st.markdown("# Grafico 2")
@st.cache
def pieFig(df,x):
    sizes = datos[x].value_counts().tolist()
    labels = datos[x].unique()
    return [sizes,labels]
fig = px.pie(datos, 
             values=pieFig(datos,opcionPie)[0], 
             names=pieFig(datos,opcionPie)[1], 
             title='Categorias especiales ',
            color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)
st.markdown("el grafico anterior nos permite tener en una vision mas general de algunas caracteristicas que han crecido, como lo son los tipos de cajas las MT (cajas mecanicas) son la mayor caracterisca de los autos actualmente, para los datos de importacion podemos observar que en su mayoria los no son importados (label 0), de esta misma forma podemos observa la lista de paises que importan vehiculos y cual de ellos es el que mas importa vehiculos al pais, tambien se puede observar que en su mayoria lo vehiculos son a gasolina, pero los vehiculos a diesel son una porcion bastante considerable dentro de nuestro dataset ")
