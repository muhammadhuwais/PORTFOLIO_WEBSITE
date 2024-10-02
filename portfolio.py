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
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact"])



# Function to get base64 image
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""


# Profile Image
image_base64 = get_base64_image(r"C:\Users\uwais\Documents\WhatsApp Image 2024-09-26 at 11.31.50_50901358.jpg")        



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
        font-family: 'Montserrat', sans-serif;  /* Clean, modern font */
        font-size: 32px;  /* Reduced font size */
        color: #2c3e50;  /* Slightly darker heading color */
        font-weight: 700;
        margin-bottom: 20px;  /* Reduced margin */
        text-transform: uppercase;  /* Capitalize for emphasis */
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
                <p>Matplotlib, Seaborn, Plotly</p>
            </div>
            <div class="skills-card">
                <img src="https://img.icons8.com/ios-filled/50/000000/web.png" alt="Web Development"/>
                <h4>Web Development</h4>
                <p>Flask, Django, Deployment Tools (Docker, Heroku)</p>
            </div>
            <div class="skills-card">
                <img src="https://img.icons8.com/ios-filled/50/000000/statistics.png" alt="Statistics"/>
                <h4>Mathematics & Statistics</h4>
                <p>Probability, Linear Algebra, Calculus</p>
            </div>
            <div class="skills-card">
                <img src="https://img.icons8.com/ios-filled/50/000000/code.png" alt="Programming Languages"/>
                <h4>Programming Languages</h4>
                <p>Python, JavaScript, SQL</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



elif page == "Projects":
    st.markdown("""
    <style>
    /* Overall Project Section Style */
    .projects-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px; /* Space between project cards */
        justify-content: center; /* Center align the project cards */
    }

    .project-section {
        background: linear-gradient(135deg, #f0f8ff, #e8f5f9);  /* Light gradient */
        border-radius: 15px;  /* Rounded edges */
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);  /* Soft shadow */
        transition: transform 0.3s ease, box-shadow 0.3s ease;  /* Smooth hover */
        width: 300px; /* Fixed width for uniformity */
        text-align: center; /* Center text alignment */
    }

    .project-section:hover {
        transform: scale(1.02);  /* Slight scaling */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);  /* Enhanced shadow */
    }

    .project-section h3 {
        font-family: 'Arial', sans-serif;
        font-size: 24px;  /* Updated font size for titles */
        color: #1E90FF; /* Title color */
        margin-bottom: 10px;
        font-weight: 700;
        position: relative;
        padding-bottom: 5px;
    }

    .project-section h3::after {
        content: '';
        position: absolute;
        width: 50px; /* Wider underline */
        height: 3px;
        background-color: #1E90FF;
        left: 50%;
        transform: translateX(-50%);
        bottom: -5px;
        border-radius: 2px;
    }

    .project-section p {
        font-family: 'Arial', sans-serif;
        font-size: 16px;  /* Adjusted font size for better readability */
        color: #333;
        line-height: 1.6;
        margin-bottom: 10px;
        text-align: justify; /* Justify text for a cleaner look */
    }

    .project-section a {
        display: inline-block;
        padding: 10px 20px;
        background-color: #1E90FF; /* Button background color */
        color: white; /* Button text color */
        border-radius: 4px; /* Rounded button */
        text-decoration: none; /* No underline */
        font-weight: bold; /* Bold text */
        text-align: center; /* Center text */
        transition: background-color 0.3s ease, transform 0.3s ease;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1); /* Button shadow */
    }

    .project-section a:hover {
        background-color: #104E8B; /* Darker button color on hover */
        transform: translateY(-2px); /* Lift effect on hover */
    }

    .project-section img {
        border-radius: 8px;  /* Rounded corners */
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1); /* Image shadow */
        margin-bottom: 10px;
        width: 100%; /* Responsive image width */
        height: auto; /* Maintain aspect ratio */
        object-fit: cover;  /* Crop images to fit the container */
    }
    </style>
    """, unsafe_allow_html=True)

    # Container for projects
    st.markdown("<div class='projects-container'>", unsafe_allow_html=True)

    # Project 1: YouTube Spam Detection
    st.markdown("<div class='project-section'>", unsafe_allow_html=True)
    st.markdown("<h3>YouTube Spam Detection</h3>", unsafe_allow_html=True)
    st.image("your_image_link_1.jpg", caption="Spam Detection Chart", use_column_width=True)  # Add your image link here
    st.markdown("""<p>This project demonstrates my ability to work with machine learning techniques to detect spam in YouTube comments. I utilized exploratory data analysis (EDA) to understand the data better and deployed a predictive model using Streamlit.</p>
    <a href="https://diabitiesapp-kcfogtrhm7z5mi8kp35ty2.streamlit.app/" target="_blank">View Project</a>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Project 2: Diabetes Prediction App
    st.markdown("<div class='project-section'>", unsafe_allow_html=True)
    st.markdown("<h3>Diabetes Prediction App</h3>", unsafe_allow_html=True)
    st.image("your_image_link_2.jpg", caption="Diabetes Prediction App", use_column_width=True)  # Add your image link here
    st.markdown("""<p>This web application predicts the likelihood of diabetes based on user input data. Built using Streamlit and Scikit-learn, it demonstrates my expertise in developing data-driven applications.</p>
    <a href="https://github.com/uwais/Diabetes-Prediction-App" target="_blank">View GitHub Repository</a>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # Closing the projects container




    # Add more projects following the same structure as above


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
        font-family: 'Montserrat', sans-serif;  /* Clean, modern font */
        font-size: 34px;
        color: #2c3e50;  /* Slightly darker heading color */
        font-weight: 700;
        margin-bottom: 20px;
        text-transform: uppercase;  /* Capitalize for emphasis */
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
            <li><a href="mailto:uwais@example.com" aria-label="Email"><img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email Logo"></a></li>
            <li><a href="https://www.linkedin.com/in/uwais" target="_blank" aria-label="LinkedIn"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn Logo"></a></li>
            <li><a href="https://github.com/uwais" target="_blank" aria-label="GitHub"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub Logo"></a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
