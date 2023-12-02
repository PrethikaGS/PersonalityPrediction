import streamlit as st
# a44a3f f19c79 cbdfbd f6f4d2 d4e09b


def main():
    st.markdown(
    """
    <style>
        body {
        background-color: #c9cba3  ;
    }
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #472d30;
        text-align: center;
        margin-top: 0px;
        justify-content: center;
    }

        .sub-header {
            font-size: 36px;
            font-weight: bold;
            color: #472d30;
            text-align: center;
            margin-top: 10px;
        }

        .description {
            font-size: 18px;
            color: #000000;
            text-align: center;
            margin-top: 20px;
        }

        .questions{
            font-size: 18px;
            color: #472d30;
            margin-top: 50px;
        }

        .notes{
            font-size: 20px;
            font-weight: bold;
            color: #e26d5c;
        }

        .st-eb {
            color: green;  /* Slider color */
        }
        
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Main header
    st.write('<div class="header">Personality Prediction</div>', unsafe_allow_html=True)
    st.image("personalities.png", use_column_width=True)
    st.write('<div class="description">Comprehending and predicting personality is an interesting study into the individuality of every person. The intricate combination of traits, and features make up our personalities. It affects our inclinations, social interactions, professional decisions, and even how we respond to challenges in life.',unsafe_allow_html=True)
    st.write("<div class='description'>The science of identifying these characteristics is the focus of personality prediction, which offers insights about a person's inclinations, preferences, and responses to diverse circumstances. Welcome to the Personality Assessment. This quick questionnaire will help you gain insights into your personality traits.",unsafe_allow_html=True)
    st.write("<div class='description'>This page is a questionnaire, each focusing on a specific personality trait: Openness, Neuroticism, Conscientiousness, Agreeableness, and Extraversion.<br><br>",unsafe_allow_html=True)
    st.image("personalities2.png", use_column_width=True)
    
    
    st.write("<br>" * 5, unsafe_allow_html=True)
    st.write('<div class="sub-header"> Lets get started!!!</div>', unsafe_allow_html=True)
    st.write("<div class='description notes'>For every question move the slider to your desired value with 10 being the most agreeable to the question and 1 being the least agreeable.",unsafe_allow_html=True)
    # Input sliders for personality scores

    st.write("<div class='questions'>How willing are you to understand and empathize with others' viewpoints, even if they differ from your own?</div>", unsafe_allow_html=True)
    agreeableness_1 = st.slider("", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How much do you enjoy working in team settings and collaborative environments?</div>", unsafe_allow_html=True)
    extraversion_1 = st.slider(" ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>Are you usually punctual and strive to meet deadlines?</div>", unsafe_allow_html=True)
    conscientiousness_1 = st.slider("   ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'> Are you drawn to adventures and travel to unfamiliar places?",unsafe_allow_html=True)
    openness_1 = st.slider("    ",min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How well do you generally react to unexpected challenges or stress in your life?</div>", unsafe_allow_html=True)
    neuroticism_1 = st.slider("     ", min_value=1, max_value=10, value=0)  
    st.write("<div class='questions'>How much do you tend to be methodical and detail-oriented in your work or projects?</div>", unsafe_allow_html=True)
    conscientiousness_2 = st.slider("      ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>In group situations, do you often go along with what the majority wants to avoid conflict?</div>", unsafe_allow_html=True)
    agreeableness_2 = st.slider("       ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How comfortable are you with unconventional or avant-garde ideas and art forms?</div>", unsafe_allow_html=True)
    openness_2 = st.slider("        ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How often are you prone to mood swings or emotional fluctuations?</div>", unsafe_allow_html=True)
    neuroticism_2 = st.slider("         ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>Do you feel energized and recharged after spending time with others?</div>", unsafe_allow_html=True)
    extraversion_2 = st.slider("          ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How well do you handle conflicts and disagreements in your relationships?</div>", unsafe_allow_html=True)
    agreeableness_3 = st.slider("           ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>Do you frequently find yourself worrying about things that might go wrong?</div>", unsafe_allow_html=True)
    neuroticism_3 = st.slider("            ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How often do you actively seek out and embrace new experiences or viewpoints in your life?</div>", unsafe_allow_html=True)
    openness_3 = st.slider("             ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How much do you enjoy socializing with new people and being the center of attention in a group?</div>", unsafe_allow_html=True)
    extraversion_3 = st.slider("              ", min_value=1, max_value=10, value=0)
    st.write("<div class='questions'>How important is it for you to keep your living and working spaces neat and well-organized?</div>", unsafe_allow_html=True)
    conscientiousness_3 = st.slider("               ", min_value=1, max_value=10, value=0)




    # Calculate and display personality description based on scores
    personality_description = get_personality_description(openness_1, neuroticism_2, conscientiousness_3, agreeableness_2, extraversion_1)
    st.write(personality_description)

def get_personality_description(openness, neuroticism, conscientiousness, agreeableness, extraversion):
    # You can implement your own logic to provide a personality description based on the scores.
    # This is just a placeholder example.
    if openness >= 7 and extraversion >= 7:
        return "You are open-minded and highly extraverted."
    elif conscientiousness >= 6:
        return "You are conscientious and responsible."
    elif agreeableness >= 6:
        return "You are a friendly and agreeable person."
    else:
        return "Your personality is a mix of traits."

if __name__ == '__main__':
    main()
