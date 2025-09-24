import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("naveen_model.joblib")  

# List of locations
locations = [
    'Electronic City Phase II', 'Chikka Tirupathi', 'Uttarahalli',
    'Lingadheeranahalli', 'Kothanur', 'Whitefield', 'Old Airport Road',
    'Rajaji Nagar', 'Marathahalli', 'other', '7th Phase JP Nagar',
    'Gottigere', 'Sarjapur', 'Mysore Road', 'Bisuvanahalli',
    'Raja Rajeshwari Nagar', 'Kengeri', 'Binny Pete', 'Thanisandra',
    'Bellandur', 'Electronic City', 'Ramagondanahalli', 'Yelahanka',
    'Hebbal', 'Kasturi Nagar', 'Kanakpura Road',
    'Electronics City Phase 1', 'Kundalahalli', 'Chikkalasandra',
    'Murugeshpalya', 'Sarjapur  Road', 'HSR Layout', 'Doddathoguru',
    'KR Puram', 'Bhoganhalli', 'Lakshminarayana Pura', 'Begur Road',
    'Varthur', 'Bommanahalli', 'Gunjur', 'Devarachikkanahalli',
    'Hegde Nagar', 'Haralur Road', 'Hennur Road', 'Kothannur',
    'Kalena Agrahara', 'Kaval Byrasandra', 'ISRO Layout',
    'Garudachar Palya', 'EPIP Zone', 'Dasanapura', 'Kasavanhalli',
    'Sanjay nagar', 'Domlur', 'Sarjapura - Attibele Road',
    'Yeshwanthpur', 'Chandapura', 'Nagarbhavi', 'Devanahalli',
    'Ramamurthy Nagar', 'Malleshwaram', 'Akshaya Nagar', 'Shampura',
    'Kadugodi', 'LB Shastri Nagar', 'Hormavu', 'Vishwapriya Layout',
    'Kudlu Gate', '8th Phase JP Nagar', 'Bommasandra Industrial Area',
    'Anandapura', 'Vishveshwarya Layout', 'Kengeri Satellite Town',
    'Kannamangala', 'Hulimavu', 'Mahalakshmi Layout', 'Hosa Road',
    'Attibele', 'CV Raman Nagar', 'Kumaraswami Layout', 'Nagavara',
    'Hebbal Kempapura', 'Vijayanagar', 'Pattandur Agrahara',
    'Nagasandra', 'Kogilu', 'Panathur', 'Padmanabhanagar',
    '1st Block Jayanagar', 'Kammasandra', 'Dasarahalli', 'Magadi Road',
    'Koramangala', 'Dommasandra', 'Budigere', 'Kalyan nagar',
    'OMBR Layout', 'Horamavu Agara', 'Ambedkar Nagar',
    'Talaghattapura', 'Balagere', 'Jigani', 'Gollarapalya Hosahalli',
    'Old Madras Road', 'Kaggadasapura', '9th Phase JP Nagar', 'Jakkur',
    'TC Palaya', 'Giri Nagar', 'Singasandra', 'AECS Layout',
    'Mallasandra', 'Begur', 'JP Nagar', 'Malleshpalya', 'Munnekollal',
    'Kaggalipura', '6th Phase JP Nagar', 'Ulsoor', 'Thigalarapalya',
    'Somasundara Palya', 'Basaveshwara Nagar', 'Bommasandra',
    'Ardendale', 'Harlur', 'Kodihalli', 'Narayanapura',
    'Bannerghatta Road', 'Hennur', '5th Phase JP Nagar', 'Kodigehaali',
    'Billekahalli', 'Jalahalli', 'Mahadevpura', 'Anekal', 'Sompura',
    'Dodda Nekkundi', 'Hosur Road', 'Battarahalli', 'Sultan Palaya',
    'Ambalipura', 'Hoodi', 'Brookefield', 'Yelenahalli', 'Vittasandra',
    '2nd Stage Nagarbhavi', 'Vidyaranyapura', 'Amruthahalli',
    'Kodigehalli', 'Subramanyapura', 'Basavangudi', 'Kenchenahalli',
    'Banjara Layout', 'Kereguddadahalli', 'Kambipura',
    'Banashankari Stage III', 'Sector 7 HSR Layout', 'Rajiv Nagar',
    'Arekere', 'Mico Layout', 'Kammanahalli', 'Banashankari',
    'Chikkabanavar', 'HRBR Layout', 'Nehru Nagar', 'Kanakapura',
    'Konanakunte', 'Margondanahalli', 'R.T. Nagar', 'Tumkur Road',
    'Vasanthapura', 'GM Palaya', 'Jalahalli East', 'Hosakerehalli',
    'Indira Nagar', 'Kodichikkanahalli', 'Varthur Road', 'Anjanapura',
    'Abbigere', 'Tindlu', 'Gubbalala', 'Parappana Agrahara',
    'Cunningham Road', 'Kudlu', 'Banashankari Stage VI', 'Cox Town',
    'Kathriguppe', 'HBR Layout', 'Yelahanka New Town',
    'Sahakara Nagar', 'Rachenahalli', 'Yelachenahalli',
    'Green Glen Layout', 'Thubarahalli', 'Horamavu Banaswadi',
    '1st Phase JP Nagar', 'NGR Layout', 'Seegehalli', 'BEML Layout',
    'NRI Layout', 'ITPL', 'Babusapalaya', 'Iblur Village',
    'Ananth Nagar', 'Channasandra', 'Choodasandra', 'Kaikondrahalli',
    'Neeladri Nagar', 'Frazer Town', 'Cooke Town', 'Doddakallasandra',
    'Chamrajpet', 'Rayasandra', '5th Block Hbr Layout', 'Pai Layout',
    'Banashankari Stage V', 'Sonnenahalli', 'Benson Town',
    '2nd Phase Judicial Layout', 'Poorna Pragna Layout',
    'Judicial Layout', 'Banashankari Stage II', 'Karuna Nagar',
    'Bannerghatta', 'Marsur', 'Bommenahalli', 'Laggere',
    'Prithvi Layout', 'Banaswadi', 'Sector 2 HSR Layout',
    'Shivaji Nagar', 'Badavala Nagar', 'Nagavarapalya', 'BTM Layout',
    'BTM 2nd Stage', 'Hoskote', 'Doddaballapur', 'Sarakki Nagar',
    'Bharathi Nagar', 'HAL 2nd Stage', 'Kadubeesanahalli'
]

