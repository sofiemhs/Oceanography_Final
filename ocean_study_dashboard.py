import streamlit as st
import random

# ==========================================
# PAGE CONFIGURATION & SAFE OCEAN CSS THEME 🌊
# ==========================================
# Fixing the "black box" issue by relying on safe CSS and native Streamlit 
# markdown instead of hard-coded HTML divs for the text content.
st.set_page_config(page_title="EPSS 15: Complete Oceanography Course", layout="wide", page_icon="🌊")

st.markdown("""
    <style>
    /* Main background - safe ocean theme */
    .stApp {
        background-color: #E0F7FA; /* Light Cyan/Blue */
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #B2EBF2 !important; /* Slightly darker cyan */
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #006064 !important; /* Deep dark cyan */
    }
    
    /* Ensure text is always readable (no black boxes!) */
    .stMarkdown p, .stMarkdown li {
        color: #004D40 !important;
        font-size: 16px;
    }
    
    .big-font { 
        font-size:36px !important; 
        color: #00838F !important; 
        font-weight: 900; 
        text-align: center;
        margin-bottom: 20px;
    }
    
    .vocab-box { 
        background-color: #FFFFFF; 
        color: #004D40 !important; 
        padding: 15px; 
        border-radius: 10px; 
        border: 2px solid #26A69A; 
        margin-bottom: 15px; 
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# COURSE DATA: COMPREHENSIVE MODULES
# ==========================================
course_data = [
    {
        "module": 0,
        "title": "Module 1: Intro, Maps, Graphs & Ocean Anatomy",
        "lesson": """
### Lecture 1 & Lab 1: Maps, Contours & Graphs
* **Interpolation vs. Extrapolation:** When plotting data on a graph, predicting values *between* plotted points is called **interpolation**. Predicting values *outside* the range of plotted points is **extrapolation**.
* **Contours:** Lines drawn on a figure that connect data of equal value. For example, contours of equal temperature are called *isotherms*, and contours of equal depth are *isobaths*. On a bathymetry map, if there is a rapid change in elevation (a steep slope), the contours will be spaced **close together**. An underwater ridge points **downhill**.
* **Vertical Exaggeration (VE):** Maps often stretch the vertical axis to make topographic features visible. 

### Lecture 2 & Lab 2: Anatomy of the Oceans & Isostasy
Earth's elevations have a **bimodal distribution**: continents average 840 meters above sea level, and oceans average 3,700 meters below sea level.
* **Isostasy:** The gravitational equilibrium between Earth's crust and mantle. The crust "floats" on the denser mantle. 
* **Crust Types:**
  * **Continental Crust:** Made of granite. Less dense (2.7 g/cm³), thicker.
  * **Oceanic Crust:** Made of basalt. More dense (3.0 g/cm³), thinner.
  * **Mantle:** Very dense (3.3 g/cm³).
* **Continental Margins:** * **Passive (Atlantic-type):** Broad, flat shelves. No trench.
  * **Active (Pacific-type):** Narrow shelves, adjacent to deep-sea trenches (e.g., Peru-Chile Trench near the Andes).
        """,
        "math_lesson": """
**📐 Math Practice: Vertical Exaggeration & Isostasy**
1. **Vertical Exaggeration Formula:** `VE = Vertical Scale / Horizontal Scale`
   * *Example:* If vertical scale is 2 cm/km and horizontal scale is 1 cm/10 km (which is 0.1 cm/km), then `VE = 2 / 0.1 = 20x`.
2. **Mass/Density Formula:** `Mass = Density × Volume`
   * *Example:* A piece of basalt (density 3.0 g/cm³) displaces 4 mL (4 cm³) of water. `Mass = 3.0 × 4 = 12 g`.
        """,
        "vocab": {
            "Isostasy": "Gravitational equilibrium between Earth's crust and mantle.",
            "Interpolation": "Predicting values between plotted data points on a graph.",
            "Active Margin": "A continental margin with a narrow shelf and a deep-sea trench (e.g., Pacific type)."
        },
        "quiz": [
            {"q": "A piece of basalt (density 3.0 g/cm³) displaces 5 mL of water. What is its mass?", "options": ["1.6 g", "15 g", "8 g"], "a": "15 g"},
            {"q": "If the vertical scale is 4 cm/km and the horizontal scale is 0.5 cm/km, what is the Vertical Exaggeration?", "options": ["8x", "2x", "4.5x"], "a": "8x"},
            {"q": "If contours on a bathymetric map are spaced very close together, this indicates:", "options": ["A flat plain", "A rapid change in elevation (steep)", "A deep sea trench specifically"], "a": "A rapid change in elevation (steep)"}
        ]
    },
    {
        "module": 1,
        "title": "Module 2: Plate Tectonics & Marine Sediments",
        "lesson": """
### Lecture 3 & Lab 3: Plate Tectonics
The lithosphere is divided into ~14 major plates moving over the plastic asthenosphere.
* **Divergent Boundaries:** Plates move apart. Creates Mid-Ocean Ridges (MORs). Characterized by high heat flow, shallow earthquakes, and abundant volcanic activity.
* **Convergent Boundaries:** Plates collide. Old seafloor is destroyed via **subduction** at deep-sea trenches. 
* **Transform Boundaries:** Plates slide past each other horizontally.
* **Hotspots:** Stationary mantle plumes that create island chains (e.g., Hawaii, Emperor Seamounts). The age of the islands increases as you move away from the active hotspot.

### Lecture 4 & Lab 4: Marine Sediments
Sediments are classified genetically:
* **Terrigenous:** Derived from land weathering (e.g., rivers, glaciers). Found near coasts and in deep abyssal plains (red clay).
* **Biogenic:** From remains of marine life. 
  * *Siliceous Ooze:* From Diatoms and Radiolarians. Usually found below the CCD in upwelling regions.
  * *Calcareous Ooze:* From Foraminifera and Coccolithophores. 
* **Chemogenic (Hydrogenous):** Precipitated directly from seawater (e.g., Manganese nodules).
* **The CCD (Calcite Compensation Depth):** The depth where calcareous shells dissolve because deep water is colder, higher pressure, and more acidic. The CCD is deepest in lower (warmer) latitudes. Calcareous oozes dissolve *below* the CCD.
        """,
        "math_lesson": """
**📐 Math Practice: Plate Velocity & Settling Time**
1. **Plate Velocity Formula:** `Velocity = Distance / Time`
   * *Example:* The distance from Hawaii to Pearl Reef is 2,000 km (200,000,000 cm). Pearl Reef is 20 million years old. `Velocity = 200,000,000 cm / 20,000,000 yrs = 10 cm/yr`.
2. **Settling Time (Stoke's Law context):** Settling time *decreases* as grain size *increases*. A larger sand grain settles in seconds, while a tiny silt grain can take 6 to 58 days to reach the abyssal plain!
        """,
        "vocab": {
            "Subduction": "The downward movement of an oceanic plate into the mantle beneath another plate.",
            "CCD": "Calcite Compensation Depth; the depth below which no calcite is preserved.",
            "Chemogenic Sediment": "Sediment precipitated directly from dissolved minerals in water (e.g., manganese nodules)."
        },
        "quiz": [
            {"q": "An island is 3,000 km (300,000,000 cm) away from a hotspot and is 30 million years old. What is the plate velocity?", "options": ["10 cm/yr", "1 cm/yr", "30 cm/yr"], "a": "10 cm/yr"},
            {"q": "Which biogenic sediment is likely to be found on the deep abyssal plain BELOW the CCD?", "options": ["Calcareous Ooze", "Siliceous Ooze", "Manganese Nodules"], "a": "Siliceous Ooze"},
            {"q": "According to settling rules, which particle will take the LONGEST time to reach the ocean floor?", "options": ["A large sand grain", "A medium silt grain", "A tiny clay particle"], "a": "A tiny clay particle"}
        ]
    },
    {
        "module": 2,
        "title": "Module 3: Seawater Properties & Stratification",
        "lesson": """
### Lecture 5 & Lab 5: Seawater Chemistry
Water is unique due to **hydrogen bonding**, which gives it a high heat capacity, high latent heat, and causes ice to be less dense than liquid water (max density is at 4°C).
* **Salinity:** Average ocean salinity is 35 PSU (parts per thousand, or 35‰). Salinity is decreased by precipitation or glacier melt, and increased by evaporation.
* **pH Scale:** The ocean is buffered by **Bicarbonate (HCO3-)** to maintain a pH around 8.0. The pH scale is logarithmic: a pH of 2 is 10x more acidic than a pH of 3, and 1,000x more acidic than a pH of 5.
* **CO2 in the Ocean:** Cold, deep water at high latitudes absorbs the highest amounts of CO2 because CO2 solubility increases in cold water.

### Lecture 6 & Lab 6: Ocean Stratification
Density in the ocean is controlled by Temperature and Salinity. 
* **Thermocline:** Rapid change in temperature.
* **Halocline:** Rapid change in salinity.
* **Pycnocline:** Rapid change in density.
Strong density stratification makes vertical ocean mixing go **slower**. Vertical mixing is most likely to happen in unstratified surface waters or at the poles where the water column is uniformly cold.
        """,
        "math_lesson": """
**📐 Math Practice: Residence Time & pH Scaling**
1. **Residence Time Formula:** `Residence Time = Total Mass in Ocean / River Flux per year`
   * *Example:* If the ocean contains 2.0 × 10^21 grams of Magnesium, and rivers add 1.2 × 10^14 grams/yr. 
   * `Time = (2.0 × 10^21) / (1.2 × 10^14) = ~1.6 × 10^7 years`.
2. **pH Scaling:** Every 1 step on the pH scale is a 10x change in H+ ions.
   * *Example:* How much more acidic is pH 4 than pH 7? 7 - 4 = 3 steps. 10 × 10 × 10 = 1,000x.
        """,
        "vocab": {
            "Residence Time": "The average amount of time an atom/ion stays dissolved in the ocean.",
            "Pycnocline": "The region of rapid density change in the ocean.",
            "Hydrogen Bonding": "The chemical bond in water giving it high heat capacity and allowing ice to float."
        },
        "quiz": [
            {"q": "If the total mass of an element in the ocean is 8 x 10^20 g, and the river flux is 4 x 10^10 g/yr, what is the residence time?", "options": ["2 x 10^10 yrs", "4 x 10^10 yrs", "2 x 10^5 yrs"], "a": "2 x 10^10 yrs"},
            {"q": "How many times larger is the H+ concentration in a solution with pH 3 compared to pH 6?", "options": ["30x", "300x", "1,000x"], "a": "1,000x"},
            {"q": "Does strong density stratification make vertical ocean mixing go faster or slower?", "options": ["Faster", "Slower", "No effect"], "a": "Slower"}
        ]
    },
    {
        "module": 3,
        "title": "Module 4: Ocean Circulation",
        "lesson": """
### Lecture 7 & 8, Lab 6: Wind-Driven & Gravity-Driven Circulation
* **The Coriolis Effect:** Because Earth rotates, moving fluids are deflected. 
  * Northern Hemisphere: Deflected to the **RIGHT**.
  * Southern Hemisphere: Deflected to the **LEFT**.
* **Ekman Transport:** The net motion of water at a 90° angle to the prevailing wind direction. This builds up pressure gradients that create Geostrophic Currents and large ocean gyres.
* **Western Boundary Currents:** Fast, deep currents flowing along the eastern coasts of continents (e.g., the Gulf Stream in the Atlantic, Kuroshio in the Pacific).
* **Thermohaline Circulation (The Great Conveyor Belt):** Deep-ocean circulation driven by density differences. 
  * The two major regions where deep water forms are the **North Atlantic (NADW)** and near **Antarctica (AABW)**. Here, cold, salty water sinks to the bottom.
  * Intermediate water can form via convergence of surface waters in subpolar gyres or highly saline water flowing out of the Mediterranean.
        """,
        "math_lesson": """
**📐 Concept Practice: Coriolis Vectors**
While not strict math, you must know your vectors!
* If wind blows purely North in the Northern Hemisphere, Ekman transport moves the water 90° to the Right (East).
* If wind blows purely South in the Southern Hemisphere, Ekman transport moves water 90° to the Left (East).
        """,
        "vocab": {
            "Ekman Transport": "Net motion of water 90 degrees to the wind direction.",
            "Western Boundary Current": "Fast, deep ocean currents on the western side of ocean basins.",
            "Thermohaline Circulation": "Deep-ocean circulation driven by temperature and salinity density gradients."
        },
        "quiz": [
            {"q": "The net motion of water at a 90° angle to the prevailing wind direction is known as:", "options": ["Geostrophic Flow", "Ekman Transport", "Coriolis Force"], "a": "Ekman Transport"},
            {"q": "Name the two primary regions of deep water formation.", "options": ["North Atlantic and Antarctica", "Equator and Pacific", "Mediterranean and Gulf of Mexico"], "a": "North Atlantic and Antarctica"},
            {"q": "In the Northern Hemisphere, the Coriolis effect deflects moving water to the:", "options": ["Right", "Left", "Equator"], "a": "Right"}
        ]
    },
    {
        "module": 4,
        "title": "Module 5: Productivity & The Marine Food Web",
        "lesson": """
### Lecture 10, 11 & Lab 7: Oceanic Food Chains
The base of the marine food web relies on **Phytoplankton** (e.g., diatoms, coccolithophores, dinoflagellates, cyanobacteria). They are consumed by **Zooplankton** (e.g., copepods, krill, forams).
* **Limiting Nutrients:** Nutrients that are depleted quickly. Macro-nutrients include Nitrogen, Phosphorous, and Silica. Micro-nutrients include trace metals like **Iron** (which is severely limiting in the Southern Ocean).
* **The Redfield Ratio:** The atomic ratio of Carbon, Nitrogen, and Phosphorus in phytoplankton is **106 C : 16 N : 1 P**.
* **Light Zones:**
  * *Euphotic:* Surface to critical depth. Photosynthesis dominates.
  * *Dysphotic:* Twilight zone. Photosynthesis happens, but respiration is greater.
  * *Aphotic:* Completely dark.
* **Compensation Depth:** The specific depth where an organism's Photosynthesis output exactly equals its Respiration consumption.

### Lecture 12: Remineralization & The Biological Pump
* **Biological Pump:** The process where plankton absorb atmospheric CO2, die, and sink as "marine snow" into the deep ocean. 
* As they sink, saprotrophic bacteria consume them (remineralization), which uses up Oxygen and releases CO2 back into the water. In highly productive upwelling regions, this causes **Oxygen Minimum Zones (OMZ)**.
        """,
        "math_lesson": """
**📐 Math Practice: The Redfield Ratio**
1. **Redfield Ratio Applications:** `106 C : 16 N : 1 P`
   * *Example:* If you have a phytoplankton bloom that consumes 32 units of Nitrogen, how many units of Phosphorus did it consume? 
   * Since N:P is 16:1, consuming 32 N (which is 16 × 2) means it consumed 2 units of P.
        """,
        "vocab": {
            "Redfield Ratio": "The 106:16:1 ratio of Carbon, Nitrogen, and Phosphorous in marine plankton.",
            "Compensation Depth": "Depth where photosynthesis output equals respiration consumption.",
            "Biological Pump": "The biologically driven sequestration of carbon from the atmosphere to the deep sea."
        },
        "quiz": [
            {"q": "What is the limiting nutrient for phytoplankton in the Southern Ocean?", "options": ["Nitrogen", "Iron", "Carbon"], "a": "Iron"},
            {"q": "What represents the Redfield Ratio of C : N : P?", "options": ["106 : 16 : 1", "1 : 16 : 106", "50 : 10 : 1"], "a": "106 : 16 : 1"},
            {"q": "At the compensation depth, what two processes are perfectly equal?", "options": ["Evaporation and Precipitation", "Photosynthesis and Respiration", "Sinking and Upwelling"], "a": "Photosynthesis and Respiration"}
        ]
    },
    {
        "module": 5,
        "title": "Module 6: Intertidal Habitats & The Deep Sea",
        "lesson": """
### Lecture 13 & Lab 8: The Intertidal Zone
The Intertidal Zone is ruled by extreme conditions. Zonal distribution is controlled by two main limits:
1. **Upper Limits:** Set by *Physical* factors (desiccation/drying out, waves, temperature).
2. **Lower Limits:** Set by *Biological* factors (predation, competition for space).

**Key Intertidal Organisms & Adaptations:**
* **High/Spray Zone:** Periwinkle snails (seal shells with mucus to avoid desiccation). Limpets (Acmaea) use a massive foot muscle to suction to rocks and "bulldoze" intruders.
* **Middle Zone:** Mussels (Mytilus californianus) anchor with byssal threads. They do not live lower down because they want to avoid their primary predator: the sea star!
* **Lower Zone:** Sea stars and anemones. Anemones secrete mucus and retract tentacles to survive short exposures to air.
* **Kelp Forests (Subtidal):** Use gas-filled **pneumatocysts** to stay buoyant and reach light. 

### Lecture 14: Deep Sea Whale Falls
When whales die and sink to the aphotic deep sea, they create a 3-stage ecosystem:
1. **Scavenger Stage:** Sleeper sharks, hagfish.
2. **Opportunistic Stage:** Crabs, polychaete worms feeding on sediment biomass.
3. **Sulfophilic Stage:** Chemosynthetic bacteria use bone lipids to make hydrogen sulfide, supporting tubeworms for up to 50 years!
        """,
        "math_lesson": """
**📐 Concept Practice: Habitat Limits**
*Question:* A tide pool organism is found only in the High Tide zone. If you move it to the Low Tide zone, it gets eaten immediately. If you move it above the Spray Zone, it dries out and dies. 
*Rule Check:* Its upper limit is physical (desiccation), and its lower limit is biological (predation).
        """,
        "vocab": {
            "Desiccation": "Extreme dryness; the primary physical threat in the upper intertidal zone.",
            "Pneumatocyst": "Gas-filled bladders in kelp that provide buoyancy.",
            "Chemosynthesis": "Biological conversion of carbon molecules/nutrients into organic matter using the oxidation of inorganic molecules (like hydrogen sulfide) rather than sunlight."
        },
        "quiz": [
            {"q": "Why isn't the California mussel very abundant below the middle intertidal zone?", "options": ["It gets washed away by waves", "It avoids its predator, the sea star", "It needs exposure to air to breathe"], "a": "It avoids its predator, the sea star"},
            {"q": "What factor generally sets the UPPER limit of where an intertidal species can live?", "options": ["Biological factors (predation)", "Physical factors (desiccation/exposure)", "Food availability"], "a": "Physical factors (desiccation/exposure)"},
            {"q": "How does the large limpet (Acmaea) avoid desiccation?", "options": ["It hides in kelp forests", "It uses a strong foot muscle to suction tightly to rocks", "It drinks massive amounts of seawater"], "a": "It uses a strong foot muscle to suction tightly to rocks"}
        ]
    },
    {
        "module": 6,
        "title": "Module 7: Resources, Ocean Change & Governance",
        "lesson": """
### Lecture 15: Marine Resources & Fishing
Human demand for seafood is high. A massive issue with commercial fishing is **Bycatch**—the capture of non-target organisms like dolphins, turtles, and unwanted fish. Over half of human seafood now comes from Aquaculture (fish farming).

### Lecture 16: Ocean Change
Excess Atmospheric CO2 causes two major problems for the ocean:
1. **Ocean Warming:** Causes sea-level rise and coral bleaching (corals expel their symbiotic zooxanthellae when stressed).
2. **Ocean Acidification:** CO2 forms carbonic acid, dropping the pH. This dissolves the calcium carbonate shells of organisms like pteropods and corals. 
* **Plastics:** Accumulate in major gyres due to Ekman transport and geostrophic currents (e.g., the Great Pacific Garbage Patch).

### Lecture 17: Governance (UNCLOS)
The United Nations Convention on the Law of the Sea defines maritime boundaries:
* **Territorial Waters:** Up to 12 nautical miles from shore.
* **Exclusive Economic Zone (EEZ):** Up to 200 nautical miles. The host nation controls all resource exploitation (fishing/mining) here.
* **High Seas:** Beyond 200 nautical miles. International waters.
        """,
        "math_lesson": """
**📐 Concept Practice: The Final Jeopardy Fossil**
*Final Review Fact:* Near the end of the Miocene epoch, the cold, nutrient-rich California Current caused massive biological productivity. The siliceous remains of diatoms built up heavily.
*Result:* The sedimentary rock formed from these California sediments is **Diatomite**.
        """,
        "vocab": {
            "Bycatch": "The unwanted fish and marine creatures caught during commercial fishing.",
            "Ocean Acidification": "Decreasing pH of ocean waters due to absorption of excess CO2, threatening calcareous organisms.",
            "EEZ": "Exclusive Economic Zone; a 200-nautical-mile zone where a coastal nation has jurisdiction over natural resources."
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
    st.write("Read the comprehensive lecture & lab materials below. Be sure to practice the math concepts, then pass the checkpoint quiz to unlock the next module! 🐢")
    
    # Using st.info for a beautiful, safe UI box that avoids black background rendering errors
    st.info(current_module['lesson'])
    
    # Render Math Section safely
    st.warning(current_module['math_lesson'])
    
    st.markdown("---")
    st.subheader("📝 Checkpoint Quiz")
    st.caption("You must answer all questions correctly to proceed!")
    
    # Render Quiz
    quiz_data = current_module["quiz"]
    user_answers = []
    
    with st.container():
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
