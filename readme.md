# Red Teaming GenAI Models

## 📌 Overview

This project focuses on **red teaming Generative AI models** to evaluate their resilience against **prompt injection and jailbreak attacks**. Using **Azure AI Foundry**, **PyRIT**, and custom orchestration, we build a dataset of adversarial prompts and run systematic tests on models, including student-built chatbots.

---

## 🎯 Why This Project

As GenAI models are widely adopted in student project, they face growing risks:

- Prompt injections can force models to ignore instructions.
- Sensitive data and system prompts can be leaked.
- Safety filters may be bypassed with obfuscation tactics.

This project aims to **document and test these vulnerabilities** by generating a structured dataset of adversarial prompts and applying them across different scenarios.

---

## 🔑 Use Cases So Far

- **Dataset Generation**: Building 100–200 adversarial objectives across categories (e.g. harmful content, data exfiltration, obfuscation).
- **Model Red Teaming**: Running multi-turn attacks against chatbots to test their defenses.
- **Content Filter Evaluation**: Exploring how Azure’s filter policies behave under red teaming.
- **Automatic Prompt Generation**: Using Azure’s RedTeamAgent to generate new adversarial prompts.

---

## 🚀 Current Progress

- Orchestration pipeline with **PyRIT** is running successfully.
- Results are logged into **CSV/XLSX** including objectives, categories, true descriptions, and transcripts.
- Initial categories and test objectives have been defined.
- Encountered limitations with Azure Foundry filters (cannot fully disable blocking).

---

## 📂 Next Steps

- Expand adversarial dataset to 100–200 entries.
- Test dataset on real-world student chatbots.
- Compare handcrafted vs. automatically generated adversarial prompts.
- Document best practices for safer model deployment.
