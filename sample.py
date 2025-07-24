import streamlit as st
import pandas as pd
from database import (
    providers_receivers_per_city,
    most_food_provider_type,
    add_food_listing,
    delete_food_listing,
    run_query,
    # ...other functions you need...
)

import pandas as pd
from database import (
    providers_receivers_per_city,
    most_food_provider_type,
    add_food_listing,   
)
# Sidebar Navigation
st.sidebar.title("📚 MENU")
selection = st.sidebar.radio("Go to", [
    "Introduction", "Database Tables", "CRUD Operations", "Analysis", "Thank You"
])

# === Page: Introduction ===
if selection == "Introduction":
    st.title("🍽️ Local Food Wastage Management System")
    st.markdown("""
    This app bridges food **providers** and **receivers** to reduce local food waste.

    ### 🎯 Objectives:
    - Track surplus food
    - Analyze waste trends
    - Optimize food distribution
    """)

# === Page: Database Tables ===
elif selection == "Database Tables":
    st.title("📊 Database Tables")
    table_choice = st.selectbox("Select Table", ["providers", "receivers", "food_listings", "claims"])
    if table_choice:
        df = None
        if table_choice == "providers":
            df = run_query("SELECT * FROM providers")
        elif table_choice == "receivers":
            df = run_query("SELECT * FROM receivers")
        elif table_choice == "food_listings":
            df = run_query("SELECT * FROM food_listings")
        elif table_choice == "claims":
            df = run_query("SELECT * FROM claims")
        if df is not None:
            st.dataframe(df)
    # Use your functions to get dataframes and display

# === Page: CRUD Operations ===
elif selection == "CRUD Operations":
    st.title("🛠️ CRUD Operations")
    

    st.subheader("Add a New Food Listing")
    with st.form("add_food_form"):
        food_id = st.number_input("Food ID", min_value=1)
        food_name = st.text_input("Food Name")
        quantity = st.number_input("Quantity", min_value=1)
        expiry_date = st.date_input("Expiry Date")
        provider_id = st.number_input("Provider ID", min_value=1)
        provider_type = st.text_input("Provider Type")
        location = st.text_input("Location")
        food_type = st.selectbox("Food Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])
        meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])
        submitted = st.form_submit_button("Add Listing")
        if submitted:
            add_food_listing((
                food_id, food_name, quantity, expiry_date,
                provider_id, provider_type, location, food_type, meal_type
            ))
            st.success(f"✅ Added food item: {food_name}")
# ...existing code...
    # Use add_food_listing, delete_food_listing, etc.

# === Page: Analysis ===
elif selection == "Analysis":
    st.subheader("📈 Data Analysis")
    # Use providers_receivers_per_city, most_food_provider_type, etc.

# === Page: Thank You ===
elif selection == "Thank You":
    st.title("🙏 Thank You")
    st.markdown("Thanks for using the Local Food Wastage Management System!")