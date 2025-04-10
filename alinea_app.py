# alinea_app.py
import streamlit as st
from datetime import datetime

# ===== FUNCIONES DE APOYO PARA EVALUACIÓN =====
def evaluar_componente(nombre, texto, formula):
    retro = f"\n**{nombre}**\n"
    if not texto.strip():
        return ""

    errores = []
    texto_lower = texto.lower()

    if not any(texto_lower.startswith(v) for v in formula['verbos']):
        errores.append("- El verbo no corresponde al nivel jerárquico esperado.")

    if not any(p in texto_lower for p in formula['indicadores']):
        errores.append("- No se encontró un indicador o medida.")

    if not any(t in texto_lower for t in formula['tiempos']):
        errores.append("- No se identifica un plazo o fecha.")

    if errores:
        retro += "\n".join(errores)
    else:
        retro += "✅ El componente cumple con los elementos clave de su fórmula."
    return retro


def evaluar_jerarquia(objetivo, estrategia, tactica, operativa):
    jerarquia = ""
    if objetivo and estrategia and not estrategia.lower().startswith(('desarrollar', 'diseñar', 'implementar')):
        jerarquia += "- La estrategia podría no estar alineada con el verbo esperado (por ejemplo: 'Desarrollar', 'Diseñar').\n"
    if estrategia and tactica and not tactica.lower().startswith(('implementar', 'ejecutar', 'organizar')):
        jerarquia += "- La táctica podría requerir un verbo más operativo como 'Implementar'.\n"
    if tactica and operativa and not operativa.lower().startswith(('realizar', 'verificar', 'controlar', 'hacer')):
        jerarquia += "- La acción operativa debe tener un verbo orientado a tareas específicas como 'Realizar', 'Verificar'.\n"

    if not jerarquia:
        return "✅ Existe coherencia jerárquica entre los componentes."
    else:
        return jerarquia

# ===== FORMATO DE VERBOS Y COMPONENTES =====
formulas = {
    'Objetivo Estratégico': {
        'verbos': ['incrementar', 'reducir', 'mejorar', 'aumentar', 'fortalecer'],
        'indicadores': ['%', 'porcentaje', 'tasa', 'nivel', 'índice'],
        'tiempos': ['2025', 'en', 'para']
    },
    'Estrategia': {
        'verbos': ['desarrollar', 'diseñar', 'implementar', 'crear'],
        'indicadores': ['campaña', 'programa', 'plan'],
        'tiempos': ['2025', 'en', 'durante']
    },
    'Táctica': {
        'verbos': ['implementar', 'ejecutar', 'organizar'],
        'indicadores': ['presupuesto', 'recurso', 'plan'],
        'tiempos': ['trimestre', 'mes', '2025']
    },
    'Operativa': {
        'verbos': ['realizar', 'verificar', 'controlar', 'hacer'],
        'indicadores': ['semanal', 'mensual', 'frecuencia'],
        'tiempos': ['día', 'semana', 'mes']
    }
}

# ===== INTERFAZ STREAMLIT =====
st.set_page_config(page_title="ALINEA - App de Planeación Estratégica")
st.title("📊 ALINEA - App para Alinear Componentes Estratégicos")

nombre_org = st.text_input("Nombre de la organización")

with st.expander("Principios y Valores"):
    principio1 = st.text_input("Principio o valor 1")
    principio2 = st.text_input("Principio o valor 2")
    principio3 = st.text_input("Principio o valor 3")

with st.expander("Políticas"):
    politica1 = st.text_input("Política 1")
    politica2 = st.text_input("Política 2")
    politica3 = st.text_input("Política 3")

mision = st.text_area("Misión")
vision = st.text_area("Visión")

# === Plan Estratégico ===
st.subheader("🎯 Plan Estratégico")

# Objetivo 1
objetivo1 = st.text_area("Objetivo Estratégico 1")
estrategia1_1 = st.text_area("Estrategia 1.1")
tactica1_1_1 = st.text_area("Táctica 1.1.1")
operativa1_1_1_1 = st.text_area("Operativa 1.1.1.1")
operativa1_1_1_2 = st.text_area("Operativa 1.1.1.2")
tactica1_1_2 = st.text_area("Táctica 1.1.2")
operativa1_1_2_1 = st.text_area("Operativa 1.1.2.1")
operativa1_1_2_2 = st.text_area("Operativa 1.1.2.2")

