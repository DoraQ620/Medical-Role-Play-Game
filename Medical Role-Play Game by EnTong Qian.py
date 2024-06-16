print("Welcome to the Medical Role-Play Game!\n")
print("Today, you will step into the shoes of two essential roles in medicine: Emergency Doctor and General Practitioner.")
print("Experience the challenges and rewards of diagnosing patients, making critical decisions, and providing compassionate care.")
print("Are you ready to embark on this immersive journey into the world of healthcare? Let's begin!")

# PART 1:
class Patient:
    def __init__(self):
        self.age = 70
        self.condition = "chest pain, radiating to left arm and back"
        self.symptoms = {
            "Airway": "Difficulty breathing and chest tightness, provide necessary oxygen.",
            "Breathing": "Rapid shallow breathing, difficulty breathing, provide oxygen support",
            "Circulation": "High heart rate and high blood pressure",
            "Disability": "Confused consciousness",
            "Exposure": "Abnormal body temperature, excessive sweating, cold skin",
        }
        self.pain_assessment = {
            "Site": "Central chest area, feels like a pressing pain.",
            "Onset": "Started about half an hour ago, initially not obvious.",
            "Character": "A pressing sensation, like something heavy pressing on the chest.",
            "Radiation": "No, mainly concentrated in the chest.",
            "Associated symptoms": "He's been sweating and has some difficulty breathing.",
            "Timing": "The pain started suddenly and has been continuous, with no specific pattern.",
            "Exacerbating and relieving factors": "He feels slightly better when sitting down, but moving or deep breathing makes it worse.",
            "Severity": "8, he is clutching his chest and looks in great pain.",
        }
        self.medical_history = ["Hypertension", "Mild diabetes"]
        self.current_medications = ["Medications for hypertension and diabetes"]
        self.family_history = ["None"]
        self.lifestyle = "He pays attention to diet and healthy living, but recently he often feels chest discomfort."

    def ask_history(self):
        questions = [
            "What past health problems or treatments has he had?",
            "Has he used any medications in the past? Any allergies or adverse reactions to medications?",
            "Does anyone in your family have similar health problems?",
            "What is his daily life like and how has he been feeling recently?",
        ]

        emotions = [
            "He has a history of hypertension and mild diabetes... I'm really worried about him.",
            "He's been taking medications for hypertension and diabetes, and I'm not sure if these medications have any side effects.",
            "No, no one in our family has had similar health issues, I really don't know what to do.",
            "He usually pays attention to diet and healthy living, but recently he's been complaining about chest discomfort. I thought it was just a minor issue, but I didn't expect it to be this serious.",
        ]

        for question, emotion in zip(questions, emotions):
            input(f"Emergency Doctor: {question}")
            print(f"Son: {emotion}")

    def bedside_tests(self):
        print("Test results are out!!")
        print("BEDSIDE test:")
        print("Blood Glucose: Normal")
        print("Blood Oxygen Saturation: Below normal")
        print("ECG: Shows signs of myocardial infarction")
        print("Blood test: Elevated cardiac enzymes")
        print("Imaging: Chest X-ray shows enlarged heart shadow")

    def follow_up_treatment(self):
        print(
            "Emergency percutaneous coronary intervention (PCI), such as coronary stent implantation"
        )
        print(
            "Narrator: Follow-up care and rehabilitation with team members: including cardiac rehabilitation nurses, physiotherapists, dietitians, psychological counselors, etc."
        )


def ask_assessment(patient):
    print(
        "You starts to find out the patient's condition based on the basic assessments (HINT: using the ABCDE assessment method):"
    )
    questions = ["Airway", "Breathing", "Circulation", "Disability", "Exposure"]

    while questions:
        question = input(
            "Pick a assessment item (Airway, Breathing, Circulation, Disability, Exposure): "
        )
        for key in questions:
            if key.lower() in question.lower():
                print(f"Answer: {patient.symptoms[key]}")
                questions.remove(key)
                break
        else:
            print("Invalid assessment item or already asked, please enter again.")
        if not questions:
            print("All assessment items are completed.")


def ask_pain_assessment(patient):
    print(
        "You starts to find out more about the patient's condition based from his son(using the SOCRATES assessment method)while taking the ABCDE treatments:"
    )
    questions = [
        "Site",
        "Onset",
        "Character",
        "Radiation",
        "Associated symptoms",
        "Timing",
        "Exacerbating and relieving factors",
        "Severity",
    ]

    while questions:
        question = input(
            "Pick a assessment item:(Site, Onset, Character, Radiation, Associated symptoms, Timing, Exacerbating and relieving factors, Severity): "
        )
        for key in questions:
            if key.lower() in question.lower():
                print(f"Answer: {patient.pain_assessment[key]}")
                questions.remove(key)
                break
        else:
            print("Invalid assessment item or already asked, please enter again.")
        if not questions:
            print("All assessment items are completed.")


