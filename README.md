# Perceived Support and Social Centrality in University Social Networks 
_SNA.2025.Project BY Saran, Lauren, Lane, Molly, and Ellie_

## Introduction
- This project explores how social connections shape students’ experiences within a university network.

- Using data from the NetHealth study, we examine how different types of relationships, levels of perceived support, and shared identities — like religion — influence students’ positions and patterns in the broader social structure.

- Our analysis highlights how friendships and social identity help shape who students are connected to.

**Research question**
> How do social connections—particularly friendships, perceived support, and shared identity—shape students’ roles and behaviors within a university network?


## Hyphothesis 1
Relationships categorized as 'Friend' are associated with higher support ratings compared to 'Family' .<br/>

### Data Structure
**Data Types:**

reltypecat is a categorical variable (e.g., Friend, Family)
suppfin, suppcomf, supphang, suppadv are numerical support variables (coded as 0 or 1)<br/>
<br/>

**Missing Data:**

Rows with missing relationship types or support values were removed to ensure valid analysis<br/><br/>

**Descriptive Stats:**

Means and distributions were calculated for support types to explore overall patterns<br/><br/>

**Unique Relationship Categories:**

Friend and Family were the two most frequent relationship types
These were selected for direct comparison in hypothesis testing<br/><br/>

#### Graphs
<img width="695" alt="Screenshot 2568-05-01 at 11 03 04" src="https://github.com/user-attachments/assets/94dda1ae-c66e-4a47-add8-fc9fc742ad32" /> <img width="616" alt="Screenshot 2568-05-01 at 11 04 24" src="https://github.com/user-attachments/assets/a4de1768-f209-4db1-ab88-b41b62d2091b" />

#### T-Test Results
<img width="600" alt="Screenshot 2568-05-01 at 11 07 25" src="https://github.com/user-attachments/assets/c6cbad7d-b7a6-43b9-ace4-61b598841915" />

> - All p-values are < 0.05 → statistically significant differences.
> - Friends offer more support for “hanging out.”
> - Family members offer more support in financial, comfort, and advice categories

## Hyphothesis 2
Students who list more ‘Friend’ alter ids are more socially embedded in the network and have a higher centrality.
<img width="321" alt="Screenshot 2568-05-01 at 11 10 48" src="https://github.com/user-attachments/assets/95cd0470-136a-43ec-bb79-58079483e3c7" /> <img width="324" alt="Screenshot 2568-05-01 at 11 10 58" src="https://github.com/user-attachments/assets/d1964ec1-88e7-4d74-b896-012796273ea6" />

Each node represents a student
Each edge represents a social connection

Node size = Degree centrality
Larger nodes have more direct ties
Indicates greater social embeddedness
Node color = Centrality level
Darker red indicates higher centrality
Central nodes are more influential in the network

> **Key takeaway:**
> The network shows a dense core of highly connected students
> This supports our hypothesis that friendship ties are linked to higher centrality

<img width="470" alt="Screenshot 2568-05-01 at 11 12 06" src="https://github.com/user-attachments/assets/31de8681-7598-4588-9ca2-22e9f3fe355c" />
**Key finding:**
There is a clear, positive correlation between the number of friendship ties and network centrality

Students who list more friends are more connected overall and occupy more central positions

**Interpretation:**
This further  supports our second hypothesis.



## Hyphothesis 3
Students are more likely to form social ties with peers who share their religious affiliation.

<img width="374" alt="Screenshot 2568-05-01 at 11 12 46" src="https://github.com/user-attachments/assets/a2224ca3-4940-4bb6-8b41-1265c8da69f6" />

Each node represents a student
Each edge represents a social connection

Node size = Degree centrality
Larger nodes have more direct connections
Indicates greater social embeddedness
Node color = Students Religious affiliation
Catholic, Protestant, NoReligion, Other, or Unknown

**Key observation:**
Clusters where students of the same religious background are more likely to be connected.
EX. Catholic students (light blue) tend to form tightly connected groups with other Catholic peers.
Protestant and non-religious students are also seen clustering, though often in smaller or more dispersed groupings.

**Interpretation:**
These patterns suggest religious homophily — students are more likely to form social ties with others who share their religious identity.
This supports Hypothesis 3 and highlights how shared beliefs can shape social structure, even in informal peer networks.

# REFERFENCES
Perry, B. L., Reczek, C., & Boardman, J. D. (2024). _Undiagnosed: Relational characteristics of mental health pre-diagnostic self-labeling_. Social Science & Medicine, 342, 116332. https://doi.org/10.1016/j.socscimed.2024.116332
