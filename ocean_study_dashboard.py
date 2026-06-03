import streamlit as st
import random

# ==========================================
# PAGE CONFIGURATION & SAFE OCEAN CSS THEME 🌊
# ==========================================
# Fixing the legibility issues: forcing dark, readable text on the 
# warning (math check), info (lesson) boxes, and specifically fixing the radio buttons (quiz text).
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
    
    /* Ensure general text is always readable */
    .stMarkdown p, .stMarkdown li {
        color: #004D40 !important;
        font-size: 16px;
    }
    
    /* ==========================================
       FIX 1: MATH CHECK & LESSON BOXES 
       ========================================== */
    /* Forces all text inside st.warning (yellow) and st.info (blue) to be a dark teal */
    [data-testid="stAlert"] * {
        color: #003333 !important; /* Darker color of the background, highly legible! */
    }
    
    /* ==========================================
       FIX 2: QUIZ RADIO BUTTONS (Text Visibility Fix)
       ========================================== */
    /* Light blue background for the quiz box, with dark text */
    .stRadio > div[role="radiogroup"] {
        background-color: #B2EBF2 !important; /* Light blue background */
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #00838F; /* Dark cyan border */
    }
    
    /* Force ALL text inside the radio group (labels, spans, paragraphs) to be dark */
    .stRadio > div[role="radiogroup"] * {
        color: #003333 !important; 
        font-weight: 500 !important;
    }
    
    /* Force the actual question text above the radio buttons to be dark */
    .stRadio > label, .stRadio > label * {
        color: #004D40 !important;
        font-size: 18px !important;
        font-weight: 800 !important;
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
# COURSE DATA: LOGICALLY ALIGNED MODULES (1 Lab + 2 Lectures per Module)
# ==========================================
course_data = [
    {
        "module": 0,
        "title": "Module 1: Lab 1 & Lectures 1-2 (Intro, Maps, Ocean Anatomy)",
        "lesson": """
### Lecture 1: Introduction to Oceanography
The ocean covers **70.8%** of the Earth, and over 40% of the world's population lives within 150 km of it. Early ocean science dates back to Aristotle (~350 BC). The first great ocean exploration expeditions were Charles Darwin's voyage on the HMS Beagle (1830s) and the Challenger Expedition (1872-1876).

### Lecture 2: Anatomy of the Oceans
Earth's elevations have a **bimodal distribution**: continents average 840 meters above sea level, and oceans average 3,700 meters below.
* **Continental Crust:** Made of granite, less dense (2.7 g/cm³), and thicker.
* **Oceanic Crust:** Made of basalt, more dense (3.0 g/cm³), and thinner.
* **Continental Margins:** * *Passive (Atlantic-type):* Broad, flat shelves without trenches.
  * *Active (Pacific-type):* Narrow shelves adjacent to deep-sea trenches (e.g., Peru-Chile Trench near the Andes Mountains).

### Lab 1: Maps, Cross-Sections & Graphs
* **Interpolation vs. Extrapolation:** When plotting data on a graph, predicting values *between* plotted points is called **interpolation**. Predicting values *outside* the range of plotted points is **extrapolation**.
* **Contours:** Lines that connect data of equal value (e.g., isotherms for temperature, isobaths for depth). On a bathymetry map, if contours are spaced **close together**, it indicates a rapid change in elevation (a steep slope). An underwater ridge points **downhill**.
        """,
        "math_lesson": """
**📐 Math Practice: Vertical Exaggeration**
Maps often stretch the vertical axis to make topographic features visible.
* **Formula:** `Vertical Exaggeration (VE) = Vertical Scale / Horizontal Scale`
* *Example Calculation:* If the vertical scale is 4.9 cm / 6 km (which is ~0.82 cm/km) and the horizontal scale is 14.2 cm / 800 km (which is ~0.0177 cm/km), the VE is roughly 46x. 
* *Simpler Example:* If vertical scale is 2 cm/km and horizontal is 0.1 cm/km, then `VE = 2 / 0.1 = 20x`.
        """,
        "vocab": {
            "Interpolation": "Predicting values between plotted data points on a graph.",
            "Extrapolation": "Predicting values outside the range of plotted points on a graph.",
            "Active Margin": "A continental margin with a narrow shelf and a deep-sea trench."
        },
        "quiz_bank": [
            {"q": "If the vertical scale of a map is 4 cm/km and the horizontal scale is 0.5 cm/km, what is the Vertical Exaggeration?", "options": ["8x", "2x", "4.5x"], "a": "8x"},
            {"q": "If contours on a bathymetric map are spaced very close together, this indicates:", "options": ["A flat abyssal plain", "A rapid change in elevation (steep slope)", "A deep sea trench specifically"], "a": "A rapid change in elevation (steep slope)"},
            {"q": "Predicting values *outside* the range of plotted points on a graph is called:", "options": ["Interpolation", "Extrapolation", "Shoaling"], "a": "Extrapolation"},
            {"q": "What is the average density of the continental crust?", "options": ["3.0 g/cm³", "3.3 g/cm³", "2.7 g/cm³"], "a": "2.7 g/cm³"},
            {"q": "Which ocean generally receives the most sediment from rivers due to its passive margins?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean"], "a": "Atlantic Ocean"},
            {"q": "What mountain range is found immediately landward (eastward) of the Peru-Chile Trench?", "options": ["The Himalayas", "The Alps", "The Andes Mountains"], "a": "The Andes Mountains"}
        ]
    },
    {
        "module": 1,
        "title": "Module 2: Lab 2 & Lectures 3-4 (Physiography, Isostasy, Tectonics, Sediments)",
        "lesson": """
### Lecture 3: Plate Tectonics
The lithosphere is divided into ~14 major plates moving over the plastic asthenosphere.
* **Divergent Boundaries:** Plates move apart. Creates Mid-Ocean Ridges (MORs) with high heat flow and volcanic activity.
* **Convergent Boundaries:** Plates collide. Old seafloor is destroyed via **subduction** at deep-sea trenches.
* **Transform Boundaries:** Plates slide past each other horizontally.

### Lecture 4: Marine Sediments
Sediments are classified genetically:
* **Terrigenous:** Derived from land weathering. Found near coasts.
* **Biogenic:** From remains of marine life (Calcareous ooze from Foraminifera; Siliceous ooze from Diatoms/Radiolarians).
* **Chemogenic (Hydrogenous):** Precipitated directly from seawater (e.g., Manganese nodules).

### Lab 2: Physiography of Ocean Basins & Isostasy
* **Isostasy:** The gravitational equilibrium between Earth's crust and mantle. The crust "floats" on the denser mantle at an elevation depending on its thickness and density. Because continental crust is less dense (2.7 g/cm³) than oceanic crust (3.0 g/cm³), it floats higher, creating the bimodal elevation of Earth!
        """,
        "math_lesson": """
**📐 Math Practice: Mass, Density, and Volume**
1. **Formula:** `Mass = Density × Volume`
* *Example:* A piece of basalt (oceanic crust) has a density of 3.0 g/cm³. If you put it in a beaker and it displaces 4 mL (4 cm³) of water, what is its mass?
* `Mass = 3.0 g/cm³ × 4 cm³ = 12 grams`.
        """,
        "vocab": {
            "Isostasy": "Gravitational equilibrium between Earth's crust and mantle allowing the crust to 'float'.",
            "Subduction": "The downward movement of an oceanic plate into the mantle beneath another plate.",
            "Chemogenic Sediment": "Sediment precipitated directly from dissolved minerals in water (e.g., manganese nodules)."
        },
        "quiz_bank": [
            {"q": "A piece of basalt (density 3.0 g/cm³) displaces 5 mL of water. What is its mass?", "options": ["1.6 g", "15 g", "8 g"], "a": "15 g"},
            {"q": "Mid-Ocean Ridges (like the Mid-Atlantic Ridge) are an example of this kind of plate boundary:", "options": ["Divergent", "Convergent", "Transform"], "a": "Divergent"},
            {"q": "A manganese nodule is an example of what kind of sediment?", "options": ["Biogenic", "Terrigenous", "Chemogenic (Hydrogenous)"], "a": "Chemogenic (Hydrogenous)"},
            {"q": "Which process destroys old oceanic lithosphere?", "options": ["Subduction", "Seafloor Spreading", "Isostasy"], "a": "Subduction"},
            {"q": "Why does the continental crust float higher on the mantle than the oceanic crust?", "options": ["It is thinner", "It is less dense (2.7 g/cm³)", "It has more water on it"], "a": "It is less dense (2.7 g/cm³)"},
            {"q": "Which type of biogenic sediment is made by Diatoms and Radiolarians?", "options": ["Calcareous Ooze", "Siliceous Ooze", "Terrigenous Clay"], "a": "Siliceous Ooze"}
        ]
    },
    {
        "module": 2,
        "title": "Module 3: Lab 3 & Lectures 5-6 (Hotspots, Seawater Chemistry & Stratification)",
        "lesson": """
### Lab 3: Plate Tectonics & Hotspots
While most volcanic activity happens at plate boundaries, **Mantle Plumes (Hotspots)** produce stationary sources of volcanism for millions of years. As the lithospheric plate moves over the hotspot, it creates an island chain (like the Hawaiian Islands). The age of the islands increases as you move further away from the active hotspot.

### Lecture 5: Seawater Chemistry
Water is unique due to **hydrogen bonding**, giving it a high heat capacity and making ice less dense than liquid water.
* **Salinity:** Average ocean salinity is 35 PSU. It decreases by precipitation/melting and increases by evaporation.
* **CO2 in the Ocean:** Cold, deep water at high latitudes absorbs the highest amounts of CO2 because CO2 solubility increases in cold water. The ocean is buffered by **Bicarbonate (HCO3-)**.

### Lecture 6: Ocean Stratification
Density in the ocean is controlled by Temperature and Salinity.
* **Thermocline:** Rapid change in temperature.
* **Halocline:** Rapid change in salinity.
* **Pycnocline:** Rapid change in density.
Strong density stratification makes vertical ocean mixing go **slower**. 
        """,
        "math_lesson": """
**📐 Math Practice: Plate Velocity**
* **Formula:** `Velocity = Distance / Time`
* *Example:* The distance from the island of Hawaii to Pearl Reef is 2,000 km (200,000,000 cm). Pearl Reef is 20 million years old. 
* `Velocity = 200,000,000 cm / 20,000,000 yrs = 10 cm/yr`.
        """,
        "vocab": {
            "Mantle Plume (Hotspot)": "A stationary source of magma rising from the deep mantle that creates island chains as plates move over it.",
            "Hydrogen Bonding": "The chemical bond in water giving it high heat capacity and allowing ice to float.",
            "Pycnocline": "The region of rapid density change in the ocean."
        },
        "quiz_bank": [
            {"q": "An island is 3,000 km (300,000,000 cm) away from a hotspot and is 30 million years old. What is the plate velocity?", "options": ["10 cm/yr", "1 cm/yr", "30 cm/yr"], "a": "10 cm/yr"},
            {"q": "The Hawaiian Island chain is an example of what kind of tectonic feature?", "options": ["Convergent Boundary", "Transform Fault", "Hotspot / Mantle Plume"], "a": "Hotspot / Mantle Plume"},
            {"q": "At what latitudes are the highest amounts of surface water dissolved CO2 observed?", "options": ["The Tropics / Equator", "High latitudes / The poles", "Mid-latitudes"], "a": "High latitudes / The poles"},
            {"q": "What acts as a buffer in the ocean to keep it from becoming too acidic/basic?", "options": ["Silica", "Sodium Chloride", "Bicarbonate (HCO3-)"], "a": "Bicarbonate (HCO3-)"},
            {"q": "Does strong density stratification make vertical ocean mixing go faster or slower?", "options": ["Faster", "Slower", "No effect"], "a": "Slower"},
            {"q": "What is the name of the region of rapid density change in the ocean?", "options": ["Thermocline", "Halocline", "Pycnocline"], "a": "Pycnocline"}
        ]
    },
    {
        "module": 3,
        "title": "Module 4: Lab 4 & Lectures 7-8 (Sediment Depth, Wind & Gravity Circulation)",
        "lesson": """
### Lab 4: Marine Sediments & The CCD
The **Calcite Compensation Depth (CCD)** is the depth where calcareous shells dissolve because deep water is colder, higher pressure, and more acidic. The CCD is deepest in warm, low latitudes. Therefore, calcareous oozes dissolve *below* the CCD, leaving only siliceous oozes or abyssal clays in the deep basins.

### Lecture 7: Circulation 1 (Wind-Driven)
* **The Coriolis Effect:** Deflects moving fluids to the **RIGHT** in the Northern Hemisphere and **LEFT** in the Southern Hemisphere.
* **Ekman Transport:** The net motion of water at a 90° angle to the prevailing wind direction. This builds up pressure gradients that create Geostrophic Currents and massive gyres.
* **Western Boundary Currents:** Fast, deep currents flowing along the eastern coasts of continents (e.g., the Gulf Stream).

### Lecture 8: Circulation 2 (Thermohaline)
Deep-ocean circulation (The Great Conveyor Belt) is driven by density differences (temperature and salinity).
* The two major regions where deep water forms are the **North Atlantic (NADW)** and near **Antarctica (AABW)**.
        """,
        "math_lesson": """
**📐 Math Practice: Settling Time (Stoke's Law)**
* **Concept:** Settling time *decreases* as grain size *increases*. 
* *Example:* A large sand grain (0.1 cm) settles 1 meter in about 5-10 seconds. However, a tiny clay or silt particle (0.001 cm) falls so slowly it can take 6 to 58 days to reach the deep ocean floor!
        """,
        "vocab": {
            "CCD (Calcite Compensation Depth)": "The depth below which calcareous shells dissolve and are not preserved in sediments.",
            "Ekman Transport": "Net motion of water 90 degrees to the wind direction due to the Coriolis effect.",
            "Thermohaline Circulation": "Deep-ocean circulation driven by temperature and salinity density gradients."
        },
        "quiz_bank": [
            {"q": "According to settling rules (Stoke's Law), which particle will take the LONGEST time to reach the ocean floor?", "options": ["A large sand grain", "A medium silt grain", "A tiny clay particle"], "a": "A tiny clay particle"},
            {"q": "Which biogenic sediment is likely to be found on the deep abyssal plain BELOW the CCD?", "options": ["Calcareous Ooze", "Siliceous Ooze", "Manganese Nodules"], "a": "Siliceous Ooze"},
            {"q": "The net motion of water at a 90° angle to the prevailing wind direction is known as:", "options": ["Geostrophic Flow", "Ekman Transport", "Coriolis Force"], "a": "Ekman Transport"},
            {"q": "In the Northern Hemisphere, the Coriolis effect deflects moving water to the:", "options": ["Right", "Left", "Equator"], "a": "Right"},
            {"q": "Name the two primary regions of deep water formation.", "options": ["North Atlantic and Antarctica", "Equator and Pacific", "Mediterranean and Gulf of Mexico"], "a": "North Atlantic and Antarctica"},
            {"q": "What is the general name of the type of current that runs fast and deep along the eastern coast of continents (like the Gulf Stream)?", "options": ["Eastern Boundary Current", "Western Boundary Current", "Equatorial Current"], "a": "Western Boundary Current"}
        ]
    },
    {
        "module": 4,
        "title": "Module 5: Lab 5 & Lectures 9-10 (Seawater Chemistry, Waves/Tides, Productivity 1)",
        "lesson": """
### Lab 5: The Physical and Chemical Properties of Seawater
The pH scale is logarithmic: every 1 step on the pH scale is a 10x change in H+ ions. The ocean's average pH is about 8.0. 
* **Residence Time:** The average time an element stays dissolved in the ocean.

### Lecture 9: Waves and Tides
* **Waves:** Energy moving through water. Speed = Wavelength × Frequency. 
* **Tsunamis:** Caused by earthquakes/landslides. They have small wave heights offshore but massive wavelengths. They grow huge when they hit shallow water (shoaling).
* **Tides:** Driven by the Moon and Sun's gravity. **Spring Tides** (biggest range) happen during Full/New moons. **Neap Tides** (moderate range) happen at half moons.

### Lecture 10: Productivity 1
Marine food webs start with **Phytoplankton** (autotrophs like Diatoms and Dinoflagellates).
* **Euphotic Zone:** Surface to critical depth. Photosynthesis dominates.
* **Compensation Depth:** The exact depth where a phytoplankton's Photosynthesis output equals its Respiration consumption.
        """,
        "math_lesson": """
**📐 Math Practice: Residence Time & pH**
1. **Residence Time:** `Mass in Ocean / River Flux per year`
   * *Example:* If ocean mass is 8 x 10^20 g, and flux is 4 x 10^10 g/yr, Time = (8 x 10^20) / (4 x 10^10) = 2 x 10^10 yrs.
2. **pH Scaling:** 1 step = 10x.
   * *Example:* How much more acidic is pH 3 than pH 6? 6 - 3 = 3 steps. 10 × 10 × 10 = 1,000x.
        """,
        "vocab": {
            "Residence Time": "The average amount of time an atom/ion stays dissolved in the ocean.",
            "Spring Tide": "Tides with the largest range, occurring during new and full moons.",
            "Compensation Depth": "Depth where photosynthesis output equals respiration consumption."
        },
        "quiz_bank": [
            {"q": "If the total mass of an element in the ocean is 8 x 10^20 g, and the river flux is 4 x 10^10 g/yr, what is the residence time?", "options": ["2 x 10^10 yrs", "4 x 10^10 yrs", "2 x 10^5 yrs"], "a": "2 x 10^10 yrs"},
            {"q": "How many times larger is the H+ concentration in a solution with pH 3 compared to pH 6?", "options": ["30x", "300x", "1,000x"], "a": "1,000x"},
            {"q": "During which moon phases do Spring Tides (largest tidal range) occur?", "options": ["First and third quarter moons", "New and full moons", "Only full moons"], "a": "New and full moons"},
            {"q": "Which of the following is an example of phytoplankton?", "options": ["Diatoms", "Copepods", "Krill"], "a": "Diatoms"},
            {"q": "What defines the Euphotic zone?", "options": ["It is the zone where respiration is highest", "It is where photosynthesis dominates", "It is completely dark"], "a": "It is where photosynthesis dominates"},
            {"q": "At the compensation depth, what two processes are perfectly equal?", "options": ["Evaporation and Precipitation", "Photosynthesis and Respiration", "Sinking and Upwelling"], "a": "Photosynthesis and Respiration"}
        ]
    },
    {
        "module": 5,
        "title": "Module 6: Lab 6 & Lectures 11-12 (Circulation Review, Productivity 2, Remineralization)",
        "lesson": """
### Lab 6: Ocean Circulation (Recap & Practice)
Density stratification acts as a barrier in the ocean. Surface currents (driven by Ekman transport) struggle to mix vertically with dense deep water across the pycnocline. Melting ice sheets decrease salinity and density, slowing down thermohaline circulation!

### Lecture 11: Productivity 2 (Nutrients)
Phytoplankton need nutrients. Macro-nutrients include Nitrogen, Phosphorous, and Silica. In the Southern Ocean, the limiting nutrient is actually a trace metal: **Iron**.
* **The Redfield Ratio:** The atomic ratio of Carbon, Nitrogen, and Phosphorus found universally in phytoplankton is **106 C : 16 N : 1 P**.

### Lecture 12: Remineralization & The Biological Pump
* **Biological Pump:** Plankton absorb atmospheric CO2, die, and sink as "marine snow." 
* As they sink, saprotrophic bacteria consume them (remineralization). This uses up Oxygen and releases CO2. In highly productive upwelling regions, this rapid decay consumes so much oxygen it creates **Oxygen Minimum Zones (OMZ)**.
        """,
        "math_lesson": """
**📐 Math Practice: The Redfield Ratio & Circulation Vectors**
1. **Redfield Ratio Applications:** `106 C : 16 N : 1 P`
   * *Example:* If a phytoplankton bloom consumes 32 units of Nitrogen, how many units of Phosphorus did it consume? Since N:P is 16:1, consuming 32 N (which is 16 × 2) means it consumed 2 units of P.
2. **Coriolis Vectors:** If wind blows North in the Northern Hemisphere, Ekman transport moves water 90° to the Right (East).
        """,
        "vocab": {
            "Redfield Ratio": "The 106:16:1 ratio of Carbon, Nitrogen, and Phosphorous in marine plankton.",
            "Biological Pump": "The biologically driven sequestration of carbon from the atmosphere to the deep sea.",
            "Oxygen Minimum Zone (OMZ)": "A zone where oxygen is severely depleted due to high rates of bacterial remineralization of sinking organic matter."
        },
        "quiz_bank": [
            {"q": "What is the limiting nutrient for phytoplankton in the Southern Ocean?", "options": ["Nitrogen", "Iron", "Carbon"], "a": "Iron"},
            {"q": "What represents the Redfield Ratio of C : N : P?", "options": ["106 : 16 : 1", "1 : 16 : 106", "50 : 10 : 1"], "a": "106 : 16 : 1"},
            {"q": "In nutrient-rich upwelling regions, sinking organic carbon is degraded so rapidly by bacteria that it creates:", "options": ["A high-oxygen euphotic zone", "An Oxygen Minimum Zone (OMZ)", "Calcareous Oozes"], "a": "An Oxygen Minimum Zone (OMZ)"},
            {"q": "If part of an ice sheet melts into the ocean, what effect will this have on the seawater's density and circulation?", "options": ["Density decreases, deep currents slow down", "Density increases, mixing goes faster", "No change"], "a": "Density decreases, deep currents slow down"},
            {"q": "In order to maintain balance, dense water masses sinking into the ocean basins must cause less dense water to rise elsewhere. What is this process called?", "options": ["Subduction", "Upwelling", "Shoaling"], "a": "Upwelling"},
            {"q": "If wind blows purely South in the Southern Hemisphere, Ekman transport moves water 90° to the:", "options": ["Left (East)", "Right (West)", "North"], "a": "Left (East)"}
        ]
    },
    {
        "module": 6,
        "title": "Module 7: Lab 7 & Lectures 13-14 (Food Chains, Habitats, Deep Sea)",
        "lesson": """
### Lab 7: Ocean Food Chains
Phytoplankton are the original source of food for nearly all marine organisms. **Upwelling currents** are vital for replenishing nutrients (like nitrogen and phosphorus) from the deep ocean to the surface euphotic zone so phytoplankton can thrive. 

### Lecture 13: Marine Habitats 1 (Kelp & Coral)
* **Kelp Forests:** Use gas-filled **pneumatocysts** to stay buoyant and reach light. 
* **Coral Reefs:** Corals live in symbiosis with **zooxanthellae** (dinoflagellates). Coral bleaching happens when stressed corals expel these algae.

### Lecture 14: Deep Sea Whale Falls
When whales sink to the deep sea, they create a 3-stage ecosystem:
1. **Scavenger Stage:** Sleeper sharks, hagfish.
2. **Opportunistic Stage:** Crabs, polychaete worms.
3. **Sulfophilic Stage:** Chemosynthetic bacteria use bone lipids to make hydrogen sulfide, supporting tubeworms for decades!
        """,
        "math_lesson": """
**📐 Concept Practice: Micro vs Macro Nutrients**
* **Macro-nutrients:** Needed in large amounts (Nitrogen, Phosphorous, Silica).
* **Micro-nutrients:** Needed in trace amounts (Iron, Copper, Selenium).
* *Upwelling* is the physical mechanism that brings these limiting nutrients back to the surface!
        """,
        "vocab": {
            "Pneumatocyst": "Gas-filled bladders in kelp that provide buoyancy.",
            "Zooxanthellae": "Photosynthetic dinoflagellates that live in symbiosis within coral polyps.",
            "Chemosynthesis": "Biological conversion of carbon molecules/nutrients into organic matter using the oxidation of inorganic molecules (like hydrogen sulfide)."
        },
        "quiz_bank": [
            {"q": "Coastal upwelling is vital to ocean food chains because it brings what to the surface?", "options": ["Warm water", "Nutrient-rich deep water", "Oxygenated water"], "a": "Nutrient-rich deep water"},
            {"q": "What purpose does a kelp’s pneumatocyst serve?", "options": ["Reproduction", "Gas-filled bladder for buoyancy", "Extracts salt from the water"], "a": "Gas-filled bladder for buoyancy"},
            {"q": "Coral bleaching is primarily a phenomenon where corals:", "options": ["Turn white from lack of sunlight", "Expel their symbiotic zooxanthellae when stressed", "Absorb too much calcium carbonate"], "a": "Expel their symbiotic zooxanthellae when stressed"},
            {"q": "During the sulfophilic stage of a whale fall, what provides the energy basis for the chemosynthetic ecosystem?", "options": ["Sunlight penetrating the deep sea", "Hydrogen sulfide generated by bacteria", "Phytoplankton raining from above"], "a": "Hydrogen sulfide generated by bacteria"},
            {"q": "Which of the following is considered a micronutrient (trace element) for phytoplankton?", "options": ["Nitrogen", "Iron", "Phosphorus"], "a": "Iron"},
            {"q": "The preserved remains of copepods and dinoflagellates are rarely found in sediments. Why?", "options": ["They never die", "They lack mineral skeletons (made of organic material that decays/is eaten)", "They float forever"], "a": "They lack mineral skeletons (made of organic material that decays/is eaten)"}
        ]
    },
    {
        "module": 7,
        "title": "Module 8: Lab 8 & Lectures 15-17 (Intertidal Zones, Resources, Ocean Change)",
        "lesson": """
### Lab 8: The Intertidal Zone
Zonal distribution is controlled by two main limits:
1. **Upper Limits:** Set by *Physical* factors (desiccation/drying out, waves).
2. **Lower Limits:** Set by *Biological* factors (predation, competition).
* *High/Spray Zone:* Periwinkle snails, limpets (use strong foot muscle to suction to rocks).
* *Middle Zone:* Mussels (avoid the lower zone because of their predator, the sea star!).
* *Lower Zone:* Sea stars, anemones.

### Lecture 15: Marine Resources
**Bycatch** is the capture of non-target organisms like dolphins and turtles during commercial fishing. 

### Lecture 16: Ocean Change
Excess Atmospheric CO2 causes **Ocean Acidification**: CO2 forms carbonic acid, dropping the pH. This dissolves the calcium carbonate shells of organisms like pteropods and corals. 

### Lecture 17: Governance (UNCLOS)
* **Territorial Waters:** Up to 12 nautical miles from shore.
* **Exclusive Economic Zone (EEZ):** Up to 200 nautical miles. The host nation controls all resource exploitation (fishing/mining) here.
        """,
        "math_lesson": """
**📐 Concept Practice: The Final Jeopardy Fossil**
*Final Review Fact:* Near the end of the Miocene epoch, the cold, nutrient-rich California Current caused massive biological productivity. The siliceous remains of diatoms built up heavily.
*Result:* The sedimentary rock formed from these California sediments is **Diatomite**.
        """,
        "vocab": {
            "Desiccation": "Extreme dryness; the primary physical threat in the upper intertidal zone.",
            "Bycatch": "The unwanted fish and marine creatures caught during commercial fishing.",
            "EEZ": "Exclusive Economic Zone; a 200-nautical-mile zone where a coastal nation has jurisdiction over natural resources."
        },
        "quiz_bank": [
            {"q": "Why isn't the California mussel very abundant below the middle intertidal zone?", "options": ["It gets washed away by waves", "It avoids its predator, the sea star", "It needs exposure to air to breathe"], "a": "It avoids its predator, the sea star"},
            {"q": "What factor generally sets the UPPER limit of where an intertidal species can live?", "options": ["Biological factors (predation)", "Physical factors (desiccation/exposure)", "Food availability"], "a": "Physical factors (desiccation/exposure)"},
            {"q": "How does the large limpet (Acmaea) avoid desiccation?", "options": ["It hides in kelp forests", "It uses a strong foot muscle to suction tightly to rocks", "It drinks massive amounts of seawater"], "a": "It uses a strong foot muscle to suction tightly to rocks"},
            {"q": "Which UNCLOS zone gives a nation the right to exploit resources up to 200 nautical miles from its coast?", "options": ["Territorial Waters", "High Seas", "Exclusive Economic Zone (EEZ)"], "a": "Exclusive Economic Zone (EEZ)"},
            {"q": "Ocean acidification primarily threatens marine organisms by:", "options": ["Making the water too hot", "Dissolving their calcium carbonate shells", "Depleting oxygen (OMZ)"], "a": "Dissolving their calcium carbonate shells"},
            {"q": "FINAL JEOPARDY: What type of sedimentary rock formed from Miocene Coastal California sediments due to the cold California Current?", "options": ["Diatomite", "Basalt", "Limestone"], "a": "Diatomite"}
        ]
    }
]

