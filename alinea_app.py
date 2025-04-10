import streamlit as st

# --------------------------------------------
# Función auxiliar para mostrar descripción y campo de texto
# --------------------------------------------

def input_section(title, description, fields):
    st.markdown(f"### {title}")
    st.markdown(description)
    data = {}
    for field in fields:
        data[field] = st.text_area(f"📝 {field}")
    st.markdown("---")
    return data

# --------------------------------------------
# Interfaz principal de la App
# --------------------------------------------

st.title("🧩 ALINEA - Aplicación para Alinear Componentes Estratégicos")
st.markdown("**Desarrollado por:** Montoya, Julio Cesar (2015). Universidad Nacional Abierta y a Distancia - UNAD.")
st.markdown("---")

org_name = st.text_input("🏢 Nombre de la organización:")

principios = input_section("🧭 Principios y Valores",
    "Ingrese los principios y valores fundamentales. Ejemplo: Transparencia, Compromiso, Innovación.",
    ["Principio 1", "Principio 2", "Principio 3"])

politicas = input_section("📜 Políticas",
    "Ingrese las políticas institucionales clave que rigen la actuación de la organización.",
    ["Política 1", "Política 2", "Política 3"])

mision = input_section("🎯 Misión",
    "Propósito fundamental de la organización. ¿Por qué existe?",
    ["Misión"])

vision = input_section("🔭 Visión",
    "Situación futura deseada. ¿Hacia dónde se dirige la organización?",
    ["Visión"])

st.markdown("## 🧠 Plan Estratégico")
st.markdown("A continuación, ingrese los objetivos, estrategias, tácticas y operativos siguiendo la estructura jerárquica y fórmulas definidas.")

objetivos = []
for i in range(1, 4):
    objetivo = st.text_input(f"🎯 Objetivo Estratégico {i} (Verbo + Objeto + Medida + Fecha):")
    estrategias = []
    for j in range(1, 3):
        estrategia = st.text_input(f"➡️ Estrategia {i}.{j} (Verbo + Método + Área + Plazo):")
        tacticas = []
        for k in range(1, 3):
            tactica = st.text_input(f"🛠️ Táctica {i}.{j}.{k} (Verbo + Acción + Recursos + Cronograma):")
            operativos = []
            for l in range(1, 3):
                operativo = st.text_input(f"🔧 Operativa {i}.{j}.{k}.{l} (Verbo + Tarea + Frecuencia [+ Responsable]):")
                operativos.append(operativo)
            tacticas.append((tactica, operativos))
        estrategias.append((estrategia, tacticas))
    objetivos.append((objetivo, estrategias))

# --------------------------------------------
# Realimentación básica automática
# --------------------------------------------

if st.button("✅ Generar realimentación"):
    st.markdown("## 📋 Realimentación Automática")
    if not org_name:
        st.warning("⚠️ Debes ingresar el nombre de la organización.")
    else:
        st.success(f"Organización: {org_name}")
        for idx, (obj, ests) in enumerate(objetivos, 1):
            if not obj:
                st.warning(f"Objetivo Estratégico {idx} está vacío.")
            elif not any(verb in obj.lower() for verb in ["incrementar", "aumentar", "reducir", "establecer", "crear"]):
                st.info(f"🔍 Revisa el verbo del Objetivo Estratégico {idx}. Verbo sugerido: 'Incrementar', 'Reducir', 'Crear'.")
            for jdx, (est, tacts) in enumerate(ests, 1):
                if not est:
                    st.warning(f"Estrategia {idx}.{jdx} está vacía.")
                elif not any(verb in est.lower() for verb in ["desarrollar", "formular", "optimizar", "diseñar", "consolidar"]):
                    st.info(f"🔍 Revisa el verbo de Estrategia {idx}.{jdx}. Verbos sugeridos: 'Desarrollar', 'Diseñar', 'Optimizar'.")
                for kdx, (tac, opers) in enumerate(tacts, 1):
                    if not tac:
                        st.warning(f"Táctica {idx}.{jdx}.{kdx} está vacía.")
                    elif not any(verb in tac.lower() for verb in ["implementar", "ejecutar", "aplicar"]):
                        st.info(f"🔍 Verbo sugerido para Táctica {idx}.{jdx}.{kdx}: 'Implementar', 'Ejecutar', 'Aplicar'.")
                    for ldx, op in enumerate(opers, 1):
                        if not op:
                            st.warning(f"Operativa {idx}.{jdx}.{kdx}.{ldx} está vacía.")
                        elif not any(verb in op.lower() for verb in ["realizar", "monitorear", "gestionar", "controlar"]):
                            st.info(f"🔍 Verbo sugerido para Operativa {idx}.{jdx}.{kdx}.{ldx}: 'Realizar', 'Monitorear', 'Controlar'.")

        st.markdown("---")
        st.markdown("**Referencia:** Montoya, Julio Cesar (2015). ALINEA - App para alinear componentes estratégicos. Universidad Nacional Abierta y a Distancia - UNAD.")

