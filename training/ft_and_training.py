import openai
import json

f = open("quests_BG_TES.json")
data = json.load(f)

def prompt_generation(quest):
  prompt = ""
  completion = ""

  # for our game, we want specific information from the dataset

  prompt += "Quest Name: {quest_name}\n".format(quest_name=quest['name'])
  prompt += "Quest Objective: {quest_objective}\n".format(quest_objective=quest['objective'])

  if quest.get('first_tasks', False) != False:
    prompt += "Task: {quest_task}\n".format(quest_task=quest['first_tasks'][0])

  if quest.get('first_task_locations', False) != False:
    prompt += "Task Location: {location}\n".format(location=quest['first_task_locations'][0]['name'])
    prompt += "Task Location Description: {location_desc}\n".format(location_desc=quest['first_task_locations'][0]['description'])

  prompt += "Quest Giver Name: {giver_name}\n".format(giver_name=quest['quest_giver']['name'])
  prompt += "Quest Giver Description: {giver_desc}\n".format(giver_desc=quest['quest_giver']['description'])
  prompt += "Quest Giver Location: {giver_loc}\n".format(giver_loc=quest['quest_giver']['location'])
  prompt += "Reward Name: {reward_name}\n".format(reward_name=quest['reward'][0]['name'])
  prompt += "Reward Description: {reward_desc}\n".format(reward_desc=quest['reward'][0]['description'])
  prompt += "Reward Amount: {reward_amount}\n".format(reward_amount=str(quest['reward'][0]['amount']))

  # not every quest has this information, so if found, add it

  if quest.get('items', False) != False:
    prompt += "Related Item Name: {item_name}\n".format(item_name=quest['items'][0]['name'])
    prompt += "Related Item Description: {item_desc}\n".format(item_desc=quest['items'][0]['description'])
    prompt += "Related Item Amount: {item_amount}\n".format(item_amount=str(quest['items'][0]['amount']))
  elif quest.get('characters', False) != False:
    prompt += "Related Character Name: {char_name}\n".format(char_name=quest['characters'][0]['name'])
    prompt += "Related Character Description: {char_desc}\n".format(char_desc=quest['characters'][0]['description'])
    prompt += "Related Character Location: {char_loc}\n".format(char_loc=quest['characters'][0]['location'])
  elif quest.get('enemies', False) != False:
    prompt += "Enemy Name: {enemy_name}\n".format(enemy_name=quest['enemies'][0]['name'])
    prompt += "Enemy Description: {enemy_desc}\n".format(enemy_desc=quest['enemies'][0]['description'])
    prompt += "Number of Enemies: {enemy_amount}\n".format(enemy_amount=str(quest['enemies'][0]['amount']))

  # goal for ai to create the dialogue and
  # the description part of each quest usually contains dialogue
  completion += "Dialogue: {dialogue}".format(dialogue=quest['description'])

  return prompt, completion

def create_fine_tuning_file(quest_file_data):

  fine_tuning_data = []
  for quest in quest_file_data:
    quest_data = {}
    prompt, completion = prompt_generation(quest)
    quest_data["messages"] = [{"role": "user", "content": prompt}, {"role": "assistant", "content": completion}]
    fine_tuning_data.append(quest_data)

  with open("quest_finetuning_data.jsonl", "w") as out:
    for data in fine_tuning_data:
      out.write(json.dumps(data))
      out.write('\n')

create_fine_tuning_file(data)

# Finetuning your model
client = openai.OpenAI(api_key="your-api-key")

finetune_file = client.files.create(
    file=open("quest_finetuning_data.jsonl", "rb"),
    purpose="fine-tune"
)

finetune_job = client.fine_tuning.jobs.create(
    training_file = finetune_file.id,
    model = "your-desired-model"
)

