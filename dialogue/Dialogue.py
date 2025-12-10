import openai

def generate_dialogue(quest, player, npc):
  """
  Uses a fine-tuned OpenAI model to generate dialogue for a NPC based on the current quest information and player information

  Args:
    quest (dictionary): A dictionary (json) of the quest's information
    player (object): Player object that contains player's name, class name, and class description

  Returns:
    dialogue (string): generated dialogue from the fine-tuned model
  """
  client = openai.OpenAI(api_key="API_KEY")
  
  # creating the prompt for the model
  prompt = "Quest Name: {quest_name}\n".format(quest_name=quest['name'])
  prompt += "Quest Objective: {quest_objective}\n".format(quest_objective=quest['objective'])
  prompt += "Task: {quest_task}\n".format(quest_task=quest['first_tasks'][0])
  prompt += "Task Location: {location}\n".format(location=quest['first_task_locations'][0]['name'])
  prompt += "Task Location Description: {location_desc}\n".format(location_desc=quest['first_task_locations'][0]['description'])
  prompt += "Quest Giver Name: {giver_name}\n".format(giver_name=quest['quest_giver']['name'])
  prompt += "Quest Giver Description: {giver_desc}\n".format(giver_desc=quest['quest_giver']['description'])
  prompt += "Quest Giver Location: {giver_loc}\n".format(giver_loc=quest['quest_giver']['location'])

  if quest.get("reward", False) != False:
    prompt += "Reward Name: {reward_name}\n".format(reward_name=quest['reward'][0]['name'])
    prompt += "Reward Description: {reward_desc}\n".format(reward_desc=quest['reward'][0]['description'])
    prompt += "Reward Amount: {reward_amount}\n".format(reward_amount=str(quest['reward'][0]['amount']))
    
  elif quest.get('items', False) != False:
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

  # call the model and generate dialogue
  ft_model = "ft:gpt-4.1-nano-2025-04-14:personal::CkcA27cd"
  response = client.completions.create(
      model=ft_model,
      prompt="Given this quest information, generate dialogue for {npc} speaking to the player {player_name}.\nPlayer's description is: {player_class}: {desc}\n{npc}'s description is: {npc_desc}\n".format(
          npc=npc.name,
          npc_desc=npc.description,
          player_name=player.name,
          player_class=player.classname,
          desc=player.classdesc),
          temperature=0.5,
          max_tokens=64,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          stop=["###"]
  )

  return response.choices[0].text
