import streamlit as st
import re
from datetime import datetime

st.set_page_config(page_title="ALINEA - App para Alinear Componentes Estratégicos", layout="wide")

st.title("ALINEA - App para Alinear Componentes Estratégicos")

# Función para validar estructura de fórmulas

def validar_componente(texto, tipo):
    errores = []
    texto = texto.strip()
    if not texto:
        return None

    # Fórmulas esperadas
    if tipo == "Objetivo":
        if not re.search(r"\\b(para|en|antes de|al|hacia)\\b", texto):
            errores.append("El objetivo debe tener una fecha límite explícita (por ejemplo: 'para diciembre de 2025').")
    elif tipo == "Estrategia":
        if not re.search(r"durante|en el|en los|hasta", texto):
            errores.append("La estrategia debe incluir un plazo (por ejemplo: 'durante el año 2025').")
    elif tipo == "Táctica":
        if not re.search(r"cada|en|para", texto):
            errores.append("La táctica debe incluir una fecha (por ejemplo: 'cada trimestre del año 2025').")
    elif tipo == "Operativa":
        if not re.search(r"diario|semanal|mensual|trimestral|anual|cada", texto):
            errores.append("La acción operativa debe indicar frecuencia (por ejemplo: 'semanalmente').")
    return errores

# Verbos sugeridos según jerarquía

verbos = {
    "Objetivo": ["Incrementar", "Reducir", "Mejorar", "Aumentar", "Alcanzar"],
    "Estrategia": ["Desarrollar", "Diseñar", "Implementar", "Establecer"],
    "Táctica": ["Ejecutar", "Lanzar", "Aplicar", "Realizar"],
    "Operativa": ["Hacer", "Revisar", "Llevar a cabo", "Registrar"]
}

def sugerir_verbos(tipo):
    return ", ".join(verbos.get(tipo, []))

# Alineación jerárquica de verbos

def alinear_jerarquia(tipo, texto_superior, texto):
    if not texto_superior or not texto:
        return ""
    verbo_superior = texto_superior.strip().split(" ")[0].lower()
    verbo_actual = texto.strip().split(" ")[0].lower()
    niveles = list(verbos.keys())
    indices = {v: i for i, v in enumerate(niveles)}
    for t, lista in verbos.items():
        if verbo_superior.capitalize() in lista:
            nivel_superior = indices[t]
        if verbo_actual.capitalize() in lista:
            nivel_actual = indices[tipo]
    if nivel_actual <= nivel_superior:
        return "\n✔️ Buena alineación jerárquica entre el verbo de este componente y el componente superior."
    else:
        return f"\n❗ El verbo de este componente puede ser demasiado general. Sugerencia: usa verbos como: {sugerir_verbos(tipo)}."

# Campo para el nombre de la organización
org = st.text_input("Nombre de la organización")

# Captura de entradas y realimentación
componentes = []
componentes.append(("Objetivo Estratégico", "Verbo + Objeto + Medida o Indicador + Fecha límite\nEj: Incrementar ventas en un 20% para diciembre de 2025."))
componentes.append(("Estrategia 1.1", "Verbo + Método o enfoque + Área de aplicación + Plazo\nEj: Desarrollar una campaña de marketing digital en redes sociales durante el año 2025."))
componentes.append(("Táctica 1.1.1", "Verbo + Acción concreta + Recursos necesarios + Fecha\nEj: Implementar promociones utilizando el presupuesto asignado cada trimestre del año 2025."))
componentes.append(("Operativa 1.1.1.1", "Verbo + Procedimiento o tarea + Frecuencia\nEj: Realizar inventarios semanalmente."))
componentes.append(("Operativa 1.1.1.2", "Verbo + Procedimiento o tarea + Frecuencia\nEj: Verificar pedidos semanalmente."))

entradas = {}
realimentaciones = {}

with st.form("form_estrategia"):
    for i, (nombre, descripcion) in enumerate(componentes):
        entradas[nombre] = st.text_area(f"{nombre}", help=descripcion)

    generar = st.form_submit_button("Generar realimentación")

if generar:
    st.subheader("Realimentación personalizada")
    textos = {}
    for i, (nombre, descripcion) in enumerate(componentes):
        tipo = nombre.split()[0]
        texto = entradas[nombre].strip()
        if not texto:
            continue
        textos[nombre] = texto
        errores = validar_componente(texto, tipo)
        real = f"🔍 **{nombre}**: "
        if errores:
            real += "\n❗ " + " ".join(errores)
        else:
            real += "\n✔️ Cumple con la estructura de fórmula esperada."
        real += f"\nSugerencia de verbos ({tipo}): {sugerir_verbos(tipo)}."
        if i > 0:
            nombre_superior = componentes[i - 1][0]
            real += alinear_jerarquia(tipo, textos.get(nombre_superior, ""), texto)
        st.markdown(real)

    st.markdown("\n---")
    st.markdown("*Montoya, Julio Cesar (2025). ALINEA - App para alinear componentes estratégicos. Universidad Nacional Abierta y a Distancia - UNAD.*")