def main():
    print("Player Role: You are now an Emergency Doctor")
    print(
        "Late in the afternoon 5 o'clock, an 70 years old elderly man is sitting on a park bench reading as usual. Suddenly, he felts a severe chest pain, like a heavy stone pressing on his chest, and the pain quickly spreads to his left arm and back. His breathing becomes rapid and his forehead began to sweat he clutches his sweater tightly, and his face turnes pale."
    )

    input("Press Enter to continue...")

    print(
        "\nThe ambulance brings the elderly man to the emergency room. You see him with a pale face, clutching his chest in pain. His anxious son is beside him."
    )

    input("Press Enter to continue...\n")

    patient = Patient()

    ask_assessment(patient)

    print(
        "\nThe patient's condition is critical, and you decide to further assess his chest pain through its history."
    )

    input("Press Enter to continue...")

    ask_pain_assessment(patient)

    print(
        "\nTo better understand the patient's social history, you start asking his son some questions about it."
    )

    input("Press Enter to continue...")

    patient.ask_history()

    print(
        "\nYou decide to perform a series of bedside tests to determine the patient's specific condition."
    )

    input("Press Enter to continue...")

    patient.bedside_tests()
    print("\nYou diagnosed it as heart attack:")

    input("Press Enter to continue...")
    print("\nYou decide to deliver the bad news to the son:")

    import time

    # Setting up the interview
    print("You set up the conversation with the patient's son...")
    time.sleep(1)

    # Assessing the patient's Perception
    print("You find a quiet room and invite the patient's son to sit down")
    time.sleep(1)
    print("\nSon: Is my father going to be okay? What's wrong with him?")
    time.sleep(1)

    # Obtaining the patient's Invitation
    print("\nYou approach the topic gently:")
    time.sleep(1)
    print("Doctor: Would you like me to explain what's happening with your father?")
    time.sleep(1)
    print("Son: Yes, please tell me everything.")
    time.sleep(1)

    # Giving Knowledge and Information
    print(
        "Doctor: Your father had a severe heart attack. The tests show his arteries are badly blocked."
    )
    time.sleep(1)

    # Addressing the patient's Emotions with Empathetic
    print("Doctor: I understand this must be terrifying for you. I'm here to help.")
    time.sleep(1)

    # Strategy and Summary
    print(
        "Doctor: Right now, our priority is stabilizing your father. We'll do everything we can."
    )
    time.sleep(1)
    print(
        "Doctor: Your father needs immediate emergency percutaneous coronary intervention (PCI), possibly including coronary stent implantation."
    )
    time.sleep(1)
    print("Doctor: We have a dedicated team working to provide the best care possible.")
    time.sleep(1)
    print(
        "Doctor: I'll be here for any questions you have, and we'll get through this together."
    )
    time.sleep(1)
    print("Son : Thank you so much, doctor. I will cooperate with you fully.")


if __name__ == "__main__":
    main()



# PART 2:
class Patient:
    def __init__(self, name):
        self.name = name
        self.condition = "fatigue, crying frequently, self-harm"
        self.symptoms = {
            "Site": "No obvious localized pain",
            "Onset": "Started about two months ago. Initially thought it might just be emotional fluctuations, but now I'm increasingly concerned about his condition.",
            "Character": "No significant localized pain",
            "Radiation": "It's worsening. Initially, he only cried occasionally, but now he feels very depressed almost every day.",
            "Associated symptoms": "His sleep has become irregular. Sometimes it's hard for him to fall asleep, and sometimes he sleeps a lot. His appetite has also decreased, and he eats much less of his favorite foods than before.",
            "Timing": "He seems worst in the evenings, especially before bedtime.",
            "Exacerbating and relieving factors": "I've noticed that if he can play with his best friend for a while, his condition may improve. But most of the time he prefers to be alone.",
            "Severity": "I think his mood is about a 7 or 8 sometimes; he really looks unhappy.",
        }
        self.medical_history = ["No significant past health problems or treatments."]
        self.current_medications = ["Occasional antipyretics for colds or fevers."]
        self.family_history = ["No one in the family has had similar emotional problems."]
        self.lifestyle = "He used to be active and sociable, but now he's become more introverted and less interested in activities."

    def ask_history(self):
        questions = [
            "What past health problems or treatments has he had?",
            "Has he used any medications in the past? Any allergies or adverse reactions to medications?",
            "Does anyone in your family have similar emotional problems or other mental health issues?",
            "What is his daily life like, and how has he been feeling recently?",
        ]

        emotions = [
            "No significant past health problems or treatments.",
            "He rarely needs medication, except for antipyretics for colds or fevers. No signs of allergic reactions to medications.",
            "No one in the family has had similar emotional problems. However, I sometimes worry that our arguments with his father might affect him.",
            "Recently, he's become more introverted and less interested in activities. He used to enjoy sports, but now he's less interested.",
        ]

        for question, emotion in zip(questions, emotions):
            input(f"GP: {question} ")
            print(f"Ms. Daphena: {emotion}")

