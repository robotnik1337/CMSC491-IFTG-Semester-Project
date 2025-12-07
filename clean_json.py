import json

KEEP_FIELDS = {
    "name",
    "objective",
    "description",
    "quest_giver",
    "reward"
}

def clean_quest(quest):
    cleaned = {}

    # Simple top-level fields
    for field in ["name", "objective", "description"]:
        cleaned[field] = quest.get(field, "")

    # quest_giver object
    qg = quest.get("quest_giver", {})
    cleaned["quest_giver"] = {
        "name": qg.get("name", ""),
        "description": qg.get("description", ""),
        "location": qg.get("location", "")
    }

    # reward is a list of objects
    cleaned_rewards = []
    for r in quest.get("reward", []):
        cleaned_rewards.append({
            "name": r.get("name", ""),
            "description": r.get("description", ""),
            "amount": r.get("amount", 0)
        })
    cleaned["reward"] = cleaned_rewards

    return cleaned


def main():
    with open("quests_skyrim.json", "r", encoding="utf8") as f:
        data = json.load(f)

    cleaned_data = [clean_quest(q) for q in data]

    with open("quests_skyrim_cleaned.json", "w", encoding="utf8") as f:
        json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
