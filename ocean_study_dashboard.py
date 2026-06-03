import streamlit as st
import random

# ==========================================
# PAGE CONFIGURATION & CUSTOM CSS (OCEAN THEME)
# ==========================================
st.set_page_config(page_title="EPSS 15: Oceanography Dashboard", layout="wide", page_icon="🌊")

# Custom CSS for Blue/Green Ocean Theme
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #e0f2f1; /* Light teal */
    }
    
    /* Headers and text */
    h1, h2, h3 {
        color: #004d40; /* Dark teal */
    }
    p, span, li {
        color: #00251a; /* Very dark teal */
    }
    
    /* Buttons */
    div.stButton > button:first-child {
        background-color: #00897b; /* Sea green */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #00695c; /* Darker sea green */
        color: #e0f2f1;
        border: 2px solid #b2dfdb;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #b2dfdb; /* Soft ocean blue-green */
    }
    
    /* Info/Success Boxes */
    div.stAlert {
        background-color: #80cbc4;
        color: #004d40;
        border: 1px solid #00897b;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# COURSE DATA: JEOPARDY & SYLLABUS
# ==========================================
syllabus_info = {
    "course_title": "EPSS 15: Blue Planet: Introduction to Oceanography",
    "term": "Spring 2026",
    "instructor": "Professor Tina Treude (ttreude@g.ucla.edu)",
    "meeting_time": "MW 2:00 - 3:15 PM, Moore 100",
    "grading": [
        "25% Homework Quizzes (8 total; lowest 2 dropped)",
        "25% Lab Final",
        "25% Midterm Exam",
        "25% Final Exam"
    ],
    "extra_credit": "Optional extra credit is available (worth 10%) by visiting an aquarium, museum, or joining a beach cleanup/zodiac field trip."
}

jeopardy_data = {
    "Ocean Circulation": [
        {"q": "What is the name of the region of rapid density change in the ocean?", "a": "Pycnocline"},
        {"q": "What is the general name of the type of current that runs along the eastern coast of continents (e.g., near Japan or the US East Coast)?", "a": "Western Boundary Current"},
        {"q": "Name both regions of deep water discussed in lab.", "a": "North Atlantic Deep Water (NADW) and Antarctic Bottom Water (AABW)"},
        {"q": "The net motion of water at a 90° angle to the prevailing wind direction is known as:", "a": "Ekman transport"},
        {"q": "Name one method of intermediate water formation.", "a": "1) Convergence in subpolar gyres sinking along isopycnals, OR 2) Warm, saline water flowing into the Atlantic from the Mediterranean."}
    ],
    "Oceanic Food Chains": [
        {"q": "Name one example of phytoplankton and one example of zooplankton.", "a": "Phyto: dinoflagellates, coccolithophores, cyanobacteria, diatoms. Zoo: copepods, krill, radiolarians, forams."},
        {"q": "Name an example of a limiting nutrient.", "a": "Nitrogen, Phosphorous, or Silica."},
        {"q": "Name an example of macroplankton.", "a": "Krill, Pteropods, or Gelatinous Plankton (Jellyfish)."},
        {"q": "What are the three trophic groups?", "a": "Producer (autotroph), consumer (heterotroph), and decomposer (saprotroph)."},
        {"q": "Define Euphotic, Dysphotic, Aphotic in terms of photosynthesis.", "a": "Euphotic: surface to critical depth (photosynthesis dominates). Dysphotic: photosynthesis not dominant but occurs. Aphotic: completely dark, no photosynthesis."}
    ],
    "Intertidal Habitats": [
        {"q": "Periwinkle snails inhabit which tidal zone(s)?", "a": "Splash zone to High tide zone."},
        {"q": "Name two ways intertidal organisms have adapted to desiccation.", "a": "Large shell volume (periwinkle), closing body cavity (mussels/barnacles), secreting mucus (anemone), moving to tidepools (sea urchin), gill chambers (crab)."},
        {"q": "How does the large limpet deal with intruders in its space?", "a": "It bulldozes other organisms off the rock."},
        {"q": "Why can red algae inhabit deep water environments?", "a": "They absorb blue light better, which penetrates deeper into the ocean."},
        {"q": "What purpose does a kelp’s pneumatocyst serve?", "a": "They are gas-filled and provide buoyancy to keep the kelp upright."}
    ],
    "Misc & Math": [
        {"q": "What wind pattern drives equatorial currents?", "a": "Trade winds."},
        {"q": "What type of sediment do you expect to find far from continents with low biological productivity?", "a": "Red (abyssal) clay."},
        {"q": "Which current would you expect to cause coastal upwelling in South America?", "a": "Peru (Humboldt) Current."},
        {"q": "How many times larger is the H+ concentration in Lemon Juice (pH 2) than Black Coffee (pH 5)?", "a": "1,000x larger (each step is 10x)."},
        {"q": "You have a piece of basalt (density 3.0 g/cm3) displacing 4 mL of water. What is the mass?", "a": "12 g (Mass = density * volume)."},
        {"q": "Write 1 million dollars in scientific notation.", "a": "10^6 dollars."}
    ],
    "Maps & Bathymetry": [
        {"q": "In a bathymetry map, contours connect lines of equal ______", "a": "Depth."},
        {"q": "In what direction would an underwater ridge be pointing on a bathymetry map?", "a": "Downhill."},
        {"q": "If there were a rapid change in elevation, how would contours be spaced?", "a": "Close together."},
        {"q": "If vertical scale is 2 cm/km and horizontal scale is 1 cm/10 km, what is the vertical exaggeration?", "a": "20x."},
        {"q": "A floating object will displace its _____ in fluid.", "a": "Weight."},
        {"q": "Why are the crests of mid-ocean ridges higher than surrounding seafloor?", "a": "They are younger and warmer (less dense)."}
    ],
    "Plate Tectonics & Sediments": [
        {"q": "Mid Ocean Ridges are an example of this kind of plate boundary.", "a": "Divergent."},
        {"q": "The Himalayas are a consequence of THIS kind of plate boundary.", "a": "Continent-Continent convergence."},
        {"q": "Which process ultimately destroys lithospheric material?", "a": "Subduction."},
        {"q": "A manganese nodule is an example of what kind of sediment?", "a": "Chemogenic (hydrogenous) sediment."},
        {"q": "Which type of sediment dissolves below the CCD?", "a": "Calcareous Oozes."},
        {"q": "In terms of latitude, where is the CCD the deepest?", "a": "Lower latitudes (warmer, less acidic water)."}
    ],
    "Sea Water & Final Jeopardy": [
        {"q": "Name a process that can decrease the salinity of seawater.", "a": "Precipitation or glacier melt."},
        {"q": "Name one consequence of hydrogen bonding in water.", "a": "High latent heat, high heat capacity, high melting/boiling point, less dense as a solid."},
        {"q": "At what latitudes are the highest amounts of surface water dissolved CO2 observed, and why?", "a": "High latitudes/The poles. CO2 solubility is higher in cold water."},
        {"q": "What acts as a buffer in the ocean to keep it from becoming too acidic/basic?", "a": "Bicarbonate (HCO3-)."},
        {"q": "FINAL JEOPARDY: What type of sedimentary rock formed from Miocene Coastal California sediments due to the cold California Current and high productivity?", "a": "Diatomite."}
    ]
}

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if 'flashcard_flipped' not in st.session_state:
    st.session_state.flashcard_flipped = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = None

def flip_card():
    st.session_state.flashcard_flipped = not st.session_state.flashcard_flipped

def next_card(category):
    st.session_state.current_question = random.choice(jeopardy_data[category])
    st.session_state.flashcard_flipped = False

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("🌊 Navigation")
app_mode = st.sidebar.radio("Choose a Section:", ["Course Syllabus Reference", "Jeopardy Flashcards", "Practice Quiz"])

st.sidebar.markdown("---")
st.sidebar.info("Developed as a study aid for **EPSS 15: Introduction to Oceanography**.")

# ==========================================
# PAGE: COURSE SYLLABUS REFERENCE
# ==========================================
if app_mode == "Course Syllabus Reference":
    st.title("📖 Course Syllabus Overview")
    st.markdown(f"### {syllabus_info['course_title']} ({syllabus_info['term']})")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Instructor:** {syllabus_info['instructor']}")
        st.info(f"**Meeting Time:** {syllabus_info['meeting_time']}")
        
    with col2:
        st.success("**Grading Breakdown (Standard):**")
        for item in syllabus_info['grading']:
            st.markdown(f"- {item}")
            
    st.markdown("### 📝 Extra Credit Opportunity")
    st.write(syllabus_info['extra_credit'])
    
    st.markdown("### 🎯 Key Learning Outcomes")
    st.markdown("""
    * **Structure of Oceans:** Bathymetry, isostasy, plate tectonics, and seafloor spreading.
    * **Ocean Currents:** Thermohaline circulation, Ekman transport, upwelling, and tides.
    * **Marine Sediments:** Calcareous/Siliceous oozes, chemogenic sediments, and the CCD.
    * **Seawater Chemistry:** Salinity, heat capacity, buffers (bicarbonate), and climate change.
    * **Ecosystem Dynamics:** Trophic levels, primary productivity, and coastal habitats.
    """)

# ==========================================
# PAGE: JEOPARDY FLASHCARDS
# ==========================================
elif app_mode == "Jeopardy Flashcards":
    st.title("🗂️ Interactive Jeopardy Flashcards")
    st.write("Select a category and test your knowledge using the final review material!")
    
    category = st.selectbox("Select a Topic Category:", list(jeopardy_data.keys()))
    
    # Initialize first card if none exists or category changes
    if st.session_state.current_question is None or st.button("Draw New Card 🔀"):
        next_card(category)

    # Flashcard UI
    if st.session_state.current_question:
        st.markdown("---")
        st.markdown(f"### Category: {category}")
        
        # Display Card Face
        if not st.session_state.flashcard_flipped:
            st.warning("### QUESTION:")
            st.title(st.session_state.current_question['q'])
            st.button("Reveal Answer 👁️", on_click=flip_card)
        else:
            st.success("### ANSWER:")
            st.title(st.session_state.current_question['a'])
            st.button("Hide Answer 🙈", on_click=flip_card)
        st.markdown("---")

# ==========================================
# PAGE: PRACTICE QUIZ
# ==========================================
elif app_mode == "Practice Quiz":
    st.title("📝 Rapid Fire Practice Quiz")
    st.write("Quiz yourself! Type in your answers below or think them through before checking.")
    
    # Flat list of all questions
    all_questions = []
    for cat, qs in jeopardy_data.items():
        for q in qs:
            all_questions.append((cat, q['q'], q['a']))
    
    # Seed fixed sample for quiz session to prevent reload shifting
    random.seed(42)
    quiz_sample = random.sample(all_questions, 5)
    
    with st.form("quiz_form"):
        for i, (cat, question, answer) in enumerate(quiz_sample):
            st.markdown(f"**Question {i+1} ({cat}):** {question}")
            st.text_input("Your Answer", key=f"q_{i}")
            
        submitted = st.form_submit_button("Submit & Check Answers 🎯")
        
        if submitted:
            st.markdown("### Answer Key:")
            for i, (cat, question, answer) in enumerate(quiz_sample):
                st.info(f"**Correct Answer {i+1}:** {answer}")
