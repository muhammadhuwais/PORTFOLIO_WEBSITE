import streamlit as st
from PIL import Image
import base64

# Set page configuration
st.set_page_config(page_title="Uwais' Portfolio", layout="wide", page_icon=":star:")


import streamlit as st

# Inject custom CSS for a modern sidebar design with light gray background and light blue text
st.markdown(
    """
    <style>
    /* Modern Sidebar Style */
    [data-testid="stSidebar"] {
        background: #f0f4f8; /* Light gray-blue background for a softer look */
        color: #2c3e50; /* Dark text color for contrast */
        padding: 30px; /* Increased padding for spaciousness */
        height: 100vh;
        width: 250px; /* Fixed width */
        overflow-y: auto; /* Vertical scrolling */
        overflow-x: hidden; /* No horizontal scrolling */
        border-right: 2px solid #e0e0e0; /* Subtle border */
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
        font-family: 'Arial', sans-serif; /* Clean font */
        transition: background-color 0.3s ease; /* Smooth background transition */
    }

    /* Style for the sidebar title */
    [data-testid="stSidebar"] h2 {
        color: #2c3e50; /* Dark text color */
        font-size: 26px; /* Slightly larger font size */
        font-weight: 600;
        margin-bottom: 20px;
        border-bottom: 2px solid #e0e0e0; /* Subtle underline */
        padding-bottom: 10px;
    }

    /* Style for the radio buttons */
    [data-testid="stSidebar"] .stRadio {
        font-size: 18px; /* Slightly larger font size for better readability */
        color: #2c3e50; /* Dark text color */
        display: block;
    }

    /* Style for each radio button item */
    [data-testid="stSidebar"] .stRadio div {
        padding: 14px 16px; /* Increased padding for a more button-like feel */
        margin-bottom: 8px;
        border-radius: 8px; /* Slightly larger border radius for a softer look */
        transition: background-color 0.3s ease, transform 0.2s ease;
        cursor: pointer; /* Pointer cursor on hover */
    }

    /* Hover effect for radio buttons */
    [data-testid="stSidebar"] .stRadio div:hover {
        background-color: #d0eaf8; /* Softer blue for hover effect */
        color: #3498db; /* Light blue text color on hover */
        transform: scale(1.03); /* Slightly enlarges the item on hover */
    }

    /* Style for the selected radio button */
    [data-testid="stSidebar"] .stRadio div[role='radio']:checked {
        background-color: #cfe9fc; /* Softer blue for selected item */
        color: #2980b9; /* Darker blue text color for selected item */
        font-weight: bold; /* Bold text for emphasis */
    }

    /* Custom scrollbars */
    [data-testid="stSidebar"] ::-webkit-scrollbar {
        width: 8px;
    }
    [data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
        background: #ccc;
        border-radius: 10px;
    }
    [data-testid="stSidebar"] ::-webkit-scrollbar-track {
        background: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with radio button navigation
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact","resume"])



# Function to get base64 image
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""


# Profile Image
image_base64 = get_base64_image(r"images\uwais.jpg")        



if page == "Home":
    # Home section with custom styling
    col1, col2 = st.columns([1, 2])

    
    with col1:
       st.markdown(f"""
    <style>
        .profile-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            background: linear-gradient(to bottom right, rgba(52, 152, 219, 0.2), rgba(255, 255, 255, 0.9));  /* Subtle gradient */
            padding: 30px;  /* Increased padding */
            border-radius: 20px;  /* More rounded corners for a softer look */
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.3);  /* Deeper shadow for depth */
            transition: background 0.3s ease;  /* Transition effect for background */
        }}

        .profile-container:hover {{
            background: linear-gradient(to bottom right, rgba(52, 152, 219, 0.3), rgba(255, 255, 255, 1));  /* Darker gradient on hover */
        }}

        .profile-pic {{
            width: 250px;
            height: 250px;
            border-radius: 50%;
            object-fit: cover;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
            border: 5px solid #3498db;  
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}

        .profile-pic:hover {{
            transform: scale(1.1);  /* Slightly increased zoom on hover */
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.5);  /* Enhanced shadow on hover */
        }}
    </style>
    <div class="profile-container">
        <img src="data:image/png;base64,{image_base64}" class="profile-pic"/>
    </div>
    """, unsafe_allow_html=True)

    with col2:
       st.markdown("""
    <style>
        .welcome-section {
            background-color: #ffffff;  /* White background for a clean look */
            padding: 40px;  /* Increased padding for more space */
            border-radius: 15px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
            text-align: left;
            animation: fadeIn 1s ease-in-out;
            transition: transform 0.2s;  /* Smooth transition for hover effect */
        }

        .welcome-section:hover {
            transform: scale(1.02);  /* Slightly enlarge on hover */
        }

        .welcome-section h1 {
            font-family: 'Roboto', sans-serif;
            font-size: 35px;  /* Increased font size for prominence */
            color: #2c3e50;
            margin-bottom: 15px;
            text-transform: uppercase;  /* Capitalize for emphasis */
            letter-spacing: 1px;  /* Spacing for a modern look */
        }

        .welcome-section p {
            font-family: 'Open Sans', sans-serif;
            font-size: 18px;
            color: #34495e;
            line-height: 1.8;  /* Increased line height for better readability */
            margin-bottom: 15px;
        }

        .highlight {
            font-weight: bold;
            color: #3498db;  /* Highlight color */
            text-decoration: underline;  /* Underline for emphasis */
        }

        .goal {
            margin-top: 10px;
            font-family: 'Open Sans', sans-serif;
            font-size: 20px;
            color: #2980b9;
            text-align: left;
            font-style: italic;
            margin-bottom: 15px;  /* Added margin for spacing */
        }

        .tagline {
            font-family: 'Open Sans', sans-serif;
            font-size: 18px;  /* Slightly increased font size */
            color: #16a085;
            margin-top: 5px;
            font-weight: bold;
            text-align: center;
            font-style: italic;  /* Italics for a sophisticated touch */
        }

        .cta-button {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 24px;  /* Increased padding for a more substantial button */
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s, box-shadow 0.3s;
            font-weight: bold;  /* Bold text for emphasis */
        }

        .cta-button:hover {
            background-color: #2980b9;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>

    <div class="welcome-section">
        <h1>Welcome to Uwais' Portfolio</h1>
        <p>Hello! I'm <span class="highlight">Muhammadh Uwais</span>, a passionate data scientist and Python developer specializing in <span class="highlight">machine learning</span> and <span class="highlight">data analytics</span>. This portfolio showcases my journey and commitment to solving real-world problems through data.</p>
        <p>I focus on <span class="highlight">predictive models</span> and conducting <span class="highlight">exploratory data analysis (EDA)</span> to derive actionable insights.</p>
        <p class="goal">My goal is to continuously evolve in the data science field and contribute to innovative solutions.</p>
        <p class="tagline">"Empowering decisions through data, one model at a time."</p>
    </div>
    """, unsafe_allow_html=True)




elif page == "About Me":
    st.markdown("""
    <style>
    .about-section {
        background: linear-gradient(135deg, #e0f7fa, #f4f4f4);  /* Subtle gradient background */
        border-radius: 15px;
        padding: 30px;  /* Reduced padding for compactness */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);  /* Slightly reduced shadow for a neater look */
        max-width: 800px;  /* Adjusted max-width */
        margin: 30px auto;  /* Adjusted margin */
        text-align: center;
        transition: transform 0.3s ease;
    }

    .about-section:hover {
        transform: scale(1.02);  /* Slight zoom effect on hover */
    }

    .about-section h2 {
        font-family: 'Montserrat', sans-serif;  /* Modern and professional font */
        font-size: 36px;  /* Slightly reduced font size */
        color: #2c3e50;  /* Dark color for the title */
        font-weight: 700;
        margin-bottom: 15px;  /* Reduced margin */
        text-transform: uppercase;  /* Capitalize the title */
        letter-spacing: 1px;  /* Reduced letter-spacing */
    }

    .about-section p {
        font-family: 'Open Sans', sans-serif;
        font-size: 16px;  /* Slightly reduced font size */
        line-height: 1.5;  /* Adjusted line-height for readability */
        color: #333;
        text-align: justify;
        margin-top: 10px;  /* Reduced margin */
        padding: 0 15px;  /* Reduced padding */
    }

    .about-section p strong {
        color: #3498db;  /* Light blue for emphasis */
        font-weight: 600;
    }

    .about-icon {
        width: 60px;  /* Adjusted icon size */
        height: 60px;
        margin: 0 auto 15px;  /* Adjusted margin */
        display: block;
        border-radius: 50%;
        background-color: #3498db;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);  /* Adjusted shadow */
    }

    .about-icon img {
        width: 30px;  /* Adjusted image size */
        height: 30px;
        filter: invert(1);  /* Invert icon color to match the background */
    }
    </style>

    <div class="about-section">
        <div class="about-icon">
            <img src="https://img.icons8.com/ios-filled/50/000000/user.png" alt="User Icon"/>
        </div>
        <h2>About Me</h2>
        <p>Hello! I am a dedicated <strong>Data Scientist</strong> passionate about transforming data into actionable insights. I hold a <strong>B.Com CA</strong> degree from <strong>Kamarajar University</strong>. My journey in data science is driven by a deep interest in <strong>machine learning</strong>, <strong>data analytics</strong>, and <strong>web application development</strong> using Streamlit. I work on real-world projects, applying advanced techniques in <strong>Exploratory Data Analysis (EDA)</strong> and performing statistical testing like <strong>z-tests</strong> and <strong>t-tests</strong>. I am continuously enhancing my skills in <strong>Python</strong> and building innovative solutions that simplify complex data problems.</p>
    </div>
    """, unsafe_allow_html=True)



elif page == "Skills":
    st.markdown("""
    <style>
    /* General styles for the skills section */
    .skills-section {
        background: linear-gradient(135deg, #e0f7fa, #f4f4f4);  /* Subtle gradient background */
        color: #333;
        border-radius: 15px;
        padding: 30px;  /* Reduced padding for compactness */
        margin-top: 0px;  /* Remove extra margin on top */
        text-align: center;
        max-width: 800px;  /* Reduced max width */
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);  /* Enhanced shadow */
    }

    .skills-section h2 {
        font-family: 'Montserrat', sans-serif;  /* Modern and professional font */
        font-size: 36px;  /* Slightly reduced font size */
        color: #2c3e50;  /* Dark color for the title */
        font-weight: 700;
        margin-bottom: 15px;  /* Reduced margin */
        text-transform: uppercase;  /* Capitalize the title */
        letter-spacing: 1px;  /* Reduced letter-spacing */
    }

    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));  /* Adjusted minimum size for smaller boxes */
        gap: 20px;  /* Slightly reduced gap */
    }

    .skills-card {
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        padding: 15px;  /* Reduced padding */
        text-align: center;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    .skills-card:hover {
        transform: translateY(-5px) scale(1.03);  /* Smaller lift effect */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .skills-card::after {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(52, 152, 219, 0.05);  /* Subtle blue overlay */
        z-index: -1;
        transition: opacity 0.4s;
    }

    .skills-card:hover::after {
        opacity: 0.15;  /* Slightly less pronounced on hover */
    }

    .skills-card img {
        width: 50px;  /* Smaller icon size */
        height: 50px;
        margin-bottom: 10px;  /* Reduced margin */
        transition: transform 0.3s;
    }

    .skills-card:hover img {
        transform: rotate(5deg) scale(1.05);  /* Slightly reduced rotate and scale effect */
    }

    .skills-card h4 {
        margin: 10px 0 5px 0;  /* Reduced margins */
        font-size: 1.2em;  /* Reduced size */
        color: #3498db;
        font-family: 'Frank Ruhl Libre', serif;
        transition: color 0.3s;
    }

    .skills-card:hover h4 {
        color: #2980b9;  /* Darken on hover */
    }

    .skills-card p {
        font-size: 0.85em;  /* Reduced size */
        color: #555;
        font-family: 'Open Sans', sans-serif;
    }
    </style>

    <div class="skills-section">
        <h2>My Skills</h2>
        <div class="skills-grid">
            <div class="skills-card">
                <img src="https://img.icons8.com/ios-filled/50/000000/machine-learning.png" alt="Machine Learning"/>
                <h4>Machine Learning</h4>
                <p>Supervised & Unsupervised Learning, Deep Learning, NLP</p>
            </div>
            <div class="skills-card">
                <img src="https://img.icons8.com/ios-filled/50/000000/graph.png" alt="Data Visualization"/>
                <h4>Data Visualization</h4>
                <p>Matplotlib, Seaborn, Powerbi</p>
            </div>
            <div class="skills-card">
                <img src="https://img.icons8.com/ios-filled/50/000000/web.png" alt="Web Development"/>
                <h4>Web Development</h4>
                <p>Flask, Streamlit, Deployment Tools (Docker)</p>
            </div>
            <div class="skills-card">
                <img src="https://img.icons8.com/ios-filled/50/000000/statistics.png" alt="Statistics"/>
                <h4>Mathematics & Statistics</h4>
                <p>Probability, Linear Algebra, Calculus</p>
            </div>
            <div class="skills-card">
                <img src="https://img.icons8.com/ios-filled/50/000000/code.png" alt="Programming Languages"/>
                <h4>Programming Languages</h4>
                <p>Python, Html, My SQL</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)




elif page == "Projects":
    st.markdown("""<style>
    /* Overall Project Section Style */
    .projects-container {
        padding: 40px;
        background: linear-gradient(135deg, #f0f4f8, #e0e5ec);
        border-radius: 15px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
    }

    /* Project card */
    .project-card {
        display: flex; /* Flexbox for layout */
        flex-direction: column; /* Align items in a column */
        background: white; /* White background for each card */
        border-radius: 10px;
        overflow: hidden; /* Clip child elements */
        transition: transform 0.3s, box-shadow 0.3s; /* Smooth transition */
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px; /* Space between project cards */
    }

    /* Project card hover effect */
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }

    /* Project content area */
    .project-content {
        flex: 1; /* Allow content to take remaining space */
        padding: 15px; /* Padding around the text */
    }

    /* Project title */
    .project-card h3 {
        font-family: 'Arial', sans-serif;
        font-size: 22px;
        color: #333;
        margin: 0 0 10px; /* Margin adjustments */
        font-weight: 700;
    }

    /* Project description */
    .project-card p {
        font-family: 'Arial', sans-serif;
        font-size: 15px;
        color: #555;
        margin: 0 0 10px; /* Margin adjustments */
        line-height: 1.5;
    }

    /* Separate explanation paragraph */
    .project-card .explanation {
        font-family: 'Arial', sans-serif;
        font-size: 14px;
        color: #444; /* Slightly darker color for explanation */
        margin: 0 0 10px; /* Margin adjustments */
        line-height: 1.4;
        border-top: 1px solid #ddd; /* Divider line */
        padding-top: 10px; /* Padding above explanation */
    }

    /* Links (GitHub, Streamlit) */
    .project-card a {
        display: inline-block;
        padding: 12px 20px;
        background-color: #007BFF; /* Button color */
        color: white;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        transition: background-color 0.3s;
        margin-top: 10px; /* Margin for spacing */
    }

    /* Hover effect for links */
    .project-card a:hover {
        background-color: #0056b3; /* Darker button on hover */
    }

    /* Heading Style */
    .section-heading {
        font-family: 'Montserrat', sans-serif;  /* Modern and professional font */
        font-size: 36px;  /* Slightly reduced font size */
        color: #2c3e50;  /* Dark color for the title */
        font-weight: 700;
        margin-bottom: 15px;  /* Reduced margin */
        text-transform: uppercase;  /* Capitalize the title */
        letter-spacing: 1px;  /* Reduced letter-spacing */
    }
    </style>""", unsafe_allow_html=True)

    # Heading for the Projects Section
    st.markdown("<h2 class='section-heading'>PROJECTS</h2>", unsafe_allow_html=True)

    # Container for projects
    st.markdown("<div class='projects-container'>", unsafe_allow_html=True)

    # Project 1: YouTube Spam Detection
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
    st.markdown("<div class='project-content'>", unsafe_allow_html=True)
    st.markdown("<h3>Loan Prediction Web </h3>", unsafe_allow_html=True)
    st.markdown("<p class='explanation'>This project demonstrates my ability to work with machine learning techniques to identifying the loan ability peoples .</p>", unsafe_allow_html=True)
    st.markdown("<p>  Purpose  :   To predict whether a loan applicant will be able to repay a loan or not, based on their financial and personal data . </p>", unsafe_allow_html=True)
    st.markdown("<P><P>", unsafe_allow_html=True)
    st.markdown("<P> uses : <P>", unsafe_allow_html=True)
    st.markdown("<P> * Banks & Financial Institutions :  Helps in faster, data-driven loan approvals, reducing the risk of defaults <P>", unsafe_allow_html=True)
    st.markdown("<P> * Applicants : Provides a fair assessment based on data, allowing more reliable access to credit for those likely to repay .<P>", unsafe_allow_html=True)
    st.markdown("<P> * Credit Risk Management : Assists in identifying high-risk applicants, helping lenders reduce losses. <P>", unsafe_allow_html=True)
    st.markdown("<P> <P>", unsafe_allow_html=True)
    
    st.markdown("""<a href="https://github.com/muhammadhuwais/LOAN_PREDICTION_STREAMLIT" target="_blank">GitHub Repository</a>
    <a href="https://loanpredictionapp-tlppkydn2b2gccn3ccxhqi.streamlit.app/" target="_blank">Streamlit App</a>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Multiple images for Project 1 in columns
    col1, col2, col3 = st.columns(3)  # Adjust the number of columns based on the number of images
    with col1:
        st.image("images2\loan 1.jpeg", width=300)
    with col2:
        st.image("images2\loan 3.webp", width=300)
    with col3:
        st.image("images2\loan 2.webp", width=300)

    st.markdown("</div>", unsafe_allow_html=True)

    # Project 2: Diabetes Prediction App
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
    st.markdown("<div class='project-content'>", unsafe_allow_html=True)
    st.markdown("<h3>Diabetes identifiying web </h3>", unsafe_allow_html=True)
    st.markdown("<p class='explanation'> This web application predicts the likelihood of diabetes based on user input data.</p>", unsafe_allow_html=True)
    st.markdown("<P> Purpose : To determine the likelihood of a patient having diabetes based on health indicators like glucose levels, blood pressure, and age. <P>", unsafe_allow_html=True)
    st.markdown("<P> Uses :<P>", unsafe_allow_html=True)
    st.markdown("<P>* Healthcare Providers : Allows early detection of diabetes, enabling timely intervention and better patient care.<P>", unsafe_allow_html=True)
    st.markdown("<P>* Patients : Helps individuals assess their risk and take preventive actions.<P>", unsafe_allow_html=True)
    st.markdown("<P>* Public Health: Supports health professionals in understanding diabetes trends in populations and planning resources accordingly. <P>", unsafe_allow_html=True)
    st.markdown("""<a href="https://github.com/uwais/Diabetes-Prediction-App" target="_blank">GitHub Repository</a>
    <a href="https://your_streamlit_app_link" target="_blank">Streamlit App</a>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Multiple images for Project 2 in columns
    col1, col2, col3 = st.columns(3)  # Adjust the number of columns based on the number of images
    with col1:
        st.image("images3\dia 1.jpeg", width=300)
    with col2:
        st.image("images3\dia 2.jpg", width=300)
    with col3:
        st.image("images3\Diabetes.jpg", width=300)

    st.markdown("</div>", unsafe_allow_html=True)

    # Project 3: Wine data prediction
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
    st.markdown("<div class='project-content'>", unsafe_allow_html=True)
    st.markdown("<h3>Wine prepration web </h3>", unsafe_allow_html=True)
    st.markdown("<p class='explanation'>This project uses machine learning to predict the winner of an IPL match based on past match data.</p>", unsafe_allow_html=True)
    st.markdown("<p>I applied different algorithms to train the model and evaluated its performance.</p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("""<a href="https://github.com/uwais/IPL-Match-Winner-Prediction" target="_blank">GitHub Repository</a>
    <a href="https://your_streamlit_app_link" target="_blank">Streamlit App</a>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Multiple images for Project 3 in columns
    col1, col2, col3 = st.columns(3)  # Adjust the number of columns based on the number of images
    with col1:
        st.image("images/ipl_prediction_1.jpg", width=100)
    with col2:
        st.image("images/ipl_prediction_2.jpg", width=100)
    with col3:
        st.image("images/ipl_prediction_3.jpg", width=100)

    st.markdown("</div>", unsafe_allow_html=True)

    # Project 4: Loan Status Prediction
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
    st.markdown("<div class='project-content'>", unsafe_allow_html=True)
    st.markdown("<h3>Loan Status Prediction</h3>", unsafe_allow_html=True)
    st.markdown("<p class='explanation'>This project predicts the loan approval status based on applicant details.</p>", unsafe_allow_html=True)
    st.markdown("<p>Implemented using logistic regression and showcased using Streamlit for user interaction.</p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("<p></p>", unsafe_allow_html=True)
    st.markdown("""<a href="https://github.com/uwais/Loan-Status-Prediction" target="_blank">GitHub Repository</a>
    <a href="https://your_streamlit_app_link" target="_blank">Streamlit App</a>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Multiple images for Project 4 in columns
    col1, col2, col3 = st.columns(3)  # Adjust the number of columns based on the number of images
    with col1:
        st.image("images/loan_prediction_1.jpg", width=100)
    with col2:
        st.image("images/loan_prediction_2.jpg", width=100)
    with col3:
        st.image("images/loan_prediction_3.jpg", width=100)

    st.markdown("</div>", unsafe_allow_html=True)

    # Closing the projects container
    st.markdown("</div>", unsafe_allow_html=True)





elif page == "Contact":
    st.markdown("""
    <style>
    /* General styles for the contact section */
    .contact-section {
        background: linear-gradient(135deg, #e0f7fa, #f4f4f4);  /* Subtle gradient background */
        color: #333;
        border-radius: 15px;
        padding: 40px;
        margin-top: 50px;
        text-align: center;
        max-width: 750px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);  /* Enhanced shadow */
        position: relative;
    }

    .contact-section h2 {
        font-family: 'Montserrat', sans-serif;  /* Modern and professional font */
        font-size: 36px;  /* Slightly reduced font size */
        color: #2c3e50;  /* Dark color for the title */
        font-weight: 700;
        margin-bottom: 15px;  /* Reduced margin */
        text-transform: uppercase;  /* Capitalize the title */
        letter-spacing: 1px;  /* Reduced letter-spacing */
    }

    .contact-section p {
        font-family: 'Open Sans', sans-serif;
        font-size: 18px;
        color: #555555;  /* Softer gray for text */
        margin-bottom: 20px;
        line-height: 1.6;
    }

    .contact-section ul {
        list-style: none;
        padding: 0;
        margin: 20px 0;  /* Spacing around the list */
    }

    .contact-section ul li {
        display: inline-block;
        margin: 0 15px;
        font-size: 22px;
    }

    .contact-section ul li a {
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .contact-section ul li a img {
        width: 40px;
        height: 40px;
        transition: transform 0.3s ease;
    }

    .contact-section ul li a:hover img {
        transform: scale(1.2);  /* Zoom effect on hover */
    }
    </style>

    <div class="contact-section">
        <h2>Contact Me</h2>
        <p>I'm always open to connecting with new people and exploring professional opportunities. Feel free to reach out via LinkedIn, GitHub, or Email.</p>
        <ul>
            <li><a href="mailto:uwaisu867@gmail.com" aria-label="Email"><img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email Logo"></a></li>
            <li><a href="https://www.linkedin.com/in/muhammadh-uwais-j-91630b327/" target="_blank" aria-label="LinkedIn"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn Logo"></a></li>
            <li><a href="https://github.com/muhammadhuwais" target="_blank" aria-label="GitHub"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub Logo"></a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)



import streamlit as st

# Resume Section in one single block
if page == "resume":
    with open("myself-1.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    # Displaying PDF in the viewer
    st.header("MY RESUME")
    st.write("Explore my resume below for detailed insights into my background, skills, and accomplishments.")
    
    # Embed PDF Viewer
    st.markdown(
        f'<iframe src="data:application/pdf;base64,{base64.b64encode(PDFbyte).decode()}" width="100%" height="850" style="border: none;"></iframe>',
        unsafe_allow_html=True
    )

    # Download Resume Button
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="my_resume.pdf",
        mime="application/pdf"
    )


