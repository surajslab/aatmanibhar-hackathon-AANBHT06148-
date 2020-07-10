import pandas as pd
import numpy as np
import sklearn

from sklearn.utils import shuffle
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def solutions():
    import random


    sol1="\nCognitive behavioural therapy\nCBT helps you evaluate how you think about danger and teaches techniques for revaluating the degree of that threat, says Dr. Norton. You learn to shift your worry\n to match the actual amount of danger, he adds. In one review, 46% of people whose anxiety was treated \nwith this talk therapy responded, versus 14% of those who received no CBT. You usually engage in an \nhour-long session every week for 3 to 4 months,insurance may cover it.\n\n\n"
    sol2="\nMeditation \nIn anxious people, we see a deactivation in areas of the brain that govern thought, so\nworries can spiral out of control, says Fadel Zaiden, PhD, a research fellow at Wake Forest School of Medicine.\n Mindfulness meditation helps you stop the cycle of worry. In Dr. Zaiden’s study, anxiety levels of meditators\neased by up to 39%.\n\n\n "
    sol3="\nYoga \n Hour-long yoga sessions three times a week improved people's moods and anxiety levels after \n12 weeks in one study. The level of GABA (gamma-aminobutyric acid), an amino acid in the brain, is lower in \npeople who report anxiety. Among study participants who took a yoga class, GABA levels increased and reports\nnext of anxiety decreased after the session. Yoga's deep breathing stimulates the parasympathetic nervous \nsystem, which is associated with the ability to relax, says Chris C. Streeter, MD, an associate professor \nat Boston University School of Medicine. \n\n\n"
    sol4="\nAttention \n Cognitive bias modification helps change a person's pattern of thinking, \nsays Risa Weisberg, PhD, an associate professor at Alpert Medical School at Brown University.\n Different clinics administer CBM differently; you might watch a computer screen with \n threatening and nonthreatening faces and perform tasks that lessen your anxiety when the \nscary face appears. You can find attention modification via a computer program, developed\nin partnership with San Diego State University, at managingyouranxiety.com. Four modules—for \nsocial anxiety, GAD, fear of public speaking, and fear of germs—are available for $139.99 each.\n\n\n"
    sol5="\nDrugs \n For chronic anxiety, your doctor may prescribe a selective serotonin reuptake inhibitor. \nSSRIs, such as paroxetine (Paxil) and sertraline (Zoloft), affect serotonin levels and can improve mood and \nlessen anxiety. It takes 4 to 8 weeks to see if the drug works for you, says Franklin Schneider, MD, a\nprofessor of clinical psychiatry at Columbia University. Tranquilizers, including alprazolam (Xanax), \nmay cause dependency, so they're usually prescribed for short-term use for problems such as fear of \nflying. These work almost immediately, says Dr. Schneier. Discuss anxiety drugs' side effects with \nyour doctor; never combine tranquilizers with alcohol.\n\n\n"
    sol6="\nHerbs \nTaking kava for 6 weeks eased anxiety for 26% of people with GAD in a 2013 study. Research \nshows that it's effective for up to 6 months. Kava is available in capsules and liquid tinctures\nfollow label directions.\n\n\n "
    sol7="\nSleep \nNorwegian researchers discovered that sleep-deprived people are more likely to be \nanxious. Here's why: Sleep loss activates areas of the brain that are also activated during anxiety,\nsays Jack B. Nitschke, PhD, an associate professor of psychiatry and psychology at the University of \nWisconsin School of Medicine in Madison. To ward off the willies, aim to get 7 to 9 hours of sleep each\nnight. Dr. Nitschke suggests stepping away from electronic devices 30 minutes before bedtime and \njotting your worries down on paper.\n\n\n"




    x = random.randint(0,6)
    solutions=[sol1,sol2,sol3,sol4,sol5,sol6,sol7]
    print("Some practices for better life and to avoid the above problems:")
    print(solutions[x])


features=["Irritability","Restlessness","Lack_of_concentration","Racing_thoughts","Unwanted_thoughts","Fatigue" ,"Sweating","Aggression","Social isolation","Delusion","Abdominal cramping","Chest pain","Headache","Dizziness","Lightheadedness","Numbness ","Faintness"]


# reading the data
df=pd.read_csv("data.csv")
predict="Predict"
x=np.array(df.drop([predict],1))
y=np.array(df[predict])

#spliting an training the data
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=42)
svm_model=SVC()
svm_model.fit(X_train,y_train)

value=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
imp=[]

print("Enter your ratings for the following feelings from (1-10)...")
for i in range(16):
    
  
    value[i]=int(input(features[i]+" :"))
    value[i]=(value[i]/10)
    if value[i]> 0.6:
        imp.append(features[i])


value=np.array(value)
y_predict=svm_model.predict(value.reshape(1,17))

if y_predict == 0:
    print("Your condition is abnormal, please do consult a doctor.")


    
   
if y_predict== 1:
    print("\nYou dont have any MENTAL ILLNESS")
    x=len(imp)
    print("\nYOU FACE PROBLEM ONLY IN :")
    for i in range((x)):
        no=str(i+1)
        print("\n"+no+"."+imp[i]+"\n")
    solutions()
    
   

    



        