# ==========================================
# SESSION STATE & QUIZ RANDOMIZER LOGIC
# ==========================================
def get_randomized_quiz(module_idx):
    if module_idx < len(course_data):
        return random.sample(course_data[module_idx]["quiz_bank"], 3)
    return []

if 'module_progress' not in st.session_state:
    st.session_state.module_progress = 0

if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = get_randomized_quiz(0)

def advance_module():
    if st.session_state.module_progress < len(course_data) - 1:
        st.session_state.module_progress += 1
        # Generate new random questions for the next module
        st.session_state.current_quiz = get_randomized_quiz(st.session_state.module_progress)
        st.balloons()
    else:
        st.session_state.module_progress = 99 # Code for 100% completion
        st.balloons()

def refresh_quiz():
    # Cycles the questions if the user gets them wrong
    st.session_state.current_quiz = get_randomized_quiz(st.session_state.module_progress)

def reset_course():
    st.session_state.module_progress = 0
    st.session_state.current_quiz = get_randomized_quiz(0)

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
    st.caption("You must answer all questions correctly to proceed! If you get them wrong, a new set of questions will cycle in.")
    
    # Render Randomized Quiz from Session State
    quiz_data = st.session_state.current_quiz
    user_answers = []
    
    with st.container():
        for idx, q_dict in enumerate(quiz_data):
            ans = st.radio(f"**{idx+1}. {q_dict['q']}**", q_dict["options"], index=None, key=f"q_{st.session_state.module_progress}_{q_dict['q']}")
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
                st.error("Oops! One or more answers are incorrect. The questions have cycled. Review the lesson box and try again! 🔄")
                refresh_quiz()
                st.rerun()