# Objetivo 2
objetivo2 = st.text_area("Objetivo Estratégico 2")
estrategia2_1 = st.text_area("Estrategia 2.1")
tactica2_1_1 = st.text_area("Táctica 2.1.1")
operativa2_1_1_1 = st.text_area("Operativa 2.1.1.1")
operativa2_1_1_2 = st.text_area("Operativa 2.1.1.2")
tactica2_1_2 = st.text_area("Táctica 2.1.2")
operativa2_1_2_1 = st.text_area("Operativa 2.1.2.1")
operativa2_1_2_2 = st.text_area("Operativa 2.1.2.2")

# Objetivo 3
objetivo3 = st.text_area("Objetivo Estratégico 3")
estrategia3_1 = st.text_area("Estrategia 3.1")
tactica3_1_1 = st.text_area("Táctica 3.1.1")
operativa3_1_1_1 = st.text_area("Operativa 3.1.1.1")
operativa3_1_1_2 = st.text_area("Operativa 3.1.1.2")
tactica3_1_2 = st.text_area("Táctica 3.1.2")
operativa3_1_2_1 = st.text_area("Operativa 3.1.2.1")
operativa3_1_2_2 = st.text_area("Operativa 3.1.2.2")

# === Botón para generar retroalimentación ===
if st.button("✅ Generar realimentación"):
    st.subheader("📌 Realimentación")

    # Objetivo 1
    st.markdown(evaluar_componente("Objetivo Estratégico 1", objetivo1, formulas['Objetivo Estratégico']))
    st.markdown(evaluar_componente("Estrategia 1.1", estrategia1_1, formulas['Estrategia']))
    st.markdown(evaluar_jerarquia(objetivo1, estrategia1_1, tactica1_1_1, operativa1_1_1_1))
    st.markdown(evaluar_componente("Táctica 1.1.1", tactica1_1_1, formulas['Táctica']))
    st.markdown(evaluar_componente("Operativa 1.1.1.1", operativa1_1_1_1, formulas['Operativa']))
    st.markdown(evaluar_componente("Operativa 1.1.1.2", operativa1_1_1_2, formulas['Operativa']))
    st.markdown(evaluar_componente("Táctica 1.1.2", tactica1_1_2, formulas['Táctica']))
    st.markdown(evaluar_componente("Operativa 1.1.2.1", operativa1_1_2_1, formulas['Operativa']))
    st.markdown(evaluar_componente("Operativa 1.1.2.2", operativa1_1_2_2, formulas['Operativa']))

    # Objetivo 2
    st.markdown(evaluar_componente("Objetivo Estratégico 2", objetivo2, formulas['Objetivo Estratégico']))
    st.markdown(evaluar_componente("Estrategia 2.1", estrategia2_1, formulas['Estrategia']))
    st.markdown(evaluar_jerarquia(objetivo2, estrategia2_1, tactica2_1_1, operativa2_1_1_1))
    st.markdown(evaluar_componente("Táctica 2.1.1", tactica2_1_1, formulas['Táctica']))
    st.markdown(evaluar_componente("Operativa 2.1.1.1", operativa2_1_1_1, formulas['Operativa']))
    st.markdown(evaluar_componente("Operativa 2.1.1.2", operativa2_1_1_2, formulas['Operativa']))
    st.markdown(evaluar_componente("Táctica 2.1.2", tactica2_1_2, formulas['Táctica']))
    st.markdown(evaluar_componente("Operativa 2.1.2.1", operativa2_1_2_1, formulas['Operativa']))
    st.markdown(evaluar_componente("Operativa 2.1.2.2", operativa2_1_2_2, formulas['Operativa']))

    # Objetivo 3
    st.markdown(evaluar_componente("Objetivo Estratégico 3", objetivo3, formulas['Objetivo Estratégico']))
    st.markdown(evaluar_componente("Estrategia 3.1", estrategia3_1, formulas['Estrategia']))
    st.markdown(evaluar_jerarquia(objetivo3, estrategia3_1, tactica3_1_1, operativa3_1_1_1))
    st.markdown(evaluar_componente("Táctica 3.1.1", tactica3_1_1, formulas['Táctica']))
    st.markdown(evaluar_componente("Operativa 3.1.1.1", operativa3_1_1_1, formulas['Operativa']))
    st.markdown(evaluar_componente("Operativa 3.1.1.2", operativa3_1_1_2, formulas['Operativa']))
    st.markdown(evaluar_componente("Táctica 3.1.2", tactica3_1_2, formulas['Táctica']))
    st.markdown(evaluar_componente("Operativa 3.1.2.1", operativa3_1_2_1, formulas['Operativa']))
    st.markdown(evaluar_componente("Operativa 3.1.2.2", operativa3_1_2_2, formulas['Operativa']))

    st.markdown("\n---\n**Referencia:** Montoya, Julio César (2025) ALINEA - App para alinear componentes estratégicos. Universidad Nacional Abierta y a Distancia - UNAD.")
