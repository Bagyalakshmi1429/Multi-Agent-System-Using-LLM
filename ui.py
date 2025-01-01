import streamlit as st
from crewai import Crew, Process
from agents import researcher, writer  # Importing the agents
from tasks import researchtask, writertask  # Importing the tasks
import os

def display_title():
    st.set_page_config(page_title="🚀 Multi-Agent News Article Writing System 📝", page_icon="📚")
    st.title("🚀 Multi-Agent News Article Writing System 📝")
    st.write(
        "This system harnesses the power of multiple agents working together to write a compelling and informative article. "
        "Our agents will research the latest trends and technologies in your desired topic and craft an engaging article for you. "
        "Let the magic happen! 💫"
    )
    st.write("### How it works:")
    st.write("1️⃣ Research Agent: Conducts in-depth research on the topic 🔍")
    st.write("2️⃣ Writer Agent: Converts research into a readable, engaging article ✍️")
    st.write("3️⃣ You receive a polished article ready for publication 📰")

def display_input():
    topic = st.text_input("Enter a topic you want an article on: ", "Mpox in 2024")
    
    if st.button("Generate Article 📜"):
        if not topic:
            st.warning("⚠️ Please enter a valid topic!")
            return

        try:
            with st.spinner(f"📝 Generating article on **{topic}**..."):
                # Dynamically set the topic and run the crew
                crew = Crew(
                    agents=[researcher, writer],
                    tasks=[researchtask, writertask],
                    process=Process.sequential,
                )
                
                # Pass the user-entered topic to crew.kickoff
                outcome = crew.kickoff(inputs={'topic': topic})
                
                # Check if the output file exists
                output_file = 'article.md'  # Matches the output_file in writertask
                if os.path.exists(output_file):
                    with open(output_file, 'r', encoding='utf-8') as file:
                        article_content = file.read()
                    
                    st.success("📰 **Article Generated Successfully!**")
                    st.write(f"Here's the article on {topic}:")
                    st.markdown(f"**{topic}**\n\n{article_content}")
                else:
                    # If the file doesn't exist, try to retrieve content directly from the outcome
                    if hasattr(outcome, 'raw_output'):
                        st.success("📰 **Article Generated Successfully!**")
                        st.write(f"Here's the article on {topic}:")
                        st.markdown(f"**{topic}**\n\n{outcome.raw_output}")
                    else:
                        st.error("❌ Unable to retrieve the article content. Please try again.")
                        
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.warning("Please try again or contact support if the issue persists.")

def main():
    display_title()
    display_input()
    st.markdown(
        """
        ---
        <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0E1117; padding: 15px; text-align: center;">
            © <a href="https://github.com/Bagyalakshmi1429/Multi-Agent-System-Using-LLM" target="_blank">Bagyalakshmi S Shinde</a> | Made with ❤️
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