# Page Config
st.set_page_config(page_title="🏠 House Price Prediction", page_icon="🏡", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏠 House Price Prediction App</h1>", unsafe_allow_html=True)
st.write("### Select house details to estimate the price")

# Form
with st.form("prediction_form", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        location = st.selectbox("📍 Location", sorted(locations))
        total_sqft = st.number_input("📐 Total Square Feet", min_value=200.0, max_value=10000.0, value=1000.0, step=50.0)

    with col2:
        bath = st.number_input("🛁 Number of Bathrooms", min_value=1, max_value=10, value=2, step=1)
        bhk = st.number_input("🛏️ Number of BHK", min_value=1, max_value=10, value=2, step=1)

    submitted = st.form_submit_button("🔮 Predict Price")

    if submitted:
        input_data = pd.DataFrame([[location, total_sqft, bath, bhk]],
                                  columns=["location", "total_sqft", "bath", "bhk"])
        
        prediction = model.predict(input_data)[0]

        st.markdown(
            f"""
            <div style="background-color:#F4F6F6;padding:20px;border-radius:12px;text-align:center;">
                <h2 style="color:#117A65;">🏡 Estimated House Price</h2>
                <h1 style="color:#2E86C1;">₹ {prediction:.2f} Lakhs</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
st.markdown("<hr>", unsafe_allow_html=True)