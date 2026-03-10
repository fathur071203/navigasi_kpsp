from pathlib import Path
import base64

import streamlit as st


st.set_page_config(
	page_title="Navigasi Tools KPSP",
	page_icon="🏦",
	layout="wide",
)


# =========================
# Konfigurasi data tombol
# =========================
TOOLS = [
	{
		"label": "Tools LTDBB PJP",
		"url": "https://toolsdpspltdbb.streamlit.app/",
		"icon": "🚀",
		"kind": "process",
	},
	{
		"label": "Tools Cleaning Data",
		"url": "https://toolscleaningkpsp.streamlit.app/",
		"icon": "🧹",
		"kind": "process",
	},
	{
		"label": "Tools Dokumen",
		"url": "https://toolsdokumen.streamlit.app/",
		"icon": "📥",
		"kind": "download",
	},
]


# =========================
# Styling halaman
# =========================
st.markdown(
	"""
	<style>
		.block-container {
			max-width: 920px;
			padding-top: 1.2rem;
			padding-bottom: 1.5rem;
		}

		.stApp {
			background:
				radial-gradient(circle at 0% 0%, rgba(56, 189, 248, 0.20), transparent 45%),
				radial-gradient(circle at 100% 100%, rgba(14, 165, 233, 0.18), transparent 40%),
				linear-gradient(145deg, #ecfeff 0%, #f0f9ff 48%, #eff6ff 100%);
		}

		.hero-wrap {
			margin-top: 8px;
			margin-bottom: 12px;
			padding: 18px 20px 20px;
			border-radius: 20px;
			text-align: center;
			background: linear-gradient(135deg, #0f4aa9 0%, #0891b2 55%, #06b6d4 100%);
			box-shadow: 0 14px 34px rgba(8, 56, 130, 0.28);
			border: 1px solid rgba(255, 255, 255, 0.25);
		}

		.hero-logo {
			display: block;
			margin: 0 auto 10px;
			max-width: 260px;
			width: 55%;
			height: auto;
			object-fit: contain;
			filter: drop-shadow(0 2px 6px rgba(0, 0, 0, 0.12));
		}

		.hero-title {
			font-size: 36px;
			font-weight: 700;
			color: #f8fbff;
			text-shadow:
				0 2px 0 rgba(6, 24, 61, 0.35),
				0 6px 16px rgba(5, 22, 58, 0.60);
			margin-top: 8px;
			margin-bottom: 6px;
			display: inline-block;
			padding: 4px 14px;
			border-radius: 12px;
			background: rgba(7, 35, 86, 0.34);
			backdrop-filter: blur(2px);
			border: 1px solid rgba(255, 255, 255, 0.20);
		}

		.hero-subtitle {
			color: #f2f8ff;
			font-size: 16px;
			margin-bottom: 2px;
			text-shadow: 0 2px 10px rgba(5, 22, 58, 0.35);
			display: inline-block;
			padding: 3px 12px;
			border-radius: 10px;
			background: rgba(7, 35, 86, 0.22);
		}

		.nav-grid {
			display: grid;
			grid-template-columns: 1fr;
			gap: 12px;
			margin-top: 14px;
		}

		.nav-btn,
		.nav-btn-disabled {
			display: flex;
			justify-content: center;
			align-items: center;
			text-align: center;
			width: 100%;
			min-height: 54px;
			border-radius: 14px;
			border: 1px solid transparent;
			color: #ffffff;
			font-weight: 700;
			font-size: 22px;
			padding: 0.65rem 0.8rem;
			text-decoration: none !important;
			transition: all .2s ease;
			box-shadow: 0 10px 22px rgba(15, 74, 169, 0.24);
		}

		.nav-btn:hover {
			transform: translateY(-2px);
			box-shadow: 0 14px 26px rgba(10, 46, 112, 0.30);
		}

		.nav-process {
			background: linear-gradient(135deg, #2563eb 0%, #06b6d4 100%);
		}

		.nav-download {
			background: linear-gradient(135deg, #16a34a 0%, #22c55e 100%);
		}

		.nav-btn-disabled {
			background: linear-gradient(135deg, #94a3b8 0%, #64748b 100%);
			opacity: 0.85;
			cursor: not-allowed;
			font-size: 22px;
		}

		.note {
			text-align: center;
			color: #4f6186;
			margin-top: 10px;
			font-size: 13px;
		}

		@media (max-width: 980px) {
			.hero-logo {
				width: 72%;
				max-width: 220px;
			}

			.hero-title {
				font-size: 30px;
			}

			.hero-subtitle {
				font-size: 14px;
			}

			.nav-grid {
				grid-template-columns: 1fr;
			}

			.nav-btn,
			.nav-btn-disabled {
				font-size: 20px;
			}
		}
	</style>
	""",
	unsafe_allow_html=True,
)

# =========================
# Header (Logo + Judul)
# =========================
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
logo_path = Path("static/Logo.png")
if logo_path.exists():
	logo_base64 = base64.b64encode(logo_path.read_bytes()).decode("utf-8")
	st.markdown(
		f'<img src="data:image/png;base64,{logo_base64}" class="hero-logo" alt="Logo Bank Indonesia" />',
		unsafe_allow_html=True,
	)
else:
	st.markdown(
		'<img src="https://via.placeholder.com/260x110.png?text=Bank+Indonesia" class="hero-logo" alt="Logo" />',
		unsafe_allow_html=True,
	)
st.markdown('<div class="hero-title">Navigasi Tools KPSP</div>', unsafe_allow_html=True)
st.markdown(
	'<div class="hero-subtitle">Satu halaman untuk akses cepat tools kerja</div>',
	unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# Tombol navigasi utama
# =========================
button_html = []
for item in TOOLS:
	kind_class = "nav-download" if item["kind"] == "download" else "nav-process"
	label = f"{item['icon']} {item['label']}"
	if item["url"]:
		button_html.append(
			f'<a class="nav-btn {kind_class}" href="{item["url"]}" target="_blank" rel="noopener noreferrer">{label}</a>'
		)
	else:
		button_html.append(f'<div class="nav-btn-disabled">{label}<br/>Segera hadir</div>')

st.markdown(f'<div class="nav-grid">{"".join(button_html)}</div>', unsafe_allow_html=True)


st.markdown(
	'<div class="note">Logo memakai file static/Logo.png. Tombol membuka tools di tab baru agar tetap stabil saat deploy Streamlit Cloud.</div>',
	unsafe_allow_html=True,
)
