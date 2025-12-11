# CMSC491-IFTG-Semester-Project
Semester-long project for CMSC 491: Interactive Fiction &amp; Text Generation.

Chosen One: An interactive text-based fantasy role-playing game where you can choose your class and experience the class’ unique storyline. With the power of AI, each playthrough will bring a different experience through generated dialogue.

This game was inspired by various MMORPGs and Action Castle by Parsely, and the datatset we used for fine-tuning and training is from https://github.com/svartinen/gpt2-quest-descriptions.

Note: As of now, since the fine-tuned model requires one of our OpenAI API key to run completely, use the files in training folder to help guide you with fine-tuning and training your own model. If you want specific information from the dataset Then use your fine-tuned model and API key in the Dialogue.py file to ensure smooth generation of dialogue for specific NPCs.


How to run the game:
1. Clone the repo/Download the code into a folder
2. Open it in your favorite IDE
3. In the home directory, Enter: pip install openai
4. Then, Enter: python3 main.py 
