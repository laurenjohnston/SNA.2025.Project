import streamlit as st
from PIL import Image

# --- Banner Image ---
st.image("banner.webp", use_container_width=True)

# --- Title and Authors ---
st.title("Perceived Support and Social Centrality in University Social Networks")
st.subheader("SNA.2025.Project by Saran, Lauren, Lane, Molly, and Ellie")

# --- Introduction ---
st.header("Introduction")
st.write("""
This project explores how social connections shape students’ experiences within a university network.

Using data from the NetHealth study, we examine how different types of relationships, levels of perceived support, and shared identities — like religion — influence students’ positions and patterns in the broader social structure.
""")

# --- Research Question ---
st.header("Research Question")
st.write("""
**How do social connections—particularly friendships, perceived support, and shared identity—shape students’ roles and behaviors within a university network?**
""")

# --- Hypotheses ---
st.header("Hypotheses")
st.markdown("""
1. **H1**: 'Friend' relationships are associated with higher support ratings than 'Family'.  
2. **H2**: Students form social ties with peers sharing religious affiliation.
""")

# --- Hypothesis 1 ---
st.subheader("Hypothesis 1: Friend vs Family Support")
st.write("""
- Categorical Variable: `reltypecat` (Friend, Family)
- Support Variables: `suppfin`, `suppcomf`, `supphang`, `suppadv` (0/1)
""")
st.image("hypothesis1_graph1.png")
st.image("hypothesis1_graph2.png")
st.markdown("""
 **Context**:
- suppfin: Financial Support
- suppcomf: Emotional/Comfort Support
- supphang: Social/Hangout Support
- suppadv: Advice Support
""")

st.image("t_test_results.png")
st.markdown("""
✅ **Findings**:
- Friends offer more support for “hanging out.”
- Family offers more support in financial, comfort, and advice categories.
""")

# --- Hypothesis 3 ---
st.subheader("Hypothesis 2: Religious Affiliation and Social Ties")
st.markdown("""
**Our Hypothesis**
- Students who report more friendship ties tend to exhibit higher degree centrality, suggesting that friendships play a key role in shaping students’ positions within the social network.
"")

st.image("religion_support_1.png", caption="Same-religion edge proportion")
st.markdown("""
📊 **Observation**:  
79.4% of all social ties (edges) in the filtered network are between students who report the same religion.  
> Out of 2,931 social ties among students with known religious affiliation, **2,327 (79.4%)** connected individuals who shared the same religion.

✅ **Conclusion**: Strong support for religious homophily — students with shared religion are significantly more likely to form ties.
""")

st.image("religion_support_2.png", caption="Tie breakdown and chi-square result")
st.markdown("""
- **2276 ties** are between two Catholics  
- **51 ties** are between two Protestants  
- **604 ties** are between a Catholic and a Protestant  

📊 **Expected values under random mixing**:
- Protestant–Protestant ties: expected 121, observed 51  
- Catholic–Protestant ties: expected 533, observed 604

🔬 **Statistical Test**:  
Chi-Square = **60.59**, p-value = **7.02e-15**  
✅ **Statistically significant**: Students connect in **non-random** ways.

📌 **Takeaway**:  
There are **more within-religion** ties and **fewer cross-religion** ties than expected. Students form connections based on **shared religion**.
""")

st.image("religion_support_3.png", caption="Edge Mixing Matrix by Religion")
st.image("religion_support_4.png", caption="Expected Matrix under Random Mixing")
st.markdown("""
🔍 **Interpretation**:
- Most edges are Catholic–Catholic (2276), showing diagonal dominance.
- Protestant–Protestant connections are very few.
- Cross-religion ties are present but less common than expected.

📌 **Conclusion**:  
These findings consistently support **religious homophily** — the tendency to connect with peers of the same religion.
""")

# --- References ---
st.header("References")
st.markdown("""
Perry, B. L., Reczek, C., & Boardman, J. D. (2024). *Undiagnosed: Relational characteristics of mental health pre-diagnostic self-labeling.* Social Science & Medicine, 342, 116332.  
[DOI](https://doi.org/10.1016/j.socscimed.2024.116332)
""")