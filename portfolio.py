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
        background: #f5f5f5; /* Light gray background */
        color: #000000; /* Black text color */
        padding: 20px;
        height: 100vh;
        width: 250px; /* Fixed width */
        overflow-y: auto; /* Vertical scrolling */
        overflow-x: hidden; /* No horizontal scrolling */
        border-right: 2px solid #e0e0e0; /* Subtle border */
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
        font-family: 'Arial', sans-serif; /* Clean font */
    }

    /* Style for the sidebar title */
    [data-testid="stSidebar"] h2 {
        color: #000000; /* Black text color */
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 20px;
        border-bottom: 2px solid #e0e0e0; /* Subtle underline */
        padding-bottom: 10px;
    }

    /* Style for the radio buttons */
    [data-testid="stSidebar"] .stRadio {
        font-size: 16px;
        color: #000000; /* Black text color */
        display: block;
    }

    /* Style for each radio button item */
    [data-testid="stSidebar"] .stRadio div {
        padding: 12px;
        margin-bottom: 8px;
        border-radius: 6px;
        transition: background-color 0.2s ease, transform 0.2s ease;
        cursor: pointer; /* Pointer cursor on hover */
    }

    /* Hover effect for radio buttons */
    [data-testid="stSidebar"] .stRadio div:hover {
        background-color: #e0e0e0; /* Slightly darker gray for hover effect */
        color: #3498db; /* Light blue text color on hover */
        transform: scale(1.02); /* Slightly enlarges the item on hover */
    }

    /* Style for the selected radio button */
    [data-testid="stSidebar"] .stRadio div[role='radio']:checked {
        background-color: #d0d0d0; /* Slightly darker gray for selected item */
        color: #3498db; /* Light blue text color for selected item */
        font-weight: bold;
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
image_base64 = get_base64_image(r"C:\Users\uwais\Downloads\motivational-theme-vp11.jpg")        



# Main content based on selection
if page == "Home":
    # Home section with custom styling
    col1, col2 = st.columns([1, 2])

    with col1:
       st.markdown(f"""
    <style>
    .profile-pic {{
        width: 250px;
        height: 250px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
        border: 5px solid #3498db;  /* Changed border to blue */
    }}
    .center {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
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
            background-color: #f4f4f4;  /* Light grey background for consistency */
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
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
            color: #3498db;
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
        background-color: #f4f4f4;  /* Light grey background */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Subtle shadow for depth */
    }

    .about-section h2 {
        font-family: 'Helvetica Neue', sans-serif;  /* Modern and professional font */
        font-size: 36px;
        color: #2c3e50;  /* black colour for title */
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
        <p>I am a passionate <strong>data scientist</strong> actively working on real-world projects. I graduated with a <strong>B.Com CA</strong> from <strong>Kamarajar University</strong>. I have a passion for machine learning, data analytics, and building web applications using Streamlit. I’m constantly learning and improving my skills in Python and data science. Currently, I’m focused on expanding my knowledge in areas like <strong>exploratory data analysis (EDA)</strong>, statistical testing <strong>(z-tests, t-tests)</strong>, and developing web applications using Streamlit to make data-driven solutions accessible. With expertise in handling real-world data, I strive to build innovative solutions to complex problems.</p>
    </div>
    """, unsafe_allow_html=True)



elif page == "Skills":
    st.markdown("""
    <style>
    /* General styles for the skills section */
    .skills-section {
        background-color: #f4f4f4;  /* Light grey background for subtlety */
        color: #333;
        border-radius: 15px;
        padding: 40px;
        margin-top: 0px;  /* Remove extra margin on top */
        text-align: center;
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
        position: relative;  /* Ensure positioning context */
    }

    .skills-section h2 {
        font-family: 'Roboto', sans-serif;  /* Modern and clean font */
        font-size: 36px;
        color: #333;
        font-weight: 700;
        margin-bottom: 30px;
    }

    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));  /* Responsive grid */
        gap: 20px;
    }

    .skills-card {
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
    }

    .skills-card:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
    }

    .skills-card img {
        width: 60px;
        height: 60px;
        margin-bottom: 10px;
    }

    .skills-card h4 {
        margin: 10px 0 0 0;
        font-size: 1.2em;
        color:  #3498db;
        font-family: 'Frank Ruhl Libre', serif;
    }

    .skills-card p {
        font-size: 0.9em;
        color: #666;
        font-family: 'Frank Ruhl Libre', serif;
    }
    </style>

    <div class="skills-section">
        <h2>Skills</h2>
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
    .project-section {
        background: linear-gradient(135deg, #e0f7fa, #e0f4f4);  /* Light gradient background */
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);  /* Deeper shadow for cards */
        transition: transform 0.2s;  /* Hover effect */
    }

    .project-section:hover {
        transform: translateY(-10px);  /* Lift effect on hover */
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    }

    .project-section h3 {
        font-family: 'Arial', sans-serif;
        font-size: 30px;
        color: #1E90FF;  /* Light blue for headings */
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
    st.markdown("<h3>YouTube Spam Detection</h3>", unsafe_allow_html=True)
    st.image(r"https://my.clevelandclinic.org/-/scassets/images/org/health/articles/7104-diabetes-symptoms", caption="Spam Detection Chart", width=600)
    st.markdown("""
    <p>This project uses machine learning to detect spam in YouTube comments. I performed exploratory data analysis and deployed the model using Streamlit.</p>
    <a href="https://diabitiesapp-kcfogtrhm7z5mi8kp35ty2.streamlit.app/" target="_blank">View GitHub Repository</a>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Project 2: Diabetes Prediction App
    st.markdown("<div class='project-section'>", unsafe_allow_html=True)
    st.markdown("<h3>Diabetes Prediction App</h3>", unsafe_allow_html=True)
    st.image(r"https://julianhealthcare.com/wp-content/uploads/2019/07/Diabetes.jpg", caption="Diabetes Prediction App", width=600)
    st.markdown("""
    <p>This is a web application that predicts diabetes based on input data. It was built with Streamlit and Scikit-learn.</p>
    <a href="https://github.com/uwais/Diabetes-Prediction-App" target="_blank">View GitHub Repository</a>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Add more projects following the same structure as above


elif page == "Contact":
    st.markdown("""
    <style>
    .contact-section {
        background-color: #f9f9f9;  /* Light gray background */
        border-radius: 10px;
        padding: 40px;
        margin-top: 50px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
        max-width: 750px;
        margin-left: auto;
        margin-right: auto;
    }

    .contact-section h2 {
        font-family: 'Roboto', sans-serif;  /* Professional font */
        font-size: 34px;
        color: #333333;  /* Dark gray for title */
        font-weight: 700;  /* Bold for strong emphasis */
        margin-bottom: 20px;
    }

    .contact-section p {
        font-family: 'Open Sans', sans-serif;
        font-size: 18px;
        color: #555555;  /* Softer gray for text */
        margin-bottom: 30px;
        line-height: 1.6;
    }

    .contact-section ul {
        list-style: none;
        padding: 0;
    }

    .contact-section ul li {
        display: inline-block;
        margin: 0 20px;
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

    /* Call to action button */
    .contact-section button {
        background-color: #0073e6;
        color: white;
        padding: 12px 25px;
        font-size: 18px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin-top: 30px;
    }

    .contact-section button:hover {
        background-color: #005bb5;  /* Darker on hover for effect */
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .contact-section h2 {
            font-size: 28px;
        }
        .contact-section p {
            font-size: 16px;
        }
        .contact-section ul li {
            font-size: 18px;
        }
    }
    </style>

    <div class="contact-section">
        <h2>Contact Me</h2>
        <p>I'm always open to connecting with new people and exploring professional opportunities. Feel free to reach out via LinkedIn, GitHub, or Email.</p>
        <ul>
            <li><a href="mailto:uwais@example.com"><img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email Logo"></a></li>
            <li><a href="https://www.linkedin.com/in/uwais" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn Logo"></a></li>
            <li><a href="https://github.com/uwais" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub Logo"></a></li>
        </ul>
        <button id="contact-button">Contact Me</button>
    </div>

    <script>
    document.getElementById('contact-button').addEventListener('click', function() {
        window.location.href = 'mailto:uwais@example.com';
    });

    // Smooth scroll to contact section
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    </script>
    """, unsafe_allow_html=True)
