import streamlit as st
import streamlit.components.v1 as components

# Configuración principal de la página
st.set_page_config(
    page_title="Para Kim 🌷",
    page_icon="🌷",
    layout="centered"
)

# Estilos CSS generales para un diseño romántico y elegante
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ffe6e9 0%, #ffc2d1 50%, #ffb3c1 100%);
    }
    .container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2.5rem 2rem;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(225, 29, 72, 0.18);
        text-align: center;
        margin-top: 1rem;
    }
    .title {
        color: #c9184a;
        font-family: 'Georgia', serif;
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 1.2rem;
    }
    .message {
        color: #590d22;
        font-size: 1.25rem;
        line-height: 1.7;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }
    .signature {
        color: #800f2f;
        font-size: 1.35rem;
        font-weight: bold;
        font-style: italic;
        margin-top: 1.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Tulipanes animados en CSS/HTML que se mecen bonito
tulip_animation = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        padding: 0;
        background: transparent;
        display: flex;
        justify-content: center;
        align-items: flex-end;
        height: 320px;
        overflow: hidden;
    }

    .garden {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        gap: 40px;
        height: 100%;
        width: 100%;
    }

    /* Animación del movimiento del tulipán */
    .tulip {
        position: relative;
        transform-origin: bottom center;
        animation: sway 3.5s ease-in-out infinite alternate;
    }

    .tulip:nth-child(2) {
        animation-delay: -1.2s;
        transform: scale(1.1);
    }

    .tulip:nth-child(3) {
        animation-delay: -2.3s;
        transform: scale(0.95);
    }

    @keyframes sway {
        0% { transform: rotate(-6deg); }
        100% { transform: rotate(6deg); }
    }

    /* Tallo de la flor */
    .stem {
        width: 8px;
        height: 180px;
        background: linear-gradient(to right, #2b9348, #55a630);
        border-radius: 4px;
        margin: 0 auto;
        position: relative;
    }

    /* Hojas */
    .leaf-left, .leaf-right {
        position: absolute;
        width: 32px;
        height: 75px;
        background: #55a630;
        border-radius: 0 100px 0 100px;
        bottom: 25px;
    }

    .leaf-left {
        left: -26px;
        transform: rotate(-28deg);
    }

    .leaf-right {
        right: -26px;
        transform: scaleX(-1) rotate(-28deg);
    }

    /* Flor del tulipán */
    .flower {
        position: absolute;
        top: -65px;
        left: 50%;
        transform: translateX(-50%);
        width: 68px;
        height: 75px;
    }

    .petal {
        position: absolute;
        bottom: 0;
        width: 40px;
        height: 68px;
        border-radius: 50px 50px 12px 12px;
    }

    /* Variación de colores para los tulipanes */
    .tulip-pink .petal {
        background: linear-gradient(to top, #ff4d6d, #ff758f);
    }
    .tulip-red .petal {
        background: linear-gradient(to top, #c9184a, #ff0054);
    }
    .tulip-softpink .petal {
        background: linear-gradient(to top, #ff8fa3, #ffb3c1);
    }

    .petal-center {
        left: 14px;
        z-index: 2;
    }

    .petal-left {
        left: 0;
        transform: rotate(-18deg);
        z-index: 1;
        filter: brightness(0.92);
    }

    .petal-right {
        right: 0;
        transform: rotate(18deg);
        z-index: 1;
        filter: brightness(0.92);
    }
</style>
</head>
<body>
    <div class="garden">
        <!-- Tulipán 1 (Rosa vibrante) -->
        <div class="tulip tulip-pink">
            <div class="flower">
                <div class="petal petal-left"></div>
                <div class="petal petal-right"></div>
                <div class="petal petal-center"></div>
            </div>
            <div class="stem">
                <div class="leaf-left"></div>
                <div class="leaf-right"></div>
            </div>
        </div>

        <!-- Tulipán 2 (Rojo romántico) -->
        <div class="tulip tulip-red">
            <div class="flower">
                <div class="petal petal-left"></div>
                <div class="petal petal-right"></div>
                <div class="petal petal-center"></div>
            </div>
            <div class="stem">
                <div class="leaf-left"></div>
                <div class="leaf-right"></div>
            </div>
        </div>

        <!-- Tulipán 3 (Rosa suave) -->
        <div class="tulip tulip-softpink">
            <div class="flower">
                <div class="petal petal-left"></div>
                <div class="petal petal-right"></div>
                <div class="petal petal-center"></div>
            </div>
            <div class="stem">
                <div class="leaf-left"></div>
                <div class="leaf-right"></div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Renderizar tarjeta romántica
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="title">Para mi niña preciosa 💖</div>', unsafe_allow_html=True)

st.markdown("""
<div class="message">
    <b>mi niña preciosa estas rosas no son reales pero son con todo lo que he aprendido a lo largo del tiempo</b><br><br>
    <b>estos tulipanes son para ti:</b>
</div>
""", unsafe_allow_html=True)

# Mostrar animación de los tulipanes
components.html(tulip_animation, height=330)

st.markdown("""
<div class="signature">
    att de tu colochito tu futuro esposo 💍✨
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)