def ask_pain_assessment(patient):
    print("You start to find out more about the patient's condition based on the SOCRATES assessment method:")
    questions = [
        "Site",
        "Onset",
        "Character",
        "Radiation",
        "Associated symptoms",
        "Timing",
        "Exacerbating and relieving factors",
        "Severity",
    ]

    while questions:
        question = input("Pick an assessment item: (Site, Onset, Character, Radiation, Associated symptoms, Timing, Exacerbating and relieving factors, Severity): ")
        for key in questions:
            if key.lower() in question.lower():
                print(f"Answer: {patient.symptoms[key]}")
                questions.remove(key)
                break
        else:
            print("Invalid assessment item or already asked, please enter again.")
        if not questions:
            print("All assessment items are completed.")

def main():
    import time

    print("Player Role: You are now a GP:\n")

    print("Ms. Daphena: Doctor, I'm Mrs. Daphena. This is my daughter, Kitty. She has been feeling exhausted every day, crying frequently in class, and sometimes even self-harming on her waist. I'm worrying that she might get depression.")
    input("Press Enter to continue...\n")

    print("GP: I understand this must be a very worrying time for you, Mrs. Daphena. Let's work together to understand what Kitty might be going through.")
    time.sleep(1)

    print("GP: Before we proceed, would you like a hint to guide our questions, or shall we begin directly?")
    input("Press Enter to continue...\n")

    print("GP: Sure, let's start with some questions to get a better picture of Kitty's situation.\n")
    time.sleep(1)

    patient = Patient("Kitty")

    ask_pain_assessment(patient)
    input("Press Enter to continue...\n")
    patient.ask_history()

    print("\nGP: Thank you, Mrs. Daphena, for providing all this information. Based on what you've shared, I believe it's a Kitty got depression. I think it would be beneficial for Kitty to see a specialist who can help her with her emotional well-being.")
    time.sleep(1)

    print("GP: I'll arrange for a referral to a therapist who can conduct a thorough evaluation and provide the appropriate support.")
    time.sleep(1)

    print("\nGP: In the meantime, please know that you're doing a great job by seeking help for Kitty. It's important to address these concerns early on.")
    time.sleep(1)

    print("GP: If you have any more questions or if there's anything else you'd like to discuss, please feel free to ask.")
    time.sleep(1)

    print(f"\nMs. Daphena: Thank you, Doctor. I appreciate your understanding and support.")
    time.sleep(1)

    print("\nGP: You're welcome, Ms. Daphena. We're here to help. Take care and we'll be in touch soon.")

if __name__ == "__main__":
    main()


# PART 3:
import time

print("NHS values:")
time.sleep(1)  # Pause for 1 second
print("- The patient will be at the heart of everything the NHS does")
time.sleep(1)
print("- The NHS provides a comprehensive service, available to all")
time.sleep(1)
print(
    "- Access to NHS services is based on clinical need, not an individual's ability to pay"
)
time.sleep(1)
print("- The NHS aspires to the highest standards of excellence and professionalism")
time.sleep(1)
print("- The NHS works across organizational boundaries")
time.sleep(1)
print("- The NHS is committed to providing best value for taxpayers' money")
time.sleep(1)
print(
    "- The NHS is accountable to the public, communities, and patients that it serves\n"
)
time.sleep(1)

print("Doctor's qualities:")
time.sleep(1)
print("- Motivation to study medicine and genuine interest in the medical profession")
time.sleep(1)
print("- Insight into your own strengths and weaknesses")
time.sleep(1)
print("- The ability to reflect on your own work")
time.sleep(1)
print("- Personal organization")
time.sleep(1)
print("- Academic ability")
time.sleep(1)
print("- Problem-solving")
time.sleep(1)
print("- Dealing with uncertainty")
time.sleep(1)
print("- Manage risk and deal effectively with problems")
time.sleep(1)
print("- Ability to take responsibility for your own actions")
time.sleep(1)
print("- Conscientiousness")
time.sleep(1)
print("- Insight into your own health")
time.sleep(1)
print(
    "- Effective communication, including reading, writing, listening, and speaking"
)
time.sleep(1)
print("- Teamwork")
time.sleep(1)
print("- Ability to treat people with respect")
time.sleep(1)
print("- Resilience and the ability to deal with difficult situations")
time.sleep(1)
print("- Empathy and the ability to care for others")
time.sleep(1)
print("- Honesty")
time.sleep(1)
print("- Medical ethics\n")
time.sleep(1)

print("Steps to become a doctor:")
time.sleep(1)
print("- Foundation Training")
time.sleep(1)
print("- Progress to either General Practitioner or Registrar and then Consultant\n")
time.sleep(1)

print("Different types of hospitals:")
time.sleep(1)
print("- Social hospital")
time.sleep(1)
print("- Outpatients, Accident & Emergency")
time.sleep(1)
print("- Primary care, secondary care, tertiary care")
time.sleep(1)
print("- Palliative Care\n")
time.sleep(1)

print("Congratulations! You've completed the Medical Role-Play Game. Did you find it exciting?")
print("Explore more about the NHS and the journey to becoming a doctor at BSMS Virtual Working Experience!")

