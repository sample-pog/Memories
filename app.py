import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# ====================== CONFIG ======================
st.set_page_config(page_title="Hamar sahabak yaadein", page_icon="❤️", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {background-color: #fffaf0;}
    h1 {color: #c2185b; text-align: center; font-family: 'Georgia', serif;}
    h2 {color: #ad1457;}
    .stImage img {border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);}
    .heart {position: absolute; font-size: 30px; animation: float 6s linear infinite; opacity: 0.8;}
    @keyframes float {
        0% {transform: translateY(0) rotate(0deg); opacity: 0.8;}
        100% {transform: translateY(-800px) rotate(30deg); opacity: 0;}
    }
    </style>
""", unsafe_allow_html=True)

# ====================== PASSWORD ======================
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Hamar premak bhaao")
    st.markdown("### Katha sabhanke kholbaak password darj karu ❤️")
    
    password = st.text_input("Password", type="password", key="pwd")
    
    if st.button("Hamar katha kholu"):
        if password.lower() == "cutie":  # ← Change this!
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("galat password, babygirl 💔")
    st.stop()  # Don't show content until authenticated

# ====================== FLOATING HEARTS + MUSIC ======================
st.success("Swagat achi hamar khubsurat patni ❤️")

# Floating hearts (HTML + JS)
hearts_html = """
<div id="hearts" style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:9999; overflow:hidden;"></div>
<script>
function createHeart() {
    const heart = document.createElement('div');
    heart.className = 'heart';
    heart.innerHTML = '❤️';
    heart.style.left = Math.random() * 100 + 'vw';
    heart.style.animationDuration = (Math.random() * 4 + 4) + 's';
    heart.style.opacity = Math.random() * 0.6 + 0.4;
    document.getElementById('hearts').appendChild(heart);
    setTimeout(() => heart.remove(), 8000);
}
setInterval(createHeart, 300);
</script>
"""
st.components.v1.html(hearts_html, height=0)

# Background Music (Dropbox direct link)
music_url = "https://www.dropbox.com/scl/fi/t3u9w9vxqjdkows6l0y8x/DJ-Snake-Let-Me-Love-You-ft.-Justin-Bieber.mp3?rlkey=7gjlth6631exu57w2zis8na3v&st=nbk101vd&dl=1"  # ← Change this
st.audio(music_url, format="audio/mp3", start_time=0)  # Auto-plays on most browsers after interaction

st.title("Hamar yaad")
st.markdown("### Sadaak lel ahaan sang, hamar duniya ❤️")

# ====================== MEMORIES (with multiple images) ======================
memories = [
    {
        "date": "May 24, 2026",
        "title": "The Real Date",
        "images": [
            "https://www.dropbox.com/scl/fi/wq5a7yl50t6t77pocmf47/IMG-20260524-WA0010.jpg?rlkey=4uugtl5fkzgfg4pfsheajghrh&st=0y8nf6dy&dl=1",
            "https://www.dropbox.com/scl/fi/5tdcbctjmvtkq7lovs984/IMG-20260524-WA0005.jpg?rlkey=fa9gwvqlygymtepib3e9cjf3j&st=uc3fb5da&dl=1",
            "https://www.dropbox.com/scl/fi/67w26tvnjr3h7ult3hap2/IMG-20260524-WA0008.jpg?rlkey=tjdp88wuk4i4knghnyji8kgj8&st=5n24okax&dl=1",
            "https://www.dropbox.com/scl/fi/84k7w2446k8u377heg2rg/IMG-20260524-WA0002.jpg?rlkey=p9uob0bilcgz965kd7qzzw5qg&st=ra8ep7u4&dl=1",
        ],
        "story": "Frock me ahaank apsara lagait chi."
    },
    # Add more memories here
    {
        "date": "Random"
        "title: Ahank katek sundar bujhe chi"
        "images": [
            "https://www.dropbox.com/scl/fi/dgtmyakxnwvs9e32nlhxx/IMG-20260331-WA0004.jpg?rlkey=zjc7tmok4u8owls66dge8cxbj&st=o7xmm0pn&dl=1",
            "https://www.dropbox.com/scl/fi/0eqzr28d4jvi0pkdvui77/IMG-20260409-WA0000.jpg?rlkey=916ode0ari029ocsjf4yrhkkn&st=7jeaqw58&dl=1",
            "https://www.dropbox.com/scl/fi/l6laaxt8rwwr8iojhvlzi/IMG-20260510-WA0001.jpg?rlkey=znqbt3f0zxdvjrn91hbiont5d&st=ac59est8&dl=1",
            "https://www.dropbox.com/scl/fi/ps7try01gr0q5xaamb6xn/IMG-20260516-WA0012.jpg?rlkey=vf23ce1geahala42dgpvwnc9k&st=mfs3y1mb&dl=1",
            "https://www.dropbox.com/scl/fi/6bv6aay2dduno3dbkq36d/IMG-20260519-WA0005.jpg?rlkey=7kp6ptebjhvszee9rwd7pvot4&st=64c4239m&dl=1",
        ],
    },

    {
        "date": "random"
        "title: Ahank vaastav me ketek sundar chi"
        "images": [
            "https://www.dropbox.com/scl/fi/2cikegn7uucstmqajfh5a/IMG-20260203-WA0008.jpg?rlkey=41kmu77wr0b410nm2626y7mdu&st=m0o9dz05&dl=1",
            "https://www.dropbox.com/scl/fi/xo58aydoz3gor8cjzh1ba/IMG-20260224-WA0006.jpg?rlkey=mknj3e0q8ryhs1ld7fmaolb0f&st=rhe4e3pz&dl=1",
            "https://www.dropbox.com/scl/fi/du9g543mnmf15fft5qjof/IMG-20260323-WA0003.jpg?rlkey=9hut8i8k655b79beic10rdwnw&st=0mo42c1v&dl=1",
            "https://www.dropbox.com/scl/fi/guxezy55mk9f1zm7xu2jr/IMG-20260407-WA0000.jpg?rlkey=zsmlo7r8co27zvv3ybah7v2bo&st=v288j5qs&dl=1",
            "https://www.dropbox.com/scl/fi/z6ytqzlh990v8b43r47cy/IMG-20260504-WA0007.jpg?rlkey=3nbotgn7hpwplxa8atiwjeebw&st=z795om0t&dl=1",
            "https://www.dropbox.com/scl/fi/b6gc3e4dfk7qrto0msly9/IMG-20260513-WA0011.jpg?rlkey=ntaiyp7q8txblw6bycthyzcxu&st=glbkh7f8&dl=1",
            "https://www.dropbox.com/scl/fi/7cpwtjjkp8d1l497qkkfu/IMG-20260518-WA0001.jpg?rlkey=hj8hyj669u94sftsehkwqn4pt&st=cyyvr708&dl=1",
            "https://www.dropbox.com/scl/fi/nr8rnjhy0oeicdbafwled/Screenshot_2026-02-13-15-36-52-54_6012fa4d4ddec268fc5c7112cbb265e7.jpg?rlkey=xazqmb5cvl1r7z8hpcrhxc0jg&st=k83qnsnt&dl=1",
            "https://www.dropbox.com/scl/fi/ga9xfvito1lvqcgypbnbq/Screenshot_2026-02-17-14-52-10-17_6012fa4d4ddec268fc5c7112cbb265e7.jpg?rlkey=3wgrfq5dkkiqmgtk0juhxdyp2&st=69ol8n64&dl=1",
            "https://www.dropbox.com/scl/fi/1u48i4vrv5eougj7fz15g/Screenshot_2026-04-14-00-52-10-60_6012fa4d4ddec268fc5c7112cbb265e7.jpg?rlkey=caa9gizqh2g50nr76hs38ae8o&st=r8ktc5in&dl=1",
        ]
    }
]

# Navigation (Mobile-friendly with session state)
if 'current_memory' not in st.session_state:
    st.session_state.current_memory = 0

current = st.session_state.current_memory

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("← Previous"):
        st.session_state.current_memory = (current - 1) % len(memories)
        st.rerun()
with col3:
    if st.button("Next →"):
        st.session_state.current_memory = (current + 1) % len(memories)
        st.rerun()

# Display current memory
memory = memories[current]

st.subheader(f"{memory['title']} — {memory['date']}")

# Multiple images in a nice layout
cols = st.columns(min(3, len(memory["images"])))
for i, url in enumerate(memory["images"]):
    with cols[i % len(cols)]:
        try:
            resp = requests.get(url)
            img = Image.open(BytesIO(resp.content))
            st.image(img, use_column_width=True)
        except:
            st.error("Image failed to load")

st.write(memory["story"])
st.progress((current + 1) / len(memories), text=f"Memory {current+1} of {len(memories)}")

st.divider()
