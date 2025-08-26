import streamlit as st

#peridic dictionary.

elements = {
    1: {"symbol": "H", "name": "Hydrogen", "atomic_weight": 1.008, "group": 1, "period": 1, "radioactive_state": "no", "category": "non-metal"},
    2: {"symbol": "He", "name": "Helium", "atomic_weight": 4.0026, "group": 18, "period": 1, "radioactive_state": "no", "category": "noble gas"},
    3: {"symbol": "Li", "name": "Lithium", "atomic_weight": 6.94, "group": 1, "period": 2, "radioactive_state": "no", "category": "alkali metal"},
    4: {"symbol": "Be", "name": "Beryllium", "atomic_weight": 9.0122, "group": 2, "period": 2, "radioactive_state": "no", "category": "alkaline earth metal"},
    5: {"symbol": "B", "name": "Boron", "atomic_weight": 10.81, "group": 13, "period": 2, "radioactive_state": "no", "category": "metalloid"},
    6: {"symbol": "C", "name": "Carbon", "atomic_weight": 12.011, "group": 14, "period": 2, "radioactive_state": "no", "category": "non-metal"},
    7: {"symbol": "N", "name": "Nitrogen", "atomic_weight": 14.007, "group": 15, "period": 2, "radioactive_state": "no", "category": "non-metal"},
    8: {"symbol": "O", "name": "Oxygen", "atomic_weight": 15.999, "group": 16, "period": 2, "radioactive_state": "no", "category": "non-metal"},
    9: {"symbol": "F", "name": "Fluorine", "atomic_weight": 18.998, "group": 17, "period": 2, "radioactive_state": "no", "category": "halogen"},
    10: {"symbol": "Ne", "name": "Neon", "atomic_weight": 20.180, "group": 18, "period": 2, "radioactive_state": "no", "category": "noble gas"},
    11: {"symbol": "Na", "name": "Sodium", "atomic_weight": 22.990, "group": 1, "period": 3, "radioactive_state": "no", "category": "alkali metal"},
    12: {"symbol": "Mg", "name": "Magnesium", "atomic_weight": 24.305, "group": 2, "period": 3, "radioactive_state": "no", "category": "alkaline earth metal"},
    13: {"symbol": "Al", "name": "Aluminium", "atomic_weight": 26.982, "group": 13, "period": 3, "radioactive_state": "no", "category": "metal"},
    14: {"symbol": "Si", "name": "Silicon", "atomic_weight": 28.085, "group": 14, "period": 3, "radioactive_state": "no", "category": "metalloid"},
    15: {"symbol": "P", "name": "Phosphorus", "atomic_weight": 30.974, "group": 15, "period": 3, "radioactive_state": "no", "category": "non-metal"},
    16: {"symbol": "S", "name": "Sulfur", "atomic_weight": 32.06, "group": 16, "period": 3, "radioactive_state": "no", "category": "non-metal"},
    17: {"symbol": "Cl", "name": "Chlorine", "atomic_weight": 35.45, "group": 17, "period": 3, "radioactive_state": "no", "category": "halogen"},
    18: {"symbol": "Ar", "name": "Argon", "atomic_weight": 39.948, "group": 18, "period": 3, "radioactive_state": "no", "category": "noble gas"},
    19: {"symbol": "K", "name": "Potassium", "atomic_weight": 39.098, "group": 1, "period": 4, "radioactive_state": "no", "category": "alkali metal"},
    20: {"symbol": "Ca", "name": "Calcium", "atomic_weight": 40.078, "group": 2, "period": 4, "radioactive_state": "no", "category": "alkaline earth metal"},
    21: {"symbol": "Sc", "name": "Scandium", "atomic_weight": 44.956, "group": 3, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    22: {"symbol": "Ti", "name": "Titanium", "atomic_weight": 47.867, "group": 4, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    23: {"symbol": "V", "name": "Vanadium", "atomic_weight": 50.942, "group": 5, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    24: {"symbol": "Cr", "name": "Chromium", "atomic_weight": 52.03, "group": 6, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    25: {"symbol": "Mn", "name": "Manganese", "atomic_weight": 54.938, "group": 7, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    26: {"symbol": "Fe", "name": "Iron", "atomic_weight": 55.845, "group": 8, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    27: {"symbol": "Co", "name": "Cobalt", "atomic_weight": 58.933, "group": 9, "period": 4, "radioactive_state": "yes", "category": "transition metal"},
    28: {"symbol": "Ni", "name": "Nickel", "atomic_weight": 58.693, "group": 10, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    29: {"symbol": "Cu", "name": "Copper", "atomic_weight": 63.546, "group": 11, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    30: {"symbol": "Zn", "name": "Zinc", "atomic_weight": 65.546, "group": 12, "period": 4, "radioactive_state": "no", "category": "transition metal"},
    31: {"symbol": "Ga", "name": "Gallium", "atomic_weight": 69.723, "group": 13, "period": 4, "radioactive_state": "no", "category": "metal"},
    32: {"symbol": "Ge", "name": "Germanium", "atomic_weight": 72.63, "group": 14, "period": 4, "radioactive_state": "no", "category": "metalloid"},
    33: {"symbol": "As", "name": "Arsenic", "atomic_weight": 74.922, "group": 15, "period": 4, "radioactive_state": "no", "category": "metalloid"},
    34: {"symbol": "Se", "name": "Selenium", "atomic_weight": 78.971, "group": 16, "period": 4, "radioactive_state": "no", "category": "non-metal"},
    35: {"symbol": "Br", "name": "Bromine", "atomic_weight": 79.904, "group": 17, "period": 4, "radioactive_state": "no", "category": "halogen"},
    36: {"symbol": "Kr", "name": "Krypton", "atomic_weight": 83.798, "group": 18, "period": 4, "radioactive_state": "no", "category": "noble gas"},
    37: {"symbol": "Rb", "name": "Rubidium", "atomic_weight": 85.468, "group": 1, "period": 5, "radioactive_state": "no", "category": "alkali metal"},
    38: {"symbol": "Sr", "name": "Strontium", "atomic_weight": 87.62, "group": 2, "period": 5, "radioactive_state": "no", "category": "alkaline earth metal"},
    39: {"symbol": "Y", "name": "Yttrium", "atomic_weight": 88.906, "group": 3, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    40: {"symbol": "Zr", "name": "Zirconium", "atomic_weight": 91.224, "group": 4, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    41: {"symbol": "Nb", "name": "Niobium", "atomic_weight": 92.906, "group": 5, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    42: {"symbol": "Mo", "name": "Molybdenum", "atomic_weight": 95.95, "group": 6, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    43: {"symbol": "Tc", "name": "Technetium", "atomic_weight": 98, "group": 7, "period": 5, "radioactive_state": "yes", "category": "transition metal"},
    44: {"symbol": "Ru", "name": "Ruthenium", "atomic_weight": 101.07, "group": 8, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    45: {"symbol": "Rh", "name": "Rhodium", "atomic_weight": 102.91, "group": 9, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    46: {"symbol": "Pd", "name": "Palladium", "atomic_weight": 106.42, "group": 10, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    47: {"symbol": "Ag", "name": "Silver", "atomic_weight": 107.868, "group": 11, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    48: {"symbol": "Cd", "name": "Cadmium", "atomic_weight": 112.414, "group": 12, "period": 5, "radioactive_state": "no", "category": "transition metal"},
    49: {"symbol": "In", "name": "Indium", "atomic_weight": 114.818, "group": 13, "period": 5, "radioactive_state": "no", "category": "metal"},
    50: {"symbol": "Sn", "name": "Tin", "atomic_weight": 118.71, "group": 14, "period": 5, "radioactive_state": "no", "category": "metal"}
}

#colours

category_colors = {
    "non-metal": "#a0d8ef",
    "noble gas": "#ffd1dc",
    "alkali metal": "#ffb347",
    "alkaline earth metal": "#77dd77",
    "metalloid": "#cbaacb",
    "metal": "#fdfd96",
    "transition metal": "#aec6cf",
    "halogen": "#ff6961"
}

# --------------------------
# Helper Functions
# --------------------------
def search_element(query):
    query = query.strip().lower()
    for atomic_number, data in elements.items():
        if (
            query == str(atomic_number) or
            query == data["name"].lower() or
            query == data["symbol"].lower()
        ):
            return atomic_number, data
    return None, None

def autocomplete_suggestions(query):
    query = query.strip().lower()
    suggestions = []
    for atomic_number, data in elements.items():
        if query in data["name"].lower() or query in data["symbol"].lower():
            suggestions.append(f"{data['name']} ({data['symbol']})")
    return suggestions

# --------------------------
# Streamlit App UI
# --------------------------
st.set_page_config(page_title="Periodic Table Explorer", layout="centered")
st.title("🔬 Periodic Table Explorer")

query = st.text_input("Search by name, symbol, or atomic number:")

if query:
    atomic_number, element_data = search_element(query)
    if element_data:
        bg_color = category_colors.get(element_data['category'], "#FFFFFF")
        st.markdown(
            f"<div style='padding: 1em; border-radius: 10px; background-color: {bg_color};'>"
            f"<h3>{element_data['name']} ({element_data['symbol']})</h3>"
            f"<p><strong>Atomic Number:</strong> {atomic_number}</p>"
            f"<p><strong>Atomic Weight:</strong> {element_data['atomic_weight']}</p>"
            f"<p><strong>Group:</strong> {element_data['group']}</p>"
            f"<p><strong>Period:</strong> {element_data['period']}</p>"
            f"<p><strong>Radioactive:</strong> {element_data['radioactive_state'].title()}</p>"
            f"<p><strong>Category:</strong> {element_data['category'].title()}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Element not found. Please try another query.")

# Show suggestions
if query:
    suggestions = autocomplete_suggestions(query)
    if suggestions:
        st.markdown("**Suggestions:**")
        st.write(", ".join(suggestions))


