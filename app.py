projects = [
    {
        "title": "Game Developer",
        "role": "ANTI Elixir",
        "location": "Miami, Florida",
        "date": "Oct 2024 - Present",
        "description": """
        - Optimized 20+ game levels for FLY HERO, reducing completion time by 8% and boosting retention by 5%.
        - Implemented Firebase-based in-game economy, increasing transactions by 11%.
        - Resolved critical bugs, enhancing game stability.
        """,
        "technologies": ["Firebase", "Unity", "C#", "Game Optimization"]
    },
    {
        "title": "Research Assistant",
        "role": "Florida International University",
        "location": "Miami, Florida",
        "date": "Oct 2022 - Aug 2024",
        "description": """
        - Developed VR tech for safer inspections at the Dept. of Energy's Waste Isolation Pilot Plant.
        - Analyzed point cloud data, achieving 96% accuracy in nuclear facility change detection.
        - Automated analysis tasks, boosting team efficiency.
        """,
        "technologies": ["Unity", "Unreal Engine", "Point Cloud Analysis", "VR Technology"],
        "video_path": "images/arc_vid.mp4"
    },
    {
        "title": "Law Enforcement De-Escalation Training",
        "role": "Project Lead",
        "location": "Miami, Florida",
        "date": "Aug 2023 - Dec 2023",
        "description": """
        - Created LEADER, an AI-driven VR Police De-escalation Simulator using DOJ guidelines.
        - Integrated Llama 2, Amazon Polly, and Hugging Face for immersive AI-driven dialogue.
        """,
        "technologies": ["Unity", "Amazon Polly", "Llama 2", "Hugging Face SDK", "VR Simulation"],
        "video_path": "images/capstone.mp4"
    },
    {
        "title": "Augmented Reality Sign Language",
        "role": "Developer",
        "location": "ShellHacks 2024, Miami, Florida",
        "date": "Sept 2024",
        "description": """
        - Developed ARSL, an AR app for ASL learning with 96% gesture recognition accuracy.
        """,
        "technologies": ["Unity", "YOLO", "Augmented Reality", "Computer Vision"],
        "video_path": "images/aslr.mp4"
    },
    {
        "title": "Game Studio Founder",
        "role": "Founder/Developer",
        "location": "Miami, Florida",
        "date": "Oct 2022 - July 2023",
        "description": """
        - Founded indie game studio; launched three mobile games.
        - Developed 'Asteroids Ahead' with physics-based gameplay and challenging AI.
        - Deployed Rainbow Run, an endless runner game, with smooth performance even on low-end devices.
        """,
        "technologies": ["Unity", "C#", "Mobile Game Development", "Physics Engine"],
        "image_path": "images/moonmoon1.png"
    },
    {
        "title": "AI-Powered Music Therapy Tool",
        "role": "Lead Developer",
        "location": "Miami, Florida",
        "date": "Sept 2023 - Nov 2023",
        "description": """
        - Built an AI-powered music recommendation website integrating Amazon Comprehend and Spotify API.
        - Provided personalized playlists based on user sentiment analysis.
        """,
        "technologies": ["Machine Learning", "Amazon Comprehend", "Spotify API", "Web Development"]
    }
]

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Daniel Estrada's Portfolio",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 8rem;
    }
    .stTitle {
        font-size: 3rem !important;
        color: #1E88E5;
    }
    .tech-tag {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        margin: 0.30rem;
        border-radius: 15px;
        background-color: #E3F2FD;
        color: #1E88E5;
        font-size: 0.9rem;
    }
    .project-header {
        color: #1E88E5;
        font-size: 1.2rem;
    }
    .location-date {
        color: #666;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Header section
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Daniel Estrada")
    st.markdown("### Game Developer | Software Engineer ")


with col2:
    st.markdown("""
    **🌎 Miami, Florida**  
    **📧 pildoestrada@gmail.com**  
    """)

# Skills section



# Function to display project with enhanced styling
def display_project(title, role, location, date, description, technologies, image_path=None, video_path=None):
    # Map project types to emojis
    emoji_map = {
        "Game Developer": "🎮",
        "Research Assistant": "🔬",
        "Project Lead": "👨‍💼",
        "Developer": "👨‍💻",
        "Founder/Developer": "🚀",
        "Lead Developer": "👨‍💻"
    }
    
    emoji = emoji_map.get(role, "💡")
    
    with st.expander(f"{emoji} {title}", expanded=False):
        st.markdown(f"**Role:** {role}")
        st.markdown(f"**🌎 {location} | 📅 {date}**")
        
        # Create columns for content
        if image_path or video_path:
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown("### Key Achievements")
                st.markdown(description)
            with col2:
                if image_path:
                    st.image(image_path, use_column_width=True)
                if video_path:
                    st.video(video_path)
        else:
            st.markdown("### Key Achievements")
            st.markdown(description)
        
        st.markdown("### 🛠️ Technologies")
        for tech in technologies:
            st.markdown(f'<span class="tech-tag">{tech}</span>', unsafe_allow_html=True)

# Add sections with enhanced headers
st.markdown("---")
st.markdown("## 💼 Professional Experience & Projects")

# Display each project
for project in projects:
    display_project(
        project["title"], 
        project["role"], 
        project["location"], 
        project["date"], 
        project["description"], 
        project["technologies"], 
        project.get("image_path"), 
        project.get("video_path")
    )
st.markdown("---")
st.markdown("## Core Technologies")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🎮 Game Development")
    st.markdown("- Unity\n- C#\n- Unreal Engine\n- C++\n- VR/AR")
with col2:
    st.markdown("### 🤖 AI & ML")
    st.markdown("- Tensorflow\n- Hugging Face\n- AWS\n- Azure\n- SQL")

# Footer
st.markdown("---")
st.markdown("### 📫 Let's Connect!")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🌐 [LinkedIn](https://linkedin.com)")
with col2:
    st.markdown("💻 [GitHub](https://github.com)")
with col3:
    st.markdown("📧 [Email](mailto:pildoestrada@gmail.com)")