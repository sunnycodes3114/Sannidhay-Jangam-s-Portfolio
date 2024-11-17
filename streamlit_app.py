import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page configuration
st.set_page_config(
    page_title="Sannidhay Jangam",
    page_icon="https://media.licdn.com/dms/image/v2/C5603AQFJG6PhEXslrA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1659520345146?e=1737590400&v=beta&t=bEQtDlfJ1tOXMbVzwH_WTfwPspjXYScGGHFxP4OocAc",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Helper function to load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animation
lottie_animation = load_lottieurl("https://lottie.host/96d2e356-1dcf-4a09-bac7-06612a4fd2fe/EVRLu4G3WJ.json")
education_animation = load_lottieurl("https://lottie.host/a3a37a03-e4e7-4ec9-9920-d144ff8c8fbd/jAmSivJqgc.json")
experience_animation = load_lottieurl("https://lottie.host/d985a3bb-8b99-448b-a2db-e0349e96c840/xwCWpGjJ25.json")
projects_animation = load_lottieurl("https://lottie.host/88ce0101-b2c0-448d-a3bf-6d572e6ce54d/zWVVDEiT6L.json")
skills_animation = load_lottieurl("https://lottie.host/9e54e233-a3bc-4062-9218-d09cd540e0b6/k43lmWgvSf.json")
hackathons_animation = load_lottieurl("https://lottie.host/b49768f2-43f9-4e9c-9b5d-2aeaee5617b4/fyLaSPPquf.json")
certifications_animation = load_lottieurl("https://lottie.host/01670180-d5bb-4902-aeb3-e0cb415a9980/vGkuENt8rg.json")
# CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;  /* Set white background for the entire page */
        font-family: 'Arial', sans-serif;
        color: #333333;  /* Dark text color for readability */
    }
    .main-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 1.5em;
        color: #555555;
        text-align: center;
        margin-bottom: 30px;
    }
    .profile-pic-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }
    .profile-pic {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        border: 5px solid #4CAF50;  /* Green border around the photo */
    }
    .about-section {
        display: flex;
        align-items: center;
        margin-top: 30px;
    }
    .about-text {
        flex: 1;
        font-size: 1.1em;
        line-height: 1.6;
        padding: 10px 20px;
        color: #555555;
    }
    .animation-container {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .cta-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
        justify-content: left;
    }
    .cta-buttons a {
        text-decoration: none;
        font-weight: bold;
        color: white;
        padding: 10px 15px;
        border-radius: 5px;
        transition: all 0.3s ease-in-out;
        display: inline-block;
    }
    .cta-buttons a:hover {
        transform: scale(1.05);
    }
    .github {
        background-color: #6e6e6e;  /* GitHub Grey */
    }
    .github:hover {
        background-color: #555555;  /* Darker grey on hover */
    }
    .linkedin {
        background-color: #0077b5;  /* LinkedIn Blue */
    }
    .linkedin:hover {
        background-color: #005582;  /* Darker LinkedIn Blue on hover */
    }
    .kaggle {
        background-color: #20beff;  /* Kaggle Blue */
    }
    .kaggle:hover {
        background-color: #00a1cc;  /* Darker Kaggle Blue on hover */
    }
    .email {
        background-color: #d44638;  /* Gmail Red */
    }
    .email:hover {
        background-color: #c13519;  /* Darker Gmail Red on hover */
    }
    .phone {
        background-color: #34b7a3;  /* Phone Green */
    }
    .phone:hover {
        background-color: #2f9981;  /* Darker Phone Green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a page", 
    [
        "👤 About Me", 
        "🎓 Education", 
        "💼 Experience", 
        "💻 Projects", 
        "🛠️ Skills", 
        "🏆 Hackathons", 
        "📜 Certifications"
    ]
)

