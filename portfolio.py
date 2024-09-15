import streamlit as st
from PIL import Image


# Set page configuration
st.set_page_config(page_title="Uwais' Portfolio", layout="wide", page_icon=":star:")

import streamlit as st

# Inject custom CSS for sidebar styling
st.markdown(
    """
    <style>
    /* Style for the entire sidebar with a gradient background */
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom right, #74ebd5, #ACB6E5);  /* Gradient color */
        color: white;
        padding: 20px;
    }

    /* Customize the sidebar title */
    [data-testid="stSidebar"] h2 {
        color: #ffffff;
        font-size: 28px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  /* Adding shadow for better contrast */
    }

    /* Style for the radio buttons */
    [data-testid="stSidebar"] .stRadio {
        font-size: 20px;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }

    /* Style for each radio button item */
    [data-testid="stSidebar"] .stRadio div {
        padding: 10px;
        margin-bottom: 5px;
        border-radius: 10px;
        transition: all 0.3s ease;  /* Smooth transition for hover effect */
    }

    /* Hover effect for the radio buttons */
    [data-testid="stSidebar"] .stRadio div:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: scale(1.05);  /* Slightly enlarges the option on hover */
    }

    /* Style the selected radio button */
    [data-testid="stSidebar"] .stRadio div[role='radio']:checked {
        background-color: rgba(255, 255, 255, 0.4);
        color: #000;
        font-weight: bold;
    }

    /* Add shadow to the radio options */
    [data-testid="stSidebar"] .stRadio div {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with radio button navigation
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact"])

# Main content based on selection
if page == "Home":
    st.write("Welcome to the Home Page!")
elif page == "About Me":
    st.write("Here's more about me...")
elif page == "Skills":
    st.write("Skills I have...")
elif page == "Projects":
    st.write("Projects I've worked on...")
elif page == "Contact":
    st.write("Contact me here.")


import base64

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert the profile image to base64
image_base64 = get_base64_image(r"C:\Users\uwais\Documents\WhatsApp Image 2024-08-06 at 10.01.51_cd4aaabb.jpg")


if page == "Home":
    # Home section with custom styling
    col1, col2 = st.columns([1, 2])

    

    with col1:
        st.markdown(f"""
    <style>
        .profile-pic {{
            width: 250px;  /* Fixed large size */
            height: 250px; /* Fixed large size */
            border-radius: 50%;  /* Ensures circular shape */
            object-fit: cover;  /* Ensures image covers the container */
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);  /* Shadow for depth */
            border: 5px solid #3498db;  /* Blue border */
        }}
        .center {{
            display: flex;
            justify-content: center;
            align-items: center;  /* Center vertically */
            height: 100%;  /* Full height to center image */
        }}
    </style>

    <div class="center">
        <img src="data:image/png;base64,{image_base64}" class="profile-pic"/>
    </div>
    """, unsafe_allow_html=True)


    

    with col2:
        st.markdown("""
    <style>
        .welcome-section {
            background-color: #fdfdfd;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: left;
        }

        .welcome-section h1 {
            font-family: 'Roboto', sans-serif;
            font-size: 40px;
            color: #2c3e50;
            margin-bottom: 20px;
        }

        .welcome-section p {
            font-family: 'Roboto', sans-serif;
            font-size: 18px;
            color: #34495e;
            line-height: 1.6;
        }

        .highlight {
            font-weight: bold;
            color: #e67e22;
        }

        .goal {
            margin-top: 15px;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            color: #2980b9;
            text-align: left;
            font-style: italic;
        }

        .tagline {
            font-family: 'Roboto', sans-serif;
            font-size: 16px;
            color: #16a085;
            margin-top: 5px;
            font-weight: bold;
        }
    </style>

    <div class="welcome-section">
        <h1>Welcome to Uwais' Portfolio</h1>
        <p>Hello! I'm <span class="highlight">Muhammadh Uwais</span>, a passionate data scientist and Python developer in <span class="highlight">machine learning</span> and <span class="highlight">data analytics</span>. This portfolio is a glimpse of my journey, showcasing various projects, technical skills, and my commitment to solving real-world problems through data.</p>
        <p>I specialize in building <span class="highlight">predictive models</span>, conducting <span class="highlight">exploratory data analysis (EDA)</span>, and deploying <span class="highlight">data-driven applications</span> that impact businesses and people positively.</p>
        <p class="goal">My goal is to continuously evolve in the data science field and contribute to innovative solutions that make a difference.</p>
        <p class="tagline">"Empowering decisions through data, one model at a time."</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "About Me":
    st.markdown("""
    <style>
    .about-section {
        background-color: #eaf6ff;  /* Light blue background */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Subtle shadow for depth */
    }

   .about-section h2 {
        font-family: 'Helvetica Neue', sans-serif;  /* Modern and professional font */
        font-size: 36px;
        color: #1E90FF;  /* Light blue for title */
        text-align: center;
        font-weight: 700;  /* Bold and professional */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);  /* Shadow for title */
    }


    .about-section p {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        line-height: 1.6;
        color: #333;
        text-align: justify;
        margin-top: 10px;
    }

    .about-section p strong {
        color: #1E90FF;  /* Light blue highlight */
    }

    </style>

    <div class="about-section">
        <h2>About Me</h2>
        <p> i'am a passionate <strong> data scientiest</strong> actively working on the real-world projects. I graduated with a <strong>B.Com CA</strong> from <strong>Kamarajar University</strong>. I have a passion for machine learning, data analytics, and building web applications using Streamlit. I’m constantly learning and improving my skills in Python and data science.Currently, I’m focused on expanding my knowledge in areas like <strong> exploratory data analysis (EDA)</strong>, statistical testing <strong> (z-tests, t-tests)</strong>, and developing web applications using Streamlit to make data-driven solutions accessible. With expertise in handling real-world data, I strive to build innovative solutions to complex problems.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Skills":
    st.markdown("""
    <style>
    .skills-section {
        background-color: #f8f9fa;  /* Light grey background for professionalism */
        border-radius: 15px;
        padding: 30px;
        margin-top: 20px;
    }

    .skills-section h2 {
        font-family: 'Arial', sans-serif;
        font-size: 36px;
        color: #333;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 600;  /* Lighter bold */
    }

    .skills-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);  /* 3-column layout */
        gap: 20px;
    }

    .skills-grid div {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;  /* Soft border for distinction */
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        transition: box-shadow 0.3s ease;  /* Subtle shadow transition on hover */
    }

    .skills-grid div:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);  /* Elegant hover shadow */
    }

    .skills-grid h3 {
        font-size: 22px;
        color: #007BFF;  /* Professional blue accent */
        margin-bottom: 15px;
        font-weight: 600;  /* Lighter bold */
    }

    .skills-grid ul {
        list-style: none;  /* No bullets */
        padding: 0;
    }

    .skills-grid ul li {
        font-size: 16px;
        color: #555;
        padding: 5px 0;
        display: flex;
        align-items: center;
        justify-content: center;  /* Center emoji and text */
    }

    .skills-grid ul li span {
        margin-right: 10px;  /* Space between emoji and text */
    }
    </style>

    <div class="skills-section">
        <h2>Skills</h2>
        <div class="skills-grid">
            <div>
                <h3>Programming</h3>
                <ul>
                    <li><span>🐍</span> Python</li>
                    <li><span>🗄️</span> SQL</li>
                    <li><span>📊</span> Excel</li>
                </ul>
            </div>
            <div>
                <h3>Libraries</h3>
                <ul>
                    <li><span>📚</span> Pandas</li>
                    <li><span>🔢</span> NumPy</li>
                    <li><span>🔍</span> Scikit-learn</li>
                </ul>
            </div>
            <div>
                <h3>Visualization</h3>
                <ul>
                    <li><span>📈</span> Matplotlib</li>
                    <li><span>🌈</span> Seaborn</li>
                    <li><span>📊</span> PowerBI</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Projects":
    st.markdown("""
    <style>
    .project-section {
        background: linear-gradient(135deg, #f9f9f9, #e0f4f4);  /* Light gradient background */
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);  /* Consistent shadow */
        transition: transform 0.2s;  /* Hover effect */
    }

    .project-section:hover {
        transform: translateY(-10px);  /* Hover lift effect */
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    }

    .project-section h3 {
        font-family: 'Arial', sans-serif;
        font-size: 30px;
        color: #1E90FF;  /* Light blue headings */
        margin-bottom: 15px;
        font-weight: 700;
        text-align: center;
    }

    .project-section p {
        font-family: 'Arial', sans-serif;
        font-size: 16px;
        color: #444;
        line-height: 1.8;
        margin-bottom: 15px;
        text-align: justify;
    }

    .project-section a {
        display: inline-block;
        padding: 10px 20px;
        background-color: #1E90FF;
        color: white;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
    }

    .project-section a:hover {
        background-color: #104E8B;  /* Darker blue on hover */
    }
    </style>
    """, unsafe_allow_html=True)

    # Project 1: YouTube Spam Detection
    st.markdown("<div class='project-section'>", unsafe_allow_html=True)
    st.markdown("<h3>Gold price web</h3>", unsafe_allow_html=True)
    
    st.image("C:/Users/uwais/Downloads/youtubesapm.jpg", caption="Spam Detection Chart", width=600)  # Fixed width
    
    st.markdown("""
    <p>This project uses machine learning to detect spam in YouTube comments. I performed exploratory data analysis and deployed the model using Streamlit.</p>
    <a href="https://diabitiesapp-kcfogtrhm7z5mi8kp35ty2.streamlit.app/" target="_blank">View GitHub Repository</a>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Project 2: Diabetes Prediction App
    st.markdown("<div class='project-section'>", unsafe_allow_html=True)
    st.markdown("<h3>Diabetes Prediction App</h3>", unsafe_allow_html=True)
    
    st.image(r"C:\Users\uwais\Downloads\Diabetes.jpg", caption="Diabetes Prediction App", width=600)  # Fixed width
    
    st.markdown("""
    <p>This is a web application that predicts diabetes based on input data. It was built with Streamlit and Scikit-learn.</p>
    <a href="https://diabitiesapp-kcfogtrhm7z5mi8kp35ty2.streamlit.app" target="_blank">View GitHub Repository</a>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # You can add more projects here, following the same structure




elif page == "Contact":
    st.markdown("""
    <style>
    .contact-section {
        background-color: #eaf6ff;  /* Light blue background */
        border-radius: 15px;
        padding: 30px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Subtle shadow for depth */
    }

    .contact-section h2 {
        font-family: 'Helvetica Neue', sans-serif;  /* Professional font */
        font-size: 36px;
        color: #1E90FF;  /* Light blue for title */
        font-weight: 600;  /* Slightly bold */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);  /* Shadow for title */
    }

    .contact-section p {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        color: #333;
        margin: 15px 0;
    }

    .contact-section ul {
        list-style: none;
        padding: 0;
    }

    .contact-section ul li {
        display: inline-block;
        margin: 10px;
        font-size: 20px;
    }

    .contact-section ul li a {
        color: #1E90FF;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }

    .contact-section ul li a:hover {
        color: #104E8B;  /* Darker blue on hover */
        text-decoration: underline;  /* Underline on hover */
    }

    .contact-section ul li a::before {
        content: "🔗";  /* Add icon before link */
        margin-right: 8px;
    }

    </style>

    <div class="contact-section">
        <h2>Contact</h2>
        <p>Feel free to connect with me on LinkedIn or GitHub. I’m always open to discussing new opportunities and collaborations.</p>
        <ul>
            <li><a href="https://www.linkedin.com/in/muhammadh-uwais-j-91630b327" target="_blank">LinkedIn</a></li>
            <li><a href="https://github.com/uwais" target="_blank">GitHub</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<footer>
    © 2024 Uwais' Portfolio
</footer>
""", unsafe_allow_html=True)


