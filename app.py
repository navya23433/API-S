import pdfplumber
pdf_path=r"d:\Kasireddy navyasree.pdf"
with pdfplumber.open(pdf_path) as pdf:
    text=""
    for page in pdf.pages:
        text+=page.extract_text()+ "\n"
count_of_skills=[]
skills=["python","java","sql","html","css","api","excel"] 
print("required_skills",skills)
for skill in skills:
    if skill.lower() in text.lower() :
        count_of_skills.append(skill)
print("matched_skills",count_of_skills)
total_skills=len(skills)
matched=len(count_of_skills)
score=(matched/total_skills)*100
print("match_percentage",score)