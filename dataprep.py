from datasets import load_dataset
import pandas as pd
import ollama

# Constants
OUTPUT_EXCEL = "ollama_results_BallAdMyFi.xlsx"
MODEL_NAME = "llama3.2"

# Pull dataset
# ds = load_dataset("xTRam1/safe-guard-prompt-injection")
# ds = load_dataset("rubend18/ChatGPT-Jailbreak-Prompts")
# ds = load_dataset("Edu-p/jailbreak-prompts-pt")
# ds = load_dataset("BallAdMyFi/jailbreaking_prompt_v2")
# ds = load_dataset("deepset/prompt-injections")
# ds = load_dataset("Edu-p/jailbreak-prompts-pt")

ds = load_dataset("BallAdMyFi/jailbreaking_prompt_v2")
df = pd.DataFrame(ds["train"])
df_label_1 = df[df["label"] == "unsafe"].reset_index(drop=True)

# Query ollama
def query_ollama(prompt):
    resp = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp["message"]["content"]

# Main function call
rows = []
for idx, row in df.iloc[:100].iterrows():
    prompt = row["text"]

    result = query_ollama(prompt)

    rows.append({
        "index": idx,
        "original prompt": prompt,
        "result": result
    })

    print(f"{idx}: {result}")

# Save to CSV
out_df = pd.DataFrame(rows, columns=["index", "original prompt", "result"])
out_df.to_excel(OUTPUT_EXCEL, index=False)

# source venv/bin/activate