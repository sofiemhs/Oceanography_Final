import streamlit as st
import random

# ==========================================
# PAGE CONFIGURATION & OCEAN CSS THEME 🌊
# ==========================================
st.set_page_config(page_title="EPSS 15: Complete Oceanography Course", layout="wide", page_icon="🌊")

st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #F0F8FF; /* Alice Blue */
    }
    
    /* Headers and text */
    html, body, p, div, span, label, li {
        color: #003333 !important; /* Very dark teal for readability */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #005B5B !important; 
        font-weight: 800 !important;
    }

    .big-font { 
        font-size:36px !important; 
        color: #008080 !important; 
        font-weight: 900; 
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 1px 1px 2px rgba(0,128,128,0.2);
    }
    
    .lesson-box { 
        background-color: #E0FFFF; /* Light Cyan */
        color: #002222 !important; 
        padding: 25px; 
        border-radius: 15px; 
        border: 3px solid #20B2AA; /* Light Sea Green */
        margin-bottom: 25px;
        box-shadow: 3px 3px 15px rgba(32, 178, 170, 0.3);
        line-height: 1.6;
        font-size: 17px;
    }
    
    .vocab-box { 
        background-color: #F5FFFA; /* Mint Cream */
        color: #003333 !important; 
        padding: 15px; 
        border-radius: 10px; 
        border: 2px solid #66CDAA; /* Medium Aquamarine */
        margin-bottom: 15px; 
        box-shadow: 2px 2px 8px rgba(102, 205, 170, 0.3);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #B0E0E6 !important; /* Powder Blue */
    }
    
    .stRadio > div[role="radiogroup"] {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        border: 2px dashed #008080;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# COURSE DATA: MODULES, LESSONS & QUIZZES
# ==========================================
# We have 8 Modules covering Lectures 1-17 and Labs 1-8.
course_data = [
    {
        "module": 0,
        "title": "Module 1: Intro, Maps & Ocean Anatomy (Lec 1-2, Lab 1-2)",
        "lesson": """
        <b>Lecture 1: Introduction to Oceanography</b><br>
        The ocean covers 70.8% of Earth, and over 40% of the world's population lives within 150 km of it. Early ocean science dates back to Aristotle (350 BC), but modern oceanography began with expeditions like Charles Darwin on the HMS Beagle and the Challenger Expedition (1872-1876).<br><br>
        
        <b>Lecture 2 & Lab 2: Anatomy of the Oceans & Isostasy</b><br>
        Earth's surface is bimodal: elevated continents and deep ocean basins. 
        <ul>
            <li><b>Continental Crust:</b> Made of granite, less dense (2.7 g/cm³), and thicker.</li>
            <li><b>Oceanic Crust:</b> Made of basalt, more dense (3.0 g/cm³), and thinner.</li>
        </ul>
        <b>Isostasy</b> is the gravitational equilibrium that allows these crusts to "float" on the denser mantle. Because oceanic crust is denser, it sinks deeper, creating ocean basins!<br>
        <b>Ocean Features:</b> Moving offshore, you cross the Continental Shelf, Continental Slope, and Continental Rise before hitting the Abyssal Plain. Active margins (like the Pacific) have narrow shelves and deep-sea trenches. Passive margins (like the Atlantic) have broad flat shelves.<br><br>
        
        <b>Lab 1 (Math Check): Vertical Exaggeration</b><br>
        Maps often stretch the vertical axis to make features visible. <br>
        <i>Formula: Vertical Exaggeration (VE) = Vertical Scale / Horizontal Scale.</i>
        """,
        "vocab": {
            "Isostasy": "Gravitational equilibrium between Earth's crust and mantle.",
            "Bathymetry": "The measurement of depth of water in oceans/seas (underwater topography).",
            "Continental Margin": "The shallow water area found in proximity to continent (includes shelf, slope, and rise)."
        },
        "quiz": [
            {"q": "A piece of basalt (density 3.0 g/cm³) displaces 4 mL of water. What is its mass? (Mass = Density * Volume)", "options": ["0.75 g", "12 g", "7 g"], "a": "12 g"},
            {"q": "On a map, the vertical scale is 2 cm/km, while the horizontal scale is 1 cm/10 km (0.1 cm/km). What is the vertical exaggeration?", "options": ["20x", "10x", "2x"], "a": "20x"},
            {"q": "Which type of continental margin is found along western South America (Pacific type) where trenches are present?", "options": ["Active Margin", "Passive Margin", "Mid-Ocean Ridge"], "a": "Active Margin"}
        ]
    },
    {
        "module": 1,
        "title": "Module 2: Plate Tectonics & Marine Sediments (Lec 3-4, Lab 3-4)",
        "lesson": """
        <b>Lecture 3 & Lab 3: Plate Tectonics</b><br>
        The lithosphere is divided into ~14 major plates that move 2-15 cm/yr over the plastic asthenosphere.
        <ul>
            <li><b>Divergent Boundaries:</b> Plates move apart. New seafloor is created at Mid-Ocean Ridges. These areas have high heat flow and shallow earthquakes.</li>
            <li><b>Convergent Boundaries:</b> Plates collide. Old seafloor is destroyed via subduction at deep-sea trenches. </li>
            <li><b>Transform Boundaries:</b> Plates slide past each other (e.g., San Andreas Fault).</li>
            <li><b>Hotspots:</b> Stationary mantle plumes that create island chains (like Hawaii) as the plate moves over them.</li>
        </ul>
        
        <b>Lecture 4 & Lab 4: Marine Sediments</b><br>
        Sediments tell the history of the ocean. They are classified by origin:
        <ul>
            <li><b>Terrigenous:</b> From continents (rivers, dust). Found near coasts and abyssal plains (red clay).</li>
            <li><b>Biogenic:</b> From dead organisms (calcareous/siliceous oozes).</li>
            <li><b>Chemogenic (Hydrogenous):</b> Precipitated from water (e.g., Manganese nodules).</li>
        </ul>
        <b>The CCD (Calcite Compensation Depth):</b> The depth where calcareous shells dissolve because deep water is colder and more acidic. Siliceous oozes survive below the CCD! CCD is deepest in warm, low-latitude waters.
        """,
        "vocab": {
            "Lithosphere": "The rigid outer part of the earth, consisting of the crust and upper mantle.",
            "Subduction": "The sideways and downward movement of the edge of a plate of the earth's crust into the mantle beneath another plate.",
            "CCD (Calcite Compensation Depth)": "The depth in the oceans below which the rate of supply of calcite lags behind the rate of solvation, such that no calcite is preserved."
        },
        "quiz": [
            {"q": "Mid-Ocean Ridges are an example of this kind of plate boundary:", "options": ["Convergent", "Transform", "Divergent"], "a": "Divergent"},
            {"q": "A manganese nodule is an example of what kind of sediment?", "options": ["Biogenic", "Terrigenous", "Chemogenic (Hydrogenous)"], "a": "Chemogenic (Hydrogenous)"},
            {"q": "Which type of biogenic sediment dissolves BELOW the CCD?", "options": ["Siliceous Ooze", "Calcareous Ooze", "Red Clay"], "a": "Calcareous Ooze"}
        ]
    },
    {
        "module": 2,
        "title": "Module 3: Seawater Chemistry & Stratification (Lec 5-6, Lab 5-6)",
        "lesson": """
        <b>Lecture 5 & Lab 5: Seawater Properties</b><br>
        Average ocean salinity is 35 PSU (35 g/kg). Water has amazing properties due to <b>hydrogen bonding</b> (high heat capacity, high boiling point, ice is less dense than liquid).<br>
        <b>Residence Time</b> is the average time an element stays dissolved in the ocean. <br><i>Formula: Residence Time = Total Mass in Ocean / River Flux per year.</i><br>
        The ocean is buffered by bicarbonate to maintain a pH around 8.0. However, cold deep water holds more CO2, making it more acidic.<br><br>
        
        <b>Lecture 6 & Lab 6: Ocean Stratification</b><br>
        Ocean water is layered by density, which is controlled mostly by Temperature and Salinity.
        <ul>
            <li><b>Thermocline:</b> Rapid change in temperature.</li>
            <li><b>Halocline:</b> Rapid change in salinity.</li>
            <li><b>Pycnocline:</b> Rapid change in density.</li>
        </ul>
        The surface "Mixed Layer" is stirred by winds. High density stratification (a strong pycnocline) acts as a barrier, making vertical mixing much slower!
        """,
        "vocab": {
            "Residence Time": "The average amount of time an atom/ion stays dissolved in the ocean.",
            "Pycnocline": "The region of rapid density change in the ocean.",
            "Hydrogen Bonding": "The chemical bond in water that gives it high heat capacity and makes ice float."
        },
        "quiz": [
            {"q": "How many times larger is the H+ concentration in Lemon Juice (pH 2) than Black Coffee (pH 5)?", "options": ["3x larger", "30x larger", "1,000x larger"], "a": "1,000x larger"},
            {"q": "What is the name of the region of rapid density change in the ocean?", "options": ["Thermocline", "Halocline", "Pycnocline"], "a": "Pycnocline"},
            {"q": "Does strong density stratification make vertical ocean mixing go faster or slower?", "options": ["Faster", "Slower", "No effect"], "a": "Slower"}
        ]
    },
    {
        "module": 3,
        "title": "Module 4: Ocean Circulation (Lec 7-8, Lab 6)",
        "lesson": """
        <b>Lecture 7: Wind-Driven Circulation</b><br>
        Surface currents are driven by winds (like the Trade Winds). 
        <b>The Coriolis Effect</b> deflects moving water to the <b>RIGHT</b> in the Northern Hemisphere and <b>LEFT</b> in the Southern Hemisphere. <br>
        <b>Ekman Transport</b> is the net motion of water at a 90° angle to the prevailing wind direction! This sets up Geostrophic Currents and massive ocean Gyres. Western Boundary Currents (like the Gulf Stream) run fast and deep along the east coasts of continents.<br><br>
        
        <b>Lecture 8: Thermohaline Circulation (The Great Conveyor Belt)</b><br>
        Deep ocean circulation is driven by density differences (cold, salty water sinks). 
        The two main regions where deep water forms are:
        <ol>
            <li><b>North Atlantic Deep Water (NADW):</b> Forms near Greenland/Iceland.</li>
            <li><b>Antarctic Bottom Water (AABW):</b> Forms near Antarctica (the densest water!).</li>
        </ol>
        This deep water travels the globe and eventually upwells, bringing vital nutrients back to the surface.
        """,
        "vocab": {
            "Ekman Transport": "Net motion of water 90 degrees to the wind direction due to the Coriolis effect.",
            "Western Boundary Current": "Fast, deep ocean currents on the western side of ocean basins (east coast of continents).",
            "Thermohaline Circulation": "Deep-ocean circulation driven by differences in water density (temperature and salinity)."
        },
        "quiz": [
            {"q": "The net motion of water at a 90° angle to the prevailing wind direction is known as:", "options": ["Geostrophic Flow", "Ekman Transport", "Thermohaline Circulation"], "a": "Ekman Transport"},
            {"q": "Name the two regions of deep water formation discussed in lab.", "options": ["Gulf Stream and Peru Current", "North Atlantic Deep Water (NADW) and Antarctic Bottom Water (AABW)", "Pacific Deep Water and Indian Deep Water"], "a": "North Atlantic Deep Water (NADW) and Antarctic Bottom Water (AABW)"},
            {"q": "What is the general name of the type of current that runs along the eastern coast of continents (like the Gulf Stream)?", "options": ["Eastern Boundary Current", "Western Boundary Current", "Transpolar Drift"], "a": "Western Boundary Current"}
        ]
    },
    {
        "module": 4,
        "title": "Module 5: Waves, Tides & Productivity 1 (Lec 9-10, Lab 7)",
        "lesson": """
        <b>Lecture 9: Waves and Tides</b><br>
        Waves are energy moving through water. <i>Speed = Wavelength × Frequency.</i><br>
        <b>Tsunamis</b> are caused by earthquakes or landslides. They have tiny wave heights offshore but massive wavelengths, and they grow huge when they hit shallow water (shoaling). <br>
        <b>Tides</b> are driven by the Moon and Sun's gravity. <b>Spring Tides</b> (biggest range) happen during Full/New moons when the Earth, Moon, and Sun align. <b>Neap Tides</b> happen at half moons.<br><br>
        
        <b>Lecture 10 & Lab 7: Oceanic Food Chains & Phytoplankton</b><br>
        Marine food webs start with <b>Phytoplankton</b> (autotrophs like Diatoms and Dinoflagellates) which do photosynthesis. They are eaten by <b>Zooplankton</b> (heterotrophs like copepods).<br>
        Ocean light zones:
        <ul>
            <li><b>Euphotic:</b> Plenty of light for photosynthesis.</li>
            <li><b>Dysphotic:</b> Twilight zone, some light but not enough to dominate.</li>
            <li><b>Aphotic:</b> Completely dark.</li>
        </ul>
        <b>Compensation Depth:</b> The exact depth where a phytoplankton's Photosynthesis equals its Respiration.
        """,
        "vocab": {
            "Spring Tide": "Tides with the largest range, occurring during new and full moons.",
            "Phytoplankton": "Microscopic, photosynthetic organisms that drift in the water (e.g., diatoms).",
            "Compensation Depth": "Depth where photosynthesis output equals respiration consumption."
        },
        "quiz": [
            {"q": "Which of the following is an example of Phytoplankton?", "options": ["Copepods", "Diatoms", "Krill"], "a": "Diatoms"},
            {"q": "What defines the Euphotic zone?", "options": ["It is completely dark", "It is where photosynthesis dominates", "It is the zone where tsunamis form"], "a": "It is where photosynthesis dominates"},
            {"q": "During which moon phases do Spring Tides occur?", "options": ["First and third quarter moons", "New and full moons", "Only full moons"], "a": "New and full moons"}
        ]
    },
    {
        "module": 5,
        "title": "Module 6: Productivity 2 & Remineralization (Lec 11-12, Lab 7)",
        "lesson": """
        <b>Lecture 11: Nutrients and Nekton</b><br>
        Phytoplankton need nutrients. The famous <b>Redfield Ratio</b> shows the atomic ratio of carbon, nitrogen, and phosphorus found in phytoplankton: <b>106 C : 16 N : 1 P</b>.<br>
        In many oceans, Nitrogen or Phosphorous is the <i>limiting nutrient</i>. Interestingly, in the Southern Ocean, the limiting nutrient is actually a trace metal: <b>Iron</b>! 
        Zooplankton undergo daily vertical migrations (hiding in the dark dysphotic zone by day, eating at the surface by night). <b>Nekton</b> are the active swimmers (fish, whales).<br><br>
        
        <b>Lecture 12: Remineralization & The Biological Pump</b><br>
        The <b>Biological Pump</b> is how the ocean removes CO2 from the atmosphere and stores it in the deep sea. Plankton take in CO2, die, and sink as "marine snow." <br>
        As they sink, bacteria eat them (remineralization), which uses up Oxygen and releases CO2 back into the water. In highly productive areas, so much dead matter sinks and decays that the water runs out of oxygen, creating <b>Oxygen Minimum Zones (OMZ)</b>.
        """,
        "vocab": {
            "Redfield Ratio": "The 106:16:1 ratio of Carbon, Nitrogen, and Phosphorous in marine plankton.",
            "Biological Pump": "The process of removing CO2 from the atmosphere and storing it in deep ocean tissue/sediment.",
            "Nekton": "Marine organisms that actively swim in the pelagic zone (e.g., fish, squids)."
        },
        "quiz": [
            {"q": "What is the limiting nutrient for phytoplankton in the Southern Ocean?", "options": ["Nitrogen", "Iron", "Carbon"], "a": "Iron"},
            {"q": "What represents the Redfield Ratio of C : N : P?", "options": ["106 : 16 : 1", "1 : 16 : 106", "50 : 10 : 1"], "a": "106 : 16 : 1"},
            {"q": "What acts as a buffer in the ocean to keep it from becoming too acidic/basic?", "options": ["Iron", "Bicarbonate (HCO3-)", "Sodium Chloride"], "a": "Bicarbonate (HCO3-)"}
        ]
    },
    {
        "module": 6,
        "title": "Module 7: Marine Habitats (Lec 13-14, Lab 8)",
        "lesson": """
        <b>Lecture 13 & Lab 8: Intertidal Zones to Coral Reefs</b><br>
        The <b>Intertidal Zone</b> is harsh! Organisms adapt to desiccation (drying out) and waves. 
        <ul>
            <li><b>High tide zone:</b> Periwinkle snails seal their shells with mucus.</li>
            <li><b>Mid tide zone:</b> Mussels close their shells and anchor with strong threads.</li>
            <li><b>Low tide zone:</b> Sea stars and anemones live here because they can't handle long air exposure. Large limpets 'bulldoze' intruders off their rocks!</li>
        </ul>
        <b>Kelp Forests:</b> Giant brown algae that use gas-filled <b>pneumatocysts</b> to stay afloat and reach sunlight. <br>
        <b>Coral Reefs:</b> Corals are animals (polyps) that live in symbiosis with <b>zooxanthellae</b> (dinoflagellates). Coral bleaching happens when stressed corals expel these algae.<br><br>
        
        <b>Lecture 14: Deep Sea & Whale Falls</b><br>
        The deep sea relies on sinking food, but occasionally gets a massive feast: a dead whale! 
        <b>Whale Falls</b> have 3 stages: 1) Scavenger stage (hagfish, sharks), 2) Opportunistic stage (crabs, worms), and 3) Sulfophilic stage (chemosynthetic bacteria use bone lipids to make hydrogen sulfide, supporting tubeworms for decades!).
        """,
        "vocab": {
            "Pneumatocyst": "Gas-filled bladders in kelp that provide buoyancy.",
            "Zooxanthellae": "Photosynthetic dinoflagellates that live in symbiosis within coral polyps.",
            "Desiccation": "The state of extreme dryness, a major threat to intertidal organisms."
        },
        "quiz": [
            {"q": "Periwinkle snails inhabit which tidal zone(s)?", "options": ["Subtidal", "Splash to High tide zone", "Low tide zone"], "a": "Splash to High tide zone"},
            {"q": "What purpose does a kelp’s pneumatocyst serve?", "options": ["Gas-filled for buoyancy", "Stores fresh water", "Reproduction"], "a": "Gas-filled for buoyancy"},
            {"q": "How does the large limpet deal with intruders in its space?", "options": ["Poisons them", "Bulldozes them off the rock", "Hides in its shell"], "a": "Bulldozes them off the rock"}
        ]
    },
    {
        "module": 7,
        "title": "Module 8: Resources, Change & Governance (Lec 15-17)",
        "lesson": """
        <b>Lecture 15: Marine Resources</b><br>
        We extract fossil fuels, minerals, and fish from the oceans. Overfishing is a massive issue, compounded by <b>Bycatch</b> (catching unwanted species like turtles/dolphins). Aquaculture (fish farming) now supplies over half of human seafood, but it can cause pollution and disease if not managed sustainably.<br><br>
        
        <b>Lecture 16: Ocean Change</b><br>
        Human CO2 emissions are causing two major problems:
        <ol>
            <li><b>Ocean Warming:</b> Leads to sea-level rise and coral bleaching.</li>
            <li><b>Ocean Acidification:</b> Extra CO2 forms carbonic acid, lowering pH. This dissolves the calcium carbonate shells of organisms like pteropods and corals.</li>
        </ol>
        Plastic waste accumulates in massive gyres (e.g., Pacific Garbage Patch). Microplastics enter the food web and we eventually eat them.<br><br>
        
        <b>Lecture 17: Governance (UNCLOS)</b><br>
        The United Nations Convention on the Law of the Sea (UNCLOS) sets boundaries:
        <ul>
            <li><b>Territorial Waters:</b> Up to 12 nautical miles from shore.</li>
            <li><b>Exclusive Economic Zone (EEZ):</b> Up to 200 nautical miles (nations control fishing/mining here).</li>
            <li><b>High Seas:</b> Beyond 200 nm, international waters.</li>
        </ul>
        Marine Protected Areas (MPAs) are established to conserve biodiversity, but currently only a small percentage of the ocean is strictly protected.
        """,
        "vocab": {
            "Bycatch": "The unwanted fish and other marine creatures caught during commercial fishing.",
            "Ocean Acidification": "The decreasing pH of ocean waters due to absorption of excess atmospheric CO2.",
            "UNCLOS": "United Nations Convention on the Law of the Sea; defines rights and responsibilities of nations regarding oceans."
        },
        "quiz": [
            {"q": "Which UNCLOS zone gives a nation the right to exploit resources up to 200 nautical miles from its coast?", "options": ["Territorial Waters", "High Seas", "Exclusive Economic Zone (EEZ)"], "a": "Exclusive Economic Zone (EEZ)"},
            {"q": "Ocean acidification primarily threatens marine organisms by:", "options": ["Making the water too hot", "Dissolving their calcium carbonate shells", "Depleting oxygen (OMZ)"], "a": "Dissolving their calcium carbonate shells"},
            {"q": "FINAL JEOPARDY: What type of sedimentary rock formed from Miocene Coastal California sediments due to the cold California Current?", "options": ["Diatomite", "Basalt", "Limestone"], "a": "Diatomite"}
        ]
    }
]

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if 'module_progress' not in st.session_state:
    st.session_state.module_progress = 0
if 'q_sample' not in st.session_state:
    st.session_state.q_sample = [0, 1, 2] # Always show all 3 questions per module

def advance_module():
    if st.session_state.module_progress < len(course_data) - 1:
        st.session_state.module_progress += 1
        st.balloons()
    else:
        st.session_state.module_progress = 99 # Code for 100% completion
        st.balloons()

def reset_course():
    st.session_state.module_progress = 0

# ==========================================
# SIDEBAR: PROGRESS & APPENDIX
# ==========================================
with st.sidebar:
    st.title("🧭 Course Navigator")
    
    if st.session_state.module_progress == 99:
        progress_percent = 100
    else:
        progress_percent = int((st.session_state.module_progress / len(course_data)) * 100)
        
    st.progress(progress_percent / 100)
    st.write(f"**Overall Progress: {progress_percent}%**")
    
    st.markdown("---")
    st.header("📚 Vocabulary Appendix")
    st.caption("Terms unlock as you progress!")
    
    # Show vocab up to current module
    max_mod = st.session_state.module_progress if st.session_state.module_progress != 99 else len(course_data)
    
    for i in range(max_mod + 1):
        if i < len(course_data):
            for term, definition in course_data[i]["vocab"].items():
                st.markdown(f"<div class='vocab-box'><b>{term}:</b> {definition}</div>", unsafe_allow_html=True)

# ==========================================
# MAIN CONTENT AREA
# ==========================================
st.markdown('<p class="big-font">🌊 EPSS 15: Introduction to Oceanography 🌊</p>', unsafe_allow_html=True)

if st.session_state.module_progress == 99:
    st.success("🎉 CONGRATULATIONS! You have completed all modules and are ready to ACE your final exam! 🎉")
    if st.button("Restart Course 🔄"):
        reset_course()
        st.rerun()
else:
    current_module = course_data[st.session_state.module_progress]
    
    st.header(current_module["title"])
    st.write("Read the comprehensive lecture & lab materials below, then pass the checkpoint quiz to unlock the next module. You've got this! 🐢")
    
    st.markdown(f"<div class='lesson-box'>{current_module['lesson']}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📝 Checkpoint Quiz")
    st.caption("You must answer all questions correctly to proceed!")
    
    # Render Quiz
    quiz_data = current_module["quiz"]
    user_answers = []
    
    for idx, q_dict in enumerate(quiz_data):
        ans = st.radio(f"**{idx+1}. {q_dict['q']}**", q_dict["options"], index=None, key=f"q_{st.session_state.module_progress}_{idx}")
        user_answers.append(ans)
        
    if st.button("Submit Checkpoint 🎯"):
        all_correct = True
        for idx, q_dict in enumerate(quiz_data):
            if user_answers[idx] != q_dict["a"]:
                all_correct = False
                break
                
        if all_correct:
            st.success("Correct! Excellent job learning the material. Unlocking the next module... 🔓")
            advance_module()
            st.rerun()
        else:
            st.error("Oops! One or more answers are incorrect. Review the lesson box and try again! 🔄")