if page == "👤 About Me":
    # Profile Photo and Title
    st.markdown('<div class="profile-pic-container"><img src="https://avatars.githubusercontent.com/u/76656957?s=400&u=bc621f5a3348e7c20b4f35584e89c994be6ff769&v=4" class="profile-pic"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Hi, I\'m Sannidhay Jangam</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI Enthusiast | Kaggle Contributor | Aspiring Data Scientist</p>', unsafe_allow_html=True)

    # About Me Section with Animation
    st.markdown("---")  # Divider
    st.markdown('<h2 style="text-align: center; color: #4CAF50;">About Me</h2>', unsafe_allow_html=True)
    st.markdown('<div class="about-section">', unsafe_allow_html=True)

    # Animation on the left
    st.markdown('<div class="animation-container">', unsafe_allow_html=True)
    st_lottie(lottie_animation, height=300, key="animation")
    st.markdown('</div>', unsafe_allow_html=True)

    # About Me Text on the right
    st.markdown(
        """
        <div class="about-text">
            Hello! , I am a passionate 3rd Year <strong>Artificial Intelligence and Data Science</strong> student at Shiv Nadar University Chennai with hands-on 
            experience in developing AI and ML solutions. Over the years, I have worked on several impactful projects such as 
            <strong>MultiModal Fake News Detection</strong>, <strong>Car Part Defect Detection</strong>, and <strong>Ovarian Cancer Detection</strong>. 
            My internships at <strong>HCL Technologies</strong> and <strong>Shiv Nadar University</strong> have allowed me to refine my skills in building 
            machine learning pipelines, optimizing model performance, and deploying AI systems in real-world scenarios.
            <br><br>
            I am skilled in frameworks like <strong>TensorFlow, PyTorch, and XGBoost , Neural Networks </strong> and have a deep understanding of various ML algorithms. 
            My work is focused on making AI systems efficient, scalable, and impactful, whether it's detecting financial fraud or recognizing mudras in Bharatanatyam.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)  # Close About Section

    # Connect with Me Section
    st.markdown("### Connect with Me")
    st.markdown(
        """
        <div class="cta-buttons">
            <a href="https://github.com/sannidhayj20" target="_blank" class="github">GitHub</a>
            <a href="https://www.linkedin.com/in/sannidhay-jangam-689641226" target="_blank" class="linkedin">LinkedIn</a>
            <a href="https://www.kaggle.com/sannidhayjangam" target="_blank" class="kaggle">Kaggle</a>
            <a href="mailto:sannidhay2004@gmail.com" class="email">Gmail</a>
            <a href="tel:+919740188366" class="phone">Phone</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "🎓 Education":
    # Title and Subtitle
    st.markdown('<h1 class="main-title">My Education</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Academic Journey</p>', unsafe_allow_html=True)
    # Display Lottie Animation
    st_lottie(
        education_animation,
        height=300,  # Adjust the height as needed
        key="education_lottie"
    )
    # Education Section
    st.markdown('<div class="education-section">', unsafe_allow_html=True)

    # Education Item 1: Bachelor of Technology at Shiv Nadar University
    st.markdown(
        """
        <div class="education-item" style="display: flex; align-items: center; margin-bottom: 20px;">
            <div class="image-container" style="width:200px; height: 100px; margin-right: 15px;">
                <img src="https://mli4sjv4v3cg.i.optimole.com/VIYEva8.EXct~4ba44/w:auto/h:auto/q:66/https://startupreporter.in/wp-content/uploads/2021/09/ShivNadarUniversityLogo-a641796f.jpg" 
                    style="width: 100%; height: 100%; object-fit: cover; border-radius: 5px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" />
            </div>
            <div>
                <h3 style="margin: 0;">Shiv Nadar University Chennai</h3>
                <p style="margin: 0;"><span>Bachelor of Technology - BTech, Computer Science (AI & DS)</span> | 2022 - 2026</p>
            </div>
        </div>
        <div style="margin-left: 75px; margin-top: 10px;">
            <h4>Relevant Courses:</h4>
            <ul style="font-size: 1.1em; line-height: 1.8; color: #555555;">
                <li>EN1001 - Communicative English</li>
                <li>MA1001 - Linear Algebra</li>
                <li>PH1001T - Engineering Physics</li>
                <li>BS1001 - Environmental Science and Engineering</li>
                <li>CS1001 - Programming in C</li>
                <li>CS1703 - Digital Design + Lab</li>
                <li>EA1001T - Extra Academic Activity</li>
                <li>EN1002 - English for Engineers</li>
                <li>MA1004 - Statistical Foundations of Data Science</li>
                <li>CS1002 - Programming in Python</li>
                <li>CS1006T - Data Structures</li>
                <li>CS1004 - Computer Organization and Architecture</li>
                <li>CS1704 - Foundations of Data Science + Lab</li>
                <li>MA2003 - Discrete Mathematics</li>
                <li>CS2003 - Object Oriented Programming</li>
                <li>CS2701 - Operating Systems + Lab</li>
                <li>CS2007 - Artificial Intelligence</li>
                <li>CS2009 - Exploratory Data Analysis and Data Visualization</li>
                <li>HS2001 - Cognitive Psychology</li>
                <li>CS2004 - Design and Analysis of Algorithms</li>
                <li>CS2001T - Database Management Systems</li>
                <li>CS2012 - Machine Learning Techniques</li>
                <li>CS2010 - Data Mining</li>
                <li>CS1502 - Fundamentals of Internet of Things</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Education Item 2: High School Diploma at Treamis School
    st.markdown(
    """
    <div class="education-item" style="display: flex; align-items: center; margin-bottom: 20px;">
        <div class="image-container" style="width: 200px; height: 100px; margin-right: 15px;">
            <img src="https://play-lh.googleusercontent.com/DIZKDqP1eREtEbdYdHnE868PunozejtHmosa2NV0G8GX6oXfVxjYogfiM5yhwPRodxE" 
                style="width: 100%; height: 100%; object-fit: cover; border-radius: 5px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" />
        </div>
        <div>
            <h3 style="margin: 0;">Treamis School</h3>
            <p style="margin: 0;"><span>High School Diploma, (SC - PCMC)</span> | Jun 2020 - Jun 2022</p>
            <p style="margin: 0;"><strong>Grade:</strong> 11 - 12</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Education Item 3: Schooling at Sri Chaitanya Techno School, Bangalore
    st.markdown(
    """
    <div class="education-item" style="display: flex; align-items: center; margin-bottom: 20px;">
        <div class="image-container" style="width: 200px; height: 100px; margin-right: 15px;">
            <img src="https://th.bing.com/th/id/OIP.pxYOiu6nj8fIh5vCQSlgVwHaD3?rs=1&pid=ImgDetMain" 
                style="width: 100%; height: 100%; object-fit: cover; border-radius: 5px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" />
        </div>
        <div>
            <h3 style="margin: 0;">Sri Chaitanya Techno School, Bangalore</h3>
            <p style="margin: 0;"><span>Jun 2018 - Mar 2020</span> | Grade: 9 - 10</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Education Item 4: Schooling at Freedom International School, India
    st.markdown(
    """
    <div class="education-item" style="display: flex; align-items: center; margin-bottom: 20px;">
        <div class="image-container" style="width: 200px; height: 100px; margin-right: 15px;">
            <img src="https://www.schoolmykids.com/smk-media/2018/11/Freedom-International-School-Bangalore.png" 
                style="width: 100%; height: 100%; object-fit: cover; border-radius: 5px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);" />
        </div>
        <div>
            <h3 style="margin: 0;">Freedom International School - India</h3>
            <p style="margin: 0;"><span>Jun 2007 - Apr 2018</span> | Grade: Nursery - 8</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
# Close Education Section
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "💼 Experience":
    # CSS for styling
    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff;  /* White background */
            font-family: 'Arial', sans-serif;
            color: #333333;  /* Text color */
        }
        .main-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 10px;
        }
        .sub-title {
            font-size: 1.5em;
            color: #555555;
            text-align: center;
            margin-bottom: 30px;
        }
        .experience-section {
            margin-top: 30px;
        }
        .experience-item {
            display: flex;
            margin-bottom: 20px;
            padding: 15px;
            border-left: 5px solid #4CAF50;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .experience-details {
            margin-left: 20px;
            width: 100%;
        }
        .experience-details h3 {
            font-size: 1.6em;
            color: #4CAF50;
            margin: 0;
        }
        .experience-details p {
            font-size: 1.1em;
            line-height: 1.6;
            color: #555555;
            margin: 5px 0;
        }
        .company-title {
            font-weight: bold;
            color: #4CAF50;
            font-size: 1.2em;
        }
        .image-container {
            width: 100px;  /* Adjust width for uniform image size */
            height: 100px; /* Adjust height to keep aspect ratio */
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 20px;
        }
        .image-container img {
            width: 100%;
            height: 100%;
            object-fit: contain;  /* Maintain aspect ratio */
        }
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }
        .skills-list span {
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 1em;
            color: #ffffff;  /* White text for contrast */
            background-color: #4CAF50;  /* Green background to highlight */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title and Subtitle
    st.markdown('<h1 class="main-title">My Experience</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Professional Journey and Contributions</p>', unsafe_allow_html=True)
    st_lottie(
        experience_animation,
        height=300,  # Adjust the height as needed
        key="experience_animation"
    )
    # Experience Section
    st.markdown('<div class="experience-section">', unsafe_allow_html=True)

    # Experience Item 1: Research Student at Shiv Nadar University Chennai
    st.markdown(
        """
        <div class="experience-item">
            <div class="image-container">
                <img src="https://media.licdn.com/dms/image/v2/C4D0BAQHGfGRVIn-zuQ/company-logo_200_200/company-logo_200_200/0/1630579158510?e=1740009600&v=beta&t=RB7XibMyC8ixSc5DrW7fBZB9Lp9Ocqb0E5FrrUASToE" />
            </div>
            <div class="experience-details">
                <p class="company-title">Shiv Nadar University Chennai</p>
                <h3>Stimuli for Technological Innovation and Research (STIRS) - Research Student</h3>
                <p>Internship | Nov 2023 - Present</p>
                <p><strong>Location:</strong> Chennai, Tamil Nadu, India</p>
                <p>As a Research Student at STIRS, I am actively involved in spearheading research and development initiatives. My primary focus is on the conceptualization and implementation of the cutting-edge Virtual Wardrobe project, blending fashion with technology.</p>
                <p><strong>Key Skills & Tech Stack:</strong></p>
                <div class="skills-list">
                    <span>TensorFlow</span>
                    <span>Machine Learning</span>
                    <span>Deep Learning</span>
                    <span>Computer Vision</span>
                    <span>Fashion Technology</span>
                    <span>Natural Language Processing</span>
                    <span>Python</span>
                    <span>Keras</span>
                    <span>Data Engineering</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Experience Item 2: Data Science Intern at HCLTech
    st.markdown(
        """
        <div class="experience-item">
            <div class="image-container">
                <img src="https://media.licdn.com/dms/image/v2/C4D0BAQF-RIoeeMTMKQ/company-logo_200_200/company-logo_200_200/0/1664197008219/hcltech_logo?e=1740009600&v=beta&t=Qcf43xJtpUb4ra8o047kiSzaO7x3SqUWqF8mJNr1yYw" />
            </div>
            <div class="experience-details">
                <p class="company-title">HCLTech</p>
                <h3>Data Science Intern</h3>
                <p>Internship | May 2024 - Jul 2024</p>
                <p>As a Data Science Intern at HCL Tech, I focused on improving fraud detection in financial transactions using machine learning techniques.</p>
                <p><strong>Key Contributions:</strong></p>
                <ul>
                    <li>Advanced data exploration and visualization using Python libraries (pandas, seaborn, matplotlib).</li>
                    <li>Developed sophisticated features to enhance fraud detection accuracy.</li>
                    <li>Implemented Synthetic Minority Over-sampling Technique (SMOTE) to address class imbalance.</li>
                    <li>Designed and optimized an XGBoost model for fraud detection, validated by accuracy and ROC-AUC metrics.</li>
                    <li>Collaborated with cross-functional teams to validate model efficacy and scalability.</li>
                </ul>
                <p><strong>Key Skills & Tech Stack:</strong></p>
                <div class="skills-list">
                    <span>Machine Learning</span>
                    <span>Python</span>
                    <span>XGBoost</span>
                    <span>Data Science</span>
                    <span>SMOTE (Synthetic Minority Over-sampling Technique)</span>
                    <span>Data Visualization (matplotlib, seaborn)</span>
                    <span>Data Analysis</span>
                    <span>Feature Engineering</span>
                    <span>Fraud Detection</span>
                    <span>Scikit-learn</span>
                    <span>Cross-validation</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Close Experience Section
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "💻 Projects":

    # Custom CSS to style the project items
    st.markdown("""
        <style>
            .main-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 10px;
            }
            .sub-title {
                font-size: 1.5em;
                color: #555555;
                text-align: center;
                margin-bottom: 30px;
            }
            .project-section {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                gap: 20px; /* Adds space between the boxes */
                margin-top: 30px;
            }
            .project-item {
                display: flex;
                flex-direction: column;
                width: 48%; /* Adjust this width to fit two boxes in a row */
                margin-bottom: 20px;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 10px;
                text-align: center;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }

            .project-title {
                font-size: 1.4em;
                font-weight: bold;
                color: #4CAF50;
                margin-bottom: 10px;
                cursor: pointer;
            }

            .skills-list {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 10px;
            }

            .skills-list span {
                padding: 8px 15px;
                border-radius: 20px;
                font-size: 1em;
                color: #ffffff;
                background-color: #4CAF50;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }

            .image-container {
                width: 60%;
                height: 200px;
                overflow: hidden;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }

            .image-container img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }

            .show-more-btn {
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #555555;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 1em;
                transition: background-color 0.3s ease;
            }

            .show-more-btn:hover {
                background-color: #444444;
            }

            /* Styling the GitHub link in a grey box */
            .github-link {
                display: inline-block;
                padding: 10px;
                background-color: #333333;
                color: white;
                border-radius: 5px;
                margin-top: 10px;
                text-decoration: none;
                font-size: 1.2em;
                text-align: center;
            }

            .github-link:hover {
                background-color: #555555;
            }

            /* Styling the Kaggle link in Kaggle blue with white text */
            .kaggle-link {
                display: inline-block;
                padding: 10px;
                background-color: #20BEFF; /* Kaggle blue */
                color: white;  /* White text */
                border-radius: 5px;
                margin-top: 10px;
                text-decoration: none;
                font-size: 1.2em;
                text-align: center;
                transition: background-color 0.3s ease;
            }

            /* Kaggle link hover effect */
            .kaggle-link:hover {
                background-color: #1A99D7; /* Darker blue on hover */
            }

            /* Ensures the link inside the Kaggle box is white */
            .kaggle-link a {
                color: white !important;  /* Force the text color to white */
                text-decoration: none;  /* Remove underline */
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-title">My Projects</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Showcasing Innovation and Creativity</p>', unsafe_allow_html=True)
    st_lottie(
        projects_animation,
        height=300,  # Adjust the height as needed
        key="projects_animation"
    )
    st.markdown('<div class="project-section">', unsafe_allow_html=True)

    # Project 1: FusionNet - Multimodal Sentiment Analysis
    with st.expander("FusionNet: Multimodal Sentiment Analysis"):
        st.markdown("""
            <p>A multimodal sentiment analysis project that achieved the highest score in the world on the EVALITA 2023 dataset.</p>
            <h3>Project Details</h3>
            <p>This project achieved an F1-score of 80.04 and an accuracy of 80.97, setting a new benchmark for sentiment classification.</p>
            <h3>Tech Stack & Skills</h3>
            <div class="skills-list">
                <span>Deep Learning</span>
                <span>Machine Learning</span>
                <span>Python</span>
                <span>Computer Vision</span>
                <span>Natural Language Processing (NLP)</span>
            </div>
            <h3>GitHub</h3>
            <p><a href="https://github.com/sannidhayj20/Multimodal-Sentiment-Classification" target="_blank" class="github-link">FusionNet GitHub</a></p>
            <h3>Kaggle</h3>
            <p><a href="https://www.kaggle.com/code/sannidhayjangam/multimodal-sentiment-classification-highest-acc" target="_blank" class="kaggle-link">FusionNet Kaggle</a></p>
            <h3>Images</h3>
            <div class="image-container">
                <img src="https://www.kaggleusercontent.com/kf/206702748/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..ups7jAzR3ldkkmVAScJywQ.1Ls90YLoAi_YJa14ZU8hbIuWK5LiCAqAT2nTsRHMh62ADK0NZgwot_8KKg4KKI7i5BfRmwPoZUBSNLIp7Uwp6Y3VsiO6jmyr8BdOFBAn0JdiSxywi4qnaC8SF4C_uNwkwxMz40MCGfbVEsASy0QRGekOXyd1NAYvW07LXy8XrdZmQY2LDPM2j-T479gePHyo-N00bOcJrHN4gXzY_RYaUkVZdbHIHtCDivfSh2IR8g1tHvBPldU4xSyCj14u4OiK2gMqxjyqQ4U3Rq9ryaGE78Ylw82bE2z25BCkCV-dtmkwiU8T8CbtUddg49jLJb3OHQdfm0jGT7FDUdtwD2SPWp88l9-Y9xiYCIBj5Vn7R-JvhOgQBePAszmvYWScfNQnGw2pSoDYMoGphgcDpbbjLpk9tnOHWjl1NTEdvsZEDRdxlaDF_XcyYWXQ8jIjeE_L_i9X69W9klwH5YvJYQVjYhV6tnETE1qLPE4hbjpljrUKwo92BUgp1qXrGjuOkJuRjGWuEKFAkjay4L5_V3_7HzdaPkT6PtOfogqU00KmKkY_jtIG0QP18Gd05AFSpxZWlJbWN_N0I92nEAFZIeiu1lxsd0oft0jBldSnXoBO3qpbucxXPWeVeX5npJxM4KnN_9ljRXY51qHZjH_c7hXHnJozuGldxsb9vnWrndzIGh3-H1s1mjwHEcBq7V5-IBfr.RywjccNmfFyaE07r6cR4kQ/__results___files/__results___23_7.png" />
            </div>
        """, unsafe_allow_html=True)


    # Project 2: Car Part Defect Detection
    with st.expander("Car Part Defect Detection"):
        st.markdown("""
            <p>AI-based system for detecting defects in car parts, ensuring high-quality standards in manufacturing.</p>
            <h3>Project Details</h3>
            <p>AI model for automotive defect detection, focusing on quality assurance and minimizing defects.</p>
            <h3>Tech Stack & Skills</h3>
            <div class="skills-list">
                <span>Machine Learning</span>
                <span>Computer Vision</span>
                <span>AI</span>
                <span>Python</span>
            </div>
            <h3>GitHub</h3>
            <p><a href="https://github.com/sannidhayj20/Car-Part-Defect-Detection" target="_blank" class="github-link">Car Part Detection GitHub</a></p>
            <h3>Images</h3>
            <div class="image-container">
                <img src="https://media.licdn.com/dms/image/v2/D562DAQHAEWkklcSWFw/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1722573533847?e=1732453200&v=beta&t=ql9wgKIxJJuxyXlCE4rM0hhKMd-RhfYXuIxo5Gmxpvw" />
            </div>
        """, unsafe_allow_html=True)

    # Project 3: Credit Card Fraud Detection
    with st.expander("Credit Card Fraud Detection"):
        st.markdown("""
            <p>Developed a machine learning model to detect fraudulent credit card transactions.</p>
            <h3>Project Details</h3>
            <p>Utilized SMOTE for handling class imbalance and XGBoost to achieve robust fraud detection.</p>
            <h3>Tech Stack & Skills</h3>
            <div class="skills-list">
                <span>Machine Learning</span>
                <span>SMOTE</span>
                <span>XGBoost</span>
                <span>Python</span>
            </div>
            <h3>GitHub</h3>
            <p><a href="https://github.com/sannidhayj20/Credit-Card-Fraud-Detection" target="_blank" class="github-link">Credit Card Fraud Detection GitHub</a></p>
            <h3>Kaggle</h3>
            <p><a href="https://www.kaggle.com/code/sannidhayjangam/xgboost-classification" target="_blank" class="kaggle-link">Credit Card Fraud Detection Kaggle</a></p>

        """, unsafe_allow_html=True)

    # Project 4: Ovarian Cancer Subtype Classification
    with st.expander("Ovarian Cancer Subtype Classification"):
        st.markdown("""
            <p>Developed a machine learning model for classifying ovarian cancer subtypes using the UBC-OCEAN dataset.</p>
            <h3>Project Details</h3>
            <p>Used Keras with a JAX backend to optimize performance for image classification.</p>
            <h3>Tech Stack & Skills</h3>
            <div class="skills-list">
                <span>Deep Learning</span>
                <span>Machine Learning</span>
                <span>Python</span>
                <span>Keras</span>
                <span>JAX</span>
            </div>
            <h3>GitHub</h3>
            <p><a href="https://github.com/sannidhayj20/Ovarian-Cancer-Subtype-Classification-UBC-Ocean.git" target="_blank" class="github-link">Ovarian Cancer Subtype GitHub</a></p>
        """, unsafe_allow_html=True)

    # Project 5: MudraMingle
    with st.expander("MudraMingle: Bharatanatyam Mudra Recognition"):
        st.markdown("""
            <p>A Flask-based ML app that detects and visualizes Bharatanatyam hand gestures in real-time.</p>
            <h3>Project Details</h3>
            <p>Uses OpenCV and MediaPipe to recognize Bharatanatyam mudras in real-time.</p>
            <h3>Tech Stack & Skills</h3>
            <div class="skills-list">
                <span>Machine Learning</span>
                <span>Computer Vision</span>
                <span>Flask</span>
                <span>Python</span>
            </div>
            <h3>GitHub</h3>
            <p><a href="https://github.com/sannidhayj20/MudraMingle" target="_blank" class="github-link">MudraMingle GitHub</a></p>
            <h3>Live Deployed Demo</h3>
            <p><a href="https://mudra-mingle.streamlit.app/" target="_blank" class="kaggle-link">Demo Link</a></p>
            <h3>Images</h3>
            <div class="image-container">
                <img src="https://media.licdn.com/dms/image/v2/D562DAQGm3KLRe5pU4A/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1703613299150?e=1732453200&v=beta&t=9QV-r2f6vc_kG5vBW9t-61chB6Us_n04wvbSVl7qFnY" />
                <img src="https://media.licdn.com/dms/image/v2/D562DAQHwy_d4uGFjfw/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1703613175341?e=1732453200&v=beta&t=veVkKRoneV8y0y2IThAcKXNdxULstcOyvQZQ9UlIZi8" />
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close the project section div

elif page == "🛠️ Skills":
    st.markdown("""
    <style>
        .section-title {
            font-size: 1.8em;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
            text-align: left;  /* Aligning the title to the left */
        }
        
        .skills-list {
            list-style-type: none;
            padding: 0;
            text-align: left;  /* Aligning the list items to the left */
        }
        
        .skills-list li {
            background-color: #f4f4f4;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .skills-list li span {
            font-weight: bold;
            color: #333;
        }
        
        .container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
            text-align: left;  /* Ensuring the entire content is left-aligned */
        }
        
        .section {
            margin-bottom: 40px;
        }
        
        </style>
    """, unsafe_allow_html=True)
    st.title("Skills & Expertise")

    # Container to wrap everything
    with st.container():

        # Technical Skills Section
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st_lottie(
        skills_animation,
        height=300,  # Adjust the height as needed
        key="skills_animation"
        )
        st.markdown('<p class="section-title">Technical Skills</p>', unsafe_allow_html=True)
        technical_skills = [
            ("Programming Languages:", "Python, Java, C, SQL"),
            ("AI/ML Frameworks:", "TensorFlow, PyTorch, XGBoost, Scikit-learn, Decision Trees, Random Forest, SVM, CNN's (DenseNet, ResNet)"),
            ("Data Analytics Tools:", "Pandas, NumPy, Matplotlib, SQL, Jupyter, Tableau, Power BI"),
            ("Deep Learning:", "CNNs, RNNs, Transfer Learning, Autoencoders, GANs"),
            ("Machine Learning:", "Supervised Learning (e.g., XGBoost, Random Forest), Unsupervised Learning (e.g., K-means, PCA), SMOTE, Model Evaluation (e.g., F1-Score, Accuracy)"),
            ("Computer Vision:", "Object Detection, Image Classification, OpenCV, MediaPipe, Image Preprocessing"),
            ("Natural Language Processing (NLP):", "Text Classification, Word Embeddings (Word2Vec, GloVe), Sequence Models (LSTMs, Transformers), BERT's (Bi-Directional Encoders Representation from Transformers)"),
            ("Data Analysis & Preprocessing:", "Data Cleaning, Feature Engineering, Dimensionality Reduction (PCA, LDA)"),
            ("AI & Automation:", "Real-time Gesture Recognition, Automated Image Inspection"),
            ("Data Visualization:", "Matplotlib, Seaborn, Plotly, Streamlit, Dashboards"),
            ("Version Control:", "Git and GitHub")
        ]
        
        st.markdown('<ul class="skills-list">', unsafe_allow_html=True)
        for skill, detail in technical_skills:
            st.markdown(f'<li><span>{skill}</span> {detail}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Soft Skills Section
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown('<p class="section-title">Soft Skills</p>', unsafe_allow_html=True)

        soft_skills = [
            "Problem-solving",
            "Teamwork",
            "Data-driven Decision Making",
            "Collaboration & Communication",
            "Research and Innovation",
            "Continuous Learning",
            "Project Management"
        ]
        
        st.markdown('<ul class="skills-list">', unsafe_allow_html=True)
        for skill in soft_skills:
            st.markdown(f'<li>{skill}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "🏆 Hackathons":
    st.markdown("""
    <style>
        .section-title {
            font-size: 1.8em;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
            text-align: left;  /* Aligning the title to the left */
        }
        
        .competitions-list {
            list-style-type: none;
            padding: 0;
            text-align: left;  /* Aligning the list items to the left */
        }
        
        .competitions-list li {
            background-color: #f4f4f4;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
            text-align: left;  /* Ensuring the entire content is left-aligned */
        }
        
        .section {
            margin-bottom: 40px;
        }
        
        </style>
    """, unsafe_allow_html=True)

    # Page title
    st.title("Hackathons & Competitions")

    # Container to wrap everything
    with st.container():

        # Hackathons & Competitions Section

        st.markdown('<div class="section">', unsafe_allow_html=True)
        st_lottie(
            hackathons_animation,
            height= 300,
            key="hakcathon-animation"
        )
        st.markdown('<p class="section-title">Hackathons & Competitions I have taken part in</p>', unsafe_allow_html=True)
    
        competitions = [
            ("VIVID 2023 Hackathon Winner:", "We Were the sole winner in Our Category and we Developed an AI-driven note-taking system using NLP and computer vision to capture lecture content."),
            ("Smart India Hackathon 2023 Qualifier (Ideation):", "Ideated and architectured a real-time AI tool to monitor groundwater levels using deep learning. The project was in the ideation phase, where we defined the modules and techniques required but didn't build it."),
            ("EY Techathon 2023 Participant:", "Created a cancer subtype prediction model leveraging cloud-based AI systems for healthcare innovation."),
            ("Tata Innovent 2024 Participant:", "Designed an AI system for real-time detection of automotive defects using computer vision and deep learning.")
        ]
        
        st.markdown('<ul class="competitions-list">', unsafe_allow_html=True)
        for competition, detail in competitions:
            st.markdown(f'<li><strong>{competition}</strong> {detail}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "📜 Certifications":
    st.markdown("""
    <style>
        .section-title {
            font-size: 1.8em;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
            text-align: left;
        }
        
        .certifications-list {
            list-style-type: none;
            padding: 0;
            text-align: left;
        }
        
        .certifications-list li {
            background-color: #f4f4f4;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
            text-align: left;
        }
        
        .section {
            margin-bottom: 40px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Page title
    st.title("My Certifications")

    # Container to wrap everything
    with st.container():

        # Licenses & Certifications Section
        st_lottie(certifications_animation,height=300,key="certification-animation")
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.markdown('<p class="section-title">Licenses & Certifications</p>', unsafe_allow_html=True)

        certifications = [
            ("Supervised Machine Learning: Regression and Classification", "Coursera", "Issued Jun 2024", "Skills: Machine Learning · Deep Learning", "https://coursera.org/share/022998f29633445a7b4e3c0775c940bc"),
            ("Deep Learning", "Kaggle", "Issued Jan 2024", "Skills: PyTorch · TensorFlow · Keras · Deep Learning", "https://www.kaggle.com/learn/certification/sannidhayjangam/intro-to-deep-learning"),
            ("Machine Learning", "Kaggle", "Issued Oct 2023", "Skills: Machine Learning · PyTorch · TensorFlow · Keras", "https://www.kaggle.com/learn/certification/sannidhayjangam/intro-to-machine-learning"),
            ("Problem Solving (Intermediate)", "HackerRank", "Issued Jun 2023", "Skills: Data Structures", "https://www.hackerrank.com/certificates/6031eba5f5e7"),
            ("Python", "HackerRank", "Issued Jun 2023", "Skills: Python", "https://www.hackerrank.com/certificates/b7bcddd557dd")
        ]
        
        st.markdown('<ul class="certifications-list">', unsafe_allow_html=True)
        for cert_name, issuer, issued_date, skills, link in certifications:
            st.markdown(f'<li><strong>{cert_name}</strong> by {issuer} <br><em>{issued_date}</em><br><span>{skills}</span><br>', unsafe_allow_html=True)
            if link:
                st.markdown(f'<a href="{link}" target="_blank">Show credential</a>', unsafe_allow_html=True)
            st.markdown('</li><br>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